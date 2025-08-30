from django.contrib import admin
from .models import Category, Tag, Post


class PostAdmin(admin.ModelAdmin):
    # 文章列表显示信息
    list_display = ['title', 'created_time', 'modified_time', 'category', 'author']
    # 控制发布文章时展示的字段
    fields = ['title', 'body', 'excerpt', 'category', 'tags']

    def save_model(self, request, obj, form, change):
        # 通过request.user获取发布文章的用户名，将其赋值给obj.author，实现发布文章时自动填充作者名
        obj.author = request.user
        super().save_model(request, obj, form, change)


# 注册创建的模型
admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Post, PostAdmin)
