from django.shortcuts import render, redirect

# from django.http import HttpResponse (package ini hanya digunakan hanya testing awal agar tampil)

# Create your views here.
from .models import Post
from django.contrib.auth.decorators import login_required
from . import forms

def posts_list(request):
    posts = Post.objects.all().order_by('-date')
    context = {'posts': posts}
    return render(request, 'posts/posts_list.html', context)

def post_page(request, slug):

    # return HttpResponse(slug) (ini hanya digunakan hanya testing awal agar tampil)

    post = Post.objects.get(slug=slug)
    context = {'post': post}
    return render(request, 'posts/post_page.html', context)

@login_required(login_url="users:login")
def post_new(request):
    if request.method == "POST":
        form = forms.CreatePost(request.POST, request.FILES) # 'request.FILES' untuk mengirimkan image.
        if form.is_valid():
            # save with user
            newpost = form.save(commit=False)
            newpost.author = request.user
            newpost.save()
            return redirect('posts:list')
    else:
        form = forms.CreatePost()
    context = {'form': form}
    return render(request, 'posts/post_new.html', context)