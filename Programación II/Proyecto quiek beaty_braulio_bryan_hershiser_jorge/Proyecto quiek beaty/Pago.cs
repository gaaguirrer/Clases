using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Proyecto_quiek_beaty
{
   public class Pago
    {
        private string _num_factura;
        private string _detalle;
        private float _sub_total;
        private DateTime _fecha_pago;
        private float _total;

        public string Num_factura { get => _num_factura; set => _num_factura = value; }


        public string Detalle { get => _detalle; set => _detalle = value; }

        public float Sub_total { get => _sub_total; set => _sub_total = value; }

        public DateTime Fecha_pago { get => _fecha_pago; set => _fecha_pago = value; }

        public float Total { get => _total; set => _total = value; }

        //contructor vacio
        public Pago()
        {

        }
        //contructor con parametros
        public Pago(string num_factura, string detalle, float sub_total, DateTime fecha_pago,float total)
        {
            this.Num_factura = num_factura;
            this.Detalle = detalle;
            this.Sub_total = sub_total;
            this.Fecha_pago = fecha_pago;
            this.Total = total;
        }
        //Metodos
        public string Registrar_pago(Pago pago)
        {

        }
        public float Aplicar_descuento(Pago pago)
        {

        }


   
    }


}
