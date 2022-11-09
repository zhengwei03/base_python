'''
Python 扫描PE文件头 by 郑瑞国
scanPE.py
获取PE文件头信息的方法:
import pefile
pe = pefile.PE('E:\\TestTool\\LaoMaoTao.exe')
print(pe)
'''
import os
import string
import hashlib
import pefile


def getmd5(file):
    m = hashlib.md5()
    with open(file, 'rb') as f:
        for line in f:
            m.update(line)
    md5code = m.hexdigest()
    # print(md5code)
    return md5code


# def getdisklist():
#     disklist = []
#     d = string.ascii_uppercase
#     # print(d)
#     for w in d:
#         disk = w + ':'
#         if os.path.isdir(disk):
#             disklist.append(disk)
#     # print(disklist)
#     return disklist


def scan(file):
    # print(disklist)
    # for disk in disklist:
        # print(disk)
        # os.chdir(disk + '/')
        # tree = os.walk('/')
        # for dir in tree:
        #     for file in dir[2]:
        if '.com' in file or '.exe' in file or '.dll' in file or '.bin' in file:
            myfile = './' + file
            try:
                pe = pefile.PE(myfile)
                mymd5code = getmd5(myfile)
                with open('d:/md5.txt', 'a') as f:
                    f.write(myfile + '\n' + mymd5code + '\n' + str(pe) + '\n')
                print(myfile)
                print('md5: ', mymd5code)
                print(pe)
            except:
                pass


if __name__ == '__main__':
    disklist = getdisklist()
    scan(disklist)