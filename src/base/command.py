# coding=utf-8
from getopt import getopt
import sys


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

    def __init__(self, opts):
        opts, args = getopt(opts, ''.join(self.short_opts), list(map(lambda s: s + '=', self.long_opts)))
        for item in opts:
            if item[0].startswith('--'):
                attribute = item[0].lstrip('--')
                if hasattr(self, attribute):
                    setattr(self, attribute, item[1])

            if item[0].startswith('-'):
                self.flags[item[0].lstrip('-')] = True

    def _is_true(self, name):
        return name in self.flags


class Helper(Command):

    parser = None

    msg = 'Welcome to use.\n'

    def default(self):
        self.tips()

    def tips(self):
        handlers = self.parser.handlers
        sys.stdout.write("eg:python <class>:<method> [options]\n")
        sys.stdout.write("Options:\n")
        for name in handlers:
            sys.stdout.write(" " * 2 + F"{name}\n")
            ms = list(filter(
                lambda mtd: not mtd.startswith("_") and not mtd.endswith("_") and callable(getattr(handlers[name], mtd)),
                dir(handlers[name])
            ))
            for m in ms:
                sys.stdout.write(" " * 6 + F"{m}\n")
