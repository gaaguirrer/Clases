# **Sensor de distancia**
<img src="C:\one\OneDrive - UNP Universidad Nacional Politécnica\Clases\Materias\Sistemas electrónicos\Materiales\clase practica\Clase práctica 07\tkc3.png" align="center" width="350" style="margin-right: 20px;">

## **Código Arduino**

```cpp
const int echo = 4, trig = 3;
int time = 0; 
float distancia = 0;
void setup ()
{
  Serial.begin (9600);
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
  
  Serial.print("tiempo= ");
  Serial.print(time);
  Serial.print("\t distancia= ");
  Serial.println(distancia);
  
}
```
[enlace en línea](https://www.tinkercad.com/things/dTtCy72ybhb-practica-07-p3-sensor-de-distancia)