import json



def set(filename, command, komi=7.5, width=19, height=19, name="AutoStart"):
    with open(filename, encoding='utf-8') as cfg:
        config = json.load(cfg)
        settings = config["leelaz"]["engine-settings-list"][0]
        settings["command"]=str(command)
        settings["komi"]=float(komi)
        settings["width"]=int(width)
        settings["name"]=str(name)
        settings["height"]=int(height)
    with open(filename, 'w', encoding='utf-8') as cfg:
        json.dump(config, cfg, ensure_ascii=False, indent=2)
        return True