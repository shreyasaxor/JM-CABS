from django.conf.urls import include, url
from django.contrib import admin
from home.views import home,Showcar

urlpatterns = [
    # Examples:
    # url(r'^$', 'mycabs.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    #url(r'^admin/', include(admin.site.urls)),
    url(r'^$', include('home.urls')),
    url(r'^show/', view=Showcar, name='Showcar'),

]
