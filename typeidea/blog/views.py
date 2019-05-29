from django.shortcuts import render
from django.http import HttpResponse

from .models import Post, Tag
# Create your views here.


def post_list(request, category_id=None, tag_id=None):
    if tag_id:
        try:
            tag = Tag.objects.get(id=tag_id)
        except Tag.DoesNotExist:
            post_li = []
        else:
            post_li = tag.post_set.filter(status=Post.STATUS_NORMAL)
    else:
        post_li = Post.objects.filter(status=Post.STATUS_NORMAL)
        if category_id:
            post_li = post_li.filter(category_id=category_id)

    return render(request, 'blog/list.html', context={'post_list': post_li})


def post_detail(request, post_id):
    try:
        post = Post.objects.get(id=post_id)
    except Post.DoesNotExist:
        post = None
    return render(request, 'blog/detail.html', context={'post': post})
