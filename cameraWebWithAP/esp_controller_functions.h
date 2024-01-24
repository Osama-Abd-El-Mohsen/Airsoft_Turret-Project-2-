#ifndef ESP_CONTROLLER_FUNC_H_
#define ESP_CONTROLLER_FUNC_H_

#include <WebServer.h>
#include <ESP32Servo.h>

WebServer server(80);

#define Motor1F 4
#define Motor1B 2
#define Motor2F 3
#define Motor2B 1
#define ShootPin 15
#define ServoUDPin 13
#define ServoLRPin 12
// #define Led 4
#define buzzer 14

int ServoUDPos = 0;
int ServoLRPos = 0;

bool ServoUD_State = true ;

Servo servoShoot;
Servo servoUD;
Servo servoLR;


// void LedOnOff() {
//   digitalWrite(Led, !digitalRead(Led));
// }

void Buzzer()
{
  digitalWrite(buzzer,HIGH);
  delay(500);
  digitalWrite(buzzer,LOW);
  delay(500);
}

void Shoot_Func() {
  servoShoot.write(110);
  Serial.println("shoot");
  delay(1000);                       
  servoShoot.write(180);
  Serial.println("return");
  delay(100);                       
  
}

void ServoUD_Stop()
{
  ServoUD_State = false;
}

void ServoUD_U() {
    if (ServoUDPos <= 90 ) {
      ServoUDPos+=1;
      Serial.println(ServoUDPos);
      servoUD.write(ServoUDPos);
    }
}

void ServoUD_D() {
    if (ServoUDPos > 0 ) {
      ServoUDPos-=1;
      Serial.println(ServoUDPos);
      servoUD.write(ServoUDPos);
    }
}

void ServoLR_L() {
  if (ServoLRPos > 0 ) {
    ServoLRPos-=5;
    Serial.println(ServoLRPos);
    servoLR.write(ServoLRPos);
  }
}

void ServoLR_R() {
    if (ServoLRPos <= 160 ) {
    ServoLRPos+=5;
    Serial.println(ServoLRPos);
    servoLR.write(ServoLRPos);
  }
}

void DcMotorsForward(void) {
  digitalWrite(Motor1F, HIGH);
  digitalWrite(Motor2F, HIGH);
  digitalWrite(Motor1B, LOW);
  digitalWrite(Motor2B, LOW);
}
void DcMotorsBackward(void) {
  digitalWrite(Motor1F, LOW);
  digitalWrite(Motor2F, LOW);
  digitalWrite(Motor1B, HIGH);
  digitalWrite(Motor2B, HIGH);
}
void DcMotorsRight(void) {
  digitalWrite(Motor1F, HIGH);
  digitalWrite(Motor2F, LOW);
  digitalWrite(Motor1B, LOW);
  digitalWrite(Motor2B, HIGH);
}
void DcMotorsLeft(void) {
  digitalWrite(Motor1F, LOW);
  digitalWrite(Motor2F, HIGH);
  digitalWrite(Motor1B, HIGH);
  digitalWrite(Motor2B, LOW);
}
void DcMotorsStop(void) {
  digitalWrite(Motor1F, LOW);
  digitalWrite(Motor2F, LOW);
  digitalWrite(Motor1B, LOW);
  digitalWrite(Motor2B, LOW);

}


void R1Stop() {
  Serial.println("R1Stop\n");
  DcMotorsStop();
  server.send(200, "text/plain", "R1Stop");
}
void R2Stop() {
  Serial.println("R2Stop\n");
  ServoUD_Stop();
  server.send(200, "text/plain", "R2Stop");
}
void UpArrowButtonOnPressFunc() {
  Serial.println("OnPressUpArrow\n");
  ServoUD_U();
  server.send(200, "text/plain", "OnPressUpArrow");
}
void DownArrowButtonOnPressFunc() {
  Serial.println("OnPressDownArrow\n");
  ServoUD_D();
  server.send(201, "text/plain", "OnPressDownArrow");
}
void RightArrowButtonOnPressFunc() {
  Serial.println("OnPressRightArrow\n");
  DcMotorsRight();
  server.send(202, "text/plain", "OnPressRightArrow");
}
void LeftArrowButtonOnPressFunc() {
  Serial.println("OnPressLeftArrow\n");
  DcMotorsLeft();
  server.send(203, "text/plain", "OnPressLeftArrow");
}
void TriangleOnPressFunc() {
  Serial.println("OnPressTr\n");
  Buzzer();
  server.send(204, "text/plain", "OnPressTr");
}
void CircleOnPressFunc() {
  Serial.println("OnPressCircle\n");
  server.send(205, "text/plain", "OnPressCircle");
}
void XOnPressFunc() {
  Serial.println("OnPressX\n");
  DcMotorsForward();
  server.send(206, "text/plain", "OnPressX");
}
void SquareOnPressFunc() {
  Serial.println("OnPressSquare\n");
  DcMotorsBackward();
  server.send(207, "text/plain", "OnPressSquare");
}
void LTOnPressFunc() {
  Serial.println("OnPressLt\n");
  server.send(208, "text/plain", "OnPressLt");
}
void RTOnPressFunc() {
  Serial.println("OnPressRt\n");
  Shoot_Func();
  server.send(209, "text/plain", "OnPressRt");
}
void LBOnPressFunc() {
  Serial.println("OnPressLb\n");
  ServoLR_L();
  server.send(210, "text/plain", "OnPressLb");
}
void RBOnPressFunc() {
  Serial.println("OnPressRb\n");
  ServoLR_R();
  server.send(211, "text/plain", "OnPressRb");
}


void UpArrowButtonOnReleaseFunc() {
  Serial.println("OnReleaseUpArrow\n");
  ServoUD_Stop();
  server.send(217, "text/plain", "OnReleaseUpArrow");
}
void DownArrowButtonOnReleaseFunc() {
  Serial.println("OnReleaseDownArrow\n");
  ServoUD_Stop();
  server.send(218, "text/plain", "OnReleaseDownArrow");
}
void RightArrowButtonOnReleaseFunc() {
  Serial.println("OnReleaseRightArrow\n");
  DcMotorsStop();
  server.send(219, "text/plain", "OnReleaseRightArrow");
}
void LeftArrowButtonOnReleaseFunc() {
  Serial.println("OnReleaseLeftArrow\n");
  DcMotorsStop();
  server.send(220, "text/plain", "OnReleaseLeftArrow");
}
void TriangleOnReleaseFunc() {
  Serial.println("OnReleaseTr\n");
  server.send(221, "text/plain", "OnReleaseTr");
}
void CircleOnReleaseFunc() {
  Serial.println("OnReleaseCircle\n");
  server.send(222, "text/plain", "OnReleaseCircle");
}
void XOnReleaseFunc() {
  Serial.println("OnReleaseX\n");
  DcMotorsStop();
  server.send(223, "text/plain", "OnReleaseX");
}
void SquareOnReleaseFunc() {
  Serial.println("OnReleaseSquare\n");
  DcMotorsStop();
  server.send(224, "text/plain", "OnReleaseSquare");
}
void LTOnReleaseFunc() {
  Serial.println("OnReleaseLt\n");
  server.send(225, "text/plain", "OnReleaseLt");
}
void RTOnReleaseFunc() {
  Serial.println("OnReleaseRt\n");
  server.send(226, "text/plain", "OnReleaseRt");
}
void LBOnReleaseFunc() {
  Serial.println("OnReleaseLb\n");
  server.send(227, "text/plain", "OnReleaseLb");
}
void RBOnReleaseFunc() {
  Serial.println("OnReleaseRb\n");
  server.send(228, "text/plain", "OnReleaseRb");
}



void R1UpFunc() {
  Serial.println("R1Up\n");
  DcMotorsForward();
  server.send(234, "text/plain", "R1Up");
}
void R1DownFunc() {
  Serial.println("R1Down\n");
  DcMotorsBackward();
  server.send(235, "text/plain", "R1Down");
}
void R1RightFunc() {
  Serial.println("R1Right\n");
  server.send(236, "text/plain", "R1Right");
  DcMotorsRight();
}
void R1LeftFunc() {
  Serial.println("R1Left\n");
  server.send(237, "text/plain", "R1Left");
  DcMotorsLeft();
}

void R2UpFunc() {
  Serial.println("R2Up\n");
  ServoUD_U();
  server.send(238, "text/plain", "R2Up");
}
void R2DownFunc() {
  Serial.println("R2Down\n");
  ServoUD_D();
  server.send(239, "text/plain", "R2Down");
}
void R2RightFunc() {
  ServoLR_R();
  Serial.println("R2Right\n");
  server.send(240, "text/plain", "R2Right");
}
void R2LeftFunc() {
  Serial.println("R2Left\n");
  ServoLR_L();
  server.send(241, "text/plain", "R2Left");
}

// void distance() {
//   long  distance;
//   distance = 25;
//   StaticJsonDocument<200> doc;
//   doc["distance"] = distance;
//   String output;
//   serializeJson(doc, output);
//   server.send(242, "application/json", output);

// }

#endif