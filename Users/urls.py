__author__ = 'butlernc'

from django.conf.urls import url
from Users import views

urlpatterns = [
    url(r'^users/$', views.user_list),
    url(r'^users/new/$', views.new_user),
    url(r'^users/send/coords/$', views.receive_gps),
    url(r'^users/(?P<username>\w+)/$', views.user_detail)
]
