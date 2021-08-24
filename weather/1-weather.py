"""
1. 三行代码极简版
"""
import requests

r = requests.get(
    url="https://api.seniverse.com/v3/weather/now.json?key=S0Nc7tJSfrZwBI400&location=hangzhou&language=zh-Hans&unit=c"
).json()["results"][0]

print(
    f"{r['location']['name']}市, {r['now']['text']}, {r['now']['temperature']} 度, 更新时间：{r['last_update']}"
)
