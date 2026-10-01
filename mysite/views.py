from django.shortcuts import render

def home(request):
    return render(request, "index.html")

def errors(request):
    return render(request, "errors.html")