from django.shortcuts import render
from django.http import HttpResponse

from config.models import SideBar
from .models import Post, Tag, Category
# Create your views here.


def post_list(request, category_id=None, tag_id=None):
    tag = None
    category = None

    if tag_id:
        post_li, tag = Post.get_by_tag(tag_id)
    elif category_id:
        post_li, category = Post.get_by_category(category_id)
    else:
        post_li = Post.latest_posts()

    context = {
        'category': category,
        'tag': tag,
        'post_list': post_li,
        'sidebars': SideBar.get_all(),
    }
    context.update(Category.get_navs())
    return render(request, 'blog/list.html', context=context)


def post_detail(request, post_id):
    try:
        post = Post.objects.get(id=post_id)
    except Post.DoesNotExist:
        post = None

    context = {
        'post': post,
        'sidebars': SideBar.get_all(),
    }
    context.update(Category.get_navs())
    return render(request, 'blog/detail.html', context=context)
