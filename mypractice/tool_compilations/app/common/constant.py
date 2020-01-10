# -*- coding=utf-8 -*-


class Code:

    SUCCESS = 10000
    NOT_EXIST = 10001
    PARAM_ERROR = 10002
    NO_LOGIN = 10003
    INVALID_PARAMS = 12000
    WRONG_PASSWORD_OR_PHONE = 20004
    INVALID_FORMAT = 40004
    SYSTEM_ERROR = 50000

    msg = {
        SUCCESS: "成功",
        NOT_EXIST: "用户不存在",
        WRONG_PASSWORD_OR_PHONE: "手机号或密码错误",
        NO_LOGIN: '未登录',
        SYSTEM_ERROR: '系统错误',
        INVALID_PARAMS: "参数错误",
        INVALID_FORMAT: "文件不支持"
    }
