from django.shortcuts import render

# Create your views here.
def entry(request):
    return render(request, "entry.html")