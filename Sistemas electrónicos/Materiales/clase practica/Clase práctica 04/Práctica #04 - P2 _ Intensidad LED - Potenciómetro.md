# **Intensidad LED - Potenciómetro**
<img src="C:\one\OneDrive - UNP Universidad Nacional Politécnica\Clases\Materias\Sistemas electrónicos\Materiales\clase practica\Clase práctica 04\tkc2.png" align="left" width="350" style="margin-right: 20px;">

## **Código Arduino**

```cpp
// C++ code
//Bloque de declaración
int led_pwm = 3, brillo = 0, ptm = 0;

void setup()
{
  pinMode(led_pwm, OUTPUT);
  // recuerda las entradas analógicas
  //no necesitan inicializarse en setup
  //porque todos los puertos analógicos son entradas
  Serial.begin(9600);
}
//recuerda las entradas analógicas van de 0 a 1023
// así que lo que se lee en la entrada analógica
// se puede dividir su voltaje / señal en 1024 partes
void loop()
{
  //Se divide entre 4 para igualar las 1024 partes
  // de la entrada analógica a las 255 partes de la
  //entrada pwm, no importan los decimales, porque
  //sólo almacena la parte entera
  brillo = analogRead(ptm)/ 4;
  Serial.println(brillo);
  digitalWrite(led_pwm, brillo);
}

```
[enlace en línea](https://www.tinkercad.com/things/gxYQFVpLkst-practica-04-p2-intensidad-led-potenciometro)