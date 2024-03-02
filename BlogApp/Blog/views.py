from django.shortcuts import render,redirect
from django.urls import reverse   ##!!!!!!1
from .models import Blog,Category
def home(request):
    
    # b1 = Blog(title="deneme",image="1.jpg",description="deneme",is_active=True,is_home=True)
    # b1.save()

    blogs=Blog.objects.filter(is_home=True)
    return render(request,"blog/index.html",{"blogs":blogs})

def blogs(request):
    blog=Blog.objects.all()
    categories=Category.objects.all()

    return render(request,"blog/blogs.html",{"blogs":blog,"categories":categories})


def blog_details(request,slug):
    if request.user.is_authenticated:
        blog=Blog.objects.get(slug=slug)
        return render(request,"blog/details.html",{"item":blog})
    else:
        login_url = reverse('login') + '?next=' + request.path          # reverse= login isimli url'yi URL sekline geri döndürüyo bkz: account/login 
                                                                        #--> account/login?next=/blog/pair-programing
        return redirect(login_url)

def blogs_by_category(request,slug):
    category=Category.objects.get(slug=slug)
    blogs=Blog.objects.filter(category=category)

    categories=Category.objects.all()
    return render(request,"blog/blogs_by_category.html",{"blogs":blogs,"categories":categories,"slug":slug})