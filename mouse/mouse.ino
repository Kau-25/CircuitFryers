#include <Adafruit_LSM6DSOX.h>

Adafruit_LSM6DSOX sox;
void setup(void) {
  Serial.begin(115200);
  if (!sox.begin_I2C()){
    Serial.println("Failed to initialize LSM6DSOX in I2C mode!");
    while (1);
  }
  Serial.println("I2C Mode initialized!");

}

void loop(){
  sensors_event_t accel, gyro, temp;
  sox.getEvent(&accel, &gyro, &temp);
  // Print out the readings
  Serial.print("Accel X: "); Serial.print(accel.acceleration.x); Serial.print(" m/s^2\t");
  Serial.print("Y: "); Serial.print(accel.acceleration.y); Serial.print(" m/s^2\t");
  Serial.print("Z: "); Serial.print(accel.acceleration.z); Serial.println(" m/s^2");

  Serial.print("Gyro X: "); Serial.print(gyro.gyro.x); Serial.print(" rad/s\t");
  Serial.print("Y: "); Serial.print(gyro.gyro.y); Serial.print(" rad/s\t");
  Serial.print("Z: "); Serial.print(gyro.gyro.z); Serial.println(" rad/s");

  Serial.println();
  delay(500);  // Delay between readings
}

