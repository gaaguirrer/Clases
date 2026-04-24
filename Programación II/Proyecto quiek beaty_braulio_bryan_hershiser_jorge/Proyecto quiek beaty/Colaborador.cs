using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Proyecto_quiek_beaty
{
    public class Colaborador
    {
        private string _cedula;
        private string _nombre;
        private string _apellido;
        private int _telefono;
        private int _edad;
        private string _sexo;
        private string _direccion;
        private string _servicios_que_presta;

        public string Cedula { get => _cedula; set => _cedula = value; }

        public string Nombre { get => _nombre; set => _nombre = value; }

        public string Apellido { get => _apellido; set => _apellido = value; }

        public int Telefono { get => _telefono; set => _telefono = value; }

        public int Edad { get => _edad; set => _edad = value; }

        public string Sexo { get => _sexo; set => _sexo = value; }

        public string Direccion { get => _direccion; set => _direccion = value; }

        public string Servicios_que_presta { get => _servicios_que_presta; set => _servicios_que_presta = value; }

        //contructor vacío
        public Colaborador()
        {

        }

        //contrutor con parametros
        public Colaborador(string cedula,string nombre,string apellido, int telefono,int edad, string sexo, string direccion, string servicios_que_presta)
        {
            this.Cedula = cedula;
            this.Nombre = nombre;
            this.Apellido = apellido;
            this.Telefono = telefono;
            this.Edad = edad;
            this.Sexo = sexo;
            this.Direccion = direccion;
            this.Servicios_que_presta = servicios_que_presta;
        }

        //Metodo Insertar colaborador

        public string Insertar(Colaborador colaborador)
        {

        }

        //eliminar colaborador
        public string Eliminar(Colaborador colaborador)
        {

        }
    }

   
}
