using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Proyecto_quiek_beaty
{
   public class Cliente
    {
        private string _cedula;
        private string _nombre;
        private string _apellido;
        private string _direccion;
        private int _telefono;
        private int _edad;
        private string _metodo_de_pago;

        public string Cedula { get => _cedula; set => _cedula = value; }

        public string Nombre { get => _nombre; set => _nombre = value; }

        public string Apellido { get => _apellido; set => _apellido = value; }

        public string Direccion { get => _direccion; set => _direccion = value; }

        public int Telefono { get => _telefono; set => _telefono = value; }

        public int Edad { get => _edad; set => _edad = value; }

        public string Metodo_de_pago { get => _metodo_de_pago; set => _metodo_de_pago = value; }

        //contructor
        public Cliente() { }

        public Cliente(string cedula,string nombre, string apellido, string direccion,int telefono, int edad,string metodo_de_pago)
        {
            this.Cedula = cedula;
            this.Nombre = nombre;
            this.Apellido = apellido;
            this.Direccion = direccion;
            this.Telefono = telefono;
            this.Edad = edad;
            this.Metodo_de_pago = metodo_de_pago;
        }

        public string Añadir()
        {

        }

        public string Editar()
        {

        }

        public string EliminarCliente()
        {

        }
    }
}
