# **Display 7 segmentos - ARRAY**
<img src="C:\one\OneDrive - UNP Universidad Nacional Politécnica\Clases\Materias\Sistemas electrónicos\Materiales\clase practica\Clase práctica 05\tkc1.png" align="left" width="350" style="margin-right: 20px;">

## **Código Arduino**

```cpp
// C++ code 
#define PTM A0 

int i = 0, lectura = 0, opt = 0;

int cero[7] = {HIGH, HIGH, HIGH, LOW, HIGH, HIGH, HIGH};
int uno[7]= {HIGH, LOW, LOW, LOW, LOW, LOW, HIGH};
int dos[7]= {HIGH, HIGH, LOW, HIGH, HIGH, HIGH, LOW};
int tres[7]= {HIGH, HIGH, LOW, HIGH, LOW, HIGH, HIGH};
int cuatro[7]= {HIGH, LOW, HIGH, HIGH, LOW, LOW, HIGH};
int cinco[7]= {LOW, HIGH, HIGH, HIGH, LOW, HIGH, HIGH};
int seis[7]= {LOW, LOW, HIGH, HIGH, HIGH, HIGH, HIGH};
int siete[7]= {HIGH, HIGH, LOW, LOW, LOW, LOW, HIGH};

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
  opt = map(lectura, 0, 1023, 0, 7);
  
  switch(opt){
    case 1: 
		for (i = 0; i < 7; i++){
    		digitalWrite(i, uno[i]);
  		}
    break;
    case 2: 
		for (i = 0; i < 7; i++){
    		digitalWrite(i, dos[i]);
  		}
    break;
    case 3: 
		for (i = 0; i < 7; i++){
    		digitalWrite(i, tres[i]);
  		}
    break;
    case 4: 
		for (i = 0; i < 7; i++){
    		digitalWrite(i, cuatro[i]);
  		}
    break;
    case 5: 
		for (i = 0; i < 7; i++){
    		digitalWrite(i, cinco[i]);
  		}
    break;
    case 6: 
		for (i = 0; i < 7; i++){
    		digitalWrite(i, seis[i]);
  		}
    break;
    case 7: 
		for (i = 0; i < 7; i++){
    		digitalWrite(i, siete[i]);
  		}
    break;
	default:
    	for (i = 0; i < 7; i++){
    		digitalWrite(i, cero[i]);
  		}
    break;
  }
}

```
[enlace en línea](https://www.tinkercad.com/things/6yAmXqS3itj-practica-05-p2-display-7-segmentos-array)