package appandroid.estructuras.paola.mydrive;

import android.os.Bundle;
import android.support.annotation.NonNull;
import android.support.design.widget.BottomNavigationView;
import android.support.v7.app.AppCompatActivity;
import android.view.MenuItem;
import android.widget.TextView;

import appandroid.estructuras.paola.mydrive.Conexion.ConexionDj;

public class Usuario extends AppCompatActivity {

    private TextView mTextMessage;
    ConexionDj n = new ConexionDj();
    String cActuales = "CC";

    private BottomNavigationView.OnNavigationItemSelectedListener mOnNavigationItemSelectedListener
            = new BottomNavigationView.OnNavigationItemSelectedListener() {

        @Override
        public boolean onNavigationItemSelected(@NonNull MenuItem item) {
            switch (item.getItemId()) {

                case R.id.navigation_home:
                    mTextMessage.setText("");
                    System.out.println(cActuales);;
                    if(cActuales!= "CC"||cActuales!= "vacio"){
                        String lista []= cActuales.split("#");
                        System.out.println(lista.length);
                        for (int i = 0; i < lista.length; i++) {
                            mTextMessage.setText("-"+mTextMessage.getText() + lista[i] +"\n");
                        }
                    }else{
                    mTextMessage.setText("vacip");}
                    return true;
                case R.id.navigation_dashboard:
                    mTextMessage.setText(R.string.title_dashboard);
                    return true;
                case R.id.navigation_notifications:
                    mTextMessage.setText(R.string.title_notifications);
                    return true;
            }
            return false;
        }

    };

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_usuario);

        cActuales = n.viewSession();

        mTextMessage = (TextView) findViewById(R.id.message);
        BottomNavigationView navigation = (BottomNavigationView) findViewById(R.id.navigation);
        navigation.setOnNavigationItemSelectedListener(mOnNavigationItemSelectedListener);
    }

}
