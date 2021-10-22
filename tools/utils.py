# !/usr/bin python3
# -*- encoding: utf-8 -*-
# @Author     : SMWHff
# @Email      : SMWHff@163.com
# @IDE        : PyCharm
# @Project    : CK20_13
# @File       : utils.py
# @Time       : 2021/10/22 23:13
import os


class Utils:
    """
    实用工具类
    """

    @classmethod
    def get_root_path(cls):
        """
        获取项目根目录的绝对路径
        :return: 返回项目根目录路径
        """
        root_path = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))
        # 替换斜杠
        return root_path.replace("\\", "/")