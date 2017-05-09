<%-- 
    Document   : EliminarActivo
    Created on : 23/03/2017, 11:45:44 AM
    Author     : Flinttloco
--%>

<%@page import="Service.Alfanumerico"%>
<%@page import="Service.WebService"%>
<%@page contentType="text/html" pageEncoding="UTF-8"%>

<%@page  import ="com.squareup.okhttp.RequestBody" %>
<%@page import="com.squareup.okhttp.FormEncodingBuilder"%>
<!DOCTYPE html>
<html>
<head>
<meta charset='utf-8' />
<link href='fullcalendar.min.css' rel='stylesheet' />
<link href='fullcalendar.print.min.css' rel='stylesheet' media='print' />
<script src='lib/moment.min.js'></script>
<script src='lib/jquery.min.js'></script>
<script src='fullcalendar.min.js'></script>
<script src='locale/es.js'></script>
        <link rel="stylesheet" href="http://fonts.googleapis.com/css?family=Roboto:400,100,300,500">
        <link rel="stylesheet" href="Estilos/Agregar/bootstrap/css/bootstrap.min.css">
        <link rel="stylesheet" href="Estilos/Agregar/font-awesome/css/font-awesome.min.css">
        <link rel="stylesheet" href="Estilos/Agregar/css/form-elements.css">
        <link rel="stylesheet" href="Estilos/Agregar/css/style.css">
<script>

	$(document).ready(function() {

		$('#calendar').fullCalendar({
			header: {
				left: 'prevYear,nextYear today',
				center: 'prev title next',
				right: 'month,agendaWeek,agendaDay'
			},
			defaultDate: '2017-05-12',
			navLinks: true, // can click day/week names to navigate views
			businessHours: true, // display business hours
			editable: true,
			events: [
				{
					title: 'Dia de las madres',
					start: '2017-05-10T13:00:00',
					constraint: 'businessHours'
				},
				{
					title: 'Business Lunch',
					start: '2017-05-03T13:00:00',
					constraint: 'businessHours'
				}
			]
		});

	});

</script>
<style>

	body {
		margin: 40px 10px;
		padding: 0;
		font-family: "Lucida Grande",Helvetica,Arial,Verdana,sans-serif;
		font-size: 14px;
	}

	#calendar {
		max-width: 900px;
		margin: 0 auto;
	}

</style>
</head>
<body>

	<div id='calendar'></div>
<div class="social-login-buttons">

                                <a class="btn btn-link-2" href="MenuPrincipal.jsp">
                                    Regresar al Menu Principal
                                </a>

                            </div>
</body>
</html>
