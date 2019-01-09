# coding=utf-8
from src.base.command import Command
from src.base import mapper


@mapper.describe('加载工具')
class Load(Command):
    @mapper.describe('测试方法')
    def test(self):
        print(self.name)
        print(self._true('h'))
        print('test')

