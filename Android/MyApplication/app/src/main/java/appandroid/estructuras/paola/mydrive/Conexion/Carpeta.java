package appandroid.estructuras.paola.mydrive.Conexion;

/**
 * Created by Paola on 5/7/2017.
 */

public class Carpeta {
    private String nombre;
    private int foto;


    public Carpeta(String nombre) {
        this.nombre = nombre;
    }

    public String getNombre() {
        return nombre;
    }

    public void setNombre(String nombre) {
        this.nombre = nombre;
    }

    public int getFoto() {
        return foto;
    }

    public void setFoto(int imagen) {
        foto = imagen;
    }
}
