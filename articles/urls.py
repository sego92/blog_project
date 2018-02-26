
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^articles/(?P<id>[0-9]+)$', views.detail),
]