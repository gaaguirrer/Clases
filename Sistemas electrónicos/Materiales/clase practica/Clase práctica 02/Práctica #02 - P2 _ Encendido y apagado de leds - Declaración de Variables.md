# **Encendido y apagado de leds - Declaración de Variables**
<img src="C:\one\OneDrive - UNP Universidad Nacional Politécnica\Clases\Materias\Sistemas electrónicos\Materiales\clase practica\Clase práctica 02\tkc1.png" align="left" width="350" style="margin-right: 20px;">

## **Código Arduino**

```cpp
// C++ code
//Bloque de Declaración 
const int led_red = 11;
int led_yellow = 12;
int led_green = 13;
int espera1s = 1000;
int espera2s = 2000;
void setup()
{
  pinMode(led_red, OUTPUT);
  pinMode(led_yellow, OUTPUT);
  pinMode(led_green, OUTPUT);  
}

void loop()
{
  
  //Encendido Ordenado
  
  // bloque de encendido 
  digitalWrite(led_green, HIGH);
  delay(espera1s);
  digitalWrite(led_yellow, HIGH);
  delay(espera1s);
  digitalWrite(led_red, HIGH);
  delay(espera1s);
  
  // bloque de apagado 
  digitalWrite(led_red, LOW);
  delay(espera1s);
  digitalWrite(led_yellow, LOW);
  delay(espera1s);
  digitalWrite(led_green, LOW);
  delay(espera1s);
  
}
```
[enlace en línea](https://www.tinkercad.com/things/krWwHGmK3JH-practica-02-p2-encendido-y-apagado-de-leds-declaracion-de)