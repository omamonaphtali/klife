"""klife URL Configuration

The `urlpatterns` list routes URLs to  For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""

from django.conf.urls import url
from .views import (product_list,
                    product_create,
                    product_detail,
                    product_update,
                    contacts,
                    gallery)

urlpatterns = [
    url(r'^$', product_list, name='home'),
    url(r'^add/', product_create, name='add'),
    url(r'^products/', product_list, name='products'),
    url(r'^(?P<pk>\d+)/$', product_detail, name='detail'),
    url(r'^(?P<pk>\d+)/edit/$', product_update, name='edit'),
    url(r'^contacts/', contacts, name='contacts'),
    url(r'^gallery/', gallery, name='gallery'),
]
