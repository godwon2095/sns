from django.shortcuts import render
from posts.models import Post
from django.db.models import Count, Avg

def home(request):
    user = request.user
    posts = Post.objects.all().order_by('-created_at').annotate(likes_count=Count('likes'))
    context = {
        'user': user,
        'posts': posts
    }
    return render(request, 'home.html', context)