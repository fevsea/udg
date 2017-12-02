//LIBRARIES
#include <Keypad.h>

//CONSTANTS
const int doorSensor = 12;
const byte ROWS = 4;
const byte COLS = 4;

//VARIABLES
int doorState;
char keys[ROWS][COLS] = {
  {'1','2','3','A'},
  {'4','5','6','B'},
  {'7','8','9','C'},
  {'#','0','*','D'}
};
byte rowPins[ROWS] = {9, 8, 7, 6};
byte colPins[COLS] = {5, 4, 3, 2};
Keypad keypad = Keypad(makeKeymap(keys), rowPins, colPins, ROWS, COLS);

//FUNCTIONS
//Read door state 
void checkDoorState() {
  int currentState = digitalRead(doorSensor);
  
  if(doorState != currentState) {
    doorState = currentState;
    
    if(currentState == 0) {
      Serial.println("Door is open");
    } else if(currentState == 1) {
      Serial.println("Door is closed");
    }
    Serial.flush();
  }
}

//Check if key is 0-9 or */#
bool isNumber(char key) {
  if (key == '0' || key == '1' || key == '2' || key == '3' || key == '4' || key == '5' || key == '6' || key == '7' || key == '8' || key == '9' || key == '*' || key == '#') {
    return true;
  } else {
    return false;
  }
}

//Read and validate pin code
void checkPinCode() {
  String password = "";

  char key = keypad.getKey();
  if (key && isNumber(key)) {
    while (key != '#') {
      if (isNumber(key)) {
        password = password + key;
        Serial.println(password);
      }
      key = keypad.getKey();
      delay(200);
    }
    
    Serial.println("{\"3\":\"" + password + "\"}");
    Serial.flush();

//    if (Serial.available() > 0) {
//      
//    }
  }
}


//SETUP
void setup() {
  Serial.begin(9600);

  pinMode(doorSensor, INPUT_PULLUP);
  doorState = digitalRead(doorSensor);
  
  Serial.println("System init!!!");
}

//MAIN
void loop() {
  //1.- Read door state, if change state notify
  checkDoorState();
  //2.- Read keyboard pin and verify code
  checkPinCode();
  
  delay(500);
}
