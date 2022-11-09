

# 字节码转16进制字符串
def bytes2hex(bytes):
    print('关键码转码……')
    num = len(bytes)
    hexstr = u""
    for i in range(num):
        t = u"%x" % bytes[i]
        if len(t) % 2:
            hexstr += u"0"
        hexstr += t
    return hexstr.upper()


# 获取文件类型
def filetype(filename):
    print('读文件二进制码中……')
    binfile = open(filename, 'rb')  # 必需二制字读取
    print('提取关键码……')
    bins = binfile.read(20)  # 提取20个字符
    binfile.close()  # 关闭文件流
    bins = bytes2hex(bins)  # 转码
    bins = bins.lower()  # 小写
    print(bins)

import mimetypes

print(mimetypes.guess_type(r"apt_1")[0])
    # print(bins)
    # tl = typeList()  # 文件类型
    # print(type(tl))
    # ftype = 'unknown'
    # print('关键码比对中……')
    # for hcode in tl.keys():
    #     lens = len(hcode)  # 需要的长度
    #     if bins[0:lens] == hcode:
    #         ftype = tl[hcode]
    #         break
    # if ftype == 'unknown':  # 全码未找到，优化处理，码表取5位验证
    #     bins = bins[0:5]
    #     for hcode in tl.keys():
    #         if len(hcode) > 5 and bins == hcode[0:5]:
    #             ftype = tl[hcode]
    #             break
    # return ftype