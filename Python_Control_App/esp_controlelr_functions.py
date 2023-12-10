import urllib.request
import customtkinter as ctk

def SendRequest(Request):
    Url = "http://192.168.1.4"
    try:
        urllib.request.urlopen(Url+Request)
    except Exception as e:
        try:
            urllib.request.urlopen(Url+Request)
        except Exception as e:
            print("Request failed:", e)

def change_apperance_mode(new_appearance_mode: str):
    ctk.AppearanceModeTracker.set_appearance_mode(new_appearance_mode)

#Arrows Functions

def UpArrowButtonFunc():
    SendRequest("/UpArrow")

def RightArrowButtonFunc():
    SendRequest("/RightArrow")

def LeftArrowButtonFunc():
    SendRequest("/LeftArrow")

def DownArrowButtonFunc():
    SendRequest("/DownArrow")

#Buttons Functions
def TrFunc():
    SendRequest("/Tr")

def OFunc():
    SendRequest("/O")

def SquareFunc():
    SendRequest("/Square")

def XFunc():
    SendRequest("/X")

#LB LT RB RT Functions
def LtFunc():
    SendRequest("/Lt")

def RtFunc():
    SendRequest("/Rt")

def LbFunc():
    SendRequest("/Lb")

def RbFunc():
    SendRequest("/Rb")
