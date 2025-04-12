// Define pin connections
const int VRx = 20;  // X-axis
const int VRy = 21;  // Y-axis
const int SW  = 1;  // Button

void setup() {
  Serial.begin(115200);
  pinMode(SW, INPUT_PULLUP); // Button is active-low
}

void loop() {
  int xVal = analogRead(VRx);
  int yVal = analogRead(VRy);
  int btn  = digitalRead(SW);

  Serial.print("X: "); Serial.print(xVal);
  Serial.print(" | Y: "); Serial.print(yVal);
  Serial.print(" | Button: "); Serial.println(btn == LOW ? "1" : "0");

  delay(200);
}
