# **Parpadeo de un LED**
<img src="C:\one\OneDrive - UNP Universidad Nacional Politécnica\Clases\Materias\Sistemas electrónicos\Materiales\clase practica\Clase práctica 01\tkc.png" align="left" width="350" style="margin-right: 20px;">

## **Código Arduino**

```cpp
// C++ code
//
void setup()
{
  pinMode(12, OUTPUT);
}

void loop()
{
  digitalWrite(12, HIGH);
  delay(300); // Wait for 300 millisecond(s)
  digitalWrite(12, LOW);
  delay(300); // Wait for 300 millisecond(s)
}
```
[enlace en línea](https://www.tinkercad.com/things/hcn4lwRh4KY-practica-01-parpadeo-de-un-led)