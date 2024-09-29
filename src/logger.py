# -*- coding: utf-8 -*-

import os
import sys
import logging

from .config import ENV

os.makedirs(ENV.log_dir, exist_ok=True)

if ENV.app_name:
    # Note. Default Settings
    app_logger = logging.getLogger(ENV.app_name)
    app_logger.setLevel(ENV.log_level)
    app_logger.propagate = False

    if ENV.log_level == 10:
        formatter = logging.Formatter(
            '%(asctime)s[%(levelname)-8s] %(filename)s-%(lineno)s: %(message)s')
            # '%(asctime)s %(filename)-16s: %(message)s')
    else:
        formatter = logging.Formatter(
            '%(asctime)s[%(levelname)-8s] %(message)s')

    # Note. Stream Handler
    streamHandler = logging.StreamHandler(sys.stdout)
    streamHandler.setFormatter(formatter)
    app_logger.addHandler(streamHandler)

    # Note. File Handler
    fileHandler = logging.FileHandler(os.path.join(ENV.log_dir, ENV.log_file))
    fileHandler.setFormatter(formatter)
    app_logger.addHandler(fileHandler)

    # Note. Timed Rotating File Handler
    # timedHandler = logging.handlers.TimedRotatingFileHandler(
    #     os.path.join(os.path.join(ENV.log_dir, ENV.log_file)), when="midnight", interval=1, encoding="UTF-8", utc=False)
    # timedHandler.setFormatter(formatter)
    # timedHandler.suffix = "%Y%m%d"
    # app_logger.addHandler(timedHandler)