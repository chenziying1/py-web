# -*- coding: utf-8 -*-
# time:2023/4/16 8:33
# file __init__.py.py
# outhor:czy
# email:1060324818@qq.com
import os
from werkzeug.serving import run_simple
from werkzeug.wrappers import Response
from cz框架.cz.emplate_engine import replace_template
from cz框架.cz.session import session, create_session_id
from cz框架.cz.wsgi_adapter import wsgi_app
#在这里我们遇到了cz.wsgi_adapter识别不出来的情况，加上文件夹名之后就可以了
import cz框架.cz.exception as exceptions
from cz框架.cz.helper import parse_static_key
from cz框架.cz.route import Route
import json


content_type = 'text/html; charset=UTF-8'

# 常见异常及其响应对象的映射关系
ERROR_MAP = {
    '2': Response('<h1>E2 Not Found File</h1>',
            content_type=content_type, status=500),
    '13': Response('<h1>E13 No Read Permission</h1>',
            content_type=content_type, status=500),
    '401': Response('<h1>401 Unknown or unsupported method.</h1>',
            content_type=content_type, status=401),
    '404': Response('<h1>404 Source Not Found.<h1>',
            content_type=content_type, status=404),
    '503': Response('<h1>503 Unknown function type.</h1>',
            content_type=content_type, status=503),
}

# 文件类型及其代号的映射关系
TYPE_MAP = {
    'css':  'text/css',
    'js': 'text/js',
    'png': 'image/png',
    'jpg': 'image/jpeg',
    'jpeg': 'image/jpeg'
}

#处理数据类型的数据结构
class ExecFunc:
    def __init__(self,func,func_type,**options):
        self.func = func #处理函数
        self.func_type = func_type #处理数据类型
        self.options = options #附带参数
        #在这里卡了大半天，主要是打错了opentions，却调用了options，初看之下根本发现不了

#模板引擎接口
def simple_template(path,**options):
    return replace_template(SYLFK, path, **options)

#路由重定向
def redirect(url,status_code = 302):
    response = Response('',status = status_code) #构建一个响应体
    response.headers['Location'] = url #将location参数设置为url 实现重定向
    return response

def render_json(data):
    """将响应体包装成响应对象并返回
    """
    # 默认响应体类型
    content_type = "text/plain"
    # 如果参数是 dict 或者 list 类型，则将其转换为 JSON 格式数据
    if isinstance(data, (list, dict)):
        data = json.dumps(data)
        # 定义响应体类型为 JSON 格式
        content_type = "application/json"
    content_type = '{}; charset=UTF-8'.format(content_type)
    # 返回封装完的响应体
    return Response(data, content_type=content_type, status=200)

def render_file(file_path, file_name=None):
    """根据文件路径创建响应对象，浏览器收到响应对象后显示下载文件的弹窗

    :param file_path: 文件路径（包含文件名）
    :param file_name: 文件名
    """

    # 判断服务器是否有该文件，没有则返回 404 错误
    if not os.path.exists(file_path):
        raise exceptions.FileNotExistsError #FileNotexistError 这个识别不出来，报错了
        return ERROR_MAP['404']

    # 判断是否有读取权限，没有则抛出权限不足异常
    if not os.access(file_path, os.R_OK):
        raise exceptions.RequireReadPermissionError

    with open(file_path, "rb") as f:
        content = f.read()

    # 如果没有设置文件名，则以 “/” 分割路径取最后一项作为文件名
    filename = file_name or file_path.split('/')[-1]

    # 封装响应报头，指定为附件类型为 attachment ，并定义下载的文件名
    headers = {
        'Content-Disposition': 'attachment; filename={}'.format(filename)
    }

    return Response(content, headers=headers, status=200)

class SYLFK:

    template_folder = 'templates' #存放本地模板文件的目录

    def __init__(self,static_folder='static'):
        self.host = "127.0.0.1"
        self.port = 8086
        self.url_map = {} #url与节点的映射
        self.static_map = {} #url与静态资源的映射
        self.function_map = {} #节点与静态资源的映射
        self.static_folder = static_folder #存放静态资源的本地文件夹
        self.route = Route(self) # 路由装饰器

    # 控制器加载
    def load_controller(self, controller):
        for rule in controller.url_map:
            self.bind_view(rule['url'],rule['view'],controller.name + '.' + rule['endpoint'])


    #视图处理
    def bind_view(self,url,view_class, endpoint):
        func = view_class.get_func(endpoint) #调用view中的方法创建一个视图函数并返回
        self.add_url_rule(url, func=func, func_type='view')

    #添加路由规则
    def add_url_rule(self,url,func,func_type,endpoint=None, **kw):

        if endpoint is None: #如果节点未命名，赋予处理函数的名字
            endpoint = func.__name__

        if url in self.url_map: #如果url已经存在，抛出url存在异常
            raise exceptions.URLExistsError

        if endpoint in self.function_map and func_type != 'static': # 如果类型不是静态资源，并且节点已存在，则抛出节点已存在异常
            raise exceptions.EndpointExistsError

        self.url_map[url] = endpoint #如果都没有问题，放进映射里
        self.function_map[endpoint] = ExecFunc(func,func_type,**kw) #添加处理函数的映射

    #处理静态文件
    def dispatch_static(self,static_path):

        if not os.path.exists(static_path): #如果静态文件不存在，返回404
            raise exceptions.PageNotFoundError
            return ERROR_MAP('404')

        key = parse_static_key(static_path) #获取后缀名
        file_type = TYPE_MAP.get(key)

        with open(static_path,'rb') as f:
            data = f.read()

        return Response(data,content_type=file_type)

    #路由
    def dispatch_request(self,request,status=200):
        headers = {
            'Server' : 'czy and zy web'
        }

        cookies = request.cookies  # 从请求中取出 Cookie
        if not 'session_id' in cookies:
            headers['Set-Cookie'] = 'session_id={}'.format(create_session_id())

        url = request.base_url.replace(request.host_url, '/') # 从 URL 中提取路径

        if url.startswith('/'+self.static_folder+'/'): #startswith检查是否是这个开头
            endpoint = 'static'
            url = url[1:]
        else:
            endpoint = self.url_map.get(url, None)

        if endpoint is None:
            raise exceptions.PageNotFoundError
            return ERROR_MAP['404']

        exec_function = self.function_map[endpoint]  # 获取节点对应的执行函数

        if exec_function.func_type == "route":  # 如果是get或者是post
            if request.method in exec_function.options.get('methods'):  # 判断是get还是post
                argcount = exec_function.func.__code__.co_argcount
                if argcount > 0:
                    rep = exec_function.func(request)
                else:
                    rep = exec_function.func()
            else:
                raise exceptions.InvalidRequestMethodError
                return ERROR_MAP['401']

        elif exec_function.func_type == 'view':
            # 所有视图处理函数都需要附带请求体来获取处理结果
            rep = exec_function.func(request)

        elif exec_function.func_type == 'static':  # 如果是静态文件
            return exec_function.func(url)

        else:
            # 返回 503 错误响应体
            # 抛出未知处理类型异常
            raise exceptions.UnknownFuncError
            return ERROR_MAP['503']

        content_type = 'text/html; charset=UTF-8' #响应体

        if isinstance(rep,Response): #是 Response 响应对象则直接返回，
            return rep

        # 返回一个符合wsgi格式的响应，被wsgi_adapter文件调用
        return Response(rep, content_type=content_type, headers=headers,
                        status=status) # 返回响应体

    #WSGI调用
    def __call__(self,environ,start_response):
        #调用了wsgi——adapter文件的wsgi_app方法，这里的关系我还有点混乱，看注释似乎是wsgi文件调用call方法并返回给用户
        return wsgi_app(self,environ=environ,start_response=start_response)


    #启动入口
    def run(self,host = None,port = None ,**options):
        for key,value in options.items(): #获取输入的参数并设置为自身的属性值
            setattr(self,key,value) #用于设置属性值，该属性不一定是存在的

        if host:
            self.host = host
        if port:
            self.port = port

        #要把静态资源相关的节点函数命名为 static
        self.function_map['static'] = ExecFunc(func=self.dispatch_static,func_type='static')

        #加载本地缓存的会话记录
        session.load_all_session()

        #传入参数 启动一个 WSGI 应用程序
        run_simple(hostname=self.host, port=self.port, application=self, **options)







