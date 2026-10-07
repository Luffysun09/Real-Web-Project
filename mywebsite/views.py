from django.shortcuts import render

def home(request):
    return render(request, "index.html")

def success(request):
    return render(request, "success.html")
