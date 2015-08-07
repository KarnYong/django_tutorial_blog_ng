from django.conf.urls import url

from . import views

urlpatterns = [
    # ex: /post/
    url(r'^$', views.index, name='index'),
    # ex: /post/5/
    url(r'^(?P<post_id>[0-9]+)/$', views.post, name='post'),
]