from django.db.models import *
from users.models import User


class TimeStampedModel(Model):
    created_at = DateTimeField(auto_now_add=True)
    updated_at = DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Post(TimeStampedModel):
    user = ForeignKey(User, on_delete=CASCADE)
    title = CharField(max_length=100)
    content = TextField()
    view_count = IntegerField(default=0)
    image = ImageField(upload_to="img/")
    likes = ManyToManyField(User, related_name="liked_users")

    def __str__(self):
       return self.title

    def comments(self):
        return Comment.objects.filter(post=self)


class Comment(TimeStampedModel):
    user = ForeignKey(User, on_delete=CASCADE)
    post = ForeignKey(Post, on_delete=CASCADE)
    message = TextField()

    def __str__(self):
        return self.message