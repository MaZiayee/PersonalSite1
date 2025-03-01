from django.shortcuts import render, redirect
from django.http import HttpResponse
from blog.models import Post
from website.models import Contact
from website.forms import ContactForm
from django.contrib import messages
from django.http import FileResponse
import os
from django.conf import settings

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

    context = {'posts':posts, 'form':form}
    return render(request,'website/index.html',context)


def download_pdf(request):
    file_path = os.path.join(settings.MEDIA_ROOT, 'pdfs', 'ziayee.pdf')  # Adjust the path
    return FileResponse(open(file_path, 'rb'), as_attachment=True, filename='ziayee.pdf')

