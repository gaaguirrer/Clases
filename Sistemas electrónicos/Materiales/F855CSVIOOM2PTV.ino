
/*
Author: Danny van den Brande. Arduinosensors.nl. BlueCore Tech.
Hello world! Today i made a little time bomb for airsoft purposes. 
I am not responsible for any other uses!
You can make a bomb with a motion sensor to, this is not what it is about. Its for fun recreational and educational use. 
 */
#include <avr/wdt.h> // Watchdog timer library

int segA = 5;  //   11
int segB = 13; //   7
int segC = 10; //   4
int segD = 8;  //   2
int segE = 7;  //   1
int segF = 4;  //   10
int segG = 11; //   5
int segPt = 9; //   3

int d1 = 6;   
int d2 = 3;   
int d3 = 2;   
int d4 = 12;  

int SecondCount = 2650; // change this if seconds dont work right. this worked for me. Its just a simple way to count down seconds without librarys.
int i=0;
int buzzer = A0;
int relay = A1;
int button = A2;
boolean val;

void setup() {
  Serial.begin(9600);
  pinMode(2, OUTPUT);
  pinMode(3, OUTPUT);
  pinMode(4, OUTPUT);
  pinMode(5, OUTPUT);
  pinMode(6, OUTPUT);
  pinMode(7, OUTPUT);
  pinMode(8, OUTPUT);
  pinMode(9, OUTPUT);
  pinMode(10, OUTPUT);
  pinMode(11, OUTPUT);
  pinMode(12, OUTPUT);
  pinMode(13, OUTPUT);
  pinMode(buzzer, OUTPUT);
  pinMode(relay, OUTPUT);
  digitalWrite(relay, LOW);
  pinMode(button, INPUT);
  

}

void loop() {
  allStart(0);//displays the numbers at the start 0 can be 1 2 3 4 5 6 7 8 9
  val = analogRead(button);
      if (val == 0){
      countingdown(0,2,0,0); //    SET COUNTDOWN TIME HERE (0,2,0,0); = 20 seconds
      all(0); // Displays the numbers at the end. You can change it to any number. 0 can be 1 2 3 4 5 6 7 8 9
      beepsoundRelay();  
      wdt_enable(WDTO_2S); // this enables the reset with Watchdog timer for arduino.
      wdt_reset(); // this will reset it using the <avr/wdt.h> Watchdog timer Library. You can change the time to restart at void beepsoundRelay(); its at 10 second now.
  }    
}

void countingdown(int a,int b,int c,int d){
  
  while (a != -1) {
    while(b != -1){
      while(c != -1){
        while (d != -1) {
          while (i<10) { // "i" here is like a timer ! Because we can't use a delay function
            selectDwriteL(1,a);
            selectDwriteL(2,b);
            selectDwriteL(3,c);
            selectDwriteL(4,d);
            i++;
          }
          i=0;
          d--;
        }
        d=9;
        c--;
      }
      c=9;
      b--;
    }
    b=9;
    a--;
    }
}

//Select Wich Digit (selectD) is going to Display (writeL)
void selectDwriteL(int d,int l){
  switch (d) { // choose a digit
    case 0: digitalWrite(d1, LOW); //case 0 - All ON
            digitalWrite(d2, LOW);
            digitalWrite(d3, LOW);
            digitalWrite(d4, LOW);
            break;
    case 1: digitalWrite(d1, LOW);//case 1 - Digit Number 1
            digitalWrite(d2, HIGH);
            digitalWrite(d3, HIGH);
            digitalWrite(d4, HIGH);
            break;
    case 2: digitalWrite(d1, HIGH);//case 1 - Digit Number 2
            digitalWrite(d2, LOW);
            digitalWrite(d3, HIGH);
            digitalWrite(d4, HIGH);
            break;
    case 3: digitalWrite(d1, HIGH);//case 1 - Digit Number 3
            digitalWrite(d2, HIGH);
            digitalWrite(d3, LOW);
            digitalWrite(d4, HIGH);
            break;
    case 4: digitalWrite(d1, HIGH);//case 1 - Digit Number 4
            digitalWrite(d2, HIGH);
            digitalWrite(d3, HIGH);
            digitalWrite(d4, LOW);
            break;
  }

  switch (l) { // choose a Number
  
    case 0: zero();
            break;
    case 1: one();
            break;
    case 2: two();
            break;
    case 3: three();
            break;
    case 4: four();
            break;
    case 5: five();
            break;
    case 6: six();
            break;
    case 7: seven();
            break;
    case 8: eight();
            break;
    case 9: nine();
            break;
    case 10: point(); 
            break;
    case 11: none(); 
            break;
            
  }
delayMicroseconds(SecondCount);
}

void all(int n){ // this will display numbers when exploding, you set it at void loop.
  selectDwriteL(0,n); // Displays whatever you set at void loop all(0); 0 can be 1 2 3 4 5 6 7 8 9
}

void allStart(int n){ // Displays whatever you set at void loop allStart(0); 0 can be 1 2 3 4 5 6 7 8 9
  selectDwriteL(0,n);
}

void zero(){
  digitalWrite(segA, HIGH);
  digitalWrite(segB, HIGH);
  digitalWrite(segC, HIGH);
  digitalWrite(segD, HIGH);
  digitalWrite(segE, HIGH);
  digitalWrite(segF, HIGH);
  digitalWrite(segG, LOW);
  digitalWrite(segPt, LOW);
}
void one(){
  digitalWrite(segA, LOW);
  digitalWrite(segB, HIGH);
  digitalWrite(segC, HIGH);
  digitalWrite(segD, LOW);
  digitalWrite(segE, LOW);
  digitalWrite(segF, LOW);
  digitalWrite(segG, LOW);
  digitalWrite(segPt, LOW);
}
void two(){
  digitalWrite(segA, HIGH);
  digitalWrite(segB, HIGH);
  digitalWrite(segC, LOW);
  digitalWrite(segD, HIGH);
  digitalWrite(segE, HIGH);
  digitalWrite(segF, LOW);
  digitalWrite(segG, HIGH);
  digitalWrite(segPt, LOW);
}
void three(){
  digitalWrite(segA, HIGH);
  digitalWrite(segB, HIGH);
  digitalWrite(segC, HIGH);
  digitalWrite(segD, HIGH);
  digitalWrite(segE, LOW);
  digitalWrite(segF, LOW);
  digitalWrite(segG, HIGH);
  digitalWrite(segPt, LOW);
}
void four(){
  digitalWrite(segA, LOW);
  digitalWrite(segB, HIGH);
  digitalWrite(segC, HIGH);
  digitalWrite(segD, LOW);
  digitalWrite(segE, LOW);
  digitalWrite(segF, HIGH);
  digitalWrite(segG, HIGH);
  digitalWrite(segPt, LOW);
}
void five(){
  digitalWrite(segA, HIGH);
  digitalWrite(segB, LOW);
  digitalWrite(segC, HIGH);
  digitalWrite(segD, HIGH);
  digitalWrite(segE, LOW);
  digitalWrite(segF, HIGH);
  digitalWrite(segG, HIGH);
  digitalWrite(segPt, LOW);
}
void six(){
  digitalWrite(segA, HIGH);
  digitalWrite(segB, LOW);
  digitalWrite(segC, HIGH);
  digitalWrite(segD, HIGH);
  digitalWrite(segE, HIGH);
  digitalWrite(segF, HIGH);
  digitalWrite(segG, HIGH);
  digitalWrite(segPt, LOW);
}
void seven(){
  digitalWrite(segA, HIGH);
  digitalWrite(segB, HIGH);
  digitalWrite(segC, HIGH);
  digitalWrite(segD, LOW);
  digitalWrite(segE, LOW);
  digitalWrite(segF, LOW);
  digitalWrite(segG, LOW);
  digitalWrite(segPt, LOW);
}
void eight(){
  digitalWrite(segA, HIGH);
  digitalWrite(segB, HIGH);
  digitalWrite(segC, HIGH);
  digitalWrite(segD, HIGH);
  digitalWrite(segE, HIGH);
  digitalWrite(segF, HIGH);
  digitalWrite(segG, HIGH);
  digitalWrite(segPt, LOW);
}
void nine(){
  digitalWrite(segA, HIGH);
  digitalWrite(segB, HIGH);
  digitalWrite(segC, HIGH);
  digitalWrite(segD, HIGH);
  digitalWrite(segE, LOW);
  digitalWrite(segF, HIGH);
  digitalWrite(segG, HIGH);
  digitalWrite(segPt, LOW);
}
void point(){
  digitalWrite(segA, LOW);
  digitalWrite(segB, LOW);
  digitalWrite(segC, LOW);
  digitalWrite(segD, LOW);
  digitalWrite(segE, LOW);
  digitalWrite(segF, LOW);
  digitalWrite(segG, LOW);
  digitalWrite(segPt, HIGH);
}
void none(){
  digitalWrite(segA, LOW);
  digitalWrite(segB, LOW);
  digitalWrite(segC, LOW);
  digitalWrite(segD, LOW);
  digitalWrite(segE, LOW);
  digitalWrite(segF, LOW);
  digitalWrite(segG, LOW);
  digitalWrite(segPt, LOW);
}

void beepsoundRelay() { //Beep Beep Beep, Boom!
digitalWrite(buzzer, HIGH);
delay(200);
digitalWrite(buzzer, LOW);
delay(100);
digitalWrite(buzzer, HIGH);
delay(200);
digitalWrite(buzzer, LOW);
delay(100);
digitalWrite(buzzer, HIGH);
delay(200);
digitalWrite(buzzer, LOW);
digitalWrite(relay, HIGH);
delay(10000); // After 10 Seconds it will reset itself using the <avr/wdt.h> library in loop using wdt_enable(WDTO_2S); and wdt_reset();
}

