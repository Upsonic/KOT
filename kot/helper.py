#!/usr/bin/python3
# -*- coding: utf-8 -*-
from functools import wraps


def no_exception(func):
    @wraps(func)
    def runner(*args, **kwargs):
        try:
            result = func(*args, **kwargs)
            return result
        except Exception as e:
            print(f"Exception occurred in function: {e}")

    return runner


@no_exception
def requires(name):
    def decorator(function):
        @wraps(function)
        def wrapper(*args, **kwargs):
            print("RUN")

            try:
                exec(f"import {name}")
            except:
                from pip._internal import main as pip

                pip(["install", name])
            retval = function(*args, **kwargs)
            return retval

        return wrapper

    return decorator
