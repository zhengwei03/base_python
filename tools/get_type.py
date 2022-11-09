import os

def typeList():
    a = {
        "68746D6C3E": 'html', 
        "d0cf11e0a1b11ae10000":'xls', 
        "44656C69766572792D64":'eml', 
        'ffd8ffe000104a464946':'jpg', 
        '89504e470d0a1a0a0000':'png', 
        '47494638396126026f01':'gif', 
        '49492a00227105008037':'tif', 
        '424d228c010000000000':'bmp', 
        '424d8240090000000000':'bmp', 
        '424d8e1b030000000000':'bmp', 
        '41433130313500000000':'dwg', 
        '3c21444f435459504520':'html', 
        '3c21646f637479706520':'htm', 
        '48544d4c207b0d0a0942':'css', 
        '696b2e71623d696b2e71':'js', 
        '7b5c727466315c616e73':'rtf', 
        '38425053000100000000':'psd', 
        '46726f6d3a203d3f6762':'eml', 
        'd0cf11e0a1b11ae10000':'doc', 
        'd0cf11e0a1b11ae10000':'vsd', 
        '5374616E64617264204A':'mdb', 
        '252150532D41646F6265':'ps', 
        '255044462d312e350d0a':'pdf', 
        '2e524d46000000120001':'rmvb', 
        '464c5601050000000900':'flv', 
        '00000020667479706d70':'mp4', 
        '49443303000000002176':'mp3', 
        '000001ba210001000180':'mpg', 
        '3026b2758e66cf11a6d9':'wmv', 
        '52494646e27807005741':'wav', 
        '52494646d07d60074156':'avi', 
        '4d546864000000060001':'mid', 
        '504b0304140000080044':'zip', 
        '504b03040a0000080000':'zip', 
        '504b03040a0000000000':'zip', 
        '526172211a0700cf9073':'rar', 
        '235468697320636f6e66':'ini', 
        '504b03040a0000000000':'jar', 
        '4d5a9000030000000400':'exe', 
        '3c25402070616765206c':'jsp', 
        '4d616e69666573742d56':'mf', 
        '3c3f786d6c2076657273':'xml', 
        '494e5345525420494e54':'sql', 
        '7061636b616765207765':'java', 
        '406563686f206f66660d':'bat', 
        '1f8b0800000000000000':'gz', 
        '6c6f67346a2e726f6f74':'properties', 
        'cafebabe0000002e0041':'class', 
        '49545346030000006000':'chm', 
        '04000000010000001300':'mxp', 
        '504b0304140006000800':'docx', 
        'd0cf11e0a1b11ae10000':'wps', 
        '6431303a637265617465':'torrent',
        "4D444D5093A7": "dmp"
    }
    b = {"48544d4c207b0d0a0942": "css", "504b03040a0000000000": "jar", "52 45 47 45 44 49 54 34": "reg", "4D5AEE": "COM", "E93B03": "COM", "FF00020004040554": "wks", "4F7B": "dw4", "8A0109000000E108": "aw", "5B666C7473696D2E": "cfg", "00000020667479706d70": "mp4", "456C6646696C6500": "evtx", "52494646d07d60074156": "avi", "52617221": "rar, RARArchive(rar)", "58435000": "cap", "49545346030000006000": "chm", "377ABCAF271C": "7z", "E4525C7B8CD8A74D": "one", "81CDAB": "wpf", "EDABEEDB": "rpm", "0000002066747970": "3gp", "4D52564E": "nvram", "4E422A00": "jnt, jtp", "5850434F4D0A5479": "xpt", "646E732E": "au", "414D594F": "syw", "010F0000": "mdf", "504147454455": "dmp", "494e5345525420494e54": "sql", "00001A0000100400": "wk3", "5000000020000000": "idx", "434F4D2B": "clb", "60EA": "arj", "FFD8FF": "JPEG(jpg), jfif", "636F6E6563746978": "vhd", "504750644D41494E": "pgd", "1A350100": "eth", "582D": "eml", "4E45534D1A01": "nsf", "564350434830": "pch", "68490000": "shd", "464F524D00": "aiff", "4D534346": "cab, ppz, snp", "41433130": "CAD(dwg)", "436174616C6F6720": "ctf", "504b0304140006000800": "docx", "454E545259564344": "vcd", "6431303a637265617465": "torrent", "01DA01010003": "rgb", "4D5A900003000000": "ax, api", "3026B2758E66CF11": "WindowsMedia(asf), wma, wmv", "4D444D5093A7": "hdmp", "68746D6C3E": "html, HTML(html)", "56455253494F4E20": "ctl", "458600000600": "qbb", "D7CDC69A": "wmf", "23204D6963726F73": "dsp", "89504E47": "png, PNG(png)", "3C21646F63747970": "dci", "252150532D41646F6265": "Postscript(eps.or.ps)", "424F4F4B4D4F4249": "prc", "FEEF": "gho, ghs", "00000020667479704D3441": "m4a", "0CED": "mp", "414376": "sle", "04000000010000001300": "mxp", "9901": "pkr", "00000100": "ico, spl", "04": "db4", "504B03040A": "ipa", "47494638": "GIF(gif)", "4B444D": "vmdk", "300000004C664C65": "evt", "4C4E0200": "gid, hlp", "235468697320636f6e66": "ini", "4d5a9000030000000400": "exe", "0000020006040600": "wk1", "534D415254445257": "sdr", "4C00000001140200": "lnk", "FFFFFFFF": "sys", "7B0D0A6F20": "lgc, lgd", "78": "dmg", "213C617263683E0A": "lib", "414F4C2046656564": "bag", "2E7261FD": "ram, RealAudio(ram)", "BE000000AB": "wri", "4D6963726F736F66742056697375616C": "sln", "5F434153455F": "cas, cbk", "2E524D46": "rm, RealMedia(rm), rmvb", "7061636b616765207765": "java", "414F4C564D313030": "pfc, org", "57415645": "wav, Wave(wav)", "43232B44A4434DA5": "rtd", "475832": "gx2", "0000000C6A502020": "jp2", "2142444E": "pst, Outlook(pst)", "E310000100000000": "info", "464C56": "flv", "504158": "pax", "4550": "mdi", "B168DE3A": "dcx", "575332303030": "ws2", "554641C6D2C1": "ufa", "43525553482076": "cru", "4D41723000": "mar", "6C33336C": "dbb", "5B47656E6572616C": "ecf", "464c5601050000000900": "flv", "B46E6844": "tib", "D42A": "arl, aut", "7B5C72746631": "rtf", "CFAD12FEC5FD746F": "dbx, OutlookExpress(dbx)", "AC9EBD8F": "qdf, Quicken(qdf)", "E3828596": "pwl, WindowsPassword(pwl)", "727473703A2F2F": "ram", "6465780A30303900": "dex", "5854": "bdr", "49492a00227105008037": "tif", "5B4D535643": "vcw", "49443303000000002176": "mp3", "CAFEBABE": "class", "7E424B00": "psp", "49544F4C49544C53": "lit", "4B47425F61726368": "kgb", "6D6F6F76": "mov, mov, Quicktime(mov)", "03000000": "qph", "3c3f786d6c2076657273": "xml", "4A47040E000000": "jg", "FFFE0000": "n, a", "B5A2B0B3B3B0A5B5": "cal", "52454745444954": "sud", "5245564E554D3A2C": "adf", "A90D000000000000": "dat", "424d8e1b030000000000": "bmp", "7b5c727466315c616e73": "rtf", "5041434B": "pak", "5F27A889": "jar", "d0cf11e0a1b11ae10000": "doc, vsd, wps", "000001BA": "mpg, MPEG(mpg), vob", "7B5C707769": "pwi", "76323030332E3130": "flt", "514649": "qemu", "424C4932323351": "bin", "9501": "skr", "0764743264647464": "dtd", "5A4F4F20": "zoo", "80": "obj", "2A2A2A2020496E73": "log", "3c25402070616765206c": "jsp", "4E49544630": "ntf", "7B5C727466": "rtf, RichTextFormat(rtf)", "CFAD12FE": "dbx", "0E4E65726F49534F": "nri", "504B0304140000": "zip", "4D4D002B": "tif, tiff", "ACED000573720012": "pdb", "3c21444f435459504520": "html", "DCDC": "cpl", "53484F57": "shw", "6375736800000002": "csh", "41724301": "arc", "46726f6d3a203d3f6762": "eml", "FFFE23006C006900": "mof", "4F504C4461746162": "dbf", "AC9EBD8F0000": "qdf", "1FA0": "tar.z", "576F726450726F": "lwp", "424D": "bmp, WindowsBitmap(bmp), dib", "38425053": "psd, AdobePhotoshop(psd)", "5157205665722E20": "abd, qsd", "255044462D312E": "pdf, AdobeAcrobat(pdf)", "696b2e71623d696b2e71": "js", "4d546864000000060001": "mid", "1F8B08": "gz", "FF464F4E54": "cpi", "FF575043": "wpd, WordPerfect(wpd), wpd, wpg, wpp, wp5, wp6", "4D53465402000100": "tlb", "4D535F564F494345": "dvf, msv", "4C5646090D0AFF00": "e01", "00004D4D585052": "qxd", "4D4D4D440000": "mmf", "43505446494C45": "cpt", "80000020031204": "adx", "414F4C4442": "aby", "414F4C494E444558": "abi", "00001A0002100400": "wk4, wk5", "424547494E3A5643": "vcf", "4D5A90000300000004000000FFFF": "zap", "44656C69766572792D646174653A": "Email[thoroughonly](eml)", "464158434F564552": "cpe", "02647373": "dss", "91334846": "hap", "2321414D52": "amr", "49545346": "chi, chm", "4D563243": "mls", "47504154": "pat", "5B57696E646F7773": "cpx", "49491A0000004845": "crw", "cafebabe0000002e0041": "class", "406563686f206f66660d": "bat", "4d616e69666573742d56": "mf", "4344303031": "iso", "255044462d312e350d0a": "pdf", "41564920": "avi, AVI(avi)", "0A050101": "pcx", "72696666": "acd", "1A45DFA393428288": "mkv", "49536328": "hdr", "3C3F786D6C2076657273696F6E3D": "manifest", "9CCBCB8D1375D211": "wab", "EB3C902A": "img", "445644": "dvr, ifo", "64000000": "p10", "4F67675300020000": "oga, ogg, ogv, ogx", "424d8240090000000000": "bmp", "3C4D616B65724669": "fm", "03": "db3", "C8007900": "lbk", "49443303000000": "koz", "38425053000100000000": "psd", "C3ABCDAB": "acs", "4E616D653A20": "cod", "664C614300000022": "flac", "55434558": "uce", "07534B46": "skf", "5B7665725D": "sam", "64737766696C65": "dsw", "5343486C": "ast", "000001ba210001000180": "mpg", "4D546864": "MIDI(mid), midi", "53514C4F434F4E56": "cnv", "4848474231": "sh3", "444D5321": "dms", "5374616E64617264204A": "MSAccess(mdb)", "1D7D": "ws", "50350A": "pgm", "49492A00": "tif, TIFF(tif)", "3C3F786D6C": "XML(xml)", "3026b2758e66cf11a6d9": "wmv", "5374756666497420": "sit", "2854686973206669": "hqx", "424d228c010000000000": "bmp", "425A68": "tar.bz2, tbz2, tb2", "3c21646f637479706520": "htm", "465753": "swf", "1100000053434341": "pf", "504B030414000600": "docx, pptx, xlsx", "434246494C45": "cbd", "6c6f67346a2e726f6f74": "properties", "DCFE": "efx", "2E524543": "ivr", "504D4343": "grp", "56657273696F6E20": "mif", "25504446": "pdf, fdf", "24464C3240282329": "sav", "C5D0D3C6": "eps", "2E7261FD00": "ra", "2112": "ain", "3C3F786D6C2076657273696F6E3D22312E30223F3E": "xml", "2e524d46000000120001": "rmvb", "00001A00051004": "123", "52494646e27807005741": "wav", "D20A0000": "ftr", "414F4C494458": "ind", "5B50686F6E655D": "dun", "0110": "tr1"", "}
    a.update(b)
    return a
"""
b85e187234dbd4d97424f45a33c9b1ff31421503
b86d2f313bd9c9d97424f45a29c9b17483c20431
97979797e8d701e80500b8004ccd21558bec83ec
"""

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
    tl = typeList()  # 文件类型
    print(type(tl))
    ftype = 'unknown'
    print('关键码比对中……')
    for hcode in tl.keys():
        lens = len(hcode)  # 需要的长度
        if bins[0:lens] == hcode:
            ftype = tl[hcode]
            break
    if ftype == 'unknown':  # 全码未找到，优化处理，码表取5位验证
        bins = bins[0:5]
        for hcode in tl.keys():
            if len(hcode) > 5 and bins == hcode[0:5]:
                ftype = tl[hcode]
                break
    return ftype


# 文件扫描，如果是目录，就将遍历文件，是文件就判断r文件类型
def filescanner(path):
    if type(path) != type('a'):  # 判断是否为字符串
        print('抱歉，你输入的不是一个字符串路径！')
    elif path.strip() == '':  # 将两头的空格移除
        print('输入的路径为空！')
    elif not os.path.exists(path):
        print('输入的路径不存在！')
    elif os.path.isfile(path):
        print('输入的路径指向的是文件，验证文件类型……')
        if path.rfind('.') > 0:
            print('文件名:',  os.path.split(path)[1])
        else:
            print('文件名中没有找到格式')
        path = filetype(path)
        print('解析文件判断格式：' + path)
    elif os.path.isdir(path):
        print('输入的路径指向的是目录，开始遍历文件')
        for p,  d,  fs in os.walk(path):
            print(os.path.split(p))
            print(d)
            print(fs)
            for n in fs:
                print(n)
                n = n.split('.')
                # print('\t' + n[0] + '\t' + n[1])


if __name__ == '__main__':
    print('WinSonZhao，欢迎你使用文件扫描工具……')
    while 1:
        path = input('请输入要扫描的文件夹路径：')
        filescanner(path)
        print('扫描结束！')

"""
ASP
3c25402050616765204c616e67756167653d2243
3c25402050616765204c616e67756167653d2243
JSP
3c25402070616765206c616e67756167653d226a
3c25402070616765206c616e67756167653d226a
"""



