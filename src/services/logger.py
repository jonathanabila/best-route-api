# -*- coding: utf-8 -*-
# !/usr/bin/env python3

import logging


LOG_FORMAT = "%(levelname) -10s %(asctime)s %(name) -30s %(funcName) -35s %(lineno) -5d: %(message)s"

root = logging.getLogger()
if root.handlers:
    for handler in root.handlers:
        root.removeHandler(handler)
logging.basicConfig(format="%(asctime)s %(message)s", level=logging.INFO)


def new(owner):
    """Cria um novo logger"""
    logger = logging.getLogger(owner)
    return logger
