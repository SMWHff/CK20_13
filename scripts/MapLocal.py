# !/usr/bin python3
# -*- encoding: utf-8 -*-
# @Author     : SMWHff
# @Email      : SMWHff@163.com
# @IDE        : PyCharm
# @Project    : CK20_13
# @File       : MapLocal.py
# @Time       : 2021/10/22 23:22
import os
from mitmproxy import http

# 获取当前文件所在目录
dir_path = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))


def request(flow: http.HTTPFlow):
    url = flow.request.pretty_url
    if "quote.json" in url and 'x=' in url:
        with open(dir_path + r"\data\quote.json", "r", encoding='utf-8') as f:
            flow.response = http.Response.make(
                200,
                f.read(),
                {'name': 'value'}
            )
