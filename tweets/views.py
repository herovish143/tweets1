from django.shortcuts import render, Http404
from django.http import HttpResponse

from .models import Tweet
# Create your views here.
def home_view(request, *args, **kwargs):
    print(args, kwargs)
    return HttpResponse("<h1>hello world</h1> Home Page")


def tweet_detail_view(request, tweet_id, *args, **kwargs):
    # print(tweet_id, args, kwargs)
    try:
        tweet = Tweet.objects.get(id=tweet_id)
    except:
        raise Http404
    return HttpResponse(f"{tweet_id} -{tweet.content}")

