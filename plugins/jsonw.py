import json
import os



#操作Lizzieyzy的Json配置文件
#加入键["AutoStart":True]将其标记为
def set(filename, command, komi=7.5, width=19, height=19, name="AutoStart"):
    with open(filename, "r", encoding='utf-8') as cfg:
        config = json.load(cfg)
        setlist = config["leelaz"]["engine-settings-list"]
        cfg_odinal = 0
        cfg_default = {
        "ip": "",
        "initialCommand": "",
        "userName": "",
        "preload": False,
        "command": "",
        "komi": 7.5,
        "isDefault": True,
        "password": "",
        "port": "",
        "name": "(CPU-NoAVX2)Kata1-15B",
        "width": 19,
        "useJavaSSH": False,
        "useKeyGen": False,
        "keyGenPath": "",
        "height": 19
        }

        for configue in setlist:
            findout = False
            try:
                autostart = configue["AutoStart"]
            except:
                autostart = False
            if(autostart):
                findout = True
                break
            else:
                setlist[cfg_odinal]["isDefault"]=False
                cfg_odinal += 1
        if(findout == False):
            setlist.append(cfg_default)

        #print(cfg_odinal)
        #config["ui"]["default-engine"] = cfg_odinal
        config["ui"]["autoload-default"] = True

        settings = setlist[cfg_odinal]                                      #引擎设置项
        settings["command"]=str(command)
        settings["komi"]=float(komi)
        settings["width"]=int(width)
        settings["name"]=str(name)
        settings["height"]=int(height)
        settings["AutoStart"]=True
        settings["isDefault"]=True

    with open(filename, "w", encoding='utf-8') as cfg:
        json.dump(config, cfg, ensure_ascii=False, indent=2)
        return True


#操作自己的配置文件
path = 'helper-config'
def checkdir():                                                             #检查目录
    if (os.path.exists(path)==False):                                       #不存在则创建
        os.mkdir(path)
def write(cbox):                                                            #写入
    checkdir()
    with open(path+'\\config.json','w+', encoding='utf-8') as cfg:
        json.dump(cbox, cfg, ensure_ascii=False, indent=2)
    return True
def load():                                                                 #加载
    checkdir()
    try:                                                                    #如果不存在则创建一个新文件，返回空字典
        with open(path+'\\config.json','r+', encoding='utf-8') as cfg:
            cbox = json.load(cfg)
    except:
        with open(path+'\\config.json','w+', encoding='utf-8') as cfg:
            return {}
    return cbox