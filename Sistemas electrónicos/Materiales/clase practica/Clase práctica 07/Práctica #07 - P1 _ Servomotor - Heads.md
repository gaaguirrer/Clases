# **Servomotor - Heads**
<img src="C:\one\OneDrive - UNP Universidad Nacional Politécnica\Clases\Materias\Sistemas electrónicos\Materiales\clase practica\Clase práctica 07\tkc1.png" align="center" width="350" style="margin-right: 20px;">

## **Código Arduino**

```cpp
// C++ code
//Cuidado con los servos, para los microservos 5V sirven
// un servo a veces necesita de 7.5 a 12V que podrían
//quemar arduino o el USB de la PC, así que de preferencia
// Al usar servos se recomienda conectar arduino a 
//una fuente de alimentación externa de 7.8 a 12v
// y que genere 750 mA revisar bien el conectar y 
//las especificaciones de los fabricantes de arduino

//Los motores servos se manejan con una cabecera / biblioteca
#include <Servo.h> //contiene la clase servo y sus funciones
Servo servo1;//Declaramos un objeto de tipo servo

const int SERVO = 2;
//Se recomienda usar 1000 y 2000 como valores de prueba para
//mínimo y maximo, estos son los valores para el simulador
const int PULSO_MIN = 500; //indica cero grados
const int PULSO_MAX= 800; //indica 180 grados

int angulo = 0;
void setup()
{
  //Inicializamos nuestro motor usando la función attach
  //sus parametros son pin, pulso minimo, pulso maximo
  servo1.attach(SERVO, PULSO_MIN, PULSO_MAX);
  
}

void loop()
{
  //indicamos al servo el ángulo al que debe posicionarse
  // La mayoría de los servos no pueden dar un giro de 360 grados
  // sólo pueden ir de 0 a 180 grados, ignorarlo quemaría el servo
 
  servo1.write(0);
  delay(2000);
  servo1.write(180);
  delay(2000);
  }

```
[enlace en línea](https://www.tinkercad.com/things/hQc1mxozhRq-practica-07-p1-control-de-servomotor-heads)