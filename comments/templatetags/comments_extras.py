from django import template
from ..forms import CommentForm

"""
Happy围观项目comments应用自定义模板标签代码
"""

register = template.Library()


@register.inclusion_tag('comments/inclusions/_form.html', takes_context=True)
def show_comment_form(context, post, form=None):
    """
    渲染评论表单
    :param context: 父模板的上下文，这里暂时不需使用
    :param post: 评论表单对应的文章
    :param form: 评论表单实例
    :return: 文章的评论表单，字典类型('form': comments_form,   'post': post_value)
    """
    if form is None:
        form = CommentForm()
    return{
        'form': form,
        'post': post,
    }


@register.inclusion_tag('comments/inclusions/_list.html', takes_context=True)
def show_comments(context, post):
    """
    展示一篇文章的全部评论内容
    :param context: 父模板的上下文，这里暂时不需使用
    :param post: 文章实例
    :return: 该文章对应是评论是相关信息，字典类型('comment_count': comment_count_value,   'comment_list': comment_list)
    """
    # 使用comment_set属性获取文章有关的评论
    # 后续改进：增加按喜欢数量排列
    comment_list = post.comment_set.all()
    comment_count = comment_list.count()   # 获取评论数量
    return{
        'comment_count': comment_count,
        'comment_list': comment_list,
    }
