from django.conf.urls import url
from udemy_api import views

urlpatterns = [
    url(r'^api/paises$', views.paises_list),
    url(r'^api/paises/(?P<pk>[0-9]+)$', views.paises_detail)
]