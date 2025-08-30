from django.db import models
from django.utils import timezone

# Create your models here.


class Comment(models.Model):
    name = models.CharField("昵称", max_length=50)
    email = models.EmailField("邮箱")   # 个人认为可以去掉
    url = models.URLField("个人网址", blank=True)
    text = models.TextField("内容")
    created_time = models.DateTimeField("创建时间", default=timezone.now)
    post = models.ForeignKey('blog.Post', verbose_name="文章", on_delete=models.CASCADE)
    # 后续
    # 1.点赞
    # 2.ip显示（或为自定义虚拟ip）

    class Meta:
        verbose_name = "评论"
        verbose_name_plural = verbose_name
        # 指定排序方式
        ordering = ['-created_time']

    def __str__(self):
        return '{}: {}'.format(self.name, self.text[:20])
