package appandroid.estructuras.paola.mydrive;

import android.support.v7.widget.RecyclerView;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.ImageView;
import android.widget.LinearLayout;
import android.widget.RelativeLayout;
import android.widget.TextView;

import java.util.List;

import appandroid.estructuras.paola.mydrive.Conexion.Carpeta;

/**
 * Created by Paola on 5/7/2017.
 */

public class Adapter extends RecyclerView.Adapter<Adapter.ViewHolder> implements View.OnClickListener{
    public Adapter(String[] carpetas) {
        this.carpetas = carpetas;
    }

    String [] carpetas;

    @Override
    public void onClick(View v) {
        System.out.println("ha presionado un holder");
    }

    public static class ViewHolder extends RecyclerView.ViewHolder {

        TextView nombre;
        ImageView imagen;
        RelativeLayout lay;

        public ViewHolder(View itemView) {
            super(itemView);
            lay = (RelativeLayout) itemView.findViewById(R.id.conten);
            nombre = (TextView) itemView.findViewById(R.id.folderName);
            imagen =(ImageView)itemView.findViewById(R.id.imagenCarpeta);
        }

    }
    @Override
    public Adapter.ViewHolder onCreateViewHolder(ViewGroup parent, int viewType) {
        View v = LayoutInflater.from(parent.getContext()).inflate(R.layout.userfolders, parent,false);
        ViewHolder holder = new ViewHolder(v);
        return holder;
    }

    @Override
    public void onBindViewHolder(Adapter.ViewHolder holder, int position) {

        holder.nombre.setText(carpetas[position]);
        holder.lay.setOnClickListener(this);

    }

    @Override
    public int getItemCount() {
        return carpetas.length ;
    }
}
