from django import forms
from .models import Comment

"""
Happy围观项目评论表单设计
"""


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment   # 指定表单对应的数据库模型
        fields = ['name', 'email', 'url', 'text']   # 表单显示的字段
