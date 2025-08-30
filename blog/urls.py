from django.urls import path
from . import views

"""
Happy围观项目绑定不同的URL到对应的处理函数
"""

app_name = 'blog'   # 命名空间
urlpatterns = [
    path('', views.index, name='index'),    # 第一个参数是去掉域名后的剩余URL，第二个参数是处理函数，参数name的值将作为处理函数的别名
    path('posts/<int:pk>/', views.detail, name='detail'),   # 匹配形如"posts/1/"的URL，展示文章具体内容
    path('archives/<int:year>/<int:month>/', views.archive, name='archive'),   # 匹配形如"archives/2025/8/"的URL，展示该年月下归档的文章
    path('categories/<int:pk>/', views.category, name='category'),   # 匹配形如"categories/2/"的URL，展示该分类下的文章
    path('tags/<int:pk>/', views.tag, name='tag')   # 匹配形如"tags/1/"的URL，展示该Tag下的文章
]

