from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader

from .models import Post

def index(request):
    latest_post_list = Post.objects.order_by('-pub_date')[:5]
    template = loader.get_template('post/index.html')
    context = RequestContext(request, {
        'latest_post_list': latest_post_list,
    })
    return HttpResponse(template.render(context))

def post(request, post_id):
    return HttpResponse("You're looking at post %s." % post_id)