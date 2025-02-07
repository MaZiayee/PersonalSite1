from django.shortcuts import render
from django.http import HttpResponse
from blog.models import Post

# Create your views here.

def home(request):
    posts = Post.objects.filter(status=1)
    context = {'posts':posts}
    return render(request,'website/index.html',context)

