package appandroid.estructuras.paola.mydrive;

import android.content.Intent;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.util.Log;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.TextView;

import org.w3c.dom.Text;

import appandroid.estructuras.paola.mydrive.Conexion.ConexionDj;

public class Principal extends AppCompatActivity implements View.OnClickListener{
    EditText user,password;
    Button loging;
    ConexionDj c = new ConexionDj();



    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_principal);

        user = (EditText)findViewById(R.id.UserBox);
        password = (EditText)findViewById((R.id.boxPassword));
        loging = (Button)findViewById(R.id.LoginBut);
        loging.setOnClickListener(this);
    }

    @Override
    public void onClick(View v) {
        Carpetas page = new Carpetas();
        String check = c.CheckLogin(user.getText().toString(),password.getText().toString());
        System.out.println("aaaaa  "+check +" 77777777777777777777777777777777777777777777");
        if(check != "False"){
            System.out.println("Se ha encontrado al usuario");
            Intent Iniciar = new Intent(Principal.this,page.getClass());
            startActivity(Iniciar);



        } else {
            page.cActuales = "No se encontro usuario";
            Intent Iniciar = new Intent(Principal.this,page.getClass());
            startActivity(Iniciar);
        }
        System.out.println("Salida--------------------");




    }
}
