#ifndef ESP_CONTROLLER_FUNC_H_
#define ESP_CONTROLLER_FUNC_H_

#include <WebServer.h>
#include <Servo_ESP32.h>

WebServer server(80);

const int servoCount = 3;
static const int servosPins[servoCount] = {12, 14, 27};
Servo_ESP32 servos[servoCount];

#define Motor1F 13
#define Motor1B 19
#define Motor2F 23
#define Motor2B 32

#define buzzer 22

int ServoUDPos = 15;
int ServoLRPos = 90;

bool ServoUD_State = true;

void BuzzerOn()
{
    digitalWrite(buzzer, HIGH);
    Serial.println("Buzzer Turned On");
}

void BuzzerOff()
{
    digitalWrite(buzzer, LOW);
    Serial.println("Buzzer Turned Off");
}

void Shoot_Func()
{
    servos[0].write(110);
    Serial.print("shoot");
    Serial.println(" : bew bew");
    delay(100);
    servos[0].write(180);
    Serial.println("return");
    delay(100);
}

void ServoUD_U()
{
    if (ServoUDPos <= 90)
    {
        ServoUDPos += 1;
        Serial.println(ServoUDPos);
        servos[1].write(ServoUDPos);
        Serial.print("Servo up with angle : ");
        Serial.println(ServoUDPos);
    }
}

void ServoUD_D()
{
    if (ServoUDPos > 0)
    {
        ServoUDPos -= 1;
        Serial.println(ServoUDPos);
        servos[1].write(ServoUDPos);
        Serial.print("Servo Down with angle : ");
        Serial.println(ServoUDPos);
    }
}

void ServoLR_L()
{
    if (ServoLRPos > 0)
    {
        ServoLRPos -= 1;
        Serial.println(ServoLRPos);
        servos[2].write(ServoLRPos);
        Serial.print("Servo Left with angle : ");
        Serial.println(ServoLRPos);
    }
}

void ServoLR_R()
{
    if (ServoLRPos <= 180)
    {
        ServoLRPos += 1;
        Serial.println(ServoLRPos);
        servos[2].write(ServoLRPos);
        Serial.print("Servo Right with angle : ");
        Serial.println(ServoLRPos);
    }
}

void DcMotorsForward(void)
{
    digitalWrite(Motor1F, HIGH);
    digitalWrite(Motor2F, HIGH);
    digitalWrite(Motor1B, LOW);
    digitalWrite(Motor2B, LOW);
    Serial.println("motor forward");
}
void DcMotorsBackward(void)
{
    digitalWrite(Motor1F, LOW);
    digitalWrite(Motor2F, LOW);
    digitalWrite(Motor1B, HIGH);
    digitalWrite(Motor2B, HIGH);
    Serial.println("motor Backward");
}
void DcMotorsRight(void)
{
    digitalWrite(Motor1F, HIGH);
    digitalWrite(Motor2F, LOW);
    digitalWrite(Motor1B, LOW);
    digitalWrite(Motor2B, HIGH);
    Serial.println("motor Right");
}
void DcMotorsLeft(void)
{
    digitalWrite(Motor1F, LOW);
    digitalWrite(Motor2F, HIGH);
    digitalWrite(Motor1B, HIGH);
    digitalWrite(Motor2B, LOW);
    Serial.println("motor Left");
}
void DcMotorsStop(void)
{
    digitalWrite(Motor1F, LOW);
    digitalWrite(Motor2F, LOW);
    digitalWrite(Motor1B, LOW);
    digitalWrite(Motor2B, LOW);
    // Serial.println("motor stop");
}

void R1Stop()
{
    DcMotorsStop();
    server.send(200, "text/plain", "R1Stop");
}
void R2Stop()
{
    server.send(200, "text/plain", "R2Stop");
}
void UpArrowButtonOnPressFunc()
{
    ServoUD_U();
    server.send(200, "text/plain", "OnPressUpArrow");
}
void DownArrowButtonOnPressFunc()
{
    ServoUD_D();
    server.send(201, "text/plain", "OnPressDownArrow");
}
void RightArrowButtonOnPressFunc()
{
    DcMotorsRight();
    server.send(202, "text/plain", "OnPressRightArrow");
}
void LeftArrowButtonOnPressFunc()
{
    DcMotorsLeft();
    server.send(203, "text/plain", "OnPressLeftArrow");
}
void TriangleOnPressFunc()
{
    BuzzerOn();
    server.send(204, "text/plain", "OnPressTr");
}
void CircleOnPressFunc()
{
    server.send(205, "text/plain", "OnPressCircle");
}
void XOnPressFunc()
{
    DcMotorsForward();
    server.send(206, "text/plain", "OnPressX");
}
void SquareOnPressFunc()
{
    DcMotorsBackward();
    server.send(207, "text/plain", "OnPressSquare");
}
void LTOnPressFunc()
{
    server.send(208, "text/plain", "OnPressLt");
}
void RTOnPressFunc()
{
    Shoot_Func();
    server.send(209, "text/plain", "OnPressRt");
}
void LBOnPressFunc()
{
    ServoLR_L();
    server.send(210, "text/plain", "OnPressLb");
}
void RBOnPressFunc()
{
    ServoLR_R();
    server.send(211, "text/plain", "OnPressRb");
}

void UpArrowButtonOnReleaseFunc()
{
    server.send(217, "text/plain", "OnReleaseUpArrow");
}
void DownArrowButtonOnReleaseFunc()
{
    server.send(218, "text/plain", "OnReleaseDownArrow");
}
void RightArrowButtonOnReleaseFunc()
{
    DcMotorsStop();
    server.send(219, "text/plain", "OnReleaseRightArrow");
}
void LeftArrowButtonOnReleaseFunc()
{
    DcMotorsStop();
    server.send(220, "text/plain", "OnReleaseLeftArrow");
}
void TriangleOnReleaseFunc()
{
    BuzzerOff();
    server.send(221, "text/plain", "OnReleaseTr");
}
void CircleOnReleaseFunc()
{
    server.send(222, "text/plain", "OnReleaseCircle");
}
void XOnReleaseFunc()
{
    DcMotorsStop();
    server.send(223, "text/plain", "OnReleaseX");
}
void SquareOnReleaseFunc()
{
    DcMotorsStop();
    server.send(224, "text/plain", "OnReleaseSquare");
}
void LTOnReleaseFunc()
{
    server.send(225, "text/plain", "OnReleaseLt");
}
void RTOnReleaseFunc()
{
    server.send(226, "text/plain", "OnReleaseRt");
}
void LBOnReleaseFunc()
{
    server.send(227, "text/plain", "OnReleaseLb");
}
void RBOnReleaseFunc()
{
    server.send(228, "text/plain", "OnReleaseRb");
}

void R1UpFunc()
{
    DcMotorsForward();
    server.send(234, "text/plain", "R1Up");
}
void R1DownFunc()
{
    DcMotorsBackward();
    server.send(235, "text/plain", "R1Down");
}
void R1RightFunc()
{
    server.send(236, "text/plain", "R1Right");
    DcMotorsRight();
}
void R1LeftFunc()
{
    server.send(237, "text/plain", "R1Left");
    DcMotorsLeft();
}

void R2UpFunc()
{
    ServoUD_U();
    server.send(238, "text/plain", "R2Up");
}
void R2DownFunc()
{
    ServoUD_D();
    server.send(239, "text/plain", "R2Down");
}
void R2RightFunc()
{
    ServoLR_R();
    server.send(240, "text/plain", "R2Right");
}
void R2LeftFunc()
{
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