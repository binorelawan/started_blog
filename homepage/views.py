# from django.http import HttpResponse (THIS IS JUST START RUN TESTING WITHOUT HTML)
from django.shortcuts import render

# Create your views here.
def home_page(request):
    # return HttpResponse("Hello World!") (THIS IS JUST START RUN TESTING WITHOUT HTML)
    return render(request, 'homepage/home.html')

def about_page(request):
    return render(request, 'homepage/about.html')