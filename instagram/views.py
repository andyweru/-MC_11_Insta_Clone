from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.views import logout
from django.contrib.auth.decorators import login_required
from .models import *

# Create your views here.
@login_required(login_url='/accounts/login/')
def entry(request):
    return render(request, "entry.html")

@login_required(login_url='/accounts/login/')
def profile(request):
    current_user = request.user
    images = Image.objects.filter(user=current_user)

    return render(request, "profile.html", {"images":images})

@login_required(login_url='/accounts/login/')
def search(request):
    return render(request, "search.html")

@login_required(login_url='/accounts/login/')
def upload(request):
    return render(request, "upload.html")
        