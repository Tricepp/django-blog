from django.urls import path
from django.shortcuts import render 
from blogging.views import list_view

path('posts/<int:post_id>/',
    detail_view,
    name="blog_detail"),

def list_view(request):
    published = Post.objects.exclude(published_date__exact=None)
    posts = published.order_by('-published_date')
    context = {'posts': posts}
    return render(request, 'list.html', context)
