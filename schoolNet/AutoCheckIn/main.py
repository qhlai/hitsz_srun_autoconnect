# -*- coding: utf-8 -*-
#import urllib.request
#import urllib
import time
#import gzip
#import http.cookiejar
import time
import os,sys
#import re#过滤
#
#import myfile
import SchoolNet
import NetState
import LogPrint

if __name__ == '__main__':
    #log = LogPrint.Logger('all.log',level='debug')
    NetEnverionment=NetState.NetEnverionmentDetect()
    LogPrint.log("启动:"+NetEnverionment)
    #LogPrint.Logger('all.log',level='info').logger.info("启动:"+NetEnverionment)
    print('输入0登陆')
    if (input()=='0'):
        LogPrint.log("登陆:"+SchoolNet.login()+NetState.NetEnverionmentDetect())
        #LogPrint.Logger('all.log',level='info').logger.info("登陆:"+SchoolNet.login()+NetReady.NetEnverionmentDetect())
    else:
        pass

    print('输入0注销(需关闭无感知认证后才有效)')
    if (input()=='0'):
        SchoolNet.logout()
        LogPrint.log("注销:"+SchoolNet.logout()+NetState.NetEnverionmentDetect())
        #LogPrint.Logger('all.log',level='info').logger.info("注销:"+SchoolNet.logout()+NetReady.NetEnverionmentDetect())
    else:
        LogPrint.log('退出:'+NetState.NetEnverionmentDetect())


    
