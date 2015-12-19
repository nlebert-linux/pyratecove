from django.shortcuts import render
from blog.models import Category, Post


# Create your views here.
def post_list(request):
    posts = Post.objects.filter(is_published=True)

    context = {'posts': posts}
    return render(request, 'blog/post_list.html', context)


def post_detail(request, slug):
    post = Post.objects.get(slug=slug)

    context = {'post': post}
    return render(request, 'blog/detail.html', context)
