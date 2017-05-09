from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^prueba/$', views.prueba, name='prueba'),
    url(r'^Registro/$', views.registro, name='registro'),
    url(r'^Login/$', views.login, name='login'),
    url(r'^RegistroE/$', views.registroE, name='registroE'),
]