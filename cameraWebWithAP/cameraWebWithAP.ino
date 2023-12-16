#include <WiFi.h>
#include <WebServer.h>
#include <ESP32Servo.h>
#include "esp_camera.h"

#define CAMERA_MODEL_AI_THINKER  // Has PSRAM
#define Led 4
#define Ser 2
int pos = 0;

#include "camera_pins.h"

const char* ssid = "EC";
const char* password = "Hunter1235";

IPAddress local_ip(192, 168, 1, 4);
IPAddress gateway(192, 168, 1, 1);
IPAddress subnet(255, 255, 255, 0);

Servo myservo;

void startCameraServer();
void setupLedFlash(int pin);

WebServer server(80);

void UpArrowButtonFunc() {
  Serial.println("UpArrow\n");
  server.send(200, "text/plain", "UpArrow");
}
void DownArrowButtonFunc() {
  Serial.println("DownArrow\n");
  server.send(200, "text/plain", "DownArrow");
}
void RightArrowButtonFunc() {
  Serial.println("RightArrow\n");
  server.send(240, "text/plain", "RightArrow");
}
void LeftArrowButtonFunc() {
  Serial.println("LeftArrow\n");
  server.send(240, "text/plain", "LeftArrow");
}
void TriangleFunc() {
  Serial.println("Triangle\n");
  server.send(240, "text/plain", "Triangle");
}
void CircleFunc() {
  Serial.println("Circle\n");
  server.send(240, "text/plain", "Circle");
}
void XFunc() {
  Serial.println("X\n");
  server.send(240, "text/plain", "X");
}
void SquareFunc() {
  Serial.println("Square\n");
  server.send(240, "text/plain", "Square");
}
void LTFunc() {
  Serial.println("LT\n");
  server.send(240, "text/plain", "LT");
}
void RTFunc() {
  Serial.println("RT\n");
  server.send(240, "text/plain", "RT");
}
void LBFunc() {
  Serial.println("LB\n");
  server.send(240, "text/plain", "LB");
}
void RBFunc() {
  Serial.println("RB\n");
  server.send(240, "text/plain", "RB");
}
void R1UpFunc() {
  Serial.println("R1Up\n");
  server.send(240, "text/plain", "R1Up");
}
void R1DownFunc() {
  Serial.println("R1Down\n");
  server.send(240, "text/plain", "R1Down");
}
void R1RightFunc() {
  Serial.println("R1Right\n");
  server.send(240, "text/plain", "R1Right");
}
void R1LeftFunc() {
  Serial.println("R1Left\n");
  server.send(240, "text/plain", "R1Left");
}
void R2UpFunc() {
  Serial.println("R2Up\n");
  server.send(240, "text/plain", "R2Up");
}
void R2DownFunc() {
  Serial.println("R2Down\n");
  server.send(240, "text/plain", "R2Down");
}
void R2RightFunc() {
  Serial.println("R2Right\n");
  server.send(240, "text/plain", "R2Right");
}
void R2LeftFunc() {
  Serial.println("R2Left\n");
  server.send(240, "text/plain", "R2Left");
}
void ShareFunc() {
  Serial.println("Share\n");
  server.send(240, "text/plain", "Share");
}
void PsFunc() {
  Serial.println("Ps\n");
  server.send(240, "text/plain", "Ps");
}
void OptionsFunc() {
  Serial.println("Options\n");
  server.send(240, "text/plain", "Options");
}
void R1ClickFunc() {
  Serial.println("R1Click\n");
  server.send(240, "text/plain", "R1Click");
}
void R2ClickFunc() {
  Serial.println("R2Click\n");
  server.send(240, "text/plain", "R2Click");
}


void setup() {
  Serial.begin(115200);
  Serial.setDebugOutput(true);
  Serial.println();
  myservo.attach(Ser);
  pinMode(Led, OUTPUT);
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
  config.frame_size = FRAMESIZE_UXGA;
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
    Serial.printf("Camera init failed with error 0x%x", err);
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
  pinMode(Led, OUTPUT);
  server.on("/UpArrow", HTTP_GET, UpArrowButtonFunc);
  server.on("/RightArrow", HTTP_GET, RightArrowButtonFunc);
  server.on("/LeftArrow", HTTP_GET, LeftArrowButtonFunc);
  server.on("/DownArrow", HTTP_GET, DownArrowButtonFunc);
  server.on("/Tr", HTTP_GET, TriangleFunc);
  server.on("/Circle", HTTP_GET, CircleFunc);
  server.on("/Square", HTTP_GET, SquareFunc);
  server.on("/X", HTTP_GET, XFunc);
  server.on("/Lt", HTTP_GET, LTFunc);
  server.on("/Rt", HTTP_GET, RTFunc);
  server.on("/Lb", HTTP_GET, LBFunc);
  server.on("/Rb", HTTP_GET, RBFunc);
  server.on("/R1Up", HTTP_GET, R1UpFunc);
  server.on("/R1Down", HTTP_GET, R1DownFunc);
  server.on("/R1Right", HTTP_GET, R1RightFunc);
  server.on("/R1Left", HTTP_GET, R1LeftFunc);
  server.on("/R2Up", HTTP_GET, R2UpFunc);
  server.on("/R2Down", HTTP_GET, R2DownFunc);
  server.on("/R2Right", HTTP_GET, R2RightFunc);
  server.on("/R2Left", HTTP_GET, R1LeftFunc);
  server.on("/Share", HTTP_GET, ShareFunc);
  server.on("/Ps", HTTP_GET, PsFunc);
  server.on("/Options", HTTP_GET, OptionsFunc);
  server.on("/R1Click", HTTP_GET, R1ClickFunc);
  server.on("/R2Click", HTTP_GET, R2ClickFunc);
  server.begin();
}

void loop() {
  server.handleClient();
  

}
