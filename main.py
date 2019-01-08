# coding=utf-8

import os
from src.base.application import Application
from src.bootstrap import run


Application.BASEDIR = os.path.dirname(os.path.abspath(__file__))
run()
