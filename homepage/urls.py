from django.urls import path
from . import views

app_name = "home"

urlpatterns = [
    path("", views.home_page, name="home_page"), # parameter 'name' is used for html templates
    path("about/", views.about_page, name="about_page"), # parameter 'name' is used for html templates
]