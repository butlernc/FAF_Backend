__author__ = 'butlernc'

from django.conf.urls import url
from Users import views

urlpatterns = [
    url(r'^users/$', views.user_list),
    url(r'^users/(?P<username>\w+)/$', views.user_detail)
]
