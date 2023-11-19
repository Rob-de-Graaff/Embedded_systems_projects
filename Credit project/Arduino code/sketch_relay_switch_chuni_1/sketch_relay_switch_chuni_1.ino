// Sound voltex
int outputPin = 9 ;
int delayPulse = 500;

void setup() {
  // put your setup code here, to run once:
  pinMode(outputPin, INPUT);
}

void loop() {
  // put your main code here, to run repeatedly:
  pinMode(outputPin, OUTPUT);
  digitalWrite(outputPin, LOW);
  delay(delayPulse);
  pinMode(outputPin, INPUT);
  delay(delayPulse);
}