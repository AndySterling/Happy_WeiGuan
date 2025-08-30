from django import template
from ..models import Post, Category, Tag

"""
Happy围观项目blog应用自定义模板标签代码
"""

register = template.Library()


@register.inclusion_tag('blog/inclusions/_recent_posts.html', takes_context=True)
# 将下面的函数装饰成register.inclusion_tag，即表明这是自定义的类型为inclusion_tag的模板标签
def show_recent_posts(context, num=5):
    """
    找出最近发布的文章
    :param context: 父模板的上下文，这里暂时不需使用
    :param num: 返回的文章个数，默认为5
    :return: 最近发布的文章列表(QuerySet)，字典类型('recent_post_list': post_list_value)，按发布时间降序排列
    """
    return{
        'recent_post_list': Post.objects.all()[:num],
    }


@register.inclusion_tag('blog/inclusions/_archives.html', takes_context=True)
def show_archives(context):
    """
    归档文章
    :param context: 父模板的上下文，这里暂时不需使用
    :return: 降序排列的文章发布的时间列表(对象类型为Python的date类型)（以月份为单位，已去重），字典结构('date_list': date_list_value)
    """
    return{
        'date_list': Post.objects.dates('created_time', 'month', order='DESC'),
    }


@register.inclusion_tag('blog/inclusions/_categories.html', takes_context=True)
def show_categories(context):
    """
    展示已有文章分类
    :param context: 父模板的上下文，这里暂时不需使用
    :return: 分类列表(QuerySet)，字典结构('category_list': categories_value)
    """
    return{
        'category_list': Category.objects.all(),
    }


@register.inclusion_tag('blog/inclusions/_tags.html', takes_context=True)
def show_tags(context):
    """
    展示已有文章标签
    :param context: 父模板的上下文，这里暂时不需使用
    :return: 标签列表(QuerySet)，字典结构('tag_list': tags_value)
    """
    return{
        'tag_list': Tag.objects.all(),
    }
