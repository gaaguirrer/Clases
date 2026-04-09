# **Control de Distribución de voltaje - Declaración de Variables**
<img src="C:\one\OneDrive - UNP Universidad Nacional Politécnica\Clases\Materias\Sistemas electrónicos\Materiales\clase practica\Clase práctica 03\tkc1.png" align="left" width="350" style="margin-right: 20px;">

## **Código Arduino**

```cpp
// C++ code
//
int ptm = A0, ldG = 5, ldR = 3, lectura = 0;
//Las resistencias son 220 ohm
void setup()
{
  pinMode(ldG, OUTPUT);
  pinMode(ldR, OUTPUT);
}

void loop()
{
  lectura = analogRead(ptm);
  analogWrite(ldG, lectura/4);
  analogWrite(ldR, (1023 - lectura)/4);
}
```
[enlace en línea](https://www.tinkercad.com/things/33qYNMkk8s4-practica-03-p1-control-de-distribucion-de-voltaje-declaracion-de)