# coding=utf-8
from getopt import getopt
from src.base import mapper
from src.base.helper import tab, under2dash
from inspect import isfunction


class Command:
    """
    定义端名称标示是否
    """
    short_opts = []
    """
    定义长名称传值
    """
    long_opts = []

    flags = {}

    def __init__(self, opts=None):
        opts, args = getopt(opts, ''.join(self.short_opts), list(map(lambda s: s + '=', self.long_opts)))
        for item in opts:
            if item[0].startswith('--'):
                attribute = item[0].lstrip('--')
                if hasattr(self, attribute):
                    setattr(self, attribute, item[1])

            if item[0].startswith('-'):
                self.flags[item[0].lstrip('-')] = True

    def _true(self, name):
        return name in self.flags


@mapper.describe('帮助')
class Helper(Command):

    parser = None

    msg = 'Welcome to use.\n'

    @mapper.describe('提示')
    def default(self):
        self._tips()

    @mapper.describe('命令提示')
    def _tips(self):
        info = {
            'eg':      "eg:python <class>:<method> [options]",
            'title':   "Options:",
            'classes': []
        }
        handlers = self.parser.handlers

        class_max_length = 4
        method_max_length = 8

        for name in handlers:
            class_max_length = max(len(name), class_max_length)
            buffer = {
                'name':    name,
                'describe': mapper.get_describe(handlers[name]),
                'methods':  []
            }
            mns = list(filter(
                lambda subsidiary:
                    not subsidiary.startswith("_")
                    and not subsidiary.endswith("_")
                    and isfunction(getattr(handlers[name], subsidiary))
                , dir(handlers[name])
            ))
            for mn in mns:
                method_max_length = max(len(mn), method_max_length)
                func = getattr(handlers[name], mn)
                content = mapper.get_describe(func)
                buffer['methods'].append({
                    'name':     under2dash(mn),
                    'describe': content
                })

            if isfunction(handlers[name]):
                c = handlers[name]()
            else:
                c = handlers[name]

            attr_describes = c.long_opts_describe if hasattr(c, 'long_opts_describe') else {}
            for on in c.long_opts:
                method_max_length = max(len(on) + 2, method_max_length)
                buffer['methods'].append({
                    'name': '--' + under2dash(on),
                    'describe': attr_describes.get(on, '')
                })
            flag_describes = c.short_opts_describe if hasattr(c, 'short_opts_describe') else {}
            for on in c.short_opts:
                method_max_length = max(len(on) + 1, method_max_length)
                buffer['methods'].append({
                    'name': '-' + under2dash(on),
                    'describe': flag_describes.get(on, '')
                })

            info['classes'].append(buffer)
        print(info['eg'])
        print(info['title'])
        for ci in info['classes']:
            print(tab(2) + ci['name'] + tab(2 + class_max_length - len(ci['name'])) + ci['describe'])
            for mi in ci['methods']:
                print(tab(6) + mi['name'] + tab(2 + method_max_length - len(mi['name'])) + mi['describe'])