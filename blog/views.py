from django.shortcuts import render

# Create your views here.
from blog.models import Post


def home(request):
    post = Post.objects.all()
    return render(request,"home.html",{'post':post})

def about(request):
    return render(request,"about.html")

def contact(request):
    return render(request,"contact.html")