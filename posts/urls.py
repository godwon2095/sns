from django.urls import path
from .views import *

app_name = "posts"
urlpatterns = [
    path('new/', new, name="new"),
    path('create/', create, name="create"),
    path('<int:id>/edit/', edit, name="edit"),
    path('<int:id>/update/', update, name="update"),
    path('<int:id>/delete/', delete, name="delete"),

    #likes
    path('<int:post_id>/like_toggle/', like_toggle, name="like_toggle"),
]
