const int pinSensor = 4;
const int pinOpen = 7;
bool state = true;

void setup() {
  // put your setup code here, to run once:
  pinMode(pinSensor, INPUT_PULLUP);
  pinMode(pinOpen, OUTPUT);
  Serial.begin(9600); //Empieza el serial para enviar dator a la consola
}

void loop() {
  // put your main code here, to run repeatedly:
  int value = digitalRead(pinSensor);
  int currentState = digitalRead(pinSensor);

  if(value == HIGH){
    digitalWrite(pinOpen, HIGH);
    }else {
    digitalWrite(pinOpen, LOW);
    }

   if(state != currentState) {
    if(currentState == 0){
     String string = ("Door is open");
     Serial.println(string);
    }else if(currentState == 1){
     String string = ("Door is closed");
     Serial.println(string);      
    }
    state = currentState;
   }

    delay(1000);
}
