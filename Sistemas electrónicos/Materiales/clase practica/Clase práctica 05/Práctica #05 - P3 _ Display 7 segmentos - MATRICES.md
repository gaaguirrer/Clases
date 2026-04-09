# **Display 7 segmentos - MATRICES**
<img src="C:\one\OneDrive - UNP Universidad Nacional Politécnica\Clases\Materias\Sistemas electrónicos\Materiales\clase practica\Clase práctica 05\tkc1.png" align="left" width="350" style="margin-right: 20px;">

## **Código Arduino**

```cpp
// C++ code 
//constante de lectura de potenciómetro
#define PTM A0 

int i = 0, lectura = 0, num = 0;

int numeros [8][7] = 
  {
  {HIGH, HIGH, HIGH, LOW, HIGH, HIGH, HIGH},//0
  {HIGH, LOW, LOW, LOW, LOW, LOW, HIGH},//1
  {HIGH, HIGH, LOW, HIGH, HIGH, HIGH, LOW},//2
  {HIGH, HIGH, LOW, HIGH, LOW, HIGH, HIGH}, //3
  {HIGH, LOW, HIGH, HIGH, LOW, LOW, HIGH}, //4
  {LOW, HIGH, HIGH, HIGH, LOW, HIGH, HIGH}, //5
  {LOW, LOW, HIGH, HIGH, HIGH, HIGH, HIGH}, //6
  {HIGH, HIGH, LOW, LOW, LOW, LOW, HIGH} // 7
  };


void setup()
{
  //inicializamos todos los puertos usando un for
  for (i = 0; i < 7; i++){
    pinMode(i, OUTPUT);
  }
}

void loop()
{
  
  lectura = analogRead(PTM);
  num = map(lectura, 0, 1023, 0, 7);
  
  for (i = 0; i < 7; i++){
    digitalWrite(i, numeros[num][i]);
  }
  
}

```
[enlace en línea](https://www.tinkercad.com/things/5hK4rFX78mk-practica-05-p3-display-7-segmentos-matrices)