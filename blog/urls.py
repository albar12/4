from django.conf.urls import url

from . import views

urlpatterns=[
    url(r'^cerita/$', views.index),
    url(r'^$', views.index),
    
]