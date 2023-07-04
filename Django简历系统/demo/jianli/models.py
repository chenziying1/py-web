from django.db import models
from django.template.defaultfilters import slugify


class xingxi(models.Model):
    name = models.CharField(max_length=128, unique=True)
    birthdate = models.CharField(max_length=128, unique=True)
    classname = models.CharField(max_length=128, unique=True)
    hoby = models.CharField(max_length=128, unique=True)
    Personalstrengths = models.CharField(max_length=128, unique=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(xingxi, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = '信息'

    def __str__(self):
        return self.name
    
class Contact(models.Model):
    name = models.CharField(max_length=100,default="默认姓名")
    phone = models.CharField(max_length=100,default="默认电话号码")
    email = models.EmailField(default="default@example.com")
    message = models.CharField(max_length=100)
    jiaoyubeijing = models.TextField(default="默认教育背景")
    gongzhuojingli = models.TextField(default="默认工作经历")
    xiangmujingli = models.TextField(default="默认项目经历")
    jinengzhengshu = models.TextField(default="默认技能证书")
    file = models.ImageField(upload_to='static/images/',default="static/iamges/default.png")

    def __str__(self):
        return self.name

class Image(models.Model):
    title = models.CharField(max_length=200)
    file = models.ImageField(upload_to='images/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title




