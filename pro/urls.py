from django.urls import path
from . import views

urlpatterns = [
    path('', views.base, name='base'),
    path('create.html', views.create, name='create-events'),
    path('event.html', views.event, name='Events'),
    path('login.html', views.login, name='login'),
    path('pw.html', views.pw, name='password'),
    path('about.html', views.about, name='About'),
    path('contact.html', views.contact, name='contact'),
    path('help.html', views.help, name='help'),
    path('reg.html', views.reg, name='sign up'),
    ]