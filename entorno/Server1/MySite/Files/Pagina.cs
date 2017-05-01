using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;

namespace WebApi.Models.AB
{
    public class Pagina
    {

        //=========

        public Pagina[] Ramas = new Pagina[5];
        public Nodo[] Claves = new Nodo[5];
        public int Cuentas = 0;
        public Queue<String> Hijos = new Queue<string>();

        public Pagina(Nodo clave)
        {
            Claves[0] = clave;
        }

        public Pagina()
        {
        }

        public Queue<String> hijos
        {
            get { return Hijos; }
            set { Hijos = value; }

        }
    }
}