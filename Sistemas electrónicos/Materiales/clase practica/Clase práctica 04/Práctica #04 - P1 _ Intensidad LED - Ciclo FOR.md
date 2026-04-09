# **Intensidad LED - Ciclo FOR**
<img src="C:\one\OneDrive - UNP Universidad Nacional Politécnica\Clases\Materias\Sistemas electrónicos\Materiales\clase practica\Clase práctica 04\tkc1.png" align="left" width="350" style="margin-right: 20px;">

## **Código Arduino**

```cpp
// C++ code
//Bloque de declaración
int led_pwm = 3, brillo = 0;

void setup()
{
  pinMode(led_pwm, OUTPUT);
}

void loop()
{
  for(brillo = 0; brillo < 256; brillo++)
  {
    analogWrite(led_pwm, brillo);
    delay(30);
  }
  for(brillo = 255; brillo >= 0; brillo--)
  {
    analogWrite(led_pwm, brillo);
    delay(30);
  }
}
  

```
[enlace en línea](https://www.tinkercad.com/things/aP2QLXK1Coa-practica-04-p1-intensidad-led-ciclo-for)