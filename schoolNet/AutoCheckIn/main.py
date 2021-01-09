# coding=utf-8
import urllib.request
import LogPrint
import urllib
import time
import gzip
import http.cookiejar
import time
import os,sys
import re#过滤
#
#import myfile
import SchoolNet
import NetReady




if __name__ == '__main__':
    log = LogPrint.Logger('all.log',level='debug')
    NetEnverionment=NetReady.NetEnverionmentDetect()
    LogPrint.Logger('all.log',level='info').logger.info("启动:"+NetEnverionment)
    print('输入0登陆')
    if (input()=='0'):
        #SchoolNet.logout()
        LogPrint.Logger('all.log',level='info').logger.info("登陆:"+SchoolNet.login()+NetReady.NetEnverionmentDetect())
    else:
        pass
        #LogPrint.Logger('all.log',level='info').logger.info('退出:'+NetReady.NetEnverionmentDetect())
    #SchoolNet.login()
    #if NetEnverionment=='校园网环境，无网络':
    #    SchoolNet.login()
    #    NetEnverionment=NetReady.NetEnverionmentDetect()
    #    LogPrint.Logger('all.log',level='info').logger.info("登录:"+NetEnverionment)
    #else:
    #    print('不进行操作')
    #    LogPrint.Logger('all.log',level='info').logger.info("不进行操作")

    #choice = 
    print('输入0注销')
    if (input()=='0'):
        #SchoolNet.logout()
        LogPrint.Logger('all.log',level='info').logger.info("注销:"+SchoolNet.logout()+NetReady.NetEnverionmentDetect())
    else:
        LogPrint.Logger('all.log',level='info').logger.info('退出:'+NetReady.NetEnverionmentDetect())
    #LogPrint.Logger('error.log', level='error').logger.error('error')
    
    #
    #NetReady.NetEnverionmentDetect()

    #SchoolNet.login()
	
    ##choice = input()
    ##print(choice)
    #choice="1"
    #if (choice=='0'):
    #    logout(header2,logout_url)
    #elif(choice == '1'):
    #    explorespace(header3)
    #    LogPrint.Logger('all.log',level='info').logger.info('浏览成功')
    #    logout(header2,logout_url)
    #LogPrint.Logger('success.log',level='info').logger.info('成功')
    ##LogPrint.Logger('error.log', level='error').logger.error('error')
    