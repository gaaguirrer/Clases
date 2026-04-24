using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Proyecto_quiek_beaty
{
   public class Catálogo
    {
        private DateTime _fecha;
        private string _nombre_de_servicio;
        private string _imagen;
        private double _precio;

        public DateTime Fecha { get => _fecha; set => _fecha = value; }

        public string Nombre_de_servicio { get => _nombre_de_servicio; set => _nombre_de_servicio = value; }

        public string Imagen { get => _imagen; set => _imagen = value; }

        public double Precio { get => _precio; set => _precio = value; }

        //contructor
        public Catálogo() { }

        public Catálogo(DateTime fecha, string nombre_de_servicio,string imagen,double precio)
        {
            this.Fecha = fecha;
            this.Nombre_de_servicio = nombre_de_servicio;
            this.Imagen = imagen;
            this.Precio = precio;
        }

        public string Agregar()
        {

        }
        
        public string Actualizar()
        {

        }
        public string Eliminar()
        {

        }
    }

}
