package org.apache.jsp;

import javax.servlet.*;
import javax.servlet.http.*;
import javax.servlet.jsp.*;
import Service.Alfanumerico;
import Service.WebService;
import com.squareup.okhttp.RequestBody;
import com.squareup.okhttp.FormEncodingBuilder;

public final class AgregarActivo_jsp extends org.apache.jasper.runtime.HttpJspBase
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
      out.write("<!DOCTYPE html>\n");
      out.write("<html lang=\"en\">\n");
      out.write("\n");
      out.write("    <head>\n");
      out.write("\n");
      out.write("        <meta charset=\"utf-8\">\n");
      out.write("        <meta http-equiv=\"X-UA-Compatible\" content=\"IE=edge\">\n");
      out.write("        <meta name=\"viewport\" content=\"width=device-width, initial-scale=1\">\n");
      out.write("        <title>Agregar Eventos</title>\n");
      out.write("        <!-- CSS -->\n");
      out.write("        <link rel=\"stylesheet\" href=\"http://fonts.googleapis.com/css?family=Roboto:400,100,300,500\">\n");
      out.write("        <link rel=\"stylesheet\" href=\"Estilos/Agregar/bootstrap/css/bootstrap.min.css\">\n");
      out.write("        <link rel=\"stylesheet\" href=\"Estilos/Agregar/font-awesome/css/font-awesome.min.css\">\n");
      out.write("        <link rel=\"stylesheet\" href=\"Estilos/Agregar/css/form-elements.css\">\n");
      out.write("        <link rel=\"stylesheet\" href=\"Estilos/Agregar/css/style.css\">\n");
      out.write("\n");
      out.write("        <!-- HTML5 Shim and Respond.js IE8 support of HTML5 elements and media queries -->\n");
      out.write("        <!-- WARNING: Respond.js doesn't work if you view the page via file:// -->\n");
      out.write("        <!--[if lt IE 9]>\n");
      out.write("            <script src=\"https://oss.maxcdn.com/libs/html5shiv/3.7.0/html5shiv.js\"></script>\n");
      out.write("            <script src=\"https://oss.maxcdn.com/libs/respond.js/1.4.2/respond.min.js\"></script>\n");
      out.write("        <![endif]-->\n");
      out.write("\n");
      out.write("        <!-- Favicon and touch icons -->\n");
      out.write("\n");
      out.write("        <link rel=\"apple-touch-icon-precomposed\" sizes=\"144x144\" href=\"Estilos/Agregar/ico/apple-touch-icon-144-precomposed.png\">\n");
      out.write("        <link rel=\"apple-touch-icon-precomposed\" sizes=\"114x114\" href=\"Estilos/Agregar/ico/apple-touch-icon-114-precomposed.png\">\n");
      out.write("        <link rel=\"apple-touch-icon-precomposed\" sizes=\"72x72\" href=\"Estilos/Agregar/ico/apple-touch-icon-72-precomposed.png\">\n");
      out.write("        <link rel=\"apple-touch-icon-precomposed\" href=\"Estilos/Agregar/ico/apple-touch-icon-57-precomposed.png\">\n");
      out.write("\n");
      out.write("    </head>\n");
      out.write("\n");
      out.write("    <body>\n");
      out.write("\n");
      out.write("        <!-- Top content -->\n");
      out.write("        <div class=\"top-content\" align=\"left\">\n");
      out.write("\n");
      out.write("            <div class=\"inner-bg\">\n");
      out.write("                <div class=\"container\">\n");
      out.write("                    <div class=\"row\">\n");
      out.write("\n");
      out.write("                        <h1> AGREGAR EVENTO</h1>\n");
      out.write("                        ");

                        String Usuario = (String)session.getAttribute("NomUs");
                        
      out.write("\n");
      out.write("                    </div>\n");
      out.write("                    <div class=\"row\">\n");
      out.write("                        <div class=\"col-sm-5 col-sm-offset-3 form-box\">\n");
      out.write("                            <div class=\"form-top\">\n");
      out.write("                                <div class=\"form-top-left\">\n");
      out.write("                                    <p>Crea un nuevo evento disponibles</p>\n");
      out.write("                                </div>\n");
      out.write("\n");
      out.write("                            </div>\n");
      out.write("                            <div class=\"form-bottom\">\n");
      out.write("                                <form role=\"form\" action=\"AgregarActivo.jsp\" method=\"post\" class=\"login-form\">\n");
      out.write("                                  \n");
      out.write("                                    <div class=\"form-group\">\n");
      out.write("                                        <label class=\"sr-only\" for=\"form-username\">Username</label>\n");
      out.write("                                        <input type=\"text\" name=\"txtNombre\" placeholder=\"Nombre\" class=\"form-username form-control\" id=\"form-username\">\n");
      out.write("                                    </div>\n");
      out.write("                                    <div class=\"form-group\">\n");
      out.write("                                        <label class=\"sr-only\" for=\"form-username\">Username</label>\n");
      out.write("                                        <input type=\"text\" name=\"txtDescripcion\" placeholder=\"Descripcion\" class=\"form-username form-control\" id=\"form-username\">\n");
      out.write("                                    </div>\n");
      out.write("                                    <div class=\"form-group\">\n");
      out.write("                                        <label class=\"sr-only\" for=\"form-username\">Username</label>\n");
      out.write("                                        <input type=\"text\" name=\"txtDire\" placeholder=\"Direccion\" class=\"form-username form-control\" id=\"form-username\">\n");
      out.write("                                    </div>\n");
      out.write("                                    <div class=\"form-group\">\n");
      out.write("                                        <label class=\"sr-only\" for=\"form-username\">Username</label>\n");
      out.write("                                        <input type=\"text\" name=\"txtFecha\" placeholder=\"Fecha\" class=\"form-username form-control\" id=\"form-username\" >\n");
      out.write("                                    </div>\n");
      out.write("                                    <div class=\"form-group\">\n");
      out.write("                                        <label class=\"sr-only\" for=\"form-username\">Username</label>\n");
      out.write("                                        <input type=\"text\" name=\"txtHora\" placeholder=\"Hora\" class=\"form-username form-control\" id=\"form-username\" >\n");
      out.write("                                    </div>\n");
      out.write("                                    <button type=\"submit\" class=\"btn\">Agregar Evento</button>\n");
      out.write("                                </form>\n");
      out.write("                            </div>\n");
      out.write("                            <!-- Codigo en Java -->\n");
      out.write("                            ");

                                WebService solicitud = new WebService();
                                Alfanumerico AlfaNum = new Alfanumerico();
                                
                                
                                String CodAct = AlfaNum.Codigo();
                                String NomAct = request.getParameter("txtNombre");
                                String DescripAct = request.getParameter("txtDescripcion");
                                String hora = request.getParameter("txtNombre");
                                String fecha = request.getParameter("txtFecha");
                                String dire = request.getParameter("txtDire");
                               
                               

                                if (NomAct != null && DescripAct != null ) {

                                    RequestBody formBody = new FormEncodingBuilder()
                                            .add("txtNombre", NomAct)
                                            .add("txtDescripcion", DescripAct)
                                            .add("txtHora", hora)
                                            .add("txtFecha", fecha)
                                            .add("txtDire", dire)
                                            .build();
                                    String r = solicitud.Agregar(formBody);
                                    System.out.println(r + "---");
                                    if (r.equalsIgnoreCase("True")) {
                                        String a = "Evento Agregado";
                                        out.println("<script>");
                                        out.println("alert('" + a + "');");
                                        out.println("</script>");
                                        
                                    } else {
                                        String a = "No se puedo Agregar el Activo";
                                        out.println("<script>");
                                        out.println("alert('" + a + "');");
                                        out.println("</script>");
                                    }
                                }


                            
      out.write("\n");
      out.write("                        \n");
      out.write("                        </div>\n");
      out.write("                            <div class=\"col-sm-6 col-sm-offset-3 social-login\">\n");
      out.write("                            <div class=\"social-login-buttons\">\n");
      out.write("\n");
      out.write("                                <a class=\"btn btn-link-2\" href=\"MenuPrincipal.jsp\">\n");
      out.write("                                    Regresar al Menu Principal\n");
      out.write("                                </a>\n");
      out.write("\n");
      out.write("                            </div>\n");
      out.write("\n");
      out.write("                        </div>\n");
      out.write("                    </div>\n");
      out.write("                    \n");
      out.write("                </div>\n");
      out.write("            </div>\n");
      out.write("\n");
      out.write("        </div>\n");
      out.write("\n");
      out.write("\n");
      out.write("        <!-- Javascript -->\n");
      out.write("        <script src=\"Estilos/Agregar/js/jquery-1.11.1.min.js\"></script>\n");
      out.write("        <script src=\"Estilos/Agregar/bootstrap/js/bootstrap.min.js\"></script>\n");
      out.write("        <script src=\"Estilos/Agregar/js/jquery.backstretch.min.js\"></script>\n");
      out.write("        <script src=\"Estilos/Agregar/js/scripts.js\"></script>\n");
      out.write("\n");
      out.write("        <!--[if lt IE 10]>\n");
      out.write("            <script src=\"assets/js/placeholder.js\"></script>\n");
      out.write("        <![endif]-->\n");
      out.write("\n");
      out.write("    </body>\n");
      out.write("\n");
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
