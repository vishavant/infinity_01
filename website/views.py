from django.shortcuts import render

# Create your views here.


def index(request):
    
    return render(request, "website/index.html")


def assignment1(request):
    return render(request, "website/assignment1.html")


def homepage(request):
    return render(request ,"website/homepage.html")