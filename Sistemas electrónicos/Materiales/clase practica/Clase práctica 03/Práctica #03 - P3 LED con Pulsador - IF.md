# **LED con Pulsador - IF**
<img src="C:\one\OneDrive - UNP Universidad Nacional Politécnica\Clases\Materias\Sistemas electrónicos\Materiales\clase practica\Clase práctica 03\tkc2.png" align="left" width="350" style="margin-right: 20px;">

## **Código Arduino**

```cpp
// C++ code
//Bloque de Declaración 
int btn_e = 2;
int led_s = 3;
bool estado = LOW;
 
void setup()
{
  pinMode(led_s, OUTPUT);
  pinMode(btn_e, INPUT);
}

void loop()
{
  //Presiono el botón y enciende led, velvo a
  //presionar el botón y se apaga el led
  // declara "bool estado = LOW;" arriba
  if (digitalRead(btn_e) == HIGH)
  {
    estado = !estado;
  }
  digitalWrite(led_s, estado);
  //delay(1000);
  
}
```
[enlace en línea](https://www.tinkercad.com/things/6B7IzGtkjFa-practica-03-p3-led-con-pulsador-if)