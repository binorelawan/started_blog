from django.shortcuts import render, redirect, get_object_or_404

# from django.http import HttpResponse (package ini hanya digunakan hanya testing awal agar tampil)

# Create your views here.
from .models import Post
from django.contrib.auth.decorators import login_required
from .forms import CreatePost

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
        form = CreatePost(request.POST, request.FILES) # 'request.FILES' untuk mengirimkan image.
        if form.is_valid():
            # save with user
            newpost = form.save(commit=False)
            newpost.author = request.user
            newpost.save()
            return redirect('posts:list')
    else:
        form = CreatePost()
    context = {'form': form}
    return render(request, 'posts/post_new.html', context)

@login_required(login_url="users:login")
def post_edit(request, pk):
    edit_post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = CreatePost(request.POST, instance=edit_post)
        if form.is_valid():
            edit_post = form.save(commit=False)
            edit_post.author = request.user
            edit_post.save()
            return redirect('posts:list')
    else:
        form = CreatePost(instance=edit_post)
    context = {'form': form}
    return render(request, 'posts/post_edit.html', context)

@login_required(login_url="users:login")
def post_delete(request, slug):
    delete_post = get_object_or_404(Post, slug=slug)
    if request.method == 'POST':
        delete_post.delete()
        return redirect('posts:list')

    context = {
        'delete_post': delete_post
    }
    return render(request, 'posts/post_delete.html', context)
