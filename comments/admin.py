from django.contrib import admin
from .models import Comment


# Register your models here.
class CommentAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'url', 'created_time', 'post']   # 个人认为应该增加text
    fields = ['name', 'email', 'url', 'text', 'post']    # 后续需要修改，理应只需要'text'


admin.site.register(Comment, CommentAdmin)

