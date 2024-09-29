# -*- coding: utf-8 -*-

import logging
from fastapi import FastAPI, APIRouter
from langchain_openai import ChatOpenAI
from contextlib import asynccontextmanager
from langchain_core.messages import HumanMessage, SystemMessage
from langchain.chains.conversational_retrieval.base import ConversationalRetrievalChain

from .config import ENV
from .init import Initializer
from .utils.memory import history
from .models.message_data import Message
from .utils.prompt import get_prompt_template


@asynccontextmanager
async def lifespan(app: FastAPI):
    initializer = Initializer()
    await initializer()
    logger.info("START CHAT AGENT")
    yield
    logger.info("CLOSE CHAT AGENT")


router = APIRouter(
    prefix="",
    tags=["Main APIs"],
    dependencies=[],
    responses={404: {"description": "Not found"}}
)

app = FastAPI(lifespan=lifespan)
logger = logging.getLogger(ENV.app_name)


@router.get("/")
async def root():
    return {"message": "Hello World"}


@router.post("/chat")
async def chat(message: Message):
    logger.debug(message)
    result = await call_gpt(message)
    return result


async def call_gpt(message: Message):
    try:
        retriever = ENV.db_object.as_retriever(
            search_type="similarity",
            search_kwargs={
                "k": 3
            }
        )

        qa_chain = ConversationalRetrievalChain.from_llm(
            llm=ChatOpenAI(temperature=0, model=ENV.openai_chat_model),
            retriever=retriever,
            return_source_documents=False,
            combine_docs_chain_kwargs={'prompt': get_prompt_template()}
        )

        result = qa_chain({'question': message.text, 'chat_history': history.get_session_history(message.session_id)})
        logger.debug(f"qa result : {result}")

        messages = [HumanMessage(content=message.text), SystemMessage(content=result["answer"])]
        history.update_session_history(session_id=message.session_id, messages=messages)

        return {"answer": result["answer"]}
    except Exception as e:
        logger.error(e)
