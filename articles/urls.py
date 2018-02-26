
from django.conf.urls import url
from . import views

app_name='articles'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^articles/(?P<id>[0-9]+)$', views.detail, name='detail'),
]