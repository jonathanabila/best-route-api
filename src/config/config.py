# -*- coding: utf-8 -*-
# !/usr/bin/env python3
"""

"""
import os
from distutils.util import strtobool


def get_env(variable):
    """
    Function to ensure that variables are declared without using default mock
    values that can cause difficulty at the
    time of debugging.
    :param variable: Variable that will be searched within the environment -
        using the dot env as the source file.
    :return: The value of the variable that is declared in the file.
    """
    if (
        os.environ.get(variable) is None
        and bool(strtobool(os.environ.get("DEBUG", "False"))) is False
        and bool(strtobool(os.environ.get("TEST", "False"))) is False
    ):
        raise KeyError(
            "The environment variable {} - is required for operation.".format(variable)
        )
    elif bool(strtobool(os.environ.get("TEST", "False"))) is True:
        return "MOCK"

    if (
        os.environ.get("STAGE_NAME") is not None
        and os.environ.get("STAGE_NAME").lower() != "prod"
        and os.environ.get(variable + "_DEV") is not None
    ):
        variable += "_DEV"

    return os.environ.get(variable)
