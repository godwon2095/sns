from django.db import models
from users.models import User
from share.timestamp import TimeStampedModel


class Post(TimeStampedModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    content = models.TextField()
    view_count = models.IntegerField(default=0)
    image = models.ImageField(upload_to="img/")
    likes = models.ManyToManyField(User, related_name="liked_users")

    def __str__(self):
       return self.title

    def comments(self):
        return Comment.objects.filter(post=self)


class Comment(TimeStampedModel):

    class Meta:
        ordering = ['-created_at']
        
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    message = models.TextField()

    def __str__(self):
        return self.message