import os
import subprocess
import random


def wallpaper(path):
    il = []
    if not os.path.isdir(path):
        exit()
    for filename in os.listdir(path):
        if os.path.isfile(path + "/" + filename):
            if filename.endswith('jpg'):
                il.append(filename)

    max = len(il) - 1
    if max < 0:
        print('Not image exist')
        exit()

    return il[random.randint(0, max)]


def run(dir_name):
    pid = subprocess.check_output(["pgrep", "dde-session"]).decode("utf-8").strip()  # 获取到dde-session的PID具体请看上面的那个问题与回答
    cmd = "grep -z DBUS_SESSION_BUS_ADDRESS /proc/" + pid + "/environ|cut -d= -f2-"

    os.environ["DBUS_SESSION_BUS_ADDRESS"] = subprocess.check_output(
        ['/bin/bash', '-c', cmd]).decode("utf-8").strip().replace("\0", "")

    command = F'gsettings set com.deepin.wrap.gnome.desktop.background picture-uri {dir_name}/{wallpaper(dir_name)}'

    os.system(command)

