from django.urls import path
from . import views

# Memberikan tanda bahwa urls di file ini digunakan didalam folder app "posts"
app_name = 'posts'

urlpatterns = [
    path("", views.posts_list, name="list"),
    path("new-post/", views.post_new, name="new-post"),
    path("<slug:slug>", views.post_page, name="page"),
]
