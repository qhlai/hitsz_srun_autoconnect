import os,sys
#加密
def encrypt(path,password,GivenNewFileName):
    #因为刚学可能有库可以直接获取这些信息吧，不过自己写个算法获取这些信息也没什么难度
    fileFullName = path.split(os.path.sep)#os.path.sep为操作系统的文件分隔符
    fileName = fileFullName[len(fileFullName)-1].split(".")[0]
    fileSuffix = fileFullName[len(fileFullName)-1].split(".")[1]

    # print("文件全名称:",fileFullName[len(fileFullName)-1])
    # print("文件名称:",fileName)
    # print("文件后缀:",fileSuffix)

    fileParent = path[0:len(path)-len(fileFullName[len(fileFullName)-1])]
    #newFileName="encrypt_"+fileFullName[len(fileFullName)-1]
    newFileName=GivenNewFileName
    newFilePath=fileParent+newFileName

    # print("文件父路径:",fileParent)
    # print("新的文件名称:",newFileName)
    # print("新的文件全路径:", newFilePath)

    f_read  = open(path,"rb")
    f_write = open(newFilePath,"wb")

    count=0 #当前密码加密索引

    #我们采用异或循环加密
    for now in f_read:
        for nowByte in now:
            newByte=nowByte^ord(password[count%len(password)])
            count+=1
            f_write.write(bytes([newByte]))

    f_read.close()
    f_write.close()

    #解密（因为我们采取的异或解密，所以其实和加密算法一样）
def decrypt(path, password,GivenNewFileName):
    # 因为刚学可能有库可以直接获取这些信息吧，不过自己写个算法获取这些信息也没什么难度
    fileFullName = path.split(os.path.sep)  # os.path.sep为操作系统的文件分隔符
    fileName = fileFullName[len(fileFullName) - 1].split(".")[0]
    fileSuffix = fileFullName[len(fileFullName) - 1].split(".")[1]

    # print("文件全名称:", fileFullName[len(fileFullName)-1])
    # print("文件名称:", fileName)
    # print("文件后缀:", fileSuffix)

    fileParent = path[0:len(path) - len(fileFullName[len(fileFullName)-1])]
    #newFileName = "decrypt_" + fileFullName[len(fileFullName) - 1]
    newFileName=GivenNewFileName
    newFilePath = fileParent + newFileName

    # print("文件父路径:", fileParent)
    # print("新的文件名称:", newFileName)
    # print("新的文件全路径:", newFilePath)

    f_read = open(path, "rb")
    f_write = open(newFilePath, "wb")

    count = 0  # 当前密码加密索引

    # 我们采用异或循环加密
    for now in f_read:
        for nowByte in now:
            newByte = nowByte ^ ord(password[count % len(password)])
            count += 1
            f_write.write(bytes([newByte]))

    f_read.close()
    f_write.close()
