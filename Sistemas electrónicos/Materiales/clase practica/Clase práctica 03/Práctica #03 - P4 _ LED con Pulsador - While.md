# **Parpadeo de un LED**
<img src="C:\one\OneDrive - UNP Universidad Nacional Politécnica\Clases\Materias\Sistemas electrónicos\Materiales\clase practica\Clase práctica 03\tkc2.png" align="left" width="350" style="margin-right: 20px;">

## **Código Arduino**

```cpp
// C++ code
//Bloque de Declaración 
int btn_e = 2;
int led_s = 3;
int estado = LOW;

void setup()
{
  pinMode(led_s, OUTPUT);
  pinMode(btn_e, INPUT);
  Serial.begin(9600);
}

void loop()
{
  while(digitalRead(btn_e) == LOW){
   
  }
 
  estado = digitalRead(led_s);
  digitalWrite(led_s, !estado);
  
  while(digitalRead(btn_e) == HIGH){
    
  }
}
```
[enlace en línea](https://www.tinkercad.com/things/eGTJqYk5g9r-practica-03-p4-led-con-pulsador-while)