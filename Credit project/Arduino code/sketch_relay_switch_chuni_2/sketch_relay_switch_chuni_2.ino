// Sound voltex
int outputPin = 9 ;
int delayPulse = 500;

void setup() {
  // put your setup code here, to run once:
  pinMode(outputPin, OUTPUT);
}

void loop() {
  // put your main code here, to run repeatedly:
  digitalWrite(outputPin, LOW);
  delay(delayPulse);
  digitalWrite(outputPin, HIGH);
  delay(delayPulse);
}