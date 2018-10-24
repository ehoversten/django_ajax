from django.conf.urls import url
from . import views

app_name = 'ajaxify'

urlpatterns = [
    url(r'^$', views.index),
    url(r'^insert$', views.insert, name='insert'),
]
