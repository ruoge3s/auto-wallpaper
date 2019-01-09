# coding=utf-8
from src.base.command import Command
from src.base import maps


@maps.describe('加载器')
class Load(Command):

    @maps.describe('测试方法')
    def test(self):
        print('test')

    @maps.describe('例子')
    def demo(self):
        print('demo')
