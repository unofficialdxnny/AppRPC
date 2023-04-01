import psutil
import pyautogui
import win32gui
import win32api
import win32con
import os
import time
from pypresence import Presence

client_id = '1091516680972288111' 
RPC = Presence(client_id) 


RPC.connect()




while True:
    
    active_window = pyautogui.getActiveWindowTitle()

   
    current_process = psutil.Process(psutil.Process().pid).name()

 
    RPC.update(state=active_window, details=current_process, large_image='me_1_', large_text='This is I')

    time.sleep(15) 

RPC.close()
