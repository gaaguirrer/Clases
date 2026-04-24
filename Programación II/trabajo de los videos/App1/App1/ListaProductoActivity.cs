using System;
using System.Collections.Generic;
using System.Drawing;
using System.Linq;
using System.Text;

using Android.App;
using Android.Content;
using Android.OS;
using Android.Runtime;
using Android.Views;
using Android.Widget;
using Newtonsoft.Json;

namespace App1
{
    [Activity(Label = "ListaProductoActivity")]
    public class ListaProductoActivity : Activity
    {
        protected override void OnCreate(Bundle savedInstanceState)
        {
            base.OnCreate(savedInstanceState);

            var items = JsonConvert.DeserializeObject<List<string[]>>(Intent.GetStringExtra("data"));

            Console.WriteLine(items[0][0]);
            Console.WriteLine(items[0][1]);

            var layout = new LinearLayout(this);
            layout.Orientation = Orientation.Vertical;

            for (int i=0; i<items.Count; i++)
                {
                var layoutH = new LinearLayout(this);
                layoutH.Orientation = Orientation.Horizontal;

                var txtProducto = new TextView(this);
                txtProducto.Text = items[i][0];
                txtProducto.SetWidth(500);
                txtProducto.SetPadding(0, 5, 5, 0);
                txtProducto.SetTextSize(Android.Util.ComplexUnitType.Sp, 24);
                txtProducto.SetTypeface(null, Android.Graphics.TypefaceStyle.Bold);
               

                var txtCantidad = new TextView(this);
                txtCantidad.Text = items[i][1];
                txtCantidad.SetWidth(500);
                txtCantidad.SetPadding(0, 5, 5, 0);
                txtCantidad.SetTextSize(Android.Util.ComplexUnitType.Sp, 24);

                layoutH.AddView(txtProducto);
                layoutH.AddView(txtCantidad);

                layout.AddView(layoutH);


            }

            SetContentView(layout); 

        }
    }
}