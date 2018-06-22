from django.urls import re_path
from . import views

urlpatterns = [
    re_path('^$', views.index, name='index'),
    re_path('^topics/$', views.topics, name='topics'),
    re_path('^new_blog/$', views.new_blog, name='new_blog'),
    re_path('^edit_blog/(?P<blog_id>\d+)/$', views.edit_blog, name='edit_blog'),
]
