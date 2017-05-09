<%-- 
    Document   : MenuPrincipal
    Created on : 23/03/2017, 11:44:37 AM
    Author     : Flinttloco
--%>



<%@page import="Service.WebService"%>
<%@ page import="java.util.*" %>
<%@page contentType="text/html" pageEncoding="UTF-8"%>

<%@page  import ="com.squareup.okhttp.RequestBody" %>
<%@page import="com.squareup.okhttp.FormEncodingBuilder"%>
<!DOCTYPE html>
<html lang="en">

    <head>

        <meta charset="utf-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <title>Menu Principal</title>
        <!-- CSS -->
        <link rel="stylesheet" href="http://fonts.googleapis.com/css?family=Roboto:400,100,300,500">
        <link rel="stylesheet" href="Estilos/Menu/bootstrap/css/bootstrap.min.css">
        <link rel="stylesheet" href="Estilos/Menu/font-awesome/css/font-awesome.min.css">
        <link rel="stylesheet" href="Estilos/Menu/css/form-elements.css">
        <link rel="stylesheet" href="Estilos/Menu/css/style.css">

        <!-- HTML5 Shim and Respond.js IE8 support of HTML5 elements and media queries -->
        <!-- WARNING: Respond.js doesn't work if you view the page via file:// -->
        <!--[if lt IE 9]>
            <script src="https://oss.maxcdn.com/libs/html5shiv/3.7.0/html5shiv.js"></script>
            <script src="https://oss.maxcdn.com/libs/respond.js/1.4.2/respond.min.js"></script>
        <![endif]-->

        <!-- Favicon and touch icons -->

        <link rel="apple-touch-icon-precomposed" sizes="144x144" href="Estilos/Menu/ico/apple-touch-icon-144-precomposed.png">
        <link rel="apple-touch-icon-precomposed" sizes="114x114" href="Estilos/Menu/ico/apple-touch-icon-114-precomposed.png">
        <link rel="apple-touch-icon-precomposed" sizes="72x72" href="Estilos/Menu/ico/apple-touch-icon-72-precomposed.png">
        <link rel="apple-touch-icon-precomposed" href="Estilos/Menu/ico/apple-touch-icon-57-precomposed.png">

    </head>

    <body>

        <!-- Top content -->
        <div class="top-content" align="left">

            <div class="inner-bg">
                <div class="container">
                    <div class="row">
                        <%
                        String Usuario = (String)session.getAttribute("NomUs");
                        
                        %>
                        <h1>Hola <strong><%out.println(Usuario);%></strong></h1>

                    </div>
                    <div class="row">
                        <div class="col-sm-5 col-sm-offset-3 form-box">
                            <div class="form-top">
                                <div class="form-top-left">

                                    <p>Que bueno que regresaste!</p>
                                </div>

                            </div>
                            <div class="form-bottom">
                                <form role="form" action="AgregarActivo.jsp" method="post" class="login-form">
                                   
                                    <button type="submit" class="btn">Agregar Evento</button>
                                </form>
                                <br>
                                 <form role="form" action="EliminarActivo.jsp" method="post" class="login-form">
                                   
                                    <button type="submit" class="btn">Eliminar Evento</button>
                                </form>
                                <br>
                                 <form role="form" action="ModificarActivo.jsp" method="post" class="login-form">
                                   
                                    <button type="submit" class="btn">Modificar Evento</button>
                                </form>
                                <br>
                                 <form role="form" action="Calendario.jsp" method="post" class="login-form">
                                   
                                    <button type="submit" class="btn">Calendario</button>
                                </form>
                                <br>
                                 <form role="form" action="IniciarSesion.jsp" method="post" class="login-form">
                                   
                                    <button type="submit" class="btn">Cerrar Sesion</button>
                                </form>
                            </div>
                     
                        </div>
                    </div>
               
                </div>
            </div>

        </div>
        <!-- Javascript -->
        <script src="Estilos/Menu/js/jquery-1.11.1.min.js"></script>
        <script src="Estilos/Menu/bootstrap/js/bootstrap.min.js"></script>
        <script src="Estilos/Menu/js/jquery.backstretch.min.js"></script>
        <script src="Estilos/Menu/js/scripts.js"></script>

        <!--[if lt IE 10]>
            <script src="assets/js/placeholder.js"></script>
        <![endif]-->

    </body>

</html>