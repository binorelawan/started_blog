from django.shortcuts import render, redirect

# Membuat user registrasi formulir
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout

# Create your views here.
def register_view(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            # form.save() INI ADALAH UNTUK MENYIMPAN REGISTRASI AKUN
            login(request, form.save()) # INI ADALAH UNTUK MENYIMPAN REGISTRASI AKUN SEKALIGUS LOGIN AKUN
            return redirect("posts:list")
    else:
        form = UserCreationForm()

    context = {'form': form}
    return render(request, "users/register.html", context)

def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            # LOGIN HERE
            login(request, form.get_user())
            if 'next' in request.POST:
                return redirect(request.POST.get('next'))
            else:
                return redirect('posts:list')
    else:
        form = AuthenticationForm()

    context = {'form': form}
    return render(request, "users/login.html", context)
    
def logout_view(request):
    if request.method == "POST":
        logout(request)
        return redirect('posts:list')
        
