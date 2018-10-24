from django.shortcuts import render, HttpResponse, redirect
from .models import Post
from .forms import PostForm

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
        # print(request.POST)
        # print("*"*50)
        # print("TITLE: " + request.POST['title'])
        # print("MESSAGE: " + request.POST['message'])
        # print("*"*50)

        post = Post(title=request.POST['title'], message=request.POST['message'])
        post.save()

        # print(post)
    # print("POST: " + post)
    return redirect('/')
