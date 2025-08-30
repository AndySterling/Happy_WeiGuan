from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Post, Category, Tag
import markdown
import re
from django.utils.text import slugify
from markdown.extensions.toc import TocExtension

"""
Happy围观项目视图处理
"""


def index(request):
    """
    展示首页
    :param request: HTTP请求
    :return: 展示模板内容（'blog/index.html'），其中post_list为所有文章
    """
    post_list = Post.objects.all()
    return render(request, 'blog/index.html', context={'post_list': post_list})


def detail(request, pk):
    """
    展示文章内容
    :param request: HTTP请求
    :param pk: 文章id
    :return: 展示模板内容（'blog/detail.html'）
    """
    post = get_object_or_404(Post, pk=pk)   # 传入的pk在Post中存在时，就返回对应的记录，否则返回404错误
    # 实例化markdown.Markdown对象
    md = markdown.Markdown(extensions=[
        'markdown.extensions.extra',
        'markdown.extensions.codehilite',
        TocExtension(slugify=slugify),   # 处理标题的URL，使其支持中文
    ])
    post.body = md.convert(post.body)   # 利用md对象将markdown格式的文章正文解析成html文本
    m = re.search(r'<div class="toc">\s*<ul>(.*)</ul>\s*</div>', md.toc, re.S)   # 正则表达式匹配<ul>标签内的内容，若不为空，证明目录不为空
    post.toc = m.group(1) if m is not None else ''   # 若目录不为空，添加文章目录，为动态添加
    return render(request, 'blog/detail.html', context={'post': post})


def archive(request, year, month):
    """
    根据年、月返回归档的文章
    :param request: HTTP请求
    :param year: 年份
    :param month: 月份
    :return: 展示模板内容（'blog/index.html'），其中post_list为该年、月发布的文章
    """
    post_list = Post.objects.filter(
        created_time__year=year,
        created_time__month=month
    )
    return render(request, 'blog/index.html', context={'post_list': post_list})


def category(request, pk):
    """
    展示某一分类下的文章
    :param request: HTTP请求
    :param pk: 文章类别的主键pk
    :return: 展示模板内容（'blog/index.html'），其中post_list为该分类下的文章
    """
    c = get_object_or_404(Category, pk=pk)
    post_list = Post.objects.filter(
        category=c
    )
    return render(request, 'blog/index.html', context={'post_list': post_list})


def tag(request, pk):
    """
    展示某一Tag下的文章
    :param request: HTTP请求
    :param pk: 文章主键pk
    :return: 展示模板内容（'blog/index.html'），其中post_list为该TAg下的文章
    """
    t = get_object_or_404(Tag, pk=pk)
    post_list = Post.objects.filter(
        tags=t
    )
    return render(request, 'blog/index.html', context={'post_list': post_list})
