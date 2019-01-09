# coding=utf-8

import os
from configparser import ConfigParser
from src.base.config import Config
from src.base.application import Application

Application.BASEDIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def enable():
    # 装载配置信息
    cf = ConfigParser()
    cf.read(Application.BASEDIR + "/config.ini", encoding='utf-8')
    Config(cf)

