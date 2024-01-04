import customtkinter as ctk
from esp_controller_functions import *
import os
from PIL import Image, ImageTk
import cv2
import threading

Cwd = os.getcwd()
color_mode_list = ['Dark', 'Light']
photo = None 

CamUrl = "http://192.168.1.4/capture" 


def update():
    global photo  # Declare photo as a global variable
    while True:
        try:
            resp = urllib.request.urlopen(CamUrl)
            img_array = np.array(bytearray(resp.read()), dtype=np.uint8)
            cap = cv2.imdecode(img_array, -1)
            frame = cv2.resize(cap, (560, 400))
            new_photo = ImageTk.PhotoImage(image=Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)))
            canvas.create_image(0, 0, image=new_photo, anchor=ctk.NW)
            photo = new_photo
        except Exception as e:
            continue
            print(f"Error fetching or updating image: {e}")
        # app.after(100, update)



if __name__ == '__main__':
    ctk.ThemeManager.load_theme('green')
    ctk.AppearanceModeTracker.set_appearance_mode('system')
    ctk.deactivate_automatic_dpi_awareness()
    app = ctk.CTk()
    icon_path = "\icon.ico"
    app.iconbitmap(Cwd+icon_path)
    app.title("ESP Control \n")
    app.geometry('1060x770')
    app.resizable(False, False)

    video_thread = threading.Thread(target=update)
    video_thread.daemon = True  # Daemonize the thread to exit when the main program ends
    video_thread.start()
    #images & Pallete
    Green      = "#4a978e"
    DarkGreen  = "#39726a"
    Red        = "#bc8282"
    DarkRed    = "#936767"
    Blue       = "#afd3f6"
    DarkBlue   = "#97b7d1"
    Pink       = "#c9b2cc"
    DarkPink   = "#af9eb2"
    Dark       = "#474a4f"
    FDark      = "#333333"
    DarkHover  = "#2d3035"
    #arrows
    RightArrow = ctk.CTkImage(Image.open(Cwd+r"\assits\RightArrow.png"),    size=(48,39))
    LeftArrow = ctk.CTkImage(Image.open(Cwd+r"\assits\LeftArrow.png"),      size=(48,39))
    UpArrow = ctk.CTkImage(Image.open(Cwd+r"\assits\UpArrow.png"),          size=(39,48))
    DownArrow = ctk.CTkImage(Image.open(Cwd+r"\assits\DownArrow.png"),      size=(39,48))

    RightArrowInfo  = ctk.CTkImage(Image.open(Cwd+r"\assits\RightArrow.png"),size=(48/2,39/2))
    LeftArrowInfo   = ctk.CTkImage(Image.open(Cwd+r"\assits\LeftArrow.png") ,size=(48/2,39/2))
    UpArrowInfo     = ctk.CTkImage(Image.open(Cwd+r"\assits\UpArrow.png")   ,size=(39/2,48/2))
    DownArrowInfo   = ctk.CTkImage(Image.open(Cwd+r"\assits\DownArrow.png") ,size=(39/2,48/2))
    #other buttons
    TrButton     = ctk.CTkImage(Image.open(Cwd+r"\assits\Tr.png"),      size=(47,47))
    OButton      = ctk.CTkImage(Image.open(Cwd+r"\assits\O.png"),       size=(47,47))
    XButton      = ctk.CTkImage(Image.open(Cwd+r"\assits\X.png"),       size=(47,47))
    SquareButton = ctk.CTkImage(Image.open(Cwd+r"\assits\Square.png"),  size=(47,47))

    TrButtonInfo     = ctk.CTkImage(Image.open(Cwd+r"\assits\Tr.png"),      size=(47/2,47/2))
    OButtonInfo      = ctk.CTkImage(Image.open(Cwd+r"\assits\O.png"),       size=(47/2,47/2))
    XButtonInfo      = ctk.CTkImage(Image.open(Cwd+r"\assits\X.png"),       size=(47/2,47/2))
    SquareButtonInfo = ctk.CTkImage(Image.open(Cwd+r"\assits\Square.png"),  size=(47/2,47/2))

    LTButton = ctk.CTkImage(Image.open(Cwd+r"\assits\LT.png"),size=(63,33))
    RTButton = ctk.CTkImage(Image.open(Cwd+r"\assits\RT.png"),size=(63,33))
    LBButton = ctk.CTkImage(Image.open(Cwd+r"\assits\LB.png"),size=(63,48))
    RBButton = ctk.CTkImage(Image.open(Cwd+r"\assits\RB.png"),size=(63,48))

    LTButtonInfo = ctk.CTkImage(Image.open(Cwd+r"\assits\LT.png"),size=(63/2,33/2))
    RTButtonInfo = ctk.CTkImage(Image.open(Cwd+r"\assits\RT.png"),size=(63/2,33/2))
    LBButtonInfo = ctk.CTkImage(Image.open(Cwd+r"\assits\LB.png"),size=(63/2,48/2))
    RBButtonInfo = ctk.CTkImage(Image.open(Cwd+r"\assits\RB.png"),size=(63/2,48/2))



    # main frame
    MainFrame = ctk.CTkFrame(app, width=800, height=600)
    MainFrame.grid(row=0, column=0, padx=10, pady=10,columnspan=4)

    # Label & info
    MainLabel = ctk.CTkLabel(MainFrame, text="AirSoft Control App", font=ctk.CTkFont('Cairo', 40,weight="bold"))
    MainLabel.grid(row=0, column=0, padx=10, pady=10)

    ControlelrFrame = ctk.CTkFrame(MainFrame)
    ControlelrFrame.grid(row=1, column=0,padx=10, pady=(10,10))
    
    SpaceFrame = ctk.CTkFrame(ControlelrFrame,fg_color="transparent")
    SpaceFrame.grid(row=0, column=2,padx=10, pady=10,rowspan=5)

    #Arrows buttons
    UpArrowButton = ctk.CTkButton(ControlelrFrame,image=UpArrow,text="",width=39,height=48,fg_color=FDark,hover_color=Dark)
    UpArrowButton.bind("<ButtonPress-1>", UpArrowButtonOnPressFunc)
    UpArrowButton.bind("<ButtonRelease-1>", UpArrowButtonOnReleaseFunc)
    UpArrowButton.grid(row=2, padx=10, pady=(20,7) ,column=0,columnspan=2)

    RightArrowButton = ctk.CTkButton(ControlelrFrame,image=RightArrow,text="",width=48,height=39,fg_color=FDark,hover_color=Dark)
    RightArrowButton.bind("<ButtonPress-1>", RightArrowButtonOnPressFunc)
    RightArrowButton.bind("<ButtonRelease-1>", RightArrowButtonOnReleaseFunc)
    RightArrowButton.grid(row=3, padx=(20,30),pady=0,column=1)

    LeftArrowButton = ctk.CTkButton(ControlelrFrame,image=LeftArrow,text="",width=48,height=39,fg_color=FDark,hover_color=Dark)
    LeftArrowButton.bind("<ButtonPress-1>", LeftArrowButtonOnPressFunc)
    LeftArrowButton.bind("<ButtonRelease-1>", LeftArrowButtonOnReleaseFunc)
    LeftArrowButton.grid(row=3, padx=(30,20),pady=0 ,column=0)

    DownArrowButton = ctk.CTkButton(ControlelrFrame,image=DownArrow,text="",width=39,height=48,fg_color=FDark,hover_color=Dark)
    DownArrowButton.bind("<ButtonPress-1>", DownArrowButtonOnPressFunc)
    DownArrowButton.bind("<ButtonRelease-1>", DownArrowButtonOnReleaseFunc)
    DownArrowButton.grid(row=4, padx=10, pady=(7,20) ,column=0,columnspan=2)

    #Other Buttons
    TrCButton = ctk.CTkButton(ControlelrFrame,image=TrButton,text="",width=37,height=37,fg_color=FDark,hover_color=Green)
    TrCButton.bind("<ButtonPress-1>", TriangleOnPressFunc)
    TrCButton.bind("<ButtonRelease-1>", TriangleOnReleaseFunc)
    TrCButton.grid(row=2, padx=10, pady=(20,7) ,column=3,columnspan=2)

    OCButton = ctk.CTkButton(ControlelrFrame,image=OButton,text="",width=37,height=37,fg_color=FDark,hover_color=Pink)
    OCButton.bind("<ButtonPress-1>", CircleOnPressFunc)
    OCButton.bind("<ButtonRelease-1>", CircleOnReleaseFunc)
    OCButton.grid(row=3, padx=(20,30),column=4)

    SquareCButton = ctk.CTkButton(ControlelrFrame,image=SquareButton,text="",width=37,height=37,fg_color=FDark,hover_color=Pink)
    SquareCButton.bind("<ButtonPress-1>", SquareOnPressFunc)
    SquareCButton.bind("<ButtonRelease-1>", SquareOnReleaseFunc)
    SquareCButton.grid(row=3, padx=(30,20) ,column=3)

    XCButton = ctk.CTkButton(ControlelrFrame,image=XButton,text="",width=37,height=37,fg_color=FDark,hover_color=Blue)
    XCButton.bind("<ButtonPress-1>", XOnPressFunc)
    XCButton.bind("<ButtonRelease-1>", XOnReleaseFunc)
    XCButton.grid(row=4, padx=10, pady=(7,20) ,column=3,columnspan=2)

    #LB LT RB RT
    LTCButton = ctk.CTkButton(ControlelrFrame,image=LTButton,text="",width=63,height=33,fg_color=FDark,hover_color=Dark)
    LTCButton.bind("<ButtonPress-1>", LtOnPressFunc)
    LTCButton.bind("<ButtonRelease-1>", LtOnReleaseFunc)
    LTCButton.grid(row=1, padx=10,column=0,columnspan=2)

    RTCButton = ctk.CTkButton(ControlelrFrame,image=RTButton,text="",width=63,height=33,fg_color=FDark,hover_color=Dark)
    RTCButton.bind("<ButtonPress-1>", RtOnPressFunc)
    RTCButton.bind("<ButtonRelease-1>", RtOnReleaseFunc)
    RTCButton.grid(row=1, pady=10 ,column=3,columnspan=2)

    LBCButton = ctk.CTkButton(ControlelrFrame,image=LBButton,text="",width=63,height=48,fg_color=FDark,hover_color=Dark)
    LBCButton.bind("<ButtonPress-1>", LbOnPressFunc)
    LBCButton.bind("<ButtonRelease-1>", LbOnReleaseFunc)
    LBCButton.grid(row=0, padx=10, pady=(20,10) ,column=0,columnspan=2)

    RBCButton = ctk.CTkButton(ControlelrFrame,image=RBButton,text="",width=63,height=48,fg_color=FDark,hover_color=Dark)
    RBCButton.bind("<ButtonPress-1>", RbOnPressFunc)
    RBCButton.bind("<ButtonRelease-1>", RbOnReleaseFunc)
    RBCButton.grid(row=0, padx=10, pady=(20,10) ,column=3,columnspan=2)

    canvas = ctk.CTkCanvas(ControlelrFrame, width=560, height=400)
    canvas.grid(row=0 ,column=2,rowspan=5,padx=0,pady=0)
    # print(vid.get(cv2.CAP_PROP_FRAME_WIDTH))
    # print(vid.get(cv2.CAP_PROP_FRAME_HEIGHT))

    #Info Frame
    InfoAppFrame = ctk.CTkFrame(app)
    InfoAppFrame.grid(row=1, padx=10, pady=0 ,column=0,columnspan=2)
    InfoFrame = ctk.CTkFrame(InfoAppFrame)
    InfoFrame.grid(row=1, padx=10, pady=10 ,column=0)
    XLabel=ctk.CTkLabel(InfoFrame,text="  Move Forward   ",image=XButtonInfo, font=ctk.CTkFont('Arial', 25,weight='bold'),compound="left")
    XLabel.grid(row=0, padx=10, pady=5 ,column=0)
    SquareLabel=ctk.CTkLabel(InfoFrame,text="  Move Backward",image=SquareButtonInfo, font=ctk.CTkFont('Arial', 25,weight='bold'),compound="left")
    SquareLabel.grid(row=1, padx=10, pady=5 ,column=0)
    LeftArrowLabel=ctk.CTkLabel(InfoFrame,text="  Move  Left         ",image=LeftArrowInfo, font=ctk.CTkFont('Arial', 25,weight='bold'),compound="left")
    LeftArrowLabel.grid(row=2, padx=10, pady=5 ,column=0)
    RightArrowLabel=ctk.CTkLabel(InfoFrame,text="  Move  Right      ",image=RightArrowInfo, font=ctk.CTkFont('Arial', 25,weight='bold'),compound="left")
    RightArrowLabel.grid(row=3, padx=10, pady=5 ,column=0)
    TriangleLabel=ctk.CTkLabel(InfoFrame,text="  Led On/Off         ",image=TrButtonInfo, font=ctk.CTkFont('Arial', 25,weight='bold'),compound="left")
    TriangleLabel.grid(row=4, padx=10, pady=5 ,column=0)

    InfoFrame2 = ctk.CTkFrame(InfoAppFrame)
    InfoFrame2.grid(row=1, padx=5, pady=10 ,column=1)

    InfoFrame3 = ctk.CTkFrame(InfoAppFrame)
    InfoFrame3.grid(row=1, padx=10, pady=10 ,column=2,columnspan=2)
    nameInfo=ctk.CTkLabel(InfoFrame3,text="By : ", font=ctk.CTkFont('Arial', 25,weight='bold'),text_color=Red,compound="left")
    nameInfo.grid(row=0, padx=10, pady=10 ,column=0)
    nameInfo=ctk.CTkLabel(InfoFrame3,text="Osama Abd El Mohsen",text_color=Red, font=ctk.CTkFont('Arial', 23,weight='bold'),compound="left")
    nameInfo.grid(row=1, padx=10, pady=10 ,column=0)
    nameInfo=ctk.CTkLabel(InfoFrame3,text="& Software Team",text_color=Green, font=ctk.CTkFont('Arial', 15),compound="left")
    nameInfo.grid(row=2, padx=10, pady=10 ,column=0)
    nameInfo=ctk.CTkOptionMenu(InfoFrame3,values=['system','dark','light'],fg_color=Green,button_color=DarkGreen, font=ctk.CTkFont('Arial', 20,weight='bold'),command=change_apperance_mode,)
    nameInfo.grid(row=3, padx=10, pady=10 ,column=0)


    InfoFrame4 = ctk.CTkFrame(InfoAppFrame)
    InfoFrame4.grid(row=1, padx=10, pady=10 ,column=6,columnspan=2)
    nameInfo=ctk.CTkLabel(InfoFrame4,text="Mazen Mohamed Atta",text_color=Red, font=ctk.CTkFont('Arial', 20,weight='bold'),compound="left")
    nameInfo.grid(row=2, padx=10, pady=10 ,column=0)
    nameInfo1=ctk.CTkLabel(InfoFrame4,text="Mohamed Salah El Din",text_color=Red, font=ctk.CTkFont('Arial', 20,weight='bold'),compound="left")
    nameInfo1.grid(row=3, padx=10, pady=10 ,column=0)
    nameInfo2=ctk.CTkLabel(InfoFrame4,text="Tarek Thabet El Gendy",text_color=Red, font=ctk.CTkFont('Arial', 20,weight='bold'),compound="left")
    nameInfo2.grid(row=4, padx=10, pady=10 ,column=0)
    nameInfo3=ctk.CTkLabel(InfoFrame4,text="Abd Allah Ashraf",text_color=Red, font=ctk.CTkFont('Arial', 20,weight='bold'),compound="left")
    nameInfo3.grid(row=5, padx=10, pady=10 ,column=0)
    

    
    RtLabel=ctk.CTkLabel(InfoFrame2,text="  Shoot           ",image=RTButtonInfo, font=ctk.CTkFont('Arial', 25,weight='bold'),compound="left")
    RtLabel.grid(row=0, padx=10, pady=5 ,column=0)
    RBLabel=ctk.CTkLabel(InfoFrame2,text="  Airsoft Right",image=RBButtonInfo, font=ctk.CTkFont('Arial', 25,weight='bold'),compound="left")
    RBLabel.grid(row=1, padx=10, pady=5 ,column=0)
    LBLabel=ctk.CTkLabel(InfoFrame2,text="  Airsoft Left   ",image=LBButtonInfo, font=ctk.CTkFont('Arial', 25,weight='bold'),compound="left")
    LBLabel.grid(row=2, padx=10, pady=5 ,column=0)
    UpArrowLabel=ctk.CTkLabel(InfoFrame2,text="   Airsoft Up    ",image=UpArrowInfo, font=ctk.CTkFont('Arial', 25,weight='bold'),compound="left")
    UpArrowLabel.grid(row=3, padx=10, pady=5 ,column=0)
    DownArrowLabel=ctk.CTkLabel(InfoFrame2,text="   AirsoftDown",image=DownArrowInfo, font=ctk.CTkFont('Arial', 25,weight='bold'),compound="left")
    DownArrowLabel.grid(row=4, padx=10, pady=5 ,column=0)

    app.mainloop()
