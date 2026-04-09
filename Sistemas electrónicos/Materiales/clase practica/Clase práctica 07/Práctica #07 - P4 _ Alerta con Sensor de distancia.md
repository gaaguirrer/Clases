# **Alerta con Sensor de distancia**
<img src="C:\one\OneDrive - UNP Universidad Nacional Politécnica\Clases\Materias\Sistemas electrónicos\Materiales\clase practica\Clase práctica 07\tkc4.png" align="center" width="350" style="margin-right: 20px;">

## **Código Arduino**

```cpp
const int led = 2, echo = 4, trig = 3;
int time = 0;
float distancia = 0;
void setup ()
{
  Serial.begin (9600);
  pinMode (led, OUTPUT);
  pinMode (echo, INPUT);
  pinMode (trig, OUTPUT);
}
void loop ()
{
  digitalWrite (trig,HIGH);
  delay(1);
  digitalWrite (trig, LOW);
  
  time= pulseIn (echo, HIGH);
  distancia=time/58.2;
  
  if (distancia <=150)
    digitalWrite (led, HIGH);
  else 
    digitalWrite (led, LOW);
}

```
[enlace en línea](https://www.tinkercad.com/things/kdX2Tsg0tZ4-practica-07-p4-alerta-con-sensor-de-distancia)