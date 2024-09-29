# -*- coding: utf-8 -*-

import os
import logging
from langchain_community.document_loaders import PyPDFLoader

from .config import ENV
from .utils.db import VectorDB

logger = logging.getLogger(ENV.app_name)

class Initializer:
    def __init__(self):
        pass

    async def __call__(self, *args, **kwargs):
        logger.info("start init")
        await self.init_db()
        logger.info("finish init")

    async def init_db(self) -> None:
        '''
        1. DB에서 테스트 데이터 검색 (id 0번 데이터)
        2. 없으면 임베딩해서 데이터 넣기
        :return: None
        '''

        VectorDB()
        test_data = ENV.db_object.get([f"{ENV.chroma_document_id}_0"])
        if len(test_data.get("ids")) == 0:
            logger.info("start create vector_store")
            dir_path = os.path.join(os.path.dirname(os.path.abspath(os.path.dirname(__file__))), "resources")
            documents = list()
            for file in os.listdir(dir_path):
                if file.endswith(".pdf"):
                    logger.info(file)
                    loader = PyPDFLoader(os.path.join(dir_path, file))
                    async for page in loader.alazy_load():
                        documents.append(page)

            ENV.db_object.create_vector_store(documents=documents)
            logger.info("finish create vector_store")
        else:
            logger.info("already exist vector_store")
