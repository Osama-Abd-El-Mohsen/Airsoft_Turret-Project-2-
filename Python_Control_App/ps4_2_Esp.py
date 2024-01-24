import pygame
from esp_controller_functions import *
import time 

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
        pass
    else:
        pass

def refresh():
    pygame.event.pump()



while True:
        # refresh()

        joystick = pygame.joystick.Joystick(0)
        joystick.init()
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.JOYBUTTONDOWN:
                if joystick.get_button(Square):
                    SquareOnPressFunc()
                if joystick.get_button(X):
                    XOnPressFunc()
                if joystick.get_button(Circle):
                    CircleOnPressFunc()
                if joystick.get_button(Triangle):
                    TriangleOnPressFunc()
                if joystick.get_button(RT):
                    RtOnPressFunc()
                if joystick.get_button(LT):
                    LtOnPressFunc()
                if joystick.get_button(UpArrow):
                    UpArrowButtonOnPressFunc()
                if joystick.get_button(DownArrow):
                    DownArrowButtonOnPressFunc()
                if joystick.get_button(RightArrow):
                    RightArrowButtonOnPressFunc()
                if joystick.get_button(LeftArrow):
                    LeftArrowButtonOnPressFunc()
                if joystick.get_button(Share):
                    ShareOnPressFunc()
                if joystick.get_button(Ps):
                    PsOnPressFunc()
                if joystick.get_button(Options):
                    OptionsOnPressFunc()
                if joystick.get_button(R1Click):
                    R1ClickOnPressFunc()
                if joystick.get_button(R2Click):
                    R2ClickOnPressFunc()

            if event.type == pygame.JOYBUTTONUP:
                if event.button == (Square):
                    SquareOnReleaseFunc()
                if event.button == (X):
                    XOnReleaseFunc()
                if event.button == (Circle):
                    CircleOnReleaseFunc()
                if event.button == (Triangle):
                    TriangleOnReleaseFunc()
                if event.button == (RT):
                    RtOnReleaseFunc()
                if event.button == (LT):
                    LtOnReleaseFunc()
                if event.button == (UpArrow):
                    UpArrowButtonOnReleaseFunc()
                if event.button == (DownArrow):
                    DownArrowButtonOnReleaseFunc()
                if event.button == (RightArrow):
                    RightArrowButtonOnReleaseFunc()
                if event.button == (LeftArrow):
                    LeftArrowButtonOnReleaseFunc()
                if event.button == (Share):
                    ShareOnReleaseFunc()
                if event.button == (Ps):
                    PsOnReleaseFunc()
                if event.button == (Options):
                    OptionsOnReleaseFunc()
                if event.button == (R1Click):
                    R1ClickOnReleaseFunc()
                if event.button == (R2Click):
                    R2ClickOnReleaseFunc()

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
                    RB_Moved = True
        

                if RB_axis > .5 and not RB_Moved:
                    RB_Moved = True
                    RbOnPressFunc()
                elif RB_axis <= .5 and RB_Moved:
                    RB_Moved = False
                    RbOnReleaseFunc()

                if LB_axis > .5 and not LB_Moved:
                    LB_Moved = True
                    LbOnPressFunc()
                elif LB_axis <= .5 and LB_Moved:
                    LB_Moved = False
                    LbOnReleaseFunc()

                if R1x_axis < -0.5 and not R1moved_left:
                    R1LeftFunc()
                    R1moved_left = True
                elif R1x_axis > -0.1 and R1moved_left:
                    R1Stop()
                    R1moved_left = False

                # Detect movement to the right
                if R1x_axis > 0.5 and not R1moved_right:
                    R1RightFunc()
                    R1moved_right = True
                elif R1x_axis < 0.1 and R1moved_right:
                    R1Stop()
                    R1moved_right = False

                # Detect movement upwards
                if R1y_axis < -0.5 and not R1moved_up:
                    R1UpFunc()
                    R1moved_up = True
                elif R1y_axis > -0.1 and R1moved_up:
                    R1Stop()
                    R1moved_up = False

                # Detect movement downwards
                if R1y_axis > 0.5 and not R1moved_down:
                    R1DownFunc()
                    R1moved_down = True
                elif R1y_axis < 0.1 and R1moved_down:
                    R1Stop()
                    R1moved_down = False

                # Detect movement to the left
                if R2x_axis < -0.5 and not R2moved_left:
                    R2LeftFunc()
                    R2moved_left = True
                elif R2x_axis > -0.1 and R2moved_left:
                    R2Stop()
                    R2moved_left = False

                # Detect movement to the right
                if R2x_axis > 0.5 and not R2moved_right:
                    R2RightFunc()
                    R2moved_right = True
                elif R2x_axis < 0.1 and R2moved_right:
                    R2Stop()
                    R2moved_right = False

                # Detect movement upwards
                if R2moved_up == True :
                    R2DownFunc()
                    print("up")
                if R2moved_down == True :
                    R2UpFunc()
                    print("down")

                if R2y_axis < -0.5 and not R2moved_up:
                    R2UpFunc()
                    R2moved_up = True
                elif R2y_axis > -0.1 and R2moved_up:
                    R2Stop()
                    print("stop")
                    R2moved_up = False

                # Detect movement downwards
                if R2y_axis > 0.5 and not R2moved_down:
                    R2DownFunc()
                    R2moved_down = True
                elif R2y_axis < 0.1 and R2moved_down:
                    R2Stop()
                    print("stop")
                    R2moved_down = False
