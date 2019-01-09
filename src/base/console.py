# coding=utf-8
import os
import sys
from src.base.application import Application
from src.base.command import Helper
from src.base.helper import singleton, dash2under
from inspect import isfunction


@singleton
class Parse:
    """
    解析命令，执行命令
    """
    command_home = 'src/commands'

    handlers = {}

    cm = {'class': 'helper', 'method': 'default'}
    opts = []

    def argv(self):
        """
        预处理参数
        :return:
        """
        argv = sys.argv[1:]
        if len(argv) > 0:
            cm = argv[0].split(':')
            if len(cm) == 2:
                if cm[0] in self.handlers:
                    cm[1] = dash2under(cm[1])
                    if hasattr(self.handlers[cm[0]], cm[1]) and callable(getattr(self.handlers[cm[0]], cm[1])):
                        self.cm['class'] = cm[0]
                        self.cm['method'] = cm[1]
                self.opts = argv[1:]
            else:
                self.opts = argv[0:]

    def commands(self):
        """
        预处理命令
        :return:
        """
        dir_name = Application.BASEDIR + '/' + self.command_home
        if os.path.isdir(dir_name):
            items = os.listdir(dir_name)
            for item in items:
                if os.path.isfile(dir_name + '/' + item) and item.endswith('.py'):
                    filename = item.rstrip('.py')
                    module = __import__("src.commands." + filename, fromlist=[filename])
                    cname = filename[0].upper() + filename[1:]
                    if hasattr(module, cname):
                        self.handlers[filename] = getattr(module, cname)

        self.handlers['helper'] = Helper


class Console:

    _parse = None

    def __init__(self):
        self.parse()

    def parse(self):
        """
        进行初始化
        """
        self._parse = Parse()
        self._parse.commands()
        self._parse.argv()

    def execute(self):
        """
        执行命令
        :return:
        """
        handler = self._parse.handlers[self._parse.cm['class']]

        # 解决用装饰器导致的返回处理器不是类名的问题
        if isfunction(handler):
            instance = handler()
        else:
            instance = handler

        instance = instance(self._parse.opts)
        if hasattr(instance, 'parser'):
            setattr(instance, 'parser', self._parse)
        getattr(instance, self._parse.cm['method'])()

