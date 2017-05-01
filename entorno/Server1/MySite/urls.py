from django.conf.urls import url
from . import views #it imports from this folder

urlpatterns = [
	url(r'^holi/$',views.home),#its gona take the url an it will be anything
	url(r'^login/$', views.another),
	url(r'^prueba/$',views.prueba),
]
