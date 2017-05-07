package appandroid.estructuras.paola.mydrive.Conexion;


import rest.devazt.networking.HttpClient;
import com.squareup.okhttp.FormEncodingBuilder;
import com.squareup.okhttp.Request;
import com.squareup.okhttp.*;
import java.net.MalformedURLException;
import java.net.URL;
import java.nio.channels.Pipe;
import java.util.ArrayList;
import java.util.Calendar;
import java.util.Date;
import java.util.GregorianCalendar;
import java.util.logging.Level;

/**
 * Created by Paola on 5/1/2017.
 */

public class ConexionDj {

    public ConexionDj() {
    }

    public static OkHttpClient webClient = new OkHttpClient();



    public String django(String name, String pass){
        RequestBody formBody = new FormEncodingBuilder()
                .add("nom", name)
                .add("nom2", pass)
                .build();

        String r = GetString("prueba/", formBody);
        System.out.println(r + " esta fue mi devolucion :33");
        return r;
    }

    public String viewSession(){
        RequestBody formBody = new FormEncodingBuilder()
                .add("nom", "n")
                .build();
        String r = GetString("verifyS/", formBody);
        return r;
    }

    public String CheckLogin(String Name, String Pass){
        RequestBody formBody = new FormEncodingBuilder()
                .add("name",Name)
                .add("pass", Pass)
                .build();
        String r = GetString("verify/", formBody);
        return r;

    }

    public static String GetString(String metodo, RequestBody formBody) {

        try {
            URL url = new URL("http://192.168.1.5:8000/accounts/"+metodo);
            Request request = new Request.Builder().url(url).post(formBody).build();
            Response response = webClient.newCall(request).execute();//Aqui obtiene la respuesta en dado caso si hayas pues un return en python
            System.out.println("Despues de response");
            String response_string = response.body().string();//y este seria el string de las respuest
            return response_string;
        } catch (MalformedURLException ex) {
            java.util.logging.Logger.getLogger(ConexionDj.class.getName()).log(Level.SEVERE, null, ex);
        } catch (Exception ex) { java.util.logging.Logger.getLogger(ConexionDj.class.getName()).log(Level.SEVERE, null, ex);
        }
        return "error";
    }



}
