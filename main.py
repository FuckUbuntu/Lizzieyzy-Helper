import os,re
import base64,os
from plugins.icon import img
from tkinter import *
from tkinter.ttk import *
from plugins import jsonw



def ui():

    root=Tk()
    root.title("Lizzieyzy快速设置")
    root.geometry('720x480')
    tmp = open("tmp.ico","wb+")
    tmp.write(base64.b64decode(img))
    tmp.close()
    root.iconbitmap("tmp.ico")
    os.remove("tmp.ico")

    enginlb = Label(root,text='引擎')
    enginlb.place(relx=0.1,rely=0.05)
    engincomb = Combobox(root,values=scan('Engin','.*.exe'))
    engincomb.current(0)
    engincomb.place(relx=0.2,rely=0.05,relwidth=0.6)

    weightlb = Label(root,text='权重')
    weightlb.place(relx=0.1,rely=0.15)
    weightcomb = Combobox(root,values=scan('Weight','.*'))
    weightcomb.current(0)
    weightcomb.place(relx=0.2,rely=0.15,relwidth=0.6)

    cfglb = Label(root,text='配置文件')
    cfglb.place(relx=0.1,rely=0.25)
    cfgcomb = Combobox(root,values=scan('Config','.*.cfg'))
    cfgcomb.current(0)
    cfgcomb.place(relx=0.2,rely=0.25,relwidth=0.6)

    varkomi = DoubleVar()
    komilb = Label(root,text='贴目')
    komilb.place(relx=0.1,rely=0.35)
    komihintlb = Label(root,text='可以自行输入')
    komihintlb.place(relx=0.42,rely=0.35)
    komicomb = Combobox(root,textvariable=varkomi,values=[0.0,0.5,2.5,6.5,7.5])
    komicomb.current(0)
    komicomb.place(relx=0.2,rely=0.35,relwidth=0.2)

    varw = StringVar(root)
    varw.set(19)
    varh = StringVar(root)
    varh.set(19)
    
    wlb= Label(root, text='棋盘尺寸：宽')
    wlb.place(relx=0.1,rely=0.45)
    wspinbox = Spinbox(root, from_=0, to=99, textvariable=varw)
    wspinbox.place(relx=0.25,rely=0.45,relwidth=0.2)

    hlb= Label(root, text='棋盘尺寸：高')
    hlb.place(relx=0.5,rely=0.45)
    hspinbox = Spinbox(root, from_=0, to=99, textvariable=varh)
    hspinbox.place(relx=0.65,rely=0.45,relwidth=0.2)

    def prev():
        cbox = {}       #初始化
        cbox['engin']=str(engincomb.get())
        cbox['weight']=str(weightcomb.get())
        cbox['cfg']=str(cfgcomb.get())
        cbox['komi']=str(komicomb.get())
        cbox['w']=str(wspinbox.get())
        cbox['h']=str(hspinbox.get())
        textshow = preview(cbox,1)      #得到显示的字符串
        textprev.config(state=NORMAL)   #恢复可编辑
        textprev.delete('1.0',END)      #清空
        textprev.insert('1.0',textshow) #插入内容
        textprev.config(state=DISABLED) #禁止编辑
        return cbox

    def start():
        cbox = prev()
        command = preview(cbox,2)
        res = jsonw.set("config.txt",command,cbox["komi"],cbox["w"],cbox["h"])
        if(res==True):
            os.system('jre\java17\\bin\javaw.exe -jar lizzie-yzy2.5.1-shaded.jar')#jar方式启动

    btnprev = Button(root, text='预览', command=prev)
    btnstart = Button(root, text='启动', command=start)
    btnprev.place(relx=0.2,rely=0.55,relwidth=0.2)
    btnstart.place(relx=0.6,rely=0.55,relwidth=0.2)

    textprev = Text(root)
    textprev.place(relx=0.1,rely=0.65,relwidth=0.8,relheight=0.3)
    textprev.config(state=DISABLED)
    #textprev.config(state=NORMAL)

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