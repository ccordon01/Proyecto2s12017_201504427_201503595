from django.conf.urls import url
from . import views #it imports from this folder

urlpatterns = [

	url(r'^holi/$',views.home),#its gona take the url an it will be anything
	url(r'^login/$', views.LogIn),
	url(r'^prueba/$',views.prueba),
	
	url(r'^signup/$',views.NewUser),
	#url(r'^log_in//$',views.)
	url(r'^prove/$',views.log),
	url(r'^example/([^\s]+)',views.dinamic),
	


#===============verificando session====================
	url(r'^verifyS/$',views.viewSession),
	url(r'^printUser/$',views.PrintUsers),
	url(r'^verify/$',views.VerifyUser),



]
