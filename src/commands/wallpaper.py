# coding=utf-8
import os
import random
import subprocess
from src.base.command import Command
from src.base.mapper import describe
from src.base.config import Config
from src.base.application import Application


class Wallpaper(Command):

    home = None

    def _get_pic(self):
        # 获取壁纸列表
        self.home = Config().get('wallpaper:home')

        if self.home[0] is not '/':
            self.home = Application.BASEDIR + '/' + self.home

        if not os.path.isdir(self.home):
            exit()
        il = []
        for filename in os.listdir(self.home):
            if os.path.isfile(self.home + "/" + filename):
                if filename.endswith('jpg'):
                    il.append(filename)

        amount = len(il) - 1
        if amount < 0:
            print('Not image exist')
            exit()

        return self.home + '/' + il[random.randint(0, amount)]

    @describe('Deepin操作系统切换壁纸')
    def deepin(self):
        pic = self._get_pic()

        pid = subprocess.check_output(["pgrep", "dde-session"]).decode("utf-8").strip()
        cmd = "grep -z DBUS_SESSION_BUS_ADDRESS /proc/" + pid + "/environ|cut -d= -f2-"

        os.environ["DBUS_SESSION_BUS_ADDRESS"] = subprocess.check_output(
            ['/bin/bash', '-c', cmd]).decode("utf-8").strip().replace("\0", "")

        command = 'gsettings set com.deepin.wrap.gnome.desktop.background picture-uri ' + pic

        os.system(command)

    def mac(self):
        """
        TODO 增加mac自动切换壁纸
        :return:
        """
        address = '/Users/qingliu/study/auto-wallpaper/wallpaper/AerialPantanal_EN-AU7117581218.jpg'
        cmd = "osascript -e \"tell application \\\"Finder\\\" to set desktop picture to POSIX file \\\"" + address + "\\\"\""
        print(cmd)
        os.system(cmd)
        # 命令未生效，待排查

    def windows(self):
        """
        TODO 增加windows自动切换壁纸
        :return:
        """
        pass
