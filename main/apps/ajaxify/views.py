from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
def index(request):
    # response = "Hi There ..."

    context = {
        "name"  : "Mike",
        "email" : "mikey@thefatkid.com",
    }

    # return HttpResponse(response)
    return render(request, "ajaxify/index.html", context)
