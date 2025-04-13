#include "FastIMU.h"
#include <Wire.h>

#define IMU_ADDRESS 0x68    //Change to the address of the IMU
#define PERFORM_CALIBRATION //Comment to disable startup calibration
MPU6500 IMU;               //Change to the name of any supported IMU! 
const int VRx = 6;  // X-axis
const int VRy = 16;  // Y-axis
const int SW  = 5;  // Button
calData calib = { 0 };  //Calibration data
AccelData accelData;    //Sensor data
GyroData gyroData;
MagData magData;
char data[30];

void setup(){
  Wire.begin();
  Wire.setClock(400000); //400khz clock
  Serial.begin(115200);
  while (!Serial) {
    ;
  }
  pinMode(SW, INPUT_PULLUP); // Button is active-low

  int err = IMU.init(calib, IMU_ADDRESS);
  if (err != 0) {
    Serial.print("Error initializing IMU: ");
    Serial.println(err);
    while (true) {
      ;
    }
  }
  
#ifdef PERFORM_CALIBRATION
  Serial.println("FastIMU calibration & data example");
  delay(5000);
  Serial.println("Keep IMU level.");
  delay(5000);
  IMU.calibrateAccelGyro(&calib);
  Serial.println("Calibration done!");
  Serial.println("Accel biases X/Y/Z: ");
  Serial.print(calib.accelBias[0]);
  Serial.print(", ");
  Serial.print(calib.accelBias[1]);
  Serial.print(", ");
  Serial.println(calib.accelBias[2]);
  Serial.println("Gyro biases X/Y/Z: ");
  Serial.print(calib.gyroBias[0]);
  Serial.print(", ");
  Serial.print(calib.gyroBias[1]);
  Serial.print(", ");
  Serial.println(calib.gyroBias[2]);
  if (IMU.hasMagnetometer()) {
    Serial.println("Mag biases X/Y/Z: ");
    Serial.print(calib.magBias[0]);
    Serial.print(", ");
    Serial.print(calib.magBias[1]);
    Serial.print(", ");
    Serial.println(calib.magBias[2]);
    Serial.println("Mag Scale X/Y/Z: ");
    Serial.print(calib.magScale[0]);
    Serial.print(", ");
    Serial.print(calib.magScale[1]);
    Serial.print(", ");
    Serial.println(calib.magScale[2]);
  }
  delay(5000);
  IMU.init(calib, IMU_ADDRESS);
#endif

  //err = IMU.setGyroRange(500);      //USE THESE TO SET THE RANGE, IF AN INVALID RANGE IS SET IT WILL RETURN -1
  //err = IMU.setAccelRange(2);       //THESE TWO SET THE GYRO RANGE TO ±500 DPS AND THE ACCELEROMETER RANGE TO ±2g
  
  if (err != 0) {
    Serial.print("Error Setting range: ");
    Serial.println(err);
    while (true) {
      ;
    }
  }
}

void loop() {
  IMU.update();
  //gets proper 
  IMU.getAccel(&accelData);
  /*
  Serial.print(accelData.accelX);
  Serial.print("\t");
  Serial.print(accelData.accelY);
  Serial.print("\t");
  Serial.print(accelData.accelZ);
  Serial.print("\t");
  */

  //Gets proper gyro data
  IMU.getGyro(&gyroData);
  /*
  Serial.print(gyroData.gyroX);
  Serial.print("\t");
  Serial.print(gyroData.gyroY);
  Serial.print("\t");
  Serial.print(gyroData.gyroZ);
  Serial.print("\t");
  */
  //Joystick data
  int xVal = analogRead(VRx);
  int yVal = analogRead(VRy);
  int btn = !digitalRead(SW);
  int sens=300;

  sprintf(data, "%d:%d:%d:%d:%d:%d\n", (int)(round(accelData.accelX*sens)), (int)round(accelData.accelY*sens), (int)round(accelData.accelZ*100), xVal, yVal, btn);
  Serial.print(data);
  delay(80);
}
