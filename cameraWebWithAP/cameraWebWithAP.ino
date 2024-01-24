#include "esp_controller_functions.h"
#include <WiFi.h>
#include "esp_camera.h"
#include <ArduinoJson.h>

#define CAMERA_MODEL_AI_THINKER  // Has PSRAM

#include "camera_pins.h"

const char* ssid = "EC";
const char* password = "Hunter1235";

IPAddress local_ip(192, 168, 1, 4);
IPAddress gateway(192, 168, 1, 1);
IPAddress subnet(255, 255, 255, 0);


void startCameraServer();
void setupLedFlash(int pin);

void setup() {
  
  ESP32PWM::allocateTimer(2);
  ESP32PWM::allocateTimer(3);
  
  Serial.begin(115200);
  Serial.setDebugOutput(true);
  Serial.println();


  camera_config_t config;
  config.ledc_channel = LEDC_CHANNEL_0;
  config.ledc_timer = LEDC_TIMER_0;
  config.pin_d0 = Y2_GPIO_NUM;
  config.pin_d1 = Y3_GPIO_NUM;
  config.pin_d2 = Y4_GPIO_NUM;
  config.pin_d3 = Y5_GPIO_NUM;
  config.pin_d4 = Y6_GPIO_NUM;
  config.pin_d5 = Y7_GPIO_NUM;
  config.pin_d6 = Y8_GPIO_NUM;
  config.pin_d7 = Y9_GPIO_NUM;
  config.pin_xclk = XCLK_GPIO_NUM;
  config.pin_pclk = PCLK_GPIO_NUM;
  config.pin_vsync = VSYNC_GPIO_NUM;
  config.pin_href = HREF_GPIO_NUM;
  config.pin_sccb_sda = SIOD_GPIO_NUM;
  config.pin_sccb_scl = SIOC_GPIO_NUM;
  config.pin_pwdn = PWDN_GPIO_NUM;
  config.pin_reset = RESET_GPIO_NUM;
  config.xclk_freq_hz = 20000000;
  config.frame_size = FRAMESIZE_SVGA;//XGA 
  config.pixel_format = PIXFORMAT_JPEG;  // for streaming
  config.grab_mode = CAMERA_GRAB_WHEN_EMPTY;
  config.fb_location = CAMERA_FB_IN_PSRAM;
  config.jpeg_quality = 12;
  config.fb_count = 1;
  if (config.pixel_format == PIXFORMAT_JPEG) {
    if (psramFound()) {
      config.jpeg_quality = 10;
      config.fb_count = 2;
      config.grab_mode = CAMERA_GRAB_LATEST;
    } else {
      config.frame_size = FRAMESIZE_SVGA;
      config.fb_location = CAMERA_FB_IN_DRAM;
    }
  } else {
    config.frame_size = FRAMESIZE_240X240;
#if CONFIG_IDF_TARGET_ESP32S3
    config.fb_count = 2;
#endif
  }
#if defined(CAMERA_MODEL_ESP_EYE)
  pinMode(13, INPUT_PULLUP);
  pinMode(14, INPUT_PULLUP);
#endif
  esp_err_t err = esp_camera_init(&config);
  if (err != ESP_OK) {
    Serial.printf("Camera init failed with error 0x%Ox", err);
    return;
  }
  sensor_t* s = esp_camera_sensor_get();
  if (s->id.PID == OV3660_PID) {
    s->set_vflip(s, 1);        // flip it back
    s->set_brightness(s, 1);   // up the brightness just a bit
    s->set_saturation(s, -2);  // lower the saturation
  }
  if (config.pixel_format == PIXFORMAT_JPEG) {
    s->set_framesize(s, FRAMESIZE_QVGA);
  }

#if defined(CAMERA_MODEL_M5STACK_WIDE) || defined(CAMERA_MODEL_M5STACK_ESP32CAM)
  s->set_vflip(s, 1);
  s->set_hmirror(s, 1);
#endif

#if defined(CAMERA_MODEL_ESP32S3_EYE)
  s->set_vflip(s, 1);
#endif
#if defined(LED_GPIO_NUM)
  setupLedFlash(LED_GPIO_NUM);
#endif


  WiFi.softAP(ssid, password);
  WiFi.softAPConfig(local_ip, gateway, subnet);
  startCameraServer();
  Serial.print(F("Camera Ready! Use 'http://"));
  Serial.print(local_ip);
  Serial.println(F("' to connect"));
  
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
  server.on("/OnPressLb", HTTP_GET, LBOnPressFunc);
  server.on("/OnPressRb", HTTP_GET, RBOnPressFunc);


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
  server.on("/OnReleaseLb", HTTP_GET, LBOnReleaseFunc);
  server.on("/OnReleaseRb", HTTP_GET, RBOnReleaseFunc);


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
  // server.on("/distance", HTTP_GET, distance);

  server.begin();
  // pinMode(Led, OUTPUT);
  pinMode(Motor1F, OUTPUT);
  pinMode(Motor1B, OUTPUT);
  pinMode(Motor2F, OUTPUT);
  pinMode(Motor2B, OUTPUT);
  pinMode(buzzer, OUTPUT);

  servoShoot.attach(ShootPin);
  servoUD.attach(ServoUDPin);
  servoLR.attach(ServoLRPin);

  servoUD.write(0);
  servoLR.write(0);
  servoShoot.write(180);
  
  
}

void loop() {
  server.handleClient();
}
