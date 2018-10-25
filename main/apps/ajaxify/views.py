from django.shortcuts import render, HttpResponse, redirect
from .models import Post
from .forms import PostForm, ContactForm

from django.views.generic import View, ListView, CreateView, TemplateView, FormView


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

    """
      We do this on both GET and POST requests
      Fetch all posts and render only the partial posts_index.html
    """

    context = {
        'posts' : Post.objects.all(),
    }

    # return render(request, 'ajaxify/index.html', context)

    return redirect('/')


# // ---- CLASS BASED VIEWS ---- //

class Posts(View):
    def get(self, request, *args, **kwargs):
        return HttpResponse("Hi, There!")

class PostTemplateView(TemplateView):
    template_name = 'ajaxify/index.html'

    def get_context_data(self, **kwargs):
        form = PostForm(request.POST)
        context = super(PostTemplateView, self).get_context_data(**kwargs)
        context['posts'] = Post.objects.all()
        return context

class PostFormView(FormView):
    template_name = 'ajaxify/index.html'
    form_class = PostForm

    # def form_valid(self, form):
    #     post_ = Post.objects.create()
    #     form.save(for_post=post_)
    #     return redirect(post_)

class NewPostView(CreateView):

    def get(self, request):
        form = PostForm(request.POST)
        context = {
            'posts' : Post.objects.all(),
            'form'  : form
        }
        return render(request, 'ajaxify/index.html', context)


    def post(self, request):
        # create new post and redirest to index route
        bound_post_form = PostForm(request.POST)
        print('POST: ', bound_post_form)
        if bound_post_form.is_valid():
            # create a new post and save it to the database
            post = Post.objects.create(title=request.POST['title'], message=request.POST['message'])
            print('New post created: ', post)


        return redirect('posts')

class PostListView(ListView):
    model = Post
    context_object_name = 'posts'
    # queryset = Post.objects.all()
    template_name = "ajaxify/index.html"

    def get_context_data(self, *args, **kwargs):
        context = super(PostListView, self).get_context_data(**kwargs)
        return context


class HomePageView(TemplateView):
    template_name = "ajaxify/home.html"


class AboutPageView(TemplateView):
    template_name = "ajaxify/about.html"

# // ---- FORMS ---- //

class ContactPageView(FormView):
    template_name = 'ajaxify/contact.html'
    form_class = ContactForm

def contacts(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            pass  # does nothing, just trigger the validation
    else:
        form = ContactForm()
    return render(request, 'ajaxify/contact.html', {'form': form})
