# coding=utf-8
from src.base.command import Command
from src.base.mapper import describe


class Change(Command):

    @describe('切换壁纸')
    def wallpaper(self):
        print('change test\n')
