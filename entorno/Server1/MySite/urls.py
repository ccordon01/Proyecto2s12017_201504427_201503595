from django.conf.urls import url
from . import views #it imports from this folder

urlpatterns = [

	url(r'^holi/$',views.home),#its gona take the url an it will be anything
	
	url(r'^prueba/$',views.prueba),
	#url(r'^log_in//$',views.)
	url(r'^prove/$',views.log),



	url(r'^signup/$',views.NewUser),
	#url(r'^root/([^\s]+)',views.dinamic),#manejo de directorio de carpetas
	url(r'^login/$', views.LogIn),#redirecciona a pagina de login


#===============verificando session====================
	url(r'^verifyS/$',views.viewSession),#verifica si la sesion ya esta iniciada
	url(r'^printUser/$',views.PrintUsers),#solo muestra usuarios
	url(r'^verify/$',views.VerifyUser),#para iniciar sesion
	url(r'^verify/$',views.VerifyUser),

	url(r'^find([^\s]+)$', views.FindUser),#encontrar usuario para mandar archivos
	url(r'^root([^\s]+)createFolder/$',views.CreateF),
	url(r'^root([^\s]+)buscarCarpeta/$',views.buscaractual),
	url(r'^root([^\s]+)findF/$',views.FindFolder),#va a agarrar desde root/uno/dos/tres



]
