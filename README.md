# Auto Wallpaper

## v2.0

1. 使用linux Crontab任务，每隔一段时间切换壁纸
2. 手动使用壁纸加载命令

## 运行环境
- Python3.7
- 扩展(无)

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

## TODO

- [ ] 壁纸源增加[unsplash](https://unsplash.com/)和[pexels](https://www.pexels.com/)
- [ ] MacOS壁纸切换
- [ ] Windows10壁纸切换
- [ ] 在壁纸上动态添加日历