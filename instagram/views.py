from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.views import logout
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='/accounts/login/')
def entry(request):
    return render(request, "entry.html")

@login_required(login_url='/accounts/login/')
def profile(request):
    return render(request, "profile.html")