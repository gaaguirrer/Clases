using Android.App;
using Android.Widget;
using Android.OS;
using System.Collections.Generic;
using Android.Content;
using Newtonsoft.Json;

namespace App1
{
    [Activity(Label = "App1", MainLauncher = true)]
    public class MainActivity : Activity
    {

        public List<string[]> miProducto = new List<string[]>();

        public object Jsonconvert { get; private set; }

        protected override void OnCreate(Bundle savedInstanceState)
        {
            base.OnCreate(savedInstanceState);

            // Set our view from the "main" layout resource
            SetContentView(Resource.Layout.Main);
         
            var btn = FindViewById<Button>(Resource.Id.btnAgregar);

            btn.Click += Btn_Click;

        }

        private void Btn_Click(object sender, System.EventArgs e)
        {
            var producto = FindViewById<EditText>(Resource.Id.txtProducto);
            var cantidad = FindViewById<EditText>(Resource.Id.txtCantidad);


            string[] data = new string[] { producto.Text, cantidad.Text };

            miProducto.Add(data);

            producto.Text = "";
            cantidad.Text = "";

            var intent = new Intent(this, typeof(ListaProductoActivity));
            intent.PutExtra("data", JsonConvert.SerializeObject(miProducto));

            StartActivity(intent);



        }
    }
}

