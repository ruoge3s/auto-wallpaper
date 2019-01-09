# coding=utf-8
from src.base.command import Command
from src.base.mapper import describe


@describe('改变')
class Change(Command):

    @describe('测试方法')
    def test(self):
        print('change test\n')
