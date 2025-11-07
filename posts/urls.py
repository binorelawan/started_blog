from django.urls import path
from . import views

# Memberikan tanda bahwa urls di file ini digunakan didalam folder app "posts"
app_name = 'posts'

urlpatterns = [
    # List of blog post page
    path("", views.posts_list, name="list"),
    # Detail blog post page
    path("<slug:slug>", views.post_page, name="page"),
    # Create blog post page
    path("new-post/", views.post_new, name="new-post"),
    # Edit blog post page
    path("<int:pk>/edit-post/", views.post_edit, name="edit-post"),
    # delete blog post page
    path("<slug:slug>/delete-post", views.post_delete, name="delete-post"),
]
