# -*- coding: utf-8 -*-

import logging
from langchain_chroma import Chroma
from langchain_openai import OpenAIEmbeddings

from ..config import ENV

logger = logging.getLogger(ENV.app_name)

class VectorDB:
    def __init__(self):
        if ENV.db_type == "CHROMA":
            ChromaDB()


class ChromaDB:
    def __init__(self):
        logger.info("chromadb init")
        try:
            ENV.db_object = Chroma(
                embedding_function=OpenAIEmbeddings(),
                persist_directory=ENV.chroma_data_path
            )
        except Exception as e:
            logger.error(f"chroma db init failed : {e}")

    def create_vector_store(self, documents):
        ENV.db_object.from_documents(
            documents=documents,
            embedding=OpenAIEmbeddings(),
            ids=[f"{ENV.chroma_document_id}_{i}" for i in range(0, len(documents))],
            persist_directory=ENV.chroma_data_path
        )
