from django.urls import path
from .views import *

app_name = "posts"
urlpatterns = [
    path('new/', new, name="new"),
    path('create/', create, name="create"),
    path('<int:id>/edit/', edit, name="edit"),
    path('<int:id>/update/', update, name="update"),
    path('<int:id>/delete/', delete, name="delete"),

    #comments
    path('<int:post_id>/create_comment/', create_comment, name="create_comment"),
    path('<int:comment_id>/delete_comment/', delete_comment, name="delete_comment"),

    #likes
    path('<int:post_id>/like_toggle/', like_toggle, name="like_toggle"),
]
