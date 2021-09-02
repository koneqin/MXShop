from django.db import models

# Create your models here.

from datetime import datetime
from django.contrib.auth.models import AbstractUser


class UserProfile(AbstractUser):
    """用户信息"""
    SEX_MALE = 1
    SEX_FEMALE = 2
    SEX_UNKNOWN = 3
    SEX_CHOICES = (
        (SEX_MALE, '男'),
        (SEX_FEMALE, '女'),
        (SEX_UNKNOWN, '未知'),
    )

    name = models.CharField(verbose_name="姓名", max_length=30)
    birthday = models.DateField(verbose_name="生日", null=True, blank=True)
    gender = models.IntegerField(verbose_name='性别', choices=SEX_CHOICES, default=SEX_UNKNOWN)
    mobile = models.CharField(verbose_name='电话', max_length=11)
    email = models.EmailField(verbose_name='邮箱')

    class Meta:
        verbose_name = "用户信息"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.username


class VerifyCode(models.Model):
    """验证码"""
    code = models.CharField(verbose_name="验证码", max_length=10)
    mobile = models.CharField(verbose_name='电话号码', max_length=11)
    add_time = models.DateTimeField(verbose_name="添加时间", default=datetime.now)

    class Meta:
        verbose_name = "短信验证"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.code
