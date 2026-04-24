using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Proyecto_quiek_beaty
{
   public class Banco
    {
        private string _cuenta_colaboradores;
        private string _nombre_banco;

        public string Cuenta_colaboradores { get => _cuenta_colaboradores; set => _cuenta_colaboradores = value; }

        public string Nombre_banco { get => _nombre_banco; set => _nombre_banco = value; }

        //contructor
        public Banco()
        {

        }
        public Banco(string cuenta_colaboradores, string nombre_banco)
        {
            this.Cuenta_colaboradores = cuenta_colaboradores;
            this.Nombre_banco = nombre_banco;
        }
        //metodos
        public string Pagar_colaboradores(Banco banco)
        {

        }
        public string Depositar_pago(Banco banco)
        {

        }
    }
}
