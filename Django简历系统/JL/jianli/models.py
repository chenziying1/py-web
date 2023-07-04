from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length=100, default="默认姓名")
    phone = models.CharField(max_length=100, default="默认电话号码")
    email = models.EmailField(default="default@example.com")
    message = models.CharField(max_length=100)
    jiaoyubeijing = models.TextField(default="默认教育背景")
    gongzhuojingli = models.TextField(default="默认工作经历")
    xiangmujingli = models.TextField(default="默认项目经历")
    jinengzhengshu = models.TextField(default="默认技能证书")
    file = models.ImageField(upload_to='static/images/', default="static/iamges/default.png")

    def __str__(self):
        return self.name






