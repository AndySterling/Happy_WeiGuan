from django.db import models
# from PIL import Image
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse
import markdown
from django.utils.html import strip_tags

"""
Happy围观项目数据库的模型定义
"""


class Category(models.Model):
    """
    分类表，表中有一个字段name和自动生成的id字段，用于存储分类名，不超过100个字符
    """
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name = "分类"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Tag(models.Model):
    """
    标签表，表中有一个字段name和自动生成的id字段，用于存储标签名，不超过100个字符
    """
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name = "标签"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


def user_directory_path(instance, filename):
    # 文件将被上传到 MEDIA_ROOT/user_<id>/<filename>
    return f"user_{instance.user.id}/{filename}"


# image_height = models.PositiveIntegerField(null=True, blank=True)   # 图像高度
# image_width = models.PositiveIntegerField(null=True, blank=True)   # 图像宽度


class Post(models.Model):
    """
    文章表，相关字段解释如下：

    title: 文章标题

    body: 文章正文

    image: 文章图片，可以为空

    create_time: 文章创建时间

    modified_time: 文章最近修改时间

    excerpt: 文章摘要，可以为空，最长为200个字符

    category: 文章分类，作为外键，引用Category表的name字段

    tags: 文章标签，与Tag表是多对多关系，可以为空

    author: 文章作者
    """
    title = models.CharField("标题", max_length=100)
    body = models.TextField("正文")

    # 目前上传图片功能不能正常实现，后续实现Markdown时会实现，可能需要删除该字段
    # image = models.ImageField(upload_to=user_directory_path, height_field=image_height, width_field=image_width, blank=True, null=True)

    created_time = models.DateTimeField("创建时间", default=timezone.now)
    modified_time = models.DateTimeField("修改时间")
    excerpt = models.CharField("摘要", max_length=200, blank=True, help_text="若不填写，则自动选取正文前六十个字符作为摘要")
    category = models.ForeignKey(Category, verbose_name="分类", on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag, verbose_name="标签", blank=True)
    author = models.ForeignKey(User, verbose_name="作者", on_delete=models.CASCADE)

    class Meta:
        # 设置模型后台显示名称
        verbose_name = "文章"
        verbose_name_plural = verbose_name
        # 指定排序方式(先按created_time降序排序，若时间相同则按title排序)
        ordering = ['-created_time', 'title']

    # 下面为后续开发新增方向
    # 浏览量：
    # 评论：comments（或许需要设计一个评论表）

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.modified_time = timezone.now()

        if self.excerpt is None:
            # 若用户没有输入摘要，自动选取正文前60个字符作为摘要
            md = markdown.Markdown(extensions=[
                'markdown.extensions.extra',
                'markdown.extensions.codehilite',
            ])
            self.excerpt = strip_tags(md.convert(self.body))[:60]  # 将去除html标签的文章正文的前60个字符作为摘要

        super().save(*args, **kwargs)

    def get_absolute_url(self):
        """
        反向解析文章的URL，将blog.urls中'posts/int:pk/'的'int:pk'替换为文章的主键pk
        :return:解析后的URL
        """
        return reverse('blog:detail', kwargs={'pk': self.pk})


# class User(models.Model):
#     """
#     用户表，相关字段解释如下：
#
#     name: 用户名，不超过100歌字符
#
#     birthday: 用户生日
#
#     likes: 用户收到的喜欢数量
#     """
#     name = models.CharField(max_length=100)
#     birthday = models.DateTimeField(blank=True)
#     likes = models.PositiveIntegerField()
#
#     # 后续开发新增方向
#     # 简介/个性签名
#     # 头像图片
#     # 账户密码之类的
#     # 粉丝数相关的
