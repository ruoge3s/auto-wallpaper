# Auto Wallpaper

## v2.0

1. 使用linux Crontab任务，每隔一段时间切换壁纸
2. 手动使用壁纸加载命令

## 运行环境
- Python3.7

## 操作命令
- 下载必应壁纸命令
```bash
python main.py bing:download
```

- 设置壁纸命令
```bash
python main.py wallpaper:deepin
```

## Linux定时任务
```text
*/3 * * * *  /dir/venv/bin/python /dir/auto-wallpaper/main.py wallpaper:deepin
```
> 每隔三分钟自动切换壁纸

## Todo

- [ ] 壁纸源增加[unsplash](https://unsplash.com/)和[pexels](https://www.pexels.com/)
- [ ] 增加壁纸拼接功能，拼接多个不同尺寸的壁纸拼接为一张进行显示
- [ ] 在壁纸上动态添加日历
- [ ] 其他linux发行版壁纸切换
- [ ] MacOS壁纸切换
- [ ] Windows10壁纸切换
