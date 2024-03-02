from django.urls import path
from . import views

urlpatterns=[
    path('',views.home),
    path('home',views.home,name="home"),
    path('category/<str:slug>',views.blogs_by_category,name="category"),
    path('blogs',views.blogs,name="blogs"),
    path('blog/<str:slug>',views.blog_details,name="details")
]