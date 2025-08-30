from django.urls import path
from . import views

"""
comments应用绑定不同的URL到对应的处理函数
"""

app_name = 'comments'
urlpatterns = [
    path('comment/<int:post_pk>', views.comment, name='comment'),
]