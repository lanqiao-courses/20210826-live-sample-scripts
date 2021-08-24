"""
1. 三行代码极简版
2. 显示数据更新距现在的时间
3. 基于本机 IP 地址获取当然城市
4. 规范代码，支持自动定位和指定城市天气实况
5. 添加到命令行别名
"""
import argparse
from typing import Mapping
import requests
from datetime import datetime


class Weather:
    def __init__(self, city: str):
        """手动指定城市或自动获取本机 IP 地址的城市
        - API 文档: https://geo.ipify.org
        """
        if city == None:
            # 如果不指定城市则自动定位，返回当前 IP 的经纬度
            local = requests.get(
                "https://geo.ipify.org/api/v1?apiKey=at_NeAcGc4uTzDcs3UNY8X29vINZMPnH"
            ).json()
            lat = local["location"]["lat"]
            lng = local["location"]["lng"]
            self.city = f"{lat}:{lng}"
        else:
            self.city = city

    def now(self):
        """获取指定城市的天气实况
        - API 文档:https://seniverse.yuque.com/docs/share/6947fcea-eec6-41c4-b7d7-7e9c01a5dc08
        """
        r = requests.get(
            url=f"https://api.seniverse.com/v3/weather/now.json?key=S0Nc7tJSfrZwBI400&location={self.city}&language=zh-Hans&unit=c"
        ).json()["results"][0]

        # 计算距离现在的时间差
        now = datetime.now()
        update_time = datetime.fromisoformat(r["last_update"][:-6])
        timedelta = now - update_time
        minutes = timedelta.seconds // 60

        print(
            f"📍 {r['location']['name']}市, {r['now']['text']}, {r['now']['temperature']} 度, {minutes} 分钟前更新。"
        )


parser = argparse.ArgumentParser(description="获取天气实况")
parser.add_argument("-c", "--city", default=None, help="指定城市英文名称")
args = parser.parse_args()
weather = Weather(args.city)
weather.now()
