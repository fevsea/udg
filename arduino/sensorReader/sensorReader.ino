//CONSTANTS
const int doorSensor = 4;

//VARIABLES
int doorState;

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
  
  delay(1000);
}
