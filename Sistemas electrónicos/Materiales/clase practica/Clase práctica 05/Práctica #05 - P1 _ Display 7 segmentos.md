# **Display 7 segmentos**
<img src="C:\one\OneDrive - UNP Universidad Nacional Politécnica\Clases\Materias\Sistemas electrónicos\Materiales\clase practica\Clase práctica 05\tkc1.png" align="left" width="350" style="margin-right: 20px;">

## **Código Arduino**

```cpp
// C++ code 
// la declaración como constante nos ayuda a ahorrar memoria
//podemos usar esta forma de declaracion
#define PTM A0 
//también podemos usar esta otra forma
const int B = 1, A = 2, F = 3, G = 4, E = 5, D = 6, C = 7;
int i = 0, lectura = 0, opt = 0;
void setup()
{
  //inicializamos todos los puertos usando un for
  for (i = 1; i < 8; i++){
    pinMode(i, OUTPUT);
  }
}

void loop()
{
  digitalWrite(A, LOW);
  digitalWrite(B, LOW);
  digitalWrite(C, LOW);
  digitalWrite(D, LOW);
  digitalWrite(E, LOW);
  digitalWrite(F, LOW);
  digitalWrite(G, LOW);
  
  lectura = analogRead(PTM);
  opt = map(lectura, 0, 1023, 0, 7);
  
  switch(opt){
    case 1: 
    	digitalWrite(A, LOW);
  		digitalWrite(B, HIGH);
  		digitalWrite(C, HIGH);
 		digitalWrite(D, LOW);
  		digitalWrite(E, LOW);
  		digitalWrite(F, LOW);
  		digitalWrite(G, LOW);
    break;
    case 2: 
       	digitalWrite(A, HIGH);
  		digitalWrite(B, HIGH);
  		digitalWrite(C, LOW);
 		digitalWrite(D, HIGH);
  		digitalWrite(E, HIGH);
  		digitalWrite(F, LOW);
  		digitalWrite(G, HIGH);
    break;
    case 3: 
        digitalWrite(A, HIGH);
  		digitalWrite(B, HIGH);
  		digitalWrite(C, HIGH);
 		digitalWrite(D, HIGH);
  		digitalWrite(E, LOW);
  		digitalWrite(F, LOW);
  		digitalWrite(G, HIGH);
    break;
    case 4: 
		digitalWrite(A, LOW);
  		digitalWrite(B, HIGH);
  		digitalWrite(C, HIGH);
 		digitalWrite(D, LOW);
  		digitalWrite(E, LOW);
  		digitalWrite(F, HIGH);
  		digitalWrite(G, HIGH);
    break;
    case 5: 
        digitalWrite(A, HIGH);
  		digitalWrite(B, LOW);
  		digitalWrite(C, HIGH);
 		digitalWrite(D, HIGH);
  		digitalWrite(E, LOW);
  		digitalWrite(F, HIGH);
  		digitalWrite(G, HIGH);
    break;
    case 6: 
        digitalWrite(A, LOW);
  		digitalWrite(B, LOW);
  		digitalWrite(C, HIGH);
 		digitalWrite(D, HIGH);
  		digitalWrite(E, HIGH);
  		digitalWrite(F, HIGH);
  		digitalWrite(G, HIGH);
    break;
    case 7: 
        digitalWrite(A, HIGH);
  		digitalWrite(B, HIGH);
  		digitalWrite(C, HIGH);
 		digitalWrite(D, LOW);
  		digitalWrite(E, LOW);
  		digitalWrite(F, LOW);
  		digitalWrite(G, LOW);
    break;
    default: 
      	digitalWrite(A, HIGH);
  		digitalWrite(B, HIGH);
  		digitalWrite(C, HIGH);
 		digitalWrite(D, HIGH);
  		digitalWrite(E, HIGH);
 		digitalWrite(F, HIGH);
  		digitalWrite(G, LOW);
    break;
  }
}
```
[enlace en línea](https://www.tinkercad.com/things/jwXDFgxly2N-practica-05-p1-display-7-segmentos)