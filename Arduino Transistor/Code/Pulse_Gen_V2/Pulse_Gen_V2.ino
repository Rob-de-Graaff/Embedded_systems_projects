int PWM_Pin = 3; /* give PWM_Pin name to D3 pin */

void setup() {
  /* set PWM_Pin as output */
  pinMode(PWM_Pin, OUTPUT);
}

// the loop function runs over and over again forever
void loop() {
  digitalWrite(PWM_Pin, HIGH);  // turn the Pin on (HIGH is the voltage level)
  delay(500);                      // wait for x milisec
  digitalWrite(PWM_Pin, LOW);   // turn the Pin off by making the voltage LOW
  delay(500);                      // wait for x milisec
}