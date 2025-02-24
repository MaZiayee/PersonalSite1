from django.shortcuts import render, redirect
from django.http import HttpResponse
from blog.models import Post
from website.models import Contact
from website.forms import ContactForm
from django.contrib import messages

# Create your views here.

def home(request):
    posts = Post.objects.filter(status=1)[:3]
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request,messages.SUCCESS,'متشکر از پیام شما! بزودی با شما تماس خواهم گرفت.')
            return redirect("website:homepage")
        else:
            messages.add_message(request,messages.ERROR,'مشکلی پیش آمده! لطفا مجدد تلاش کنید.')
            return redirect("website:homepage")
    form = ContactForm()
    print(messages)

    context = {'posts':posts, 'form':form}
    return render(request,'website/index.html',context)


