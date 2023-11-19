const int UpButton = 0;
const int DownButton = 5;
const int LeftButton = 10;
const int RightButton = 15;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  pinMode(UpButton, INPUT_PULLDOWN);
  pinMode(DownButton, INPUT_PULLDOWN);
  pinMode(LeftButton, INPUT_PULLDOWN);
  pinMode(RightButton, INPUT_PULLDOWN);
}

void loop() {
  // put your main code here, to run repeatedly:
  if(digitalRead(UpButton) == HIGH)
  {
    Serial.println("up");
  }
  if(digitalRead(DownButton) == HIGH)
  {
    Serial.println("down");
  }
  if(digitalRead(LeftButton) == HIGH)
  {
    Serial.println("left");
  }
  if(digitalRead(RightButton) == HIGH)
  {
    Serial.println("right");
  }
  delay(50);
}
