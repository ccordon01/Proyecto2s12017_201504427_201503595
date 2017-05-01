package appandroid.estructuras.paola.mydrive;

import android.content.Intent;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.util.Log;
import android.view.View;
import android.widget.Button;

public class MainActivity extends AppCompatActivity implements View.OnClickListener{

    Button logIn,SignUp;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        logIn = (Button)findViewById(R.id.IniciarSesion);
        SignUp = (Button)findViewById(R.id.Registrarse);
        logIn.setOnClickListener(this);
        SignUp.setOnClickListener(this);


    }



    @Override
    public void onClick(View v) {
        switch (v.getId()){
            case R.id.IniciarSesion:
                Intent Iniciar = new Intent(MainActivity.this,Principal.class);
                startActivity(Iniciar);
                break;
            case R.id.Registrarse:
                Log.d("sss","que onda");


        }

    }
}
