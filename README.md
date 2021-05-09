# hitsz_net_autoconnect
哈尔滨工业大学（深圳）校园网无界面自动登陆  深澜网络

Beta stage

此项目是在我另一个自动签到项目上改的，一个晚上拼拼凑凑做完，代码质量一般。

基于伪装重新生成请求登陆，反正比用selenium优雅，速度更快，占用空间更少，主要原理是破译web认证界面的请求数据，然后脚本伪装加解密，实现登录与注销功能。

仅用于无界面linux使用，非法使用后果自负


# 使用方法

## 1.安装python依赖包

代码目录下执行使用终端

pip3 install -r requirements.txt

## 2.设置数据
将SchoolNet.py里的username password改为自己的账号密码

运行main.py，或使用OneClick.py快速运行

# 补充
退出登录仅在关闭无感知认证后有效，学校设定比较奇葩，其实你自己在网页上手动点注销也一般是退出不了的。

登录数据记录在log.txt处

# 更新日志

2021.5.13 Beta stage 增加一键脚本，修复log打印多次的问题

2021.1.13 Alpha stage 实现功能

# 在当前目录生成requestment
#pipreqs . --encoding=utf8 --force