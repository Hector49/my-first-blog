from django.conf.urls import url, include
from . import views
from .models import Post


urlpatterns= [
    url(r'^$', views.post_list, name='post_list'),
]
