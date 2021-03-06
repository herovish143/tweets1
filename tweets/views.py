from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home_view(request, *args, **kwargs):
    print(args, kwargs)
    return HttpResponse("<h1>hello world</h1> Home Page")


def tweet_detail_view(request, tweet_id, *args, **kwargs):
    print(tweet_id, args, kwargs)
    return HttpResponse(f"hello {tweet_id}")

