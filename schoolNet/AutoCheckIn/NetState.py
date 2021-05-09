#coding=utf-8
#!/usr/bin/env python
import socket
MaxSuccessTime=1
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
    ve=False

    for i in range(MaxTry):
        s=socket.socket()
        s.settimeout(1)
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
    return isNetOK(testserver)

def isNetChinaOK():
    #isOK = (isNetOK(('www.baidu.com',443))) and (isNetOK(('www.sina.com',443)))
    return (isNetOK(('www.baidu.com',443))) and (isNetOK(('www.sina.com',443)))


def isNetWorldOK():
    #isOK = (isNetOK(('www.youtube.com',443))) or (isNetOK(('www.google.com',443)))
    return (isNetOK(('www.youtube.com',443))) or (isNetOK(('www.google.com',443)))

def isNetMyServerOK():
    #isOK = isNetOK(('blog.omate.net',443))
    return isNetOK(('blog.omate.net',443))


def NetEnverionmentDetect():
    result='State:'
    if isNetSchoolOK()==True:
        result+='校园网 '
    if isNetChinaOK()==True:
        result+='国内网 '
    if isNetWorldOK()==True:
        result+=' 外网 '
    if isNetMyServerOK()==True:
        result+='MyServer'
    print(result)
    return result


def main():
    #print(isNetSchoolOK())
    #print(isNetChinaOK())
    #print(isNetWorldOK())
    #print(isNetMyServerOK())
    NetEnverionmentDetect()

if __name__ == '__main__':
    main()
