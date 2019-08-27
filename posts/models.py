from django.db import models
from users.models import User
from share.timestamp import TimeStampedModel
from django.utils.translation import ugettext_lazy as _


class Post(TimeStampedModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    content = models.TextField()
    view_count = models.IntegerField(default=0)
    image = models.ImageField(upload_to="img/")
    like_users = models.ManyToManyField(User,
                                        blank=True,
                                        related_name='like_users',
                                        through='Like')

    def __str__(self):
       return self.title

    @property
    def comments(self):
        return Comment.objects.filter(post=self)

    @property
    def likes_count(self):
        return self.like_users.count()


class Comment(TimeStampedModel):

    class Meta:
        ordering = ['-created_at']
        
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    message = models.TextField()

    def __str__(self):
        return self.message


class Like(TimeStampedModel):
    user = models.ForeignKey(User, verbose_name=_('작성자'), on_delete=models.CASCADE)
    post = models.ForeignKey(Post, verbose_name=_('게시글'), on_delete=models.CASCADE)

    class Meta:
        verbose_name = '게시글 좋아요'
        verbose_name_plural = '게시글 좋아요'
        unique_together = (
            ('user', 'post')
        )