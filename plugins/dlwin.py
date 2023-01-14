import os
import re
import base64
from tkinter import *
import requests
from urllib.parse import unquote
from plugins.icon import img
import ctypes
from bs4 import BeautifulSoup



def ui(kind):
    
    title = ""
    if(kind == 0):
        title = "引擎"
    elif(kind == 1):
        title = "权重"
    ctypes.windll.shcore.SetProcessDpiAwareness(1)
    ScaleFactor=ctypes.windll.shcore.GetScaleFactorForDevice(0)

    win=Tk()
    win.tk.call('tk', 'scaling', ScaleFactor/68)
    win.title(title + "下载")
    win.geometry("840x520")
    tmp = open("tmp.ico","wb+")
    tmp.write(base64.b64decode(img))
    tmp.close()
    win.iconbitmap("tmp.ico")
    os.remove("tmp.ico")


    win.mainloop()

def engui():
    ui(0)

def weiui():
    ui(1)

def urlget(kind, port=114514):
    
    url = "https://katago.dog"
    if (kind==0):
        url = "https://katagotraining.org/networks/"
    requests.DEFAULT_RETRIES = 35
    response = requests.Request.get(url, timeout=300)
    purl = (response.text)