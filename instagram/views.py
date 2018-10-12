from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.views import logout
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import NewImageForm

# Create your views here.
@login_required(login_url='/accounts/login/')
def entry(request):
    images = Image.objects.all()
    return render(request, "entry.html", {"images":images[::-1]})

@login_required(login_url='/accounts/login/')
def profile(request):
    current_user = request.user
    images = Image.objects.filter(user=current_user)

    return render(request, "profile.html", {"images":images})

@login_required(login_url='/accounts/login/')
def search(request):
    
    if 'user' in request.GET and request.GET["user"]:
        search_term = request.GET.get("user")
        searched_users = Profile.find_username(search_term)
        message = f"{search_term}"

        return render(request, 'search.html',{"message":message,"users": searched_users})


    else:
        message = "User does not exist"
        return render(request, 'search.html',{"message":message})


@login_required(login_url='/accounts/login/')
def upload(request):
    current_user = request.user
    if request.method == 'POST':
        form = NewImageForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.save(commit=False)
            image.user = current_user
            image.save()
    else:
        form = NewImageForm()
    return render(request, 'upload.html', {"form": form})
        