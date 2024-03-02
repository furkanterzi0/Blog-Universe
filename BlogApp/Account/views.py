from django.shortcuts import redirect, render
from django.contrib.auth import authenticate , login as authLogin , logout as authLogout
from django.contrib.auth.models import User
from Blog.models import Blog

def login(request):
    if request.user.is_authenticated:
        blogs=Blog.objects.filter(is_home=True)
        return render(request,"blog/index.html",{"blogs":blogs})
        

    if request.method == "GET":
        next_url = request.GET.get("next", "/")
        return render(request, "account/login.html", {"next_url": next_url})
    
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            authLogin(request, user)
            return redirect(request.POST.get("next_url"))
        else:
            return render(request, "account/login.html", {"error": "Username or password is invalid", "username": username})
    
    return render(request, "account/login.html")

def register(request):
    if request.user.is_authenticated:
        blogs=Blog.objects.filter(is_home=True)
        return render(request,"blog/index.html",{"blogs":blogs})
    
    if request.method=="POST":
        name = request.POST["name"]
        surname = request.POST["surname"]
        email = request.POST["email"]
        username = request.POST["username"]
        password = request.POST["password"]

        if User.objects.filter(email=email).exists():
            return render(request,"account/register.html",{"error":"email already using"})
        
        if User.objects.filter(username=username).exists():
            return render(request,"account/register.html",{"error":"username already using"})
        
        User.objects.create_user(username=username,email=email,password=password,first_name=name,last_name=surname)
        return redirect('login')
    
    return render(request,"account/register.html")


def logout(request):
    authLogout(request)
    return redirect("home")