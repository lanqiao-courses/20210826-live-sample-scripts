"""
1. 三行代码极简版
2. 显示数据更新距现在的时间
3. 基于本机 IP 地址获取当然城市
"""

import requests
from datetime import datetime

# 获取当前主机的公网 IP 所在经纬度
local = requests.get(
    "https://geo.ipify.org/api/v1?apiKey=at_NeAcGc4uTzDcs3UNY8X29vINZMPnH"
).json()
lat = local["location"]["lat"]
lng = local["location"]["lng"]

r = requests.get(
    url=f"https://api.seniverse.com/v3/weather/now.json?key=S0Nc7tJSfrZwBI400&location={lat}:{lng}&language=zh-Hans&unit=c"
).json()["results"][0]

# 计算距离现在的时间差
now = datetime.now()
update_time = datetime.fromisoformat(r["last_update"][:-6])
timedelta = now - update_time
minutes = timedelta.seconds // 60

print(
    f"{r['location']['name']}市, {r['now']['text']}, {r['now']['temperature']} 度, {minutes} 分钟前更新。"
)
