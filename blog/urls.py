from django.urls import path , include
from blog.views import *

app_name = 'blog'

urlpatterns = [
    path('',blog_home, name = 'blog-home'),
    path('blog-datails',blog_details, name = 'blog-details'),
]