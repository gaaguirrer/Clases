using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Proyecto_quiek_beaty
{
    public class Reserva
    {
        private string _direccion;
        private int _num_reserva;
        private DateTime _fecha_reserva;
        private DateTime _hora_reserva;
        private string _estado_reserva;
        private string _lista_servicio;

        public string Direccion { get => _direccion; set => _direccion = value; }


        public int Num_reserva { get => _num_reserva; set => _num_reserva = value; } 

        public DateTime Fecha_reserva { get => _fecha_reserva; set => _fecha_reserva = value; }

        public DateTime Hora_reserva { get => _hora_reserva; set => _hora_reserva = value; }

        public string Estado_reserva { get => _estado_reserva; set => _estado_reserva = value; }

        public string Lista_servicio { get => _lista_servicio; set => _lista_servicio = value; }

        //contructor
        public Reserva() { }

        public Reserva(string direccion, int num_reserva, DateTime fecha_reserva, DateTime hora_reserva, string estado_reserva, string lista_servicio)
        {
            this.Direccion = direccion;
            this.Num_reserva = num_reserva;
            this.Fecha_reserva = fecha_reserva;
            this.Hora_reserva = hora_reserva;
            this.Estado_reserva = estado_reserva;
            this.Lista_servicio = lista_servicio;
        }

        //metodos
        public string VerReserva()
        {

        }

        public string RegistrarReserva()
        {

        }

        public string Posponer()
        {

        }
    }
}
