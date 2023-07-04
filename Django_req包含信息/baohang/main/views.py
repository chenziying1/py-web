from django.shortcuts import render

# Create your views here.
def index(request):

    """
    1  HttpRequest.scheme 　     请求的协议，一般为http或者https，字符串格式(以下属性中若无特殊指明，均为字符串格式)
    2  HttpRequest.body  　　    http请求的主体，二进制格式。
    3  HttpRequest.path             所请求页面的完整路径(但不包括协议以及域名)，也就是相对于网站根目录的路径。
    4  HttpRequest.path_info     获取具有 URL 扩展名的资源的附加路径信息。相对于HttpRequest.path，使用该方法便于移植
    """

    print(request.scheme)
    print(request.body)
    print(request.path)
    print(request.path_info)

    """
    
    """


    return render(request,"frist.html")