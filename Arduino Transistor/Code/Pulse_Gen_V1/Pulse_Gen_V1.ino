int PWM_Pin = 3; /* give PWM_Pin name to D3 pin */
// Perform initialization inside setup()
void setup()
{
pinMode(PWM_Pin,OUTPUT);  /*declare D3 pin as an output pin */ 
}
// loop() executes continously 
void loop()
{
analogWrite(PWM_Pin,127);  /* Produce 50% duty cycle PWM on D3 */
analogWrite(LED_BUILTIN,127);
}