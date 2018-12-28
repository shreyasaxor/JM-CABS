from django.conf.urls import include, url
from django.contrib import admin
from django.conf.urls import *
from django.conf.urls.static import static
from django.views.generic.base import RedirectView
from .views import home,Showcar
urlpatterns = [

     url(r'^$', view=home, name='home'),

]
