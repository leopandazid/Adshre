from django.urls import path
from . import views

urlpatterns= [
    path('feed',views.feed,name="feed"),
    path('make_post',views.make_post,name="make_post"),
]




