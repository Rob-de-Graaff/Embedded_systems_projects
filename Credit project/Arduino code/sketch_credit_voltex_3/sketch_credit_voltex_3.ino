
int outputPin = 13;
int startDelay = 120;
bool ready = false;

void setup() {
  // put your setup code here, to run once:
  pinMode(outputPin, INPUT);

  
  for(int i = 0; i < startDelay; i++) {
    delay(1000);  
    if(i >= startDelay){ready = true;}
   
  }

}

void loop() {
  if (ready == true){
    for(int i = 0; i < 99; i++) {
      pinMode(outputPin, OUTPUT);
      digitalWrite(outputPin, LOW);
      delay(40);
      pinMode(outputPin, INPUT);
      delay(30);
    }
  }
}