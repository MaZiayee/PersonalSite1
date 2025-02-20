from django.urls import path , include
from blog.views import *

app_name = 'blog'

urlpatterns = [
    path('',blog_home, name = 'blog-home'),
    path('<int:pid>',blog_details, name = 'blog-details'),
    path('category/<str:cat_name>',blog_category, name = 'category'),
    path('author/<str:author_username>',blog_home, name = 'author'),
]