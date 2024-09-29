# -*- coding: utf-8 -*-

import logging
from langchain_core.chat_history import BaseChatMessageHistory
from langchain_community.chat_message_histories import ChatMessageHistory

from ..config import ENV

logger = logging.getLogger(ENV.app_name)


class History:
    def __init__(self):
        pass

    # 세션 ID를 기반으로 세션 기록을 가져오는 함수
    def get_session_history(self, session_id: str) -> BaseChatMessageHistory:
        logger.debug(f"find session history by [{session_id}]")
        if session_id not in ENV.session_history:  # 세션 ID가 ENV.session_history에 없는 경우
            # 새로운 ChatMessageHistory 객체를 생성하여 ENV.session_history에 저장
            ENV.session_history[session_id] = ChatMessageHistory(
                memory_key="chat_history",
                input_key="question"
            )

        logger.debug(ENV.session_history[session_id])
        return ENV.session_history[session_id].messages  # 해당 세션 ID에 대한 세션 기록 반환

    def update_session_history(self, session_id: str, messages: list):
        user_history: ChatMessageHistory = ENV.session_history[session_id]
        user_history.add_messages(messages)


history = History()
