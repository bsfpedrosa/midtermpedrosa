from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Post
from .forms import PostModelForm
from datetime import datetime

# Create your views here.

def index(request):
    context = {}
    posts = Post.objects.all()
    context['posts'] = posts
    return render(request,'index.html',context)

def detail(request, post_id):
    context = {}
    context['post'] = Post.objects.get(id=post_id)
    return render(request, 'detail.html', context)

def update(request, post_id):
    context = {}
    post = Post.objects.get(id=post_id)
    if request.method == 'POST':
        form = PostModelForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return HttpResponse('Post updated')
        else:
            context['form'] = form
            render(request, 'update.html', context)
    else:
        #post = Post.objects.get(id=post_id)
        context['form'] = PostModelForm(instance=post)
        #context['p_id'] = post_id
    return render(request, 'update.html', context)


def create(request):
    context = {}
    context['form'] = PostModelForm(initial={'date_created' : datetime.now(), 'date_updated' : datetime.now()})
    if request.method == 'POST':
        form = PostModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/post/')
        else:
            context['form'] = form
            render(request, 'create.html', context)
    else:
        return render(request, 'create.html', context)

def comment(request):
    context = {}
    context['form'] = PostModelForm(initial={'date_created' : datetime.now()})
    if request.method == 'POST':
        form = PostModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/post/detail.html')
        else:
            context['form'] = form
            render(request, 'comment.html', context)
    else:
        return render(request, 'comment.html', context)
