# Lizzieyzy快速设置工具

快速配置启动引擎、权重、配置文件、贴目等。<br>
并写入到配置文件。

已添加保存配置的功能，启动KataGo时自动保存，下次启动会自动加载上一次的配置。

# 使用方法
下载[Lizzieyzy](https://github.com/yzyray/lizzieyzy)的整合包，可访问[下载站](https://www.katago.dog)获取<br>
将本软件复制进Lizzieyzy文件夹内<br>
启动本软件<br>
启动软件时，目录下会自动生成Engine、Weight、Config三个文件夹，请分别将KataGo引擎、权重、配置文件放置在三个文件夹或棋子目录内，再次启动程序，会自动识别。<br>
配置好各项参数，点击启动。<br>
KataGo的首个配置文件将被替换成"Autostart"，点击启动即可，也可将其设置为默认加载项。<br>
**更新：改为通过exe方式启动，可手动选择，正则匹配文件名为[.\*Lizzieyzy.\*.exe]的程序，也可手动输入。**

# 计划
* 新增配置项而非覆盖第一个
* 将配置项设定为自动加载的配置
* 适配iKatago、LeelaZero等更多引擎
* 可通过网络获取引擎/权重