package appandroid.estructuras.paola.mydrive.Conexion;

import android.support.v7.widget.RecyclerView;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.ImageButton;
import android.widget.ImageView;
import android.widget.TextView;

import org.w3c.dom.Text;

import java.util.List;

import appandroid.estructuras.paola.mydrive.R;

/**
 * Created by Paola on 5/7/2017.
 */

public class Adapter extends RecyclerView.Adapter<Adapter.ViewHolder> {


    List<Carpeta> carpetas;

    public class ViewHolder extends RecyclerView.ViewHolder{

        TextView nombre;
        ImageView imagen;

        public ViewHolder(View itemView) {
            super(itemView);
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

        holder.nombre.setText(carpetas.get(position).getNombre());

    }

    @Override
    public int getItemCount() {
        return  carpetas.size();
    }
}
