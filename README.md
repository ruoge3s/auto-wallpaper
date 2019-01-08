# Deepin Auto Change Wallpaper

## v1.0

1. 使用linux Crontab任务，每隔一段时间切换壁纸
2. 手动使用壁纸加载命令

## 运行环境
- Python3
- 扩展(无)

## 操作命令
- 下载必应壁纸命令
```bash
python main.py load
```

- 设置壁纸命令
```bash
python main.py change
```

## 定时任务
```text
*/3 * * * *  /dir/venv/bin/python /dir/auto-wallpaper/main.py change
```
> 每隔三分钟自动切换壁纸