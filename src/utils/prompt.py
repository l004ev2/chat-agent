# -*- coding: utf-8 -*-
from langchain.prompts import PromptTemplate


def get_prompt_template() -> PromptTemplate:
    template = """
    If you don't know the answer, just say that you don't know, don't try to make up an answer.
    Reply in the same language as user.
    {context}
    history: {chat_history}
    Question: {question}
    Assistant:
    """
    # return PromptTemplate.from_template(template)
    return PromptTemplate(input_variables=["context", "chat_history", "question"], template=template)
