import pygame
from socket import *
import time
import os
import termcolor
import pyfiglet
import urllib.request
from esp_controller_functions import *




pygame.init()
pygame.joystick.init()


def joy_Get_Init():
    get_init = pygame.joystick.get_init()
    if get_init == True:
        print(
            f"\033[1;31mThe State Of Initialization  => \33[37m✅\033[1;31m")
        print("\33[37m="*40)
        pass
    else:
        print(
            f"\033[1;31mThe State Of Initialization  => \33[37m❌\033[1;31m")
        print("\33[37m="*40)
        pass


def num_Of_Joys():
    global joyNumbers
    joyNumbers = pygame.joystick.get_count()


def joy_Name():
    global joyName
    joyName = joystick.get_name()
    print(f"\033[1;31mJoystick Name Is : \33[37m{joyName}")


def joy_Id():
    global joyId
    joyId = joystick.get_id()
    print(f"\033[1;31mJoystick Id : \33[37m{joyId}")


def joy_Num_Axes():
    global joyNumAxes
    joyNumAxes = joystick.get_numaxes()
    print(f"\33[33mNumber Of Axes: \33[37m{joyNumAxes}")


def joy_Num_Buttons():
    global joyNumButtons
    joyNumButtons = joystick.get_numbuttons()
    print(f"\33[33mNumber Of Buttons: \33[37m{joyNumButtons}")


def Axes():
    global axesTuple
    axesArray = []
    for i in range(joyNumAxes):
        axes_Val = round(joystick.get_axis(i), 2)
        print(f"\33[32mAxis {i} => \33[37m{axes_Val}")
        axesArray.append(axes_Val)
    axesTuple = tuple(axesArray)


def joy_Num_Balls():
    global joyNumBalls
    joyNumBalls = joystick.get_numballs()
    print(f"\33[33mNumber Of Balls : \33[37m{joyNumBalls}")


def Buton():
    global buttonsTuple
    buttonsArray = []
    for i in range(joyNumButtons):
        button_Val = bool(joystick.get_button(i))
        print(f"\33[32mButton {i:02} => \33[37m{button_Val}")

        if button_Val == False:
            button_Val = 0
        elif button_Val == True:
            button_Val = 1
        buttonsArray.append(button_Val)
    buttonsTuple = tuple(buttonsArray)


def joy_Num_Hats():
    global joyNumHats
    joyNumHats = joystick.get_numhats()
    print(f"\33[33mNumber Of Hats : \33[37m{joyNumHats}")


def hat():
    for i in range(joyNumHats):
        ht = joystick.get_hat(i)
        print(f"\33[34mHat {i} => \33[37m{ht}")


def refresh():
    pygame.event.pump()


num_Of_Joys()
if joyNumbers == 0:
    pygame.joystick.quit()
    print("\33[37m="*40)
    joy_Get_Init()
    print("\33[33m\033[1mNo Joystick Connected Pls Check cable connection\33[34m")
    print("\33[37m="*40)
    exit()
print("\33[37m="*40)

while True:
    for i in range(joyNumbers):
        joystick = pygame.joystick.Joystick(i)
        joystick.init()
        print("="*40)
        print(termcolor.colored(pyfiglet.figlet_format("OSAMA"), color="blue"))
        print("="*40)
        num_Of_Joys()
        print(f"\33[37m{joyNumbers}\033[1;31m Joystick Connected")
        joy_Get_Init()
        print("\33[37m/"*40)
        joy = f" \33[32mjoystick joy_Numbers{i+1}\33[37m "
        joy = joy.center(50, "/")
        print(f"{joy}")
        print("/"*40)
        print("\33[37m="*40)
        joy_Name()
        joy_Id()
        print("="*40)
        joy_Num_Axes()
        joy_Num_Buttons()
        joy_Num_Balls()
        joy_Num_Hats()
        print("="*40)
        Axes()
        print("="*40)
        Buton()
        print("="*40)
        hat()
        print("="*40)
        refresh()


        events = pygame.event.get()
        for event in events:
            if event.type == pygame.JOYBUTTONDOWN:
                if joystick.get_button(Square):
                    SquareFunc()
                    print("SquareFunc")
                if joystick.get_button(X):
                    XFunc()
                    print("XFunc")
                if joystick.get_button(Circle):
                    CircleFunc()
                    print("CircleFunc")
                if joystick.get_button(Triangle):
                    TriangleFunc()
                    print("TriangleFunc")
                if joystick.get_button(RT):
                    RtFunc()
                    print("RtFunc")
                if joystick.get_button(LT):
                    LtFunc()
                    print("LtFunc")
                if joystick.get_button(UpArrow):
                    UpArrowButtonFunc()
                    print("UpArrowButtonFunc")
                if joystick.get_button(DownArrow):
                    DownArrowButtonFunc()
                    print("DownArrowButtonFunc")
                if joystick.get_button(RightArrow):
                    RightArrowButtonFunc()
                    print("RightArrowButtonFunc")
                if joystick.get_button(LeftArrow):
                    LeftArrowButtonFunc()
                    print("LeftArrowButtonFunc")
                if joystick.get_button(Share):
                    ShareFunc()
                    print("ShareFunc")
                if joystick.get_button(Ps):
                    PsFunc()
                    print("PsFunc")
                if joystick.get_button(Options):
                    OptionsFunc()
                    print("OptionsFunc")
                if joystick.get_button(R1Click):
                    R1ClickFunc()
                    print("R1ClickFunc")
                if joystick.get_button(R2Click):
                    R2ClickFunc()
                    print("R2ClickFunc")

            if event.type == pygame.JOYAXISMOTION:
                axis = event.axis
                value = event.value
                if ((axis == RB) and (value > .80)) :
                    RbFunc()
                    print("RbFunc")
                if ((axis == LB) and (value > .80)) :
                    LbFunc()
                    print("LbFunc")
                if ((axis == R1Up_Down) and (value > .80)) :
                    R1DownFunc()
                    print("R1DownFunc")
                if ((axis == R1Up_Down) and (value < -.80)) :
                    R1UpFunc()
                    print("R1UpFunc")
                if ((axis == R1Right_Left) and (value > .80)) :
                    R1RightFunc()
                    print("R1RightFunc")
                if ((axis == R1Right_Left) and (value < -.80)) :
                    R1LeftFunc()
                    print("R1LeftFunc")
                if ((axis == R2Up_Down) and (value > .80)) :
                    R2DownFunc()
                    print("R2DownFunc")
                if ((axis == R2Up_Down) and (value < -.80)) :
                    R2UpFunc()
                    print("R2UpFunc")
                if ((axis == R2Right_Left) and (value > .80)) :
                    R2RightFunc()
                    print("R2RightFunc")
                if ((axis == R2Right_Left) and (value < -.80)) :
                    R2LeftFunc()
                    print("R2LeftFunc")

        time.sleep(.1)
        os.system('cls')
