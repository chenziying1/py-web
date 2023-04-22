# -*- coding: utf-8 -*-
# time:2023/4/16 8:34
# file exception.py
# outhor:czy
# email:1060324818@qq.com
from werkzeug import Response

from cz框架.cz import ERROR_MAP


class HahaException(Exception):
    """异常类基类
    """

    def __init__(self, code='', message='Error'):
        self.code = code  # 异常编号
        self.message = message  # 异常信息

    def __str__(self):
        return self.message  # 当作为字符串使用时，返回异常信息


class EndpointExistsError(HahaException):
    """endpoint 节点已存在触发此异常
    """

    def __init__(self, message='Endpoint exists.'):
        super().__init__(message)


class URLExistsError(HahaException):
    """URL 路由已存在触发此异常
    """

    def __init__(self, message='URL exists.'):
        super().__init__(message)


# 文件未找到
class FileNotExistsError(HahaException):
    def __init__(self, code='2', message='File not found'):
        super(FileNotExistsError, self).__init__(code, message)


# 权限不足
class RequireReadPermissionError(HahaException):
    def __init__(self, code='13', message='Require read permission'):
        super().__init__(code, message)


# 不支持的请求方法
class InvalidRequestMethodError(HahaException):
    def __init__(self, code='401', message='Unknown or unsupported request method'):
        super().__init__(code, message)

# URL 未找到
class PageNotFoundError(HahaException):
    def __init__(self, code='404', message='Source not found'):
        super().__init__(code, message)


# URL 未知处理类型
class UnknownFuncError(HahaException):
    def __init__(self, code='503', message='Unknown function type'):
        super().__init__(code, message)

# ...

def capture(ERROR_MAP):
    """捕获异常的装饰器
    """

    def wrapper(f):
        def decorator(*args, **options):
            # 开始捕获异常
            try:
                # 尝试执行函数
                rep = f(*args, **options)
            except HahaException as e:
                # 当捕获到 HahaException 这个分类的异常时，判断下异常的编号
                # 如果不为空且关联再 ERROR_MAP 中，进行对应的处理，反之接着抛出
                if e.code in ERROR_MAP and ERROR_MAP[e.code]:
                    # 获取异常关联的结果
                    rep = ERROR_MAP[e.code]
                    # 如果异常编号小于 100，响应状态码统一设置为 500 服务端错误
                    status = int(e.code) if int(e.code) >= 100 else 500
                    # 判断结果是否一个响应体
                    # 如果不是应该就是自定义异常处理函数，调用它并封装为响应体返回
                    if isinstance(rep, Response) or rep is None:
                        return rep
                    data, content_type, status = rep()
                    return Response(data, content_type=content_type,
                            status=status)
                # 接着抛出没有对应处理的异常
                raise e
            # 返回函数执行正常的结果
            return rep
        # 返回装饰器
        return decorator
    return wrapper

# ...

def reload(code):
    """异常处理重装装饰器

    :param code: 异常编号，为了便于使用，编号为 int 类型
    """

    def decorator(f):
        # 替换 ERROR_MAP 中 异常编号关联的处理逻辑为所装饰的函数
        ERROR_MAP[str(code)] = f

    return decorator