from django.shortcuts import render

# Create your views here.

def feed(request):
    context={}
    return render(request, 'post/feed.html',context)

def make_post(request):
    context={}
    return render(request, 'post/make_post.html',context)
