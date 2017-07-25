# -*- coding:utf-8 -*-

import time


def application(environ, start_response):
    status = "200 OK"
    headers = [
        ("Content-Type", "text/plain;charset=UTF-8"),
    ]

    start_response(status, headers)

    return "当前时间: "+time.ctime()
