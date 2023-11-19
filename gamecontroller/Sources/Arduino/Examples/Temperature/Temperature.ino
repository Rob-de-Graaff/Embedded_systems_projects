int time = 0;
void setup() {
    Serial.begin(9600);
}

void loop() {
    Serial.print("the value is ");
    Serial.print(time++);
    Serial.println(" seconds");
}