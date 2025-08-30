from django.shortcuts import render, get_object_or_404, redirect
from blog.models import Post
from django.views.decorators.http import require_POST
from .forms import CommentForm
from django.contrib import messages


# Create your views here.
@require_POST
def comment(request, post_pk):
    """
    评论视图处理函数，若数据合法则保存评论表单数据；若数据不合法则展示错误
    :param request: 用户提交评论数据的HTTP POST请求
    :param post_pk: 评论绑定的文章的主键
    :return: 若数据合法，则返回文章详情页的url，若数据不合法，则渲染一个也买你展示表单的错误
    """
    post = get_object_or_404(Post, pk=post_pk)   # 获取被评论的文章
    form = CommentForm(request.POST)   # 生成绑定用户评论数据的表单

    if form.is_valid():
        # 数据合法
        user_comment = form.save(commit=False)   # commit=False用于生成Comment模型类实例，但不保存数据到数据库中
        user_comment.post = post
        user_comment.save()   # 保存评论数据进入数据库中

        # 使用add_message方法发送评论成功信息
        messages.add_message(request, messages.SUCCESS, "评论发表成功！", extra_tags='success')
        return redirect(post)   # 使用redirect函数重定向到post的详情页

    # 数据不合法
    context = {
        'post': post,
        'form': form,
    }
    messages.add_message(request, messages.ERROR, "评论发表失败！请根据提示重新修改后提交！", extra_tags='danger')
    return render(request, 'comments/preview.html', context=context)
