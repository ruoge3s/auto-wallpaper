# coding=utf-8
from functools import wraps

maps = {}


def get(group, name, default=''):
    if group in maps and name in maps[group]:
        return maps[group][name]
    return default


def add(group, name, content):
    if group not in maps:
        maps[group] = {}
    maps[group][name] = content


def describe(content):
    """
    添加方法描述
    :param content:
    :return:
    """
    def wrapper(obj):
        add('describe', F"{obj.__module__}.{obj.__qualname__}", content)

        @wraps(obj)
        def origin(*args, **kwargs):
            obj(*args, **kwargs)
            return obj

        return origin

    return wrapper


def get_describe(obj, default=''):
    """
    获取对象说明(包括类和类方法对象)
    :param obj:
    :param default:
    :return:
    """
    return get('describe', F"{obj.__module__}.{obj.__qualname__}", default)
