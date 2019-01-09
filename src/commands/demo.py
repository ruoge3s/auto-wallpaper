# coding=utf-8
from src.base.command import Command
from src.base import mapper


@mapper.describe('示例命令处理器')
class Demo(Command):
    short_opts = ['h']
    short_opts_describe = {'h': '单字母标记'}

    long_opts = ['attr']
    long_opts_describe = {'attr': '属性参数'}

    attr = '属性默认值'

    @mapper.describe('测试方法')
    def test(self):
        print(self.attr)
        print("h flag is ", self._true('h'))
        print('You are called demo:test')
