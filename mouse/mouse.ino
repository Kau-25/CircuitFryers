#include <Wire.h>
#include <MPU6050.h>

MPU6050 mpu;

void setup() {
  Serial.begin(115200);
  Wire.begin();

  Serial.println("Initializing MPU...");
  mpu.initialize();

  // Check if connected
  if (!mpu.testConnection()) {
    Serial.println("MPU connection failed!");
    while (1);
  }

  Serial.println("MPU successfully connected!");
}

void loop() {
  int16_t ax, ay, az;
  int16_t gx, gy, gz;

  // Get raw acceleration and gyro values
  mpu.getMotion6(&ax, &ay, &az, &gx, &gy, &gz);

  // Convert to proper units if needed (raw values now)
  Serial.print("Accel (raw) X: "); Serial.print(ax);
  Serial.print(" Y: "); Serial.print(ay);
  Serial.print(" Z: "); Serial.println(az);

  Serial.print("Gyro (raw) X: "); Serial.print(gx);
  Serial.print(" Y: "); Serial.print(gy);
  Serial.print(" Z: "); Serial.println(gz);

  Serial.println();
  delay(500);
}
