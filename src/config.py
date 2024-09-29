# -*- config: utf-* -*-

import os
from pydantic import Field
from datetime import datetime
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    app_name: str = Field("chatAgent", env="CHAT_AGENT_APP_NAME")
    base_dir: str = Field(os.path.dirname(os.path.abspath(__file__)), env="CHAT_AGENT_BASE_DIR")

    # Note. Logger Settings
    log_dir: str = Field(f"{os.path.expanduser('~')}/logs", env="CHAT_AGENT_LOG_DIR")
    log_file: str = Field(f"{datetime.now().strftime('%Y%m%d')}.log", env="CHAT_AGENT_LOG_FILE")
    log_level: int = Field(10, env="CHAT_AGENT_LOG_LEVEL")  # DEBUG=10, INFO=20

    # Note. OpenAI Settings
    openai_api_key: str = Field("", env="OPENAI_API_KEY")
    openai_chat_model: str = Field("gpt-4o-mini", env="OPENAI_CHAT_MODEL")

    # Note. DB Settings
    db_object: object = None
    db_type: str = Field("CHROMA", env="CHAT_AGENT_DB_TYPE")
    chroma_data_path: str = Field(
        os.path.join(os.path.dirname(os.path.abspath(os.path.dirname(__file__))), "chroma_db"),
        env="CHAT_AGENT_CHROMA_DATA_PATH")
    chroma_document_id: str = Field("chat_agent", env="CHAT_AGENT_CHROMA_DOCUMENT_ID")

    history_key: str = Field("chat_history", env="CHAT_AGENT_HISTORY_KEY")
    session_history: dict[str, object] = Field(dict(), env="CHAT_AGENT_SESSION_HISTORY")


ENV = Settings()
ENV.log_file = f"{ENV.app_name}-{ENV.log_file}"
