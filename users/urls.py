from django.urls import path
from .views import *

app_name = "users"
urlpatterns = [
    path('<int:id>/', show, name="show"),
    path('<int:id>/update/', update, name="update"),
    path('<int:id>/follow_toggle/', follow_toggle, name="follow_toggle"),
]
