import os,re
import base64,os
import webbrowser
from plugins.icon import img
from tkinter import *
from tkinter.ttk import *
from plugins import jsonw
import ctypes



def ui():
    #使用程序自身的dpi适配
    ctypes.windll.shcore.SetProcessDpiAwareness(1)
    ScaleFactor=ctypes.windll.shcore.GetScaleFactorForDevice(0)
    
    root=Tk()
    root.tk.call('tk', 'scaling', ScaleFactor/68)
    root.title("Lizzieyzy快速设置")
    root.geometry('960x540')
    tmp = open("tmp.ico","wb+")
    tmp.write(base64.b64decode(img))
    tmp.close()
    root.iconbitmap("tmp.ico")
    os.remove("tmp.ico")


    varengin = StringVar(root)
    varweight = StringVar(root)
    varcfg = StringVar(root)
    varyzy = StringVar(root)
    varkomi = DoubleVar(root)
    varh = IntVar(root)
    varw = IntVar(root)
    enginlist = scan('Engin','.*.exe')
    weightlist = scan('Weight','.*')
    cfglist = scan('Config','.*.cfg')
    yzylist = scan('.\\','.*Lizzie.*.exe')
    cbox=jsonw.load()
    varengin.set(cbox['engin'] if 'engin' in cbox.keys() else enginlist[0])
    varweight.set(cbox['weight'] if 'weight' in cbox.keys() else weightlist[0])
    varcfg.set(cbox['cfg'] if 'cfg' in cbox.keys() else cfglist[0])
    varyzy.set(cbox['yzy'] if 'yzy' in cbox.keys() else yzylist[0])
    varkomi.set(cbox['komi'] if 'komi' in cbox.keys() else 7.5)
    varw.set(cbox['w'] if 'w' in cbox.keys() else 19)
    varh.set(cbox['h'] if 'h' in cbox.keys() else 19)


    enginlb = Label(root,text='引擎')
    enginlb.place(relx=0.05,rely=0.05)
    engincomb = Combobox(root, values=enginlist, textvariable=varengin)
    engincomb.place(relx=0.15,rely=0.05,relwidth=0.65)
    btengindown = Button(root, text = "下载")
    btengindown.place(relx = 0.8, rely = 0.05, relwidth=0.1)

    weightlb = Label(root,text='权重')
    weightlb.place(relx=0.05,rely=0.15)
    weightcomb = Combobox(root, values=weightlist, textvariable=varweight)
    weightcomb.place(relx=0.15,rely=0.15,relwidth=0.65)

    cfglb = Label(root,text='配置文件')
    cfglb.place(relx=0.05,rely=0.25)
    cfgcomb = Combobox(root, values=cfglist ,textvariable=varcfg)
    cfgcomb.place(relx=0.15,rely=0.25,relwidth=0.65)

    komilb = Label(root,text='贴目')
    komilb.place(relx=0.05,rely=0.35)
    komihintlb = Label(root,text='可输入')
    komihintlb.place(relx=0.27,rely=0.35)
    komicomb = Combobox(root,textvariable=varkomi,values=[0.0,0.5,2.5,3.5,6.5,7.5])
    komicomb.place(relx=0.15,rely=0.35,relwidth=0.1)

    yzylb = Label(root,text='指定yzy程序')
    yzylb.place(relx=0.41,rely=0.35)
    yzycomb = Combobox(root, values=yzylist, textvariable=varyzy)
    yzycomb.place(relx=0.55,rely=0.35,relwidth=0.35)

    
    wlb= Label(root, text='棋盘尺寸：宽')
    wlb.place(relx=0.05,rely=0.45)
    wspinbox = Spinbox(root, from_=0, to=99, textvariable=varw)
    wspinbox.place(relx=0.2,rely=0.45,relwidth=0.2)

    hlb= Label(root, text='棋盘尺寸：高')
    hlb.place(relx=0.55,rely=0.45)
    hspinbox = Spinbox(root, from_=0, to=99, textvariable=varh)
    hspinbox.place(relx=0.7,rely=0.45,relwidth=0.2)

    def prev():
        cbox = {}       #初始化
        cbox['engin']=str(engincomb.get())
        cbox['weight']=str(weightcomb.get())
        cbox['cfg']=str(cfgcomb.get())
        cbox['yzy']=str(yzycomb.get())
        cbox['komi']=float(komicomb.get())
        cbox['w']=int(wspinbox.get())
        cbox['h']=int(hspinbox.get())
        textshow = preview(cbox,1)      #得到显示的字符串
        textprev.config(state=NORMAL)   #恢复可编辑
        textprev.delete('1.0',END)      #清空
        textprev.insert('1.0',textshow) #插入内容
        textprev.config(state=DISABLED) #禁止编辑
        return cbox

    def start():        #启动Lizzieyzy
        cbox = prev()
        command = preview(cbox,2)
        res = jsonw.set("config.txt",command,cbox["komi"],cbox["w"],cbox["h"])
        if(res==True):
            jsonw.write(cbox)
            os.system(str(yzycomb.get()))#jar方式启动


    btnprev = Button(root, text='预览', command=prev)
    btnstart = Button(root, text='启动', command=start)
    btnprev.place(relx=0.2,rely=0.55,relwidth=0.2)
    btnstart.place(relx=0.6,rely=0.55,relwidth=0.2)

    textprev = Text(root)
    textprev.place(relx=0.05,rely=0.65,relwidth=0.9,relheight=0.25)
    textprev.config(state=DISABLED)
    #textprev.config(state=NORMAL)

    btnlink = Label(root, text='KataGo公益下载站 www.katago.dog',foreground='blue')
    btnlink.place(relx=0.5, rely=0.94,anchor="center")
    def open_url(event):
        webbrowser.open("https://www.katago.dog", new=0)
    btnlink.bind("<Button-1>", open_url)

    root.mainloop()


def scan(path,type):
    if (os.path.exists(path)==False):           #检查创建目录
        os.mkdir(path)                          #创建缺失的
    filelist = []                               #初始化
    def find(path):
        li = os.listdir(path)
        for file in li:
            currpath = os.path.join(path,file)  #构造完整的路径
            if (os.path.isdir(currpath)):       #如果是目录而非文件
                find(currpath)                  #则向下递归
            elif(re.search(type,file)):         #对于拓展名进行正则匹配
                filelist.append(currpath)       #加上路径，避免混淆
    find(path)
    if (len(filelist)==0):
        filelist=[path+"目录下找不到文件"]

    return filelist

def preview(cbox,req):
    engin = str(cbox['engin'])
    weight = str(cbox['weight'])
    cfg = str(cbox['cfg'])
    komi = str(cbox['komi'])
    w = str(cbox['w'])
    h = str(cbox['h'])
    command = "\"" + engin + "\" gtp -model \"" + weight + "\" -config \"" + cfg + "\""
    text = "命令：" + command + "\n贴目：" + komi + "\n棋盘：" + w + "*" + h 
    if(req == 1):
        return text
    elif(req == 2):
        return command


ui()