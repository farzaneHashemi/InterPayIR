"""InterpayIran URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import url, include
from django.contrib import admin
from interpay import views
from django.conf.urls.i18n import i18n_patterns
from django.utils.translation import ugettext_lazy as _

urlpatterns = [
    url(r'^i18n/', include('django.conf.urls.i18n')),
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.home),
    url(r'^home/', views.home),
    url(r'^wallets/', views.wallets),
    url(r'^trans-history/', views.home),
    url(r'^reports/', views.home),
    url(r'^general/', views.home),
    url(r'^change_lang/', views.change_lang),
]

urlpatterns += i18n_patterns(
    url(r'^admin/', admin.site.urls),
    url(r'^home/', views.home),
    url(r'^wallets/', views.wallets),
    url(r'^trans-history/', views.home),
    url(r'^reports/', views.home),
    url(r'^general/', views.home),
    url(r'^', views.home),
)
