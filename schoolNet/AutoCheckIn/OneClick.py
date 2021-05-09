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
    NetEnv=NetState.NetEnverionmentDetect()
    LogPrint.log("一键登录启动:"+NetEnv)
    NetEnv=NetState.NetEnverionmentDetect()
    LogPrint.log("一键登录:"+SchoolNet.login()+NetEnv)
    os.system( 'pause' ) 


    
