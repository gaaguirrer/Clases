# **Prendido y apagado de leds ordenados - Declaración de Variables**
<img src="C:\one\OneDrive - UNP Universidad Nacional Politécnica\Clases\Materias\Sistemas electrónicos\Materiales\clase practica\Clase práctica 02\tkc1.png" align="left" width="350" style="margin-right: 20px;">

## **Código Arduino**

```cpp
// C++ code
//Bloque de Declaración 
const int led_red = 11;
int led_yellow = 12;
int led_green = 13;
void setup()
{
  pinMode(led_red, OUTPUT);
  pinMode(led_yellow, OUTPUT);
  pinMode(led_green, OUTPUT);  
}

void loop()
{
  //leds intermitentes
  digitalWrite(led_red, HIGH);
  delay(300);
  digitalWrite(led_red, LOW);
  delay(300);
  digitalWrite(led_yellow, HIGH);
  delay(300);
  digitalWrite(led_yellow, LOW);
  delay(300);
  digitalWrite(led_green, HIGH);
  delay(300);
  digitalWrite(led_green, LOW);
  delay(300);
}
```

[enlace en línea](https://www.tinkercad.com/things/aTfUZXeMB4w-practica-02-p1-prendido-y-apagado-de-leds-ordenados-declaracion)