# coding=utf-8
from src.base.command import Command
from src.base import mapper


@mapper.describe('加载')
class Load(Command):
    short_opts = ['h']
    long_opts = ['name']
    long_opts_describe = {
        'name': '用户名'
    }
    name = ''

    @mapper.describe('测试方法')
    def test(self):
        print(self.name)
        print(self._true('h'))
        print('test')

    @mapper.describe('例子')
    def demo(self):
        print('demo')
