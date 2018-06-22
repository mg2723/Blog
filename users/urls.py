from django.urls import re_path
from django.contrib.auth.views import login
from . import views

urlpatterns = [
    re_path('^login/$', login, {'template_name': 'users/login.html'},
            name='login'),
    re_path('^logout/$', views.logout_view, name='logout'),
    re_path('^register$', views.register, name='register'),
]
