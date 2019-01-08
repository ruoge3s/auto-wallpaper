# coding=utf-8

from src.base.helper import singleton
from configparser import ConfigParser


@singleton
class Config:
    """
    配置管理类
    """
    _cf = None

    def __init__(self, cf=None):
        """
        :param cf: configparser.ConfigParser
        """
        if cf:
            if isinstance(cf, ConfigParser):
                self._cf = cf
            else:
                raise Exception('需要传入ConfigParse对象')

    def get(self, name, default=None):
        """
        获取配置
        :param name:str
        :param default: 未配置时的默认值
        :return:
        """
        res = name.split(":")

        if res.__len__() == 2:
            return self._cf.get(res[0], res[1], fallback=default)
        else:
            return default

    def set(self):
        pass
