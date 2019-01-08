# coding=utf-8
import os
import sys
from src.base.application import Application
from src.base.command import Helper
from src.base.helper import singleton


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
        dir_name = F"{Application.BASEDIR}/{self.command_home}"
        if os.path.isdir(dir_name):
            items = os.listdir(dir_name)
            for item in items:
                if os.path.isfile(F"{dir_name}/{item}") and item.endswith('.py'):
                    filename = item.rstrip('.py')
                    module = __import__(F"src.commands.{filename}", fromlist=[filename])
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
        instance = self._parse.handlers[self._parse.cm['class']](self._parse.opts)
        if hasattr(instance, 'parser'):
            setattr(instance, 'parser', self._parse)
        getattr(instance, self._parse.cm['method'])()

