from django.shortcuts import render
from django.http import HttpResponse, Http404, JsonResponse

from .models import Tweet
# Create your views here.
def home_view(request, *args, **kwargs):
    # print(args, kwargs)
    # return HttpResponse("<h1>hello world</h1> Home Page")
    return render(request, "pages/home.html", context={}, status=200)


def tweet_detail_view(request, tweet_id, *args, **kwargs):
    """
    REST API VIEW
    Consume by Javascript
    return json data
    """
    data = {
        "id": tweet_id,
        # "content": tweet.content,
        # "image": tweet.image.url,
    }
    status = 200
    try:
        tweet = Tweet.objects.get(id=tweet_id)
        data['content'] = tweet.content
    except:
        status = 404
        data['message'] = "Not Found"
    
    return JsonResponse(data, status=status)

