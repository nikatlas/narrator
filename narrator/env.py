# pylint: skip-file

import builtins
import os


def get(key):
    return os.environ.get(key)


def str(key, default=Ellipsis):
    if default is Ellipsis:
        if bool("__strict_env__", True):
            return os.environ[key]
        else:
            return os.environ.get(key)
    else:
        return os.environ.get(key, default)


def list(key, default=None, separator=","):
    value = str(key, default)
    if value is None:
        return []
    else:
        return value.split(separator)


def int(key, default):
    return builtins.int(str(key, default))


def bool(key, default):
    if key in os.environ and (str_var := os.environ.get(key)) is not None:
        return str_var.lower() in ("yes", "true", "y", "1")
    else:
        return default
