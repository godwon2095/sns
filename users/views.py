from django.shortcuts import render, redirect, get_object_or_404
from .models import User
from .forms import *
from django.views.generic import UpdateView


def show(request, id):
    user = get_object_or_404(User, pk=id)
    context = {
        'user': user
    }
    return render(request, 'users/show.html', context)


def update(request, id):
    user = get_object_or_404(User, pk=id)
    if user != request.user:
        return redirect('home')
    context = {
        'user': user,
        'form': UserChangeForm(instance=user)
    }
    if request.method == "POST":
        form = UserChangeForm(request.POST, request.FILES or None, instance=user)
        if form.is_valid():
            form.save()
        return redirect('home')
    
    return render(request, 'users/update.html', context)


def follow_toggle(request, id):
    user = request.user
    if user.is_anonymous:
        return redirect('account_login')
    followed_user = get_object_or_404(User, pk=id)

    is_follower = user in followed_user.followers.all()

    if is_follower:
        user.followings.remove(followed_user)
    else:
        user.followings.add(followed_user)

    return redirect('home')