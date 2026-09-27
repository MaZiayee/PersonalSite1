from django.urls import path , include
from website.views import *

app_name = 'website'

urlpatterns = [
    path('',home, name = 'homepage'),
]