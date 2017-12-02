//LIBRARIES
#include <Keypad.h>

//CONSTANTS
#define NOTE_G6  1568
#define NOTE_C7  2093
#define NOTE_E7  2637
#define NOTE_G7  3136
#define melodyPin 10
const int buzzer = 10;
const int doorSensor = 12;
const byte ROWS = 4;
const byte COLS = 4;

//VARIABLES
int doorState;
int melody[] = {
  NOTE_E7, NOTE_E7, 0, NOTE_E7,
  0, NOTE_C7, NOTE_E7, 0,
  NOTE_G7, 0, 0,  0,
  NOTE_G6, 0, 0, 0,
};
int tempo[] = {
  12, 12, 12, 12,
  12, 12, 12, 12,
  12, 12, 12, 12,
  12, 12, 12, 12,
};
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
      Serial.println("{\"1\":\"Door is open\"}");
    } else if(currentState == 1) {
      Serial.println("{\"2\":\"Door is closed\"}");
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

//Buzz
void buzz(int targetPin, long frequency, long length) {
  digitalWrite(10, HIGH);
  long delayValue = 1000000 / frequency / 2;
  long numCycles = frequency * length / 1000;
  for (long i = 0; i < numCycles; i++) {
    digitalWrite(targetPin, HIGH);
    delayMicroseconds(delayValue);
    digitalWrite(targetPin, LOW);
    delayMicroseconds(delayValue);
  }
  digitalWrite(1000, LOW);
}

//Play ok
void playOK() {
  int song = 1;
  if (song == 1) {
    int size = sizeof(melody) / sizeof(int);
    for (int thisNote = 0; thisNote < size; thisNote++) {
      int noteDuration = 1000 / tempo[thisNote];

      buzz(melodyPin, melody[thisNote], noteDuration);

      int pauseBetweenNotes = noteDuration * 1.30;
      delay(pauseBetweenNotes);

      buzz(melodyPin, 0, noteDuration);
    }
  }
}

//Play ko
void playKO() {
  tone(buzzer, 1000);
  delay(100);
  noTone(buzzer);
}

//Read and validate pin code
void checkPinCode() {
  String password = "";

  char key = keypad.getKey();
  if (key && isNumber(key)) {
    while (key != '#') {
      if (isNumber(key)) {
        password = password + key;
      }
      key = keypad.getKey();
    }
    
    Serial.println("{\"3\":\"" + password + "\"}");
    Serial.flush();

    String response = "";
    while ((response != "{\"4\":\"OK\"}") && (response != "{\"4\":\"KO\"}")) {
      response = Serial.readString();
      Serial.println(response);
    }

    Serial.println(response);
    //Play music in function of response code
    if (response == "{\"4\":\"OK\"}") {
      Serial.println("OK");
      playOK();
    } else {
      Serial.println("KO");
      playKO();
    }
  }
}


//SETUP
void setup() {
  Serial.begin(9600);

  pinMode(doorSensor, INPUT_PULLUP);
  doorState = digitalRead(doorSensor);

  pinMode(10, OUTPUT);
  
  Serial.println("System init!!!");
}

//MAIN
void loop() {
  //1.- Read door state, if change state notify
  checkDoorState();
  //2.- Read keyboard pin and verify code
  checkPinCode();
  
  delay(200);
}
