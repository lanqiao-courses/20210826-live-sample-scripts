"""
1. 三行代码极简版
2. 显示数据更新距现在的时间
"""

import requests
from datetime import datetime

r = requests.get(
    url="https://api.seniverse.com/v3/weather/now.json?key=S0Nc7tJSfrZwBI400&location=hangzhou&language=zh-Hans&unit=c"
).json()["results"][0]

# 计算距离现在的时间差
now = datetime.now()
update_time = datetime.fromisoformat(r["last_update"][:-6])
timedelta = now - update_time
minutes = timedelta.seconds // 60

print(
    f"{r['location']['name']}市, {r['now']['text']}, {r['now']['temperature']} 度, {minutes} 分钟前更新。"
)
