"""Instagram URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from accounts.views import login_view,register_view,logout_view
from posts import views
from accounts.views import followlist_view,unfollow_view, follow_view, profile_view, search_view, profile_follower, profile_following, editprofile, otherprofile

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^login/', login_view,name='login'),
    url(r'^logout/', logout_view,name='logout'),
    url(r'^register/', register_view,name='register'),
    url(r'^follow/', followlist_view,name='follow'),
    url(r'^unfollow/(?P<id>\d+)/$', unfollow_view,name='unfollow'),
    url(r'^followuser/(?P<id>\d+)/$', follow_view, name='followuser'),
    url(r'^profile/(?P<id>\d+)/$', profile_view,name='profile'),
    url(r'^profile_follower/(?P<id>\d+)/$', profile_follower, name='profile_follower'),
    url(r'^profile_following/(?P<id>\d+)/$', profile_following, name='profile_following'),
    url(r'^search/', search_view,name='search'),
    url(r'^editprofile/(?P<id>\d+)/$', editprofile,name='editprofile'),
    url(r'^otherprofile/(?P<id>\d+)/$', otherprofile,name='otherprofile'),
    url(r'^', include("posts.urls",namespace='posts')),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)