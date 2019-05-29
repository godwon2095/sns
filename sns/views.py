from django.shortcuts import render
from posts.models import Post

def home(request):
    user = request.user
    posts = Post.objects.all().order_by('-created_at')
    current_user_followings = None
    if user.is_authenticated:
        current_user_followings = user.followings.all()
    context = {
        'posts': posts,
        'current_user_followings': current_user_followings
    }
    return render(request, 'home.html', context)