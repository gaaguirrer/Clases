# **Control de Servomotor**
<img src="C:\one\OneDrive - UNP Universidad Nacional Politécnica\Clases\Materias\Sistemas electrónicos\Materiales\clase practica\Clase práctica 07\tkc2.png" align="center" width="350" style="margin-right: 20px;">

## **Código Arduino**

```cpp
// C++ code

#include <Servo.h>
Servo servo1;

const int SERVO = 2;

const int PULSO_MIN = 500; //indica cero grados
const int PULSO_MAX = 800; //indica 180 grados

//control de potenciometro
const int PTM = 0, 
int valor_ptm = 0;

int angulo = 0;

void setup()
{
  servo1.attach(SERVO, PULSO_MIN, PULSO_MAX);
}

void loop()
{
  valor_ptm = analogRead(PTM);
  //convertimos el valor del potenciometro en ángulo usando map
  //map toma como argumentos (valor a convertir, valor base 
  //de la fuente, valor máximo de la fuente, valor base del detino
  //valor máximo del destino), en este caso la fuente es 
  //analógica, por eso inicia el cero y el máximo es 1023,
  //el destino es un ángulo de 0 a 180 grados
  angulo = map(valor_ptm, 0, 1023, 0, 180);
  servo1.write(angulo);
  delay(20);//le damos tiempo al servo de moverse, el retardo
  //debe aumentar proporcionalmente al peso que mueve

}
```
[enlace en línea](https://www.tinkercad.com/things/8osopeAd574-practica-07-p2-control-de-servomotor-heads)