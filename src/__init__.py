# -*- coding: utf-8 -*-

from fastapi.middleware.cors import CORSMiddleware

from . import main
from . import utils
from . import models
from . import logger
from .main import router as main_router

__all__ = [
    "models",
    "utils",
    "main"
]

app = main.app
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

app.include_router(main_router)
