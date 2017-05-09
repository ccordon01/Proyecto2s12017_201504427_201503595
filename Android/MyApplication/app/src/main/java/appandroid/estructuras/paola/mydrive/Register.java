package appandroid.estructuras.paola.mydrive;

import android.content.Intent;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.TextView;

import org.w3c.dom.Text;

import appandroid.estructuras.paola.mydrive.Conexion.ConexionDj;

public class Register extends AppCompatActivity implements View.OnClickListener {

    EditText user;
    EditText password;
    TextView mensaje;
    ConexionDj c = new ConexionDj();
    @Override
    protected void onCreate(Bundle savedInstanceState) {

        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_register);
        inicializar();
    }


    private void inicializar(){
        user = (EditText)findViewById(R.id.user);
        password= (EditText)findViewById(R.id.pass);
        mensaje = (TextView) findViewById(R.id.mensaje);
        Button registrar= (Button)findViewById(R.id.registro);
        registrar.setOnClickListener(this);
        //ConexionDj n = new ConexionDj();

    }

    @Override
    public void onClick(View v) {
        if(user.getText()!=null){
            if(password.getText()!= null){
                c.django(user.getText().toString(),password.getText().toString());
                Intent Iniciar = new Intent(Register.this,Usuario.class);
                startActivity(Iniciar);
            }else{
                mensaje.setText("Escriba una Contraseña");
            }
        }else{
            mensaje.setText("Escriba un usuario");
        }

    }
}
