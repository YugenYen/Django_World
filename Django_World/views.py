from django.shortcuts import render

def index(request):
    return render(request, "index.htm")

def login(request):
    return render(request, "login.htm")

def home(request):
    username = request.POST.get("username")
    return render(request, "home.htm", context={"username": username})