from django.shortcuts import render, HttpResponse, redirect
from .models import Post
from .forms import PostForm


import json
import requests
# Create your views here.
def index(request):
    # create an instance of the form
    posts = Post.objects.all()

    form = PostForm()
    context = {
        "form"  : form,
        "posts" : posts,
    }
    return render(request, "ajaxify/index.html", context)


def insert(request):
    # print("REQUEST: " + request.POST)
    if request.method == "POST":
        # create new post and redirest to index route
        bound_post_form = PostForm(request.POST)
        print('POST: ', bound_post_form)
        if bound_post_form.is_valid():
            # create a new post and save it to the database
            post = Post.objects.create(title=request.POST['title'], message=request.POST['message'])
            print('New post created: ', post)

        # ---- OR ----- (Less safe way?) -- /
        # post = Post(title=request.POST['title'], message=request.POST['message'])
        # print('New post created: ', post)
        # post.save()

    # """
    #   We do this on both GET and POST requests
    #   Fetch all posts and render only the partial posts_index.html
    # """

    # context = {
    #     'posts' : Post.objects.all(),
    # }
    #
    # return render(request, 'ajaxify/index.html', context)

    return redirect('/')
