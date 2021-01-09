#coding=utf-8
#!/usr/bin/env python
import socket
MaxSuccessTime=2
MaxFailTime=1

NoNetSchool=1
NoNetNOMAL=2

def Max(A,B):
    if A>B:
        return A
    else:
        return B
    
def isNetOK(testserver):
    MaxTry=Max(MaxSuccessTime,MaxFailTime);
    success=0
    fail=0
    isOK=False

    for i in range(MaxTry):
        s=socket.socket()
        s.settimeout(3)
        try:
            status = s.connect_ex(testserver)
            if status == 0:
                s.close()
                success=success+1
                #return True
            else:
                fail=fail+1
                #return False
        except Exception as e:
            fail=fail+1
            #return False
        if (success>=MaxSuccessTime):
            isOK=True
            #print("OK")
            break
        elif (fail >= MaxFailTime):
            isOK=False
            #print("NO")
            break
    return isOK


def isNetSchoolOK(testserver=('10.248.98.2',443)):
    isOK = isNetOK(testserver)
    return isOK

def isNetChinaOK():
    isOK = (isNetOK(('www.baidu.com',443))) and (isNetOK(('www.sina.com',443)))
    return isOK


def isNetWorldOK():
    isOK = (isNetOK(('www.youtube.com',443))) and (isNetOK(('www.google.com',443)))
    return isOK


def NetEnverionmentDetect():
    if isNetChinaOK()==False:
        if isNetSchoolOK==True:
            print('校园网环境')
            return '校园网环境，无网络'
        else:
            print('校园网环境，无网络')
            return '校园网环境，无网络'
    elif isNetChinaOK()==True:
        if isNetWorldOK==True:
            print('联网，可上外网')
            return '联网，可上外网'
        else:
            print('联网，不可上外网')
            return '联网，不可上外网'

def main():
    print(isNetSchoolOK())
    print(isNetChinaOK())
    print(isNetGoogleOK())
    print(isNetYouTubeOK())


if __name__ == '__main__':
    main()