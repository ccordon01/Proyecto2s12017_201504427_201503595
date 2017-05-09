package org.apache.jsp;

import javax.servlet.*;
import javax.servlet.http.*;
import javax.servlet.jsp.*;
import Service.Alfanumerico;
import Service.WebService;
import com.squareup.okhttp.RequestBody;
import com.squareup.okhttp.FormEncodingBuilder;

public final class Calendario_jsp extends org.apache.jasper.runtime.HttpJspBase
    implements org.apache.jasper.runtime.JspSourceDependent {

  private static final JspFactory _jspxFactory = JspFactory.getDefaultFactory();

  private static java.util.List<String> _jspx_dependants;

  private org.glassfish.jsp.api.ResourceInjector _jspx_resourceInjector;

  public java.util.List<String> getDependants() {
    return _jspx_dependants;
  }

  public void _jspService(HttpServletRequest request, HttpServletResponse response)
        throws java.io.IOException, ServletException {

    PageContext pageContext = null;
    HttpSession session = null;
    ServletContext application = null;
    ServletConfig config = null;
    JspWriter out = null;
    Object page = this;
    JspWriter _jspx_out = null;
    PageContext _jspx_page_context = null;

    try {
      response.setContentType("text/html;charset=UTF-8");
      pageContext = _jspxFactory.getPageContext(this, request, response,
      			null, true, 8192, true);
      _jspx_page_context = pageContext;
      application = pageContext.getServletContext();
      config = pageContext.getServletConfig();
      session = pageContext.getSession();
      out = pageContext.getOut();
      _jspx_out = out;
      _jspx_resourceInjector = (org.glassfish.jsp.api.ResourceInjector) application.getAttribute("com.sun.appserv.jsp.resource.injector");

      out.write("\n");
      out.write("\n");
      out.write("\n");
      out.write("\n");
      out.write("\n");
      out.write("\n");
      out.write("\n");
      out.write("\n");
      out.write("<!DOCTYPE html>\n");
      out.write("<html lang=\"en\">\n");
      out.write("\n");
      out.write("    <head>\n");
      out.write("\n");
      out.write("        <meta charset=\"utf-8\">\n");
      out.write("        <meta http-equiv=\"X-UA-Compatible\" content=\"IE=edge\">\n");
      out.write("        <meta name=\"viewport\" content=\"width=device-width, initial-scale=1\">\n");
      out.write("        <title>Eliminar Activos</title>\n");
      out.write("        <!-- CSS -->\n");
      out.write("        <link rel=\"stylesheet\" href=\"http://fonts.googleapis.com/css?family=Roboto:400,100,300,500\">\n");
      out.write("        <link rel=\"stylesheet\" href=\"Estilos/Eliminar/bootstrap/css/bootstrap.min.css\">\n");
      out.write("        <link rel=\"stylesheet\" href=\"Estilos/Eliminar/font-awesome/css/font-awesome.min.css\">\n");
      out.write("        <link rel=\"stylesheet\" href=\"Estilos/Eliminar/css/form-elements.css\">\n");
      out.write("        <link rel=\"stylesheet\" href=\"Estilos/Eliminar/css/style.css\">\n");
      out.write("\n");
      out.write("        <link rel=\"apple-touch-icon-precomposed\" sizes=\"144x144\" href=\"Estilos/Eliminar/ico/apple-touch-icon-144-precomposed.png\">\n");
      out.write("        <link rel=\"apple-touch-icon-precomposed\" sizes=\"114x114\" href=\"Estilos/Eliminar/ico/apple-touch-icon-114-precomposed.png\">\n");
      out.write("        <link rel=\"apple-touch-icon-precomposed\" sizes=\"72x72\" href=\"Estilos/Eliminar/ico/apple-touch-icon-72-precomposed.png\">\n");
      out.write("        <link rel=\"apple-touch-icon-precomposed\" href=\"Estilos/Eliminar/ico/apple-touch-icon-57-precomposed.png\">\n");
      out.write("           <script type=\"text/javascript\">\n");
      out.write("        var mostrarValor = function(foo, bar){\n");
      out.write("        document.getElementById('txtcod').value = foo; \n");
      out.write("        };\n");
      out.write("    </script>\n");
      out.write("    <meta charset='utf-8' />\n");
      out.write("<link href='fullcalendar.min.css' rel='stylesheet' />\n");
      out.write("<link href='fullcalendar.print.min.css' rel='stylesheet' media='print' />\n");
      out.write("<script src='lib/moment.min.js'></script>\n");
      out.write("<script src='lib/jquery.min.js'></script>\n");
      out.write("<script src='fullcalendar.min.js'></script>\n");
      out.write("<script src='locale/es.js'></script>\n");
      out.write("<script>\n");
      out.write("\n");
      out.write("\t$(document).ready(function() {\n");
      out.write("\n");
      out.write("\t\t$('#calendar').fullCalendar({\n");
      out.write("\t\t\theader: {\n");
      out.write("\t\t\t\tleft: 'prevYear,nextYear today',\n");
      out.write("\t\t\t\tcenter: 'prev title next',\n");
      out.write("\t\t\t\tright: 'month,agendaWeek,agendaDay'\n");
      out.write("\t\t\t},\n");
      out.write("\t\t\tdefaultDate: '2017-05-12',\n");
      out.write("\t\t\tnavLinks: true, // can click day/week names to navigate views\n");
      out.write("\t\t\tbusinessHours: true, // display business hours\n");
      out.write("\t\t\teditable: true,\n");
      out.write("\t\t\tevents: [\n");
      out.write("\t\t\t\t{\n");
      out.write("\t\t\t\t\ttitle: 'Dia de las madres',\n");
      out.write("\t\t\t\t\tstart: '2017-05-10T13:00:00',\n");
      out.write("\t\t\t\t\tconstraint: 'businessHours'\n");
      out.write("\t\t\t\t},\n");
      out.write("\t\t\t\t{\n");
      out.write("\t\t\t\t\ttitle: 'Business Lunch',\n");
      out.write("\t\t\t\t\tstart: '2017-05-03T13:00:00',\n");
      out.write("\t\t\t\t\tconstraint: 'businessHours'\n");
      out.write("\t\t\t\t}\n");
      out.write("\t\t\t]\n");
      out.write("\t\t});\n");
      out.write("\n");
      out.write("\t});\n");
      out.write("\n");
      out.write("</script>\n");
      out.write("<style>\n");
      out.write("\n");
      out.write("\tbody {\n");
      out.write("\t\tmargin: 40px 10px;\n");
      out.write("\t\tpadding: 0;\n");
      out.write("\t\tfont-family: \"Lucida Grande\",Helvetica,Arial,Verdana,sans-serif;\n");
      out.write("\t\tfont-size: 14px;\n");
      out.write("\t}\n");
      out.write("\n");
      out.write("\t#calendar {\n");
      out.write("\t\tmax-width: 900px;\n");
      out.write("\t\tmargin: 0 auto;\n");
      out.write("\t}\n");
      out.write("\n");
      out.write("</style>\n");
      out.write("    </head>\n");
      out.write("\n");
      out.write("    <body>\n");
      out.write("\n");
      out.write("\n");
      out.write("        <!-- Top content -->\n");
      out.write("        <div class=\"top-content\" align=\"left\">\n");
      out.write("            <div id='calendar'></div>\n");
      out.write("\n");
      out.write("        </div>\n");
      out.write("\n");
      out.write("\n");
      out.write("        <!-- Javascript -->\n");
      out.write("        <script src=\"Estilos/Eliminar/js/jquery-1.11.1.min.js\"></script>\n");
      out.write("        <script src=\"Estilos/Eliminar/bootstrap/js/bootstrap.min.js\"></script>\n");
      out.write("        <script src=\"Estilos/Eliminar/js/jquery.backstretch.min.js\"></script>\n");
      out.write("        <script src=\"Estilos/Eliminar/js/scripts.js\"></script>\n");
      out.write("    </body>\n");
      out.write("    \n");
      out.write("</html>");
    } catch (Throwable t) {
      if (!(t instanceof SkipPageException)){
        out = _jspx_out;
        if (out != null && out.getBufferSize() != 0)
          out.clearBuffer();
        if (_jspx_page_context != null) _jspx_page_context.handlePageException(t);
        else throw new ServletException(t);
      }
    } finally {
      _jspxFactory.releasePageContext(_jspx_page_context);
    }
  }
}
