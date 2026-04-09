# **Controlar varios leds - SWITCH**
<img src="C:\one\OneDrive - UNP Universidad Nacional Politécnica\Clases\Materias\Sistemas electrónicos\Materiales\clase practica\Clase práctica 02\tkc1.png" align="left" width="350" style="margin-right: 20px;">

## **Código Arduino**

```cpp
// C++ code
//
int ledRd = 3, ledYllw = 5, ledGrn = 6; //declaramos los puertos y leds
void setup()
{ //inicializamos los puertos en estado de salida
  pinMode(ledRd, OUTPUT);
  pinMode(ledYllw, OUTPUT);
  pinMode(ledGrn, OUTPUT);
}

void loop()
{
  int inicial = random(1,4); //generamos un número aleatorio entre 1 y 3
  switch(inicial){
    case 1:
    	digitalWrite(ledRd, HIGH);
    	digitalWrite(ledYllw, LOW);
    	digitalWrite(ledGrn, LOW);
    break;
    case 2:
    	digitalWrite(ledRd, LOW);
    	digitalWrite(ledYllw, HIGH);
    	digitalWrite(ledGrn, LOW);
    break;
    case 3:
    	digitalWrite(ledRd, LOW);
    	digitalWrite(ledYllw, LOW);
    	digitalWrite(ledGrn, HIGH);
    break;
  }  
  delay(1000);
}

```
[enlace en línea](https://www.tinkercad.com/things/5LJsFDHP1rS-practica-04-p3-controlar-varios-leds-switch)