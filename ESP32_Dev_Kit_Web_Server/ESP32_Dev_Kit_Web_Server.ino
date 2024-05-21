#include <PS4Controller.h>
#include "esp_controller_functions.h"

const char *ssid = "EC";
const char *password = "Hunter1235";

void setServos(int degrees)
{
    for (int i = 0; i < servoCount; ++i)
    {
        servos[i].write((degrees + (35 * i)) % 180);
    }
}

void setup()
{
    Serial.begin(115200);
    Serial.println("Ready.");

    for (int i = 0; i < servoCount; ++i)
    {
        if (!servos[i].attach(servosPins[i]))
        {
            Serial.print("Servo ");
            Serial.print(i);
            Serial.println("attach error");
        }
    }

    servos[1].write(ServoUDPos);
    servos[2].write(ServoLRPos);
    servos[0].write(180);

    pinMode(Motor1F, OUTPUT);
    pinMode(Motor1B, OUTPUT);
    pinMode(Motor2F, OUTPUT);
    pinMode(Motor2B, OUTPUT);
    pinMode(buzzer, OUTPUT);

    WiFi.mode(WIFI_STA);
    WiFi.begin(ssid, password);
    Serial.println("");

    // Wait for connection
    while (WiFi.status() != WL_CONNECTED)
    {
        delay(500);
        Serial.print(".");
    }

    Serial.println("");
    Serial.print("Connected to ");
    Serial.println(ssid);
    Serial.print("IP address: ");
    Serial.println(WiFi.localIP());
    server.on("/OnPressUpArrow", HTTP_GET, UpArrowButtonOnPressFunc);
    server.on("/OnPressRightArrow", HTTP_GET, RightArrowButtonOnPressFunc);
    server.on("/OnPressLeftArrow", HTTP_GET, LeftArrowButtonOnPressFunc);
    server.on("/OnPressDownArrow", HTTP_GET, DownArrowButtonOnPressFunc);
    server.on("/OnPressTr", HTTP_GET, TriangleOnPressFunc);
    server.on("/OnPressCircle", HTTP_GET, CircleOnPressFunc);
    server.on("/OnPressSquare", HTTP_GET, SquareOnPressFunc);
    server.on("/OnPressX", HTTP_GET, XOnPressFunc);
    server.on("/OnPressLt", HTTP_GET, LTOnPressFunc);
    server.on("/OnPressRt", HTTP_GET, RTOnPressFunc);
    server.on("/OnPressRb", HTTP_GET, LBOnPressFunc);
    server.on("/OnPressLb", HTTP_GET, RBOnPressFunc);

    server.on("/OnReleaseUpArrow", HTTP_GET, UpArrowButtonOnReleaseFunc);
    server.on("/OnReleaseRightArrow", HTTP_GET, RightArrowButtonOnReleaseFunc);
    server.on("/OnReleaseLeftArrow", HTTP_GET, LeftArrowButtonOnReleaseFunc);
    server.on("/OnReleaseDownArrow", HTTP_GET, DownArrowButtonOnReleaseFunc);
    server.on("/OnReleaseTr", HTTP_GET, TriangleOnReleaseFunc);
    server.on("/OnReleaseCircle", HTTP_GET, CircleOnReleaseFunc);
    server.on("/OnReleaseSquare", HTTP_GET, SquareOnReleaseFunc);
    server.on("/OnReleaseX", HTTP_GET, XOnReleaseFunc);
    server.on("/OnReleaseLt", HTTP_GET, LTOnReleaseFunc);
    server.on("/OnReleaseRt", HTTP_GET, RTOnReleaseFunc);
    server.on("/OnReleaseRb", HTTP_GET, LBOnReleaseFunc);
    server.on("/OnReleaseLb", HTTP_GET, RBOnReleaseFunc);

    server.on("/R1Up", HTTP_GET, R1UpFunc);
    server.on("/R1Down", HTTP_GET, R1DownFunc);
    server.on("/R1Right", HTTP_GET, R1RightFunc);
    server.on("/R1Left", HTTP_GET, R1LeftFunc);
    server.on("/R2Up", HTTP_GET, R2UpFunc);
    server.on("/R2Down", HTTP_GET, R2DownFunc);
    server.on("/R2Right", HTTP_GET, R2RightFunc);
    server.on("/R2Left", HTTP_GET, R2LeftFunc);
    server.on("/R1Stop", HTTP_GET, R1Stop);
    server.on("/R2Stop", HTTP_GET, R2Stop);

    server.begin();
    PS4.begin("58:a0:23:ac:82:93");
}

void loop()
{
    server.handleClient();
    if (PS4.isConnected())
    {
        if (PS4.Down())
        {
            ServoUD_D();
        }
        if (PS4.Up())
        {
            ServoUD_U();
        }
        if (PS4.Right())
        {
            ServoLR_R();
        }
        if (PS4.Left())
        {
            ServoLR_L();
        }

        if (PS4.Triangle())
        {
            BuzzerOn();
        }
        else
        {
            BuzzerOff();
        }

        if (PS4.R1())
        {
            Shoot_Func();
        }

        if (PS4.L2())
        {
            ServoLR_R();
        }
        else
        {
            Serial.println("L2 Released");
        }

        if (PS4.R2())
        {
            ServoLR_L();
        }
        else
        {
            Serial.println("L2 Released");
        }

        if (PS4.RStickX() > 120)
        {
            ServoLR_L();
        }
        else if (PS4.RStickX() < -120)
        {
            ServoLR_R();
        }

        else if (PS4.RStickY() > 120)
        {
            ServoUD_U();
        }
        else if (PS4.RStickY() < -120)
        {
            ServoUD_D();
        }
        else
        {
            Serial.println("Centre");
        }

        // Left Stick
        if (PS4.Square())
        {
            DcMotorsBackward();
        }
        else if (PS4.Cross())
        {
            DcMotorsForward();
        }
        else if (PS4.LStickX() > 120)
        {
            DcMotorsRight();
        }
        else if (PS4.LStickX() < -120)
        {
            DcMotorsLeft();
        }
        else if (PS4.LStickY() > 120)
        {
            DcMotorsForward();
        }
        else if (PS4.LStickY() < -120)
        {
            DcMotorsBackward();
        }
        else
        {
            if (!PS4.Cross() && !PS4.Square())
            {
                DcMotorsStop();
            }
        }
    }
    delay(20);
}
