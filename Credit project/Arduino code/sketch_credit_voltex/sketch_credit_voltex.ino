
int outputPin = 13;
int startDelay = 300;

void setup() {
  // put your setup code here, to run once:
  pinMode(outputPin, INPUT);

  
  for(int i = 0; i < startDelay; i++) {
    delay(1000);  
    if (i >=startDelay -1){insertCoins();}
  }

}

void loop() {
  // put your main code here, to run repeatedly:

}

void insertCoins() {
  for(int i = 0; i < 99; i++) {
    pinMode(outputPin, OUTPUT);
    digitalWrite(outputPin, LOW);
    delay(40);
    pinMode(outputPin, INPUT);
    delay(30);
  }
}