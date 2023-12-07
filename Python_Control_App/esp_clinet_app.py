import customtkinter as ctk
import urllib.request
import os

URL = "http://192.168.1.4"
color_mode_list = ['Dark', 'Light']

#functions
def SendRequest(URL):
    try:
        urllib.request.urlopen(URL)
    except Exception as e:
        print("Request failed:", e)

def LedOn():
    for x in range(2):
        SendRequest(URL+"/ledon")

def LedOff():
    for x in range(2):
        SendRequest(URL+"/ledoff")
    
def change_apperance_mode(new_appearance_mode: str):
    ctk.AppearanceModeTracker.set_appearance_mode(new_appearance_mode)

if __name__ == '__main__':

    # config my app
    ctk.ThemeManager.load_theme('green')
    ctk.AppearanceModeTracker.set_appearance_mode('system')
    ctk.deactivate_automatic_dpi_awareness()
    app = ctk.CTk()
    icon_path = "\icon.ico"
    app.iconbitmap(os.getcwd()+icon_path)
    app.title("ESP Control \n")
    app.geometry('200x250')
    app.resizable(False, False)
    app.grid_columnconfigure(1, weight=1)

    # opp
    mainFrame = ctk.CTkFrame(app)
    mainLabel = ctk.CTkLabel(
        mainFrame, text="ESP Control App",
        font=ctk.CTkFont('Arial', 20, weight='bold'))
    Button1 = ctk.CTkButton(
        mainFrame, text="Led On",
        font=ctk.CTkFont('Arial', 20, weight='bold'),
        command=LedOn)
    Button2 = ctk.CTkButton(
        mainFrame, text="Led Off",
        font=ctk.CTkFont('Arial', 20, weight='bold'),
        command=LedOff)
    apperance_button = ctk.CTkOptionMenu(
            mainFrame,
            font=ctk.CTkFont('Arial', 20,weight='bold'),
            values=['system','dark','light'],
            command=change_apperance_mode,
            height=48)
    
    # customization (graphices)
    mainFrame.grid(row=0, column=0, padx=(
        10, 10), pady=(20, 10))
    mainLabel.grid(row=1, column=0, padx=(
        10, 10), pady=(10, 10))
    Button1.grid(row=2, column=0, padx=(
        10, 10), pady=(10, 10))
    Button2.grid(row=3, column=0, padx=(
        10, 10), pady=(10, 10))
    apperance_button.grid(row=4, column=0, padx=(
        10, 10), pady=(10, 10))

    app.mainloop()
