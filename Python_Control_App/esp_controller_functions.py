import urllib.request
import customtkinter as ctk
import json
import requests
import numpy as np
import cv2 as cv
# buttons
X = 0
Circle = 1
Square = 2
Triangle = 3

Share = 4
Ps = 5
Options = 6

R1Click = 7
R2Click = 8

LT = 9
RT = 10

UpArrow = 11
DownArrow = 12
LeftArrow = 13
RightArrow = 14
TouchPad = 15

# axis
R1Right_Left = 0 # Right 1 Left -1
R1Up_Down = 1 # Up -1 Down 1

R2Right_Left = 2
R2Up_Down = 3

LB = 4
RB = 5

def CapCam():
    CamUrl = "http://192.168.1.4/capture" 
    while True:
        try :
            resp = urllib.request.urlopen(CamUrl)
            img_array = np.array(bytearray(resp.read()), dtype=np.uint8)
        except :
            try :
                resp = urllib.request.urlopen(CamUrl)
                img_array = np.array(bytearray(resp.read()), dtype=np.uint8)
            except :
                print("error")
        cap = cv.imdecode(img_array, -1)
        
        frame = cv.resize(cap,(560,400))
        cv.imshow('frame', frame)
        
        if cv.waitKey(1) == 27:
            break

    cv.destroyAllWindows()



def SendRequest(Request):
    Url = "http://192.168.1.4"
    try:
        urllib.request.urlopen(Url+Request)
    except Exception as e:
        try:
            pass
            urllib.request.urlopen(Url+Request)
        except Exception as e:
            print("Request failed:", e)

def GetRequest(Request):
    Url = "http://192.168.1.4"
    try:
        with urllib.request.urlopen(Url+Request) as response:
            data = json.loads(response.read())
            data = data[Request[1:]]
            return data
            
    except urllib.error.URLError as e:
        try : 
            with urllib.request.urlopen(Url+Request) as response:
                data = json.loads(response.read())
                data = data[Request[1:]]
                return data
        except Exception as e:
            print(f"Request failed: {e}")



def change_apperance_mode(new_appearance_mode: str):
    ctk.AppearanceModeTracker.set_appearance_mode(new_appearance_mode)

# Arrows OnPressFunctions
def UpArrowButtonOnPressFunc(event =1):
    SendRequest("/OnPressUpArrow")
def RightArrowButtonOnPressFunc(event =1):
    SendRequest("/OnPressRightArrow")
def LeftArrowButtonOnPressFunc(event =1):
    SendRequest("/OnPressLeftArrow")
def DownArrowButtonOnPressFunc(event =1):
    SendRequest("/OnPressDownArrow")

# Buttons OnPressFunctions
def TriangleOnPressFunc(event =1):
    SendRequest("/OnPressTr")
def CircleOnPressFunc(event =1):
    SendRequest("/OnPressCircle")
def SquareOnPressFunc(event =1):
    SendRequest("/OnPressSquare")
def XOnPressFunc(event =1):
    SendRequest("/OnPressX")

# LB LT RB RT OnPressFunctions
def LtOnPressFunc(event =1):
    SendRequest("/OnPressLt")
def RtOnPressFunc(event =1):
    SendRequest("/OnPressRt")
def LbOnPressFunc(event =1):
    SendRequest("/OnPressLb")
def RbOnPressFunc(event =1):
    SendRequest("/OnPressRb")

# axis
def R1Stop(event =1):
    SendRequest("/R1Stop")
def R2Stop(event =1):
    SendRequest("/R2Stop")

def R1UpFunc(event =1):
    SendRequest("/R1Up")
def R1DownFunc(event =1):
    SendRequest("/R1Down")
def R1RightFunc(event =1):
    SendRequest("/R1Right")
def R1LeftFunc(event =1):
    SendRequest("/R1Left")

def R2UpFunc(event =1):
    SendRequest("/R2Up")
def R2DownFunc(event =1):
    SendRequest("/R2Down")
def R2RightFunc(event =1):
    SendRequest("/R2Right")
def R2LeftFunc(event =1):
    SendRequest("/R2Left")


#other
def ShareOnPressFunc(event =1):
    SendRequest("/OnPressShare")
def PsOnPressFunc(event =1):
    SendRequest("/OnPressPs")
def OptionsOnPressFunc(event =1):
    SendRequest("/OnPressOptions")
def R1ClickOnPressFunc(event =1):
    SendRequest("/OnPressR1Click")
def R2ClickOnPressFunc(event =1):
    SendRequest("/OnPressR2Click")
########################################################
# Arrows OnReleaseFunctions
def UpArrowButtonOnReleaseFunc(event =1):
    SendRequest("/OnReleaseUpArrow")
def RightArrowButtonOnReleaseFunc(event =1):
    SendRequest("/OnReleaseRightArrow")
def LeftArrowButtonOnReleaseFunc(event =1):
    SendRequest("/OnReleaseLeftArrow")
def DownArrowButtonOnReleaseFunc(event =1):
    SendRequest("/OnReleaseDownArrow")

# Buttons OnReleaseFunctions
def TriangleOnReleaseFunc(event =1):
    SendRequest("/OnReleaseTr")
def CircleOnReleaseFunc(event =1):
    SendRequest("/OnReleaseCircle")
def SquareOnReleaseFunc(event =1):
    SendRequest("/OnReleaseSquare")
def XOnReleaseFunc(event =1):
    SendRequest("/OnReleaseX")

# LB LT RB RT OnReleaseFunctions
def LtOnReleaseFunc(event =1):
    SendRequest("/OnReleaseLt")
def RtOnReleaseFunc(event =1):
    SendRequest("/OnReleaseRt")
def LbOnReleaseFunc(event =1):
    SendRequest("/OnReleaseLb")
def RbOnReleaseFunc(event =1):
    SendRequest("/OnReleaseRb")



#other
def ShareOnReleaseFunc(event =1):
    SendRequest("/OnReleaseShare")
def PsOnReleaseFunc(event =1):
    SendRequest("/OnReleasePs")
def OptionsOnReleaseFunc(event =1):
    SendRequest("/OnReleaseOptions")
def R1ClickOnReleaseFunc(event =1):
    SendRequest("/OnReleaseR1Click")
def R2ClickOnReleaseFunc(event =1):
    SendRequest("/OnReleaseR2Click")


def set_resolution(url: str, index: int=1, verbose: bool=False):
    try:
        if verbose:
            resolutions = "10: UXGA(1600x1200)\n9: SXGA(1280x1024)\n8: XGA(1024x768)\n7: SVGA(800x600)\n6: VGA(640x480)\n5: CIF(400x296)\n4: QVGA(320x240)\n3: HQVGA(240x176)\n0: QQVGA(160x120)"
            print("available resolutions\n{}".format(resolutions))

        if index in [10, 9, 8, 7, 6, 5, 4, 3, 0]:
            requests.get(url + "/control?var=framesize&val={}".format(index))
        else:
            print("Wrong index")
    except:
        print("SET_RESOLUTION: something went wrong")

def set_quality(url: str, value: int=1, verbose: bool=False):
    try:
        if value >= 10 and value <=63:
            requests.get(url + "/control?var=quality&val={}".format(value))
    except:
        print("SET_QUALITY: something went wrong")