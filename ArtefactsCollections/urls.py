"""ArtefactsCollections URL Configuration

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
# from django.conf.urls import url, include, path
from django.urls import path, include
from django.contrib import admin
from django.views.generic import RedirectView
from django.views import static
from home import urls as urls_home

from django.conf import settings
from django.conf.urls.static import static

from home.views import home_view

from accounts.views import index, logout, login, registration, user_profile, landing_page


urlpatterns = [
    path('logout/', logout, name="logout"),
    path('login/', login, name="login"),
    path('register/', registration, name="registration"),
    path('profile/', user_profile, name="profile"),
    path('admin/', admin.site.urls),
    # url(r'^h/$', home_view, name="home"),
    path('home/', include('home.urls')),    
    path('', landing_page, name="landingpage"),   

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
