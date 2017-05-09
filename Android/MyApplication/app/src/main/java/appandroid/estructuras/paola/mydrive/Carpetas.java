package appandroid.estructuras.paola.mydrive;

import android.content.DialogInterface;
import android.graphics.Paint;
import android.media.Image;
import android.os.StrictMode;
import android.support.v7.app.AlertDialog;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.support.v7.widget.LinearLayoutCompat;
import android.support.v7.widget.LinearLayoutManager;
import android.support.v7.widget.RecyclerView;
import android.text.InputType;
import android.view.View;
import android.widget.AdapterView;
import android.widget.Button;
import android.widget.EditText;
import android.widget.ImageView;
import android.widget.LinearLayout;
import android.widget.TextView;
import android.widget.Toast;

import com.google.gson.Gson;
import com.google.gson.GsonBuilder;
import com.google.gson.JsonArray;

import org.json.JSONArray;
import org.json.JSONObject;

import java.util.ArrayList;
import java.util.List;

import appandroid.estructuras.paola.mydrive.Conexion.Carpeta;
import appandroid.estructuras.paola.mydrive.Conexion.ConexionDj;

public class Carpetas extends AppCompatActivity implements View.OnClickListener{

    //LinearLayout contenido;
    //LinearLayout despl;
    /*TextView t,impresion;
    Button prueba;*/

    ImageView imLogout, immodif,imelimina,imatras,imnuevo;
    EditText nombre;
    private String m_Text = "";
    ConexionDj n = new ConexionDj();
    String rutaActual= "root";
    String cActuales = "CC";


    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_carpetas);
        System.out.println("se ha creado pagina carpetas");
        System.out.println("el texto de carpetas actuales es "+cActuales);

        imLogout = (ImageView)findViewById(R.id.imlogout);
        immodif = (ImageView)findViewById(R.id.imModif);
        imelimina = (ImageView)findViewById(R.id.imelimina);
        imatras = (ImageView)findViewById(R.id.imatras);
        imnuevo = (ImageView)findViewById(R.id.imnueva);
        nombre = (EditText)findViewById(R.id.nameFolder);

        imLogout.setOnClickListener(this);
        imelimina.setOnClickListener(this);
        imatras.setOnClickListener(this);
        imnuevo.setOnClickListener(this);
        immodif.setOnClickListener(this);


        String[] listaCarpetas = llenarLista();
        RecyclerView recycler = (RecyclerView)findViewById(R.id.Lista);
        LinearLayoutManager llm = new LinearLayoutManager( this);
        recycler.setLayoutManager(llm);
        System.out.println("EL PINSHI TAMANO CAA ES "+listaCarpetas.length);
        if(!listaCarpetas[0].equalsIgnoreCase("vacio")){
            Adapter adaptador = new Adapter(listaCarpetas);
            recycler.setAdapter(adaptador);
        }

    }

    private String [] llenarLista() {
        cActuales = n.viewSession();
        String devuelve[] = cActuales.split("#");
        return devuelve;


    }


    
    private void cargar(){
        if(!cActuales.equalsIgnoreCase("vacio")){
            String [] folders = cActuales.split("#");
            for (int i = 0; i < folders.length; i++) {
            }
        }

    }


    @Override
    public void onClick(View v) {
        switch (v.getId()){
            case R.id.imnueva:
                System.out.println("se va a buscar "+nombre.getText().toString() + rutaActual);
                Boolean  fd = n.BuscarCarpeta(nombre.getText().toString(),rutaActual);
                if (!fd){
                    n.Crear(rutaActual, nombre.getText().toString());
                }else{

                    poprem();
                }



        }

    }


    public void poprem(){
        AlertDialog.Builder builder1 = new AlertDialog.Builder(this);
        builder1.setTitle("Title");
        builder1.setMessage("my message");
        builder1.setCancelable(true);
        builder1.setNeutralButton(android.R.string.ok,
                new DialogInterface.OnClickListener() {
                    public void onClick(DialogInterface dialog, int id) {
                        dialog.cancel();
                    }
                });

        AlertDialog alert11 = builder1.create();
        alert11.show();
    }


    public void popup(){

        AlertDialog.Builder builder = new AlertDialog.Builder(this);
        builder.setTitle("modificacion ");

// Set up the input
        final EditText input = new EditText(this);

// Specify the type of input expected; this, for example, sets the input as a password, and will mask the text
        input.setInputType(InputType.TYPE_CLASS_TEXT | InputType.TYPE_TEXT_VARIATION_PASSWORD);
        builder.setView(input);

// Set up the buttons
        builder.setPositiveButton("OK", new DialogInterface.OnClickListener() {
            @Override
            public void onClick(DialogInterface dialog, int which) {
                m_Text = input.getText().toString();
            }
        });
        builder.setNegativeButton("Cancel", new DialogInterface.OnClickListener() {
            @Override
            public void onClick(DialogInterface dialog, int which) {
                dialog.cancel();
            }
        });

        builder.show();
    }



    private void crearcarpeta(String name){


    }










    /*private void crear() {

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
    }*/

}






















