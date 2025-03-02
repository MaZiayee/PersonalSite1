from django.shortcuts import render,get_object_or_404
from blog.models import Post,Comment
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from blog.forms import CommentForm
from django.contrib import messages
# Create your views here.

def blog_home(request,**kwargs):
    posts = Post.objects.filter(status=1)
    if kwargs.get('author_username') != None:
        posts = posts.filter(author__username = kwargs['author_username'])

    posts = Paginator(posts,5)
    try:
        page_number = request.GET.get('page')
        posts = posts.get_page(page_number)
    except PageNotAnInteger:
        posts = posts.get_page(1)
    except EmptyPage:
        posts = posts.get_page(1)
    
    context = {'posts':posts}
    return render(request,'blog/blog-list.html',context)

def blog_details(request,pid):
        if request.method == 'POST':
            form = CommentForm(request.POST)
            if form.is_valid():
                form.save()
                messages.add_message(request,messages.SUCCESS,'متشکر از پیام شما.')
            else:
                messages.add_message(request,messages.ERROR,'مشکلی پیش آمده! لطفا مجدد تلاش کنید.')
        form = CommentForm()
        post = get_object_or_404(Post,pk=pid,status=1)
        comments = Comment.objects.filter(post=post.id,approved=True).order_by('-created_date')
        form = CommentForm()
        previous_post = Post.objects.filter(id__lt=post.id,status=1).order_by('-id').first()
        next_post = Post.objects.filter(id__gt=post.id,status=1).order_by('id').first()
        context = {'post':post,'comments':comments,'form':form, 'previous_post': previous_post, 'next_post': next_post}
        return render(request,'blog/blog-details.html',context)

#def r_post(request):
 #   rposts = Post.objects.filter(status=1)[:3]
  #  context2 = {'rposts':rposts}
#    return render(request,'blog/blog-details.html',context2)

def blog_category(request,cat_name):
    posts = Post.objects.filter(status=1)
    posts = posts.filter(category__name=cat_name)
    posts = Paginator(posts,5)
    try:
        page_number = request.GET.get('page')
        posts = posts.get_page(page_number)
    except PageNotAnInteger:
        posts = posts.get_page(1)
    except EmptyPage:
        posts = posts.get_page(1)
    context = {'posts':posts}
    return render(request,'blog/blog-list.html',context)

def blog_search(request):
    posts = Post.objects.filter(status=1)
    if request.method == 'GET':
        if s := request.GET.get('s'):
            posts = posts.filter(content__contains=s)
            
    context = {'posts':posts}
    return render(request,'blog/blog-list.html',context)