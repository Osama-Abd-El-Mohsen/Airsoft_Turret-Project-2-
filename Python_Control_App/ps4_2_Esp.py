import pygame
from socket import *
import time
import os
# import termcolor
# import pyfiglet
import urllib.request
from esp_controller_functions import *

pygame.init()
pygame.joystick.init()


# Flags to track movement direction
R1moved_left = False
R1moved_right = False
R1moved_up = False
R1moved_down = False

R2moved_left = False
R2moved_right = False
R2moved_up = False
R2moved_down = False

RB_Moved = False
LB_Moved = False

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
        # print(termcolor.colored(pyfiglet.figlet_format("OSAMA"), color="blue"))
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
                    SquareOnPressFunc()
                    print("SquareOnPressFunc")
                if joystick.get_button(X):
                    XOnPressFunc()
                    print("XOnPressFunc")
                if joystick.get_button(Circle):
                    CircleOnPressFunc()
                    print("CircleOnPressFunc")
                if joystick.get_button(Triangle):
                    TriangleOnPressFunc()
                    print("TriangleOnPressFunc")
                if joystick.get_button(RT):
                    RtOnPressFunc()
                    print("RtOnPressFunc")
                if joystick.get_button(LT):
                    LtOnPressFunc()
                    print("LtOnPressFunc")
                if joystick.get_button(UpArrow):
                    UpArrowButtonOnPressFunc()
                    print("UpArrowButtonOnPressFunc")
                if joystick.get_button(DownArrow):
                    DownArrowButtonOnPressFunc()
                    print("DownArrowButtonOnPressFunc")
                if joystick.get_button(RightArrow):
                    RightArrowButtonOnPressFunc()
                    print("RightArrowButtonOnPressFunc")
                if joystick.get_button(LeftArrow):
                    LeftArrowButtonOnPressFunc()
                    print("LeftArrowButtonOnPressFunc")
                if joystick.get_button(Share):
                    ShareOnPressFunc()
                    print("ShareOnPressFunc")
                if joystick.get_button(Ps):
                    PsOnPressFunc()
                    print("PsOnPressFunc")
                if joystick.get_button(Options):
                    OptionsOnPressFunc()
                    print("OptionsOnPressFunc")
                if joystick.get_button(R1Click):
                    R1ClickOnPressFunc()
                    print("R1ClickOnPressFunc")
                if joystick.get_button(R2Click):
                    R2ClickOnPressFunc()
                    print("R2ClickOnPressFunc")

            if event.type == pygame.JOYBUTTONUP:
                if event.button == (Square):
                    SquareOnReleaseFunc()
                    print("SquareOnReleaseFunc")
                if event.button == (X):
                    XOnReleaseFunc()
                    print("XOnReleaseFunc")
                if event.button == (Circle):
                    CircleOnReleaseFunc()
                    print("CircleOnReleaseFunc")
                if event.button == (Triangle):
                    TriangleOnReleaseFunc()
                    print("TriangleOnReleaseFunc")
                if event.button == (RT):
                    RtOnReleaseFunc()
                    print("RtOnReleaseFunc")
                if event.button == (LT):
                    LtOnReleaseFunc()
                    print("LtOnReleaseFunc")
                if event.button == (UpArrow):
                    UpArrowButtonOnReleaseFunc()
                    print("UpArrowButtonOnReleaseFunc")
                if event.button == (DownArrow):
                    DownArrowButtonOnReleaseFunc()
                    print("DownArrowButtonOnReleaseFunc")
                if event.button == (RightArrow):
                    RightArrowButtonOnReleaseFunc()
                    print("RightArrowButtonOnReleaseFunc")
                if event.button == (LeftArrow):
                    LeftArrowButtonOnReleaseFunc()
                    print("LeftArrowButtonOnReleaseFunc")
                if event.button == (Share):
                    ShareOnReleaseFunc()
                    print("ShareOnReleaseFunc")
                if event.button == (Ps):
                    PsOnReleaseFunc()
                    print("PsOnReleaseFunc")
                if event.button == (Options):
                    OptionsOnReleaseFunc()
                    print("OptionsOnReleaseFunc")
                if event.button == (R1Click):
                    R1ClickOnReleaseFunc()
                    print("R1ClickOnReleaseFunc")
                if event.button == (R2Click):
                    R2ClickOnReleaseFunc()
                    print("R2ClickOnReleaseFunc")

            if event.type == pygame.JOYAXISMOTION:
                axis = event.axis
                value = event.value


                R1x_axis = joystick.get_axis(R1Right_Left)  
                R1y_axis = joystick.get_axis(R1Up_Down)  
                R2x_axis = joystick.get_axis(R2Right_Left)  
                R2y_axis = joystick.get_axis(R2Up_Down) 
                RB_axis = joystick.get_axis(RB) 
                LB_axis = joystick.get_axis(LB) 

                if ((RB_axis > .5) and not RB_Moved):
                    RbOnPressFunc()
                    print("RbOnPressFunc")
                    RB_Moved = True
        

                if RB_axis > .5 and not RB_Moved:
                    RB_Moved = True
                    RbOnPressFunc()
                    print("LB button pressed")
                elif RB_axis <= .5 and RB_Moved:
                    RB_Moved = False
                    RbOnReleaseFunc()
                    print("LB button released")

                if LB_axis > .5 and not LB_Moved:
                    LB_Moved = True
                    LbOnPressFunc()
                    print("LB button pressed")
                elif LB_axis <= .5 and LB_Moved:
                    LB_Moved = False
                    LbOnReleaseFunc()
                    print("LB button released")

                if R1x_axis < -0.5 and not R1moved_left:
                    R1LeftFunc()
                    print("R1LeftFunc")
                    R1moved_left = True
                elif R1x_axis > -0.1 and R1moved_left:
                    R1Stop()
                    print("R1 Returned to Center ")
                    R1moved_left = False

                # Detect movement to the right
                if R1x_axis > 0.5 and not R1moved_right:
                    R1RightFunc()
                    print("R1RightFunc")
                    R1moved_right = True
                elif R1x_axis < 0.1 and R1moved_right:
                    R1Stop()
                    print("R1 Returned to Center ")
                    R1moved_right = False

                # Detect movement upwards
                if R1y_axis < -0.5 and not R1moved_up:
                    R1UpFunc()
                    print("R1UpFunc")
                    R1moved_up = True
                elif R1y_axis > -0.1 and R1moved_up:
                    R1Stop()
                    print("R1 Returned to Center ")
                    R1moved_up = False

                # Detect movement downwards
                if R1y_axis > 0.5 and not R1moved_down:
                    R1DownFunc()
                    print("R1DownFunc")
                    R1moved_down = True
                elif R1y_axis < 0.1 and R1moved_down:
                    R1Stop()
                    print("R1 Returned to Center ")
                    R1moved_down = False

                # Detect movement to the left
                if R2x_axis < -0.5 and not R2moved_left:
                    R2LeftFunc()
                    print("R2LeftFunc")
                    R2moved_left = True
                elif R2x_axis > -0.1 and R2moved_left:
                    R2Stop()
                    print("R2 Returned to Center ")
                    R2moved_left = False

                # Detect movement to the right
                if R2x_axis > 0.5 and not R2moved_right:
                    R2RightFunc()
                    print("R2RightFunc")
                    R2moved_right = True
                elif R2x_axis < 0.1 and R2moved_right:
                    R2Stop()
                    print("R2 Returned to Center ")
                    R2moved_right = False

                # Detect movement upwards
                if R2y_axis < -0.5 and not R2moved_up:
                    R2UpFunc()
                    print("R2UpFunc")
                    R2moved_up = True
                elif R2y_axis > -0.1 and R2moved_up:
                    R2Stop()
                    print("R2 Returned to Center ")
                    R2moved_up = False

                # Detect movement downwards
                if R2y_axis > 0.5 and not R2moved_down:
                    R2DownFunc()
                    print("R2DownFunc")
                    R2moved_down = True
                elif R2y_axis < 0.1 and R2moved_down:
                    R2Stop()
                    print("R2 Returned to Center ")
                    R2moved_down = False
        time.sleep(.1)
        os.system('cls')
