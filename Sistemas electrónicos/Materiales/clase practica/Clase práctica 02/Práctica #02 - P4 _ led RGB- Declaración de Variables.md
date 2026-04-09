# **Semáforo - Declaración de Variables**
<img src="C:\one\OneDrive - UNP Universidad Nacional Politécnica\Clases\Materias\Sistemas electrónicos\Materiales\clase practica\Clase práctica 02\tkc2.png" align="left" width="350" style="margin-right: 20px;">

## **Código Arduino**

```cpp
// C++ code
//
int ledR = 9, ledG = 11, ledB = 10;
int espera= 1000;
void setup()
{
  pinMode(ledR, OUTPUT);
  pinMode(ledG, OUTPUT);
  pinMode(ledB, OUTPUT);
}

void loop()
{
  digitalWrite(ledR, LOW);
  digitalWrite(ledG, LOW);
  //Color AZUL
  digitalWrite(ledB, HIGH);
  delay(espera);
  //Color Verde
  digitalWrite(ledB, LOW);
  digitalWrite(ledG, HIGH);
  delay(espera);
  //Color Cian
  digitalWrite(ledB, HIGH);
  delay(espera);
  //Color ROJO
  digitalWrite(ledB, LOW);
  digitalWrite(ledG, LOW);
  digitalWrite(ledR, HIGH);
  delay(espera);
  //Magenta
  digitalWrite(ledB, HIGH);
  delay(espera);
  //Amarillo
  digitalWrite(ledB, LOW);
  digitalWrite(ledG, HIGH);
  delay(espera);
  //Blanco
  digitalWrite(ledB, HIGH);
  delay(espera);
  
}
```
[enlace en línea](https://www.tinkercad.com/things/5WRUN4WovN9-practica-02-p4-led-rgb-declaracion-de-variables)