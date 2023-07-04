from django.shortcuts import render, redirect
import speech_recognition as sr

# Create your views here.
def index(request):
    transcript = ""
    if request.method == "POST":
        print("we have a post!")

        # 如果file不在请求里面，重定向到提交的页面
        if request.FILES.get("file") == "":
            return redirect(request.get_full_path())

        # 如果提交的是空白文件
        file = request.FILES.get("file")
        if file == "":
            return redirect(request.get_full_path())

        if file:
            # 初始化
            recognizer = sr.Recognizer()
            # 将文件转化为sr模块可以理解的方式
            audiofile = sr.AudioFile(file)
            with audiofile as source:
                data = recognizer.record(source)

            text = recognizer.recognize_sphinx(data)
            # 使用Sphinx识别语音
            try:
                print("Sphinx识别结果为:" + text)
            except sr.UnknownValueError:
                print("无法识别音频")
            except sr.RequestError as e:
                print("识别错误; {0}".format(e))
            transcript = text

    return render(request,"frist.html", context={"transcript":transcript})


"""
总结资料：
https://zhuanlan.zhihu.com/p/92604225
https://www.cnblogs.com/zhe-hello/p/13273523.html
https://cdkm.com/cn/mp3-to-wav#:~:text=1%EF%BC%9A%E9%80%89%E6%8B%A9%E5%A4%9A%E4%B8%AA%E6%9C%AC%E5%9C%B0MP3%E6%96%87%E4%BB%B6%E6%88%96%E8%BE%93%E5%85%A5%E5%9C%A8%E7%BA%BFMP3%E6%96%87%E4%BB%B6%E7%9A%84URL%E3%80%82,2%EF%BC%9A%E9%80%89%E6%8B%A9WAV%E4%BD%9C%E4%B8%BA%E7%9B%AE%E6%A0%87%E6%A0%BC%E5%BC%8F%E5%B9%B6%E8%AE%BE%E7%BD%AE%E8%BD%AC%E6%8D%A2%E9%80%89%E9%A1%B9%EF%BC%88%E5%8F%AF%E9%80%89%EF%BC%89%E3%80%82%203%EF%BC%9A%E7%82%B9%E5%87%BB%E2%80%9C%E5%BC%80%E5%A7%8B%E8%BD%AC%E6%8D%A2%E2%80%9D%E6%8C%89%E9%92%AE%E5%B0%86MP3%E6%96%87%E4%BB%B6%E5%9C%A8%E7%BA%BF%E6%89%B9%E9%87%8F%E8%BD%AC%E6%8D%A2%E4%B8%BAWAV%E6%96%87%E4%BB%B6%E3%80%82
https://blog.csdn.net/HowToPause/article/details/127457904
https://www.yisu.com/zixun/176807.html#:~:text=%E6%80%8E%E4%B9%88%E5%9C%A8django%E4%B8%AD%E5%88%A9%E7%94%A8request%20%E8%8E%B7%E5%8F%96%E6%B5%8F%E8%A7%88%E5%99%A8%E5%8F%82%E6%95%B0%201%201.%20url%3A%20%E9%9C%80%E8%A6%81%E6%AD%A3%E5%88%99%E5%8E%BB%E5%8C%B9%E9%85%8D%20url%20%28r%27%5Eindex%2F,3%203.%20%E8%AF%B7%E6%B1%82%E4%BD%93%20...%204%204.%20%E6%8A%A5%E6%96%87%E5%A4%B4%20
https://www.cnblogs.com/hao-guo/p/12672224.html
https://blog.csdn.net/sinat_33255495/article/details/124958969

后期要改的问题太多了：
呼呼，页面美化，输入语音然后转化为文字，自动翻译输出，或者按照命令执行
"""
