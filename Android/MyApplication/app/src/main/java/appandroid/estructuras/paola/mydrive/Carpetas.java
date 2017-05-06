package appandroid.estructuras.paola.mydrive;

import android.os.StrictMode;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.support.v7.widget.LinearLayoutCompat;
import android.view.View;
import android.widget.Button;
import android.widget.LinearLayout;
import android.widget.TextView;
import android.widget.Toast;

import com.google.gson.Gson;
import com.google.gson.GsonBuilder;
import com.google.gson.JsonArray;

import org.json.JSONArray;
import org.json.JSONObject;

import java.util.ArrayList;

import appandroid.estructuras.paola.mydrive.Conexion.ConexionDj;
import appandroid.estructuras.paola.mydrive.Conexion.Person;
import rest.devazt.networking.HttpClient;
import rest.devazt.networking.OnHttpRequestComplete;
import rest.devazt.networking.Response;

public class Carpetas extends AppCompatActivity implements View.OnClickListener {

    LinearLayout contenido;
    LinearLayout despl;
    TextView t,impresion;
    Button prueba;
    ConexionDj n = new ConexionDj();
    String cActuales = "CC";


    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_carpetas);
        System.out.println("se ha creado pagina carpetas");
        System.out.println("el texto de carpetas actuales es "+cActuales);




        probar();
        //crear();
    }

    private void probar() {
        //prueba = (Button)findViewById(R.id.prueba);
        //impresion = (TextView)findViewById(R.id.impresion);
        //contenido = (LinearLayout)findViewById(R.id.panels);
       // t = (TextView)findViewById(R.id.textores);
        cActuales = n.viewSession();
        //despl = (LinearLayout)findViewById(R.id.LinLay);

        //prueba.setOnClickListener(this);
        TextView  tv = (TextView)findViewById(R.id.TV);
        tv.setText("Este es un textview");


    }
    
    private void cargar(){
        if(!cActuales.equalsIgnoreCase("vacio")){
            String [] folders = cActuales.split("|");
            for (int i = 0; i < folders.length; i++) {

            }
        }

    }


    @Override
    public void onClick(View v) {
        //t.setText(cActuales);
        //impresion.setText(impresion.getText() + "\n" +n.django("quesito", "jamon"));

    }










    private void crear() {

        System.out.println("SE ha creado esta babosada==============================================");


        HttpClient cliente = new HttpClient(new OnHttpRequestComplete() {
            @Override
            public void onComplete(Response status) {
                if(status.isSuccess()){
                    Gson gson = new GsonBuilder().create();
                    try{
                        JSONObject jsono = new JSONObject(status.getResult());
                        JSONArray jsonarray = jsono.getJSONArray("records");
                        ArrayList<Person> personas = new ArrayList<Person>();
                        for (int i=0; i<7;i++){
                            String person = jsonarray.getString(i);//obtiene el array, el objeto json
                            System.out.println(person);
                            Person p = gson.fromJson(person,Person.class);
                            personas.add(p);
                            System.err.println(p.getName());
                            t.setText(t.getText()+"\n"+p.getName());

                            System.out.println("ESto debeira imprimir");
                            System.out.println(p.getName());

                        }
                        contenido.addView(t);
                    }catch (Exception e){
                        System.out.println("Sha la cagajteee we####################################");

                    }
                    //Toast.makeText(Carpetas.this,status.getResult(),Toast.LENGTH_LONG).show();
                }else{

                    System.out.println("No se ejecuto la peticion ");
                }
            }
        });

        cliente.excecute("https://www.w3schools.com/angular/customers.php");
    }

}






















