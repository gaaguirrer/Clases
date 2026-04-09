# **Pantalla LCD 16x2**
<img src="C:\one\OneDrive - UNP Universidad Nacional Politécnica\Clases\Materias\Sistemas electrónicos\Materiales\clase practica\Clase práctica 08\tkc2.png" align="center" width="350" style="margin-center: 20px;">
<br>
<img src="C:\one\OneDrive - UNP Universidad Nacional Politécnica\Clases\Materias\Sistemas electrónicos\Materiales\clase practica\Clase práctica 08\tkc3.png" align="center" width="350" style="margin-right: 20px;">
<br>

## **Código Arduino**

```cpp
#include <LiquidCrystal.h>
//declaramos las constantes de la data de la pantalla
const int RS = 2, E = 3, D4 = 4, D5 = 5, D6 = 6, D7 = 7;
int num = 9; //inicializamos la cuenta regresiva

//Declaramos el Objeto que nos permitirá manipular la pantalla
LiquidCrystal lcd(RS, E, D4, D5, D6, D7);

void setup() {
  // Inicializaremos la pantalla enviando al objeto la 
  //información de nuestra pantalla en este caso es una 16x2
  lcd.begin(16, 2);
}

void loop() {
  // indicamos a la pantalla la posición inicial con coordenadas
  lcd.setCursor(0, 0);
  //al igual que con el puerto serial se usa print para 
  // mostrar la información por pantalla
  lcd.print("cuenta regresiva");
  
  //indicamos que vamos a escribir en la segunda fila
  lcd.setCursor(0, 1);
  lcd.print(num);
 
  num--; //como es cuenta regresiva restamos uno
  delay(1000);
  
  if (num < 1) {
    num = 9;
  }
  
  lcd.clear(); //limpiamos pantalla
}

```
[enlace en línea](https://www.tinkercad.com/things/7B6L6WMmvzu-practica-08-p2-pantalla-lcd-16x2)
