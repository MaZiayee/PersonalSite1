from django.shortcuts import render,get_object_or_404
from blog.models import Post
# Create your views here.

def blog_home(request):
    posts = Post.objects.filter(status=1)
    context = {'posts':posts}
    return render(request,'blog/blog-list.html',context)

def blog_details(request,pid):
    post = get_object_or_404(Post,pk=pid,status=1)
#    rposts = Post.objects.filter(status=1)[:3]
    context = {'post':post}
    return render(request,'blog/blog-details.html',context)

#def r_post(request):
 #   rposts = Post.objects.filter(status=1)[:3]
  #  context2 = {'rposts':rposts}
#    return render(request,'blog/blog-details.html',context2)

def blog_category(request,cat_name):
    posts = Post.objects.filter(status=1)
    posts = posts.filter(category__name=cat_name)
    context = {'posts':posts}
    return render(request,'blog/blog-list.html',context)