# coding=utf-8

from configparser import ConfigParser
from src.base.config import Config
from src.base.console import Console
from src.base.application import Application


def run():
    # 装载配置信息
    cf = ConfigParser()
    cf.read(F"{Application.BASEDIR}/config.ini", encoding='utf-8')
    Config(cf)

    # 解析命令
    Console().execute()

    # TODO 调用命令处理程序
