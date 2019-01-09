# coding=utf-8

from functools import wraps


def singleton(cls):
    """
    单例
    :param cls:
    :return:
    """
    instances = {}

    @wraps(cls)
    def get_instance(*args, **kw):
        if cls not in instances:
            instances[cls] = cls(*args, **kw)
        return instances[cls]

    return get_instance


def tab(num=1):
    return " " * num


def under2dash(string):
    return string.replace('_', '-')


def dash2under(string):
    return string.replace('-', '_')
