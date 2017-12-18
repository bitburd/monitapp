from django.conf.urls import include, url
#from django.conf.urls import url
from django.views.generic.base import TemplateView
from django.views.generic import RedirectView 
from . import views
from . import settings
from django.contrib import auth
from django.contrib.auth import views as auth_views

urlpatterns = [
        url(r'^$', views.index, name='index'),
        url(r'^dashboard/', views.dashboard, name='dashboard'),
	url(r'^home/', views.home, name='home'),
	url(r'^monit/', views.monit, name='home'),
	url(r'^status/', views.status, name='status'),
	url(r'^loginapp/', views.loginapp, name='loginapp'),
        url(r'^login/$', auth_views.login, name='login'),
        url(r'^logout/$', auth_views.logout, name='logout'),
]


