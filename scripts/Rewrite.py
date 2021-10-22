# !/usr/bin python3
# -*- encoding: utf-8 -*-
# @Author     : SMWHff
# @Email      : SMWHff@163.com
# @IDE        : PyCharm
# @Project    : CK20_13
# @File       : Rewrite.py
# @Time       : 2021/10/22 12:27
import json
from mitmproxy import http

# 设置股票涨跌幅
global_percent = 0.00

def response(flow: http.HTTPFlow):
    global global_percent
    url = flow.request.pretty_url
    if "quote.json" in url and 'x=' in url:
        body = flow.response.content
        data = json.loads(body)
        n = data['data']['items_size']
        for i in range(n):
            data['data']['items'][i]['quote']['percent'] = global_percent
        flow.response.text = json.dumps(data)
