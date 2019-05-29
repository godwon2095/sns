from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from .forms import *
from users.models import User
from django.db.models import Count


def new(request):
    context = {
            'form': PostForm(initial={'user': request.user})
    }
    return render(request, 'posts/new.html', context)


def create(request):
    context = {}
    if request.method == "POST":
       form = PostForm(request.POST, request.FILES or None)
       if form.is_valid():
           form.save()
    return redirect('home')


def edit(request, id):
    post = get_object_or_404(Post, pk=id)
    if 'id' is not None:
        context = {
            'post': post,
            'form': PostForm(instance=post)
        }
        return render(request, 'posts/edit.html', context)


def update(request, id):
    post = get_object_or_404(Post, pk=id)
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES or None, instance=post)
        if form.is_valid():
            form.save()

        return redirect('home')


def delete(request, id):
    post = get_object_or_404(Post, pk=id)
    if request.method == "POST":
        post.delete()

        return redirect('home')
    return redirect('home')


def follow_toggle(request, id):
    user = request.user
    followed_user = get_object_or_404(User, pk=id)
    if followed_user in user.followings.all():
        user.followings.remove(followed_user)
    else:
        user.followings.add(followed_user)

    return redirect('home')