import urllib.request
import customtkinter as ctk

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

def SendRequest(Request):
    pass


def change_apperance_mode(new_appearance_mode: str):
    ctk.AppearanceModeTracker.set_appearance_mode(new_appearance_mode)

# Arrows Functions


def UpArrowButtonFunc():
    SendRequest("/UpArrow")


def RightArrowButtonFunc():
    SendRequest("/RightArrow")


def LeftArrowButtonFunc():
    SendRequest("/LeftArrow")


def DownArrowButtonFunc():
    SendRequest("/DownArrow")

# Buttons Functions


def TriangleFunc():
    SendRequest("/Tr")


def CircleFunc():
    SendRequest("/Circle")


def SquareFunc():
    SendRequest("/Square")


def XFunc():
    SendRequest("/X")

# LB LT RB RT Functions


def LtFunc():
    SendRequest("/Lt")


def RtFunc():
    SendRequest("/Rt")


def LbFunc():
    SendRequest("/Lb")


def RbFunc():
    SendRequest("/Rb")

# axis
def R1UpFunc():
    SendRequest("/R1Up")
def R1DownFunc():
    SendRequest("/R1Down")
def R1RightFunc():
    SendRequest("/R1Right")
def R1LeftFunc():
    SendRequest("/R1Left")

def R2UpFunc():
    SendRequest("/R2Up")
def R2DownFunc():
    SendRequest("/R2Down")
def R2RightFunc():
    SendRequest("/R2Right")
def R2LeftFunc():
    SendRequest("/R2Left")


#other
def ShareFunc():
    SendRequest("/Share")
def PsFunc():
    SendRequest("/Ps")
def OptionsFunc():
    SendRequest("/Options")
def R1ClickFunc():
    SendRequest("/R1Click")
def R2ClickFunc():
    SendRequest("/R2Click")