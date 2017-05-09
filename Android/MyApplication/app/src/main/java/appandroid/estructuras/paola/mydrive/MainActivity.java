package appandroid.estructuras.paola.mydrive;

import android.content.Intent;
import android.os.StrictMode;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.util.Log;
import android.view.View;
import android.widget.Button;

import appandroid.estructuras.paola.mydrive.Conexion.ConexionDj;

public class MainActivity extends AppCompatActivity implements View.OnClickListener{

    Button logIn,SignUp;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        int SDK_INT = android.os.Build.VERSION.SDK_INT;
        if (SDK_INT > 8)
        {
            StrictMode.ThreadPolicy policy = new StrictMode.ThreadPolicy.Builder()
                    .permitAll().build();
            StrictMode.setThreadPolicy(policy);
            //your codes here
        }
        System.out.println("SE A ENTRADO A LA PAGINA PRINCIPAL");
        verificar();

        logIn = (Button)findViewById(R.id.IniciarSesion);
        SignUp = (Button)findViewById(R.id.Registrarse);
        logIn.setOnClickListener(this);
        SignUp.setOnClickListener(this);

    }

    private void verificar() {
        try {
            ConexionDj con = new ConexionDj();
            String estado = con.viewSession();
            System.out.println("EL ESTADO ACTUAL ES |"+estado+"|");
            if(!estado.equalsIgnoreCase("True")){
                Intent carpetas = new Intent(MainActivity.this,Carpetas.class);
                startActivity(carpetas);
            }

        }catch (Exception e){

            System.out.println("nope :v");
        }


    }


    @Override
    public void onClick(View v) {
        switch (v.getId()){
            case R.id.IniciarSesion:
                Intent Iniciar = new Intent(MainActivity.this,Principal.class);
                startActivity(Iniciar);
                break;
            case R.id.Registrarse:
                Intent Registro = new Intent(MainActivity.this,Register.class);
                startActivity(Registro);
                break;


        }

    }
}
