import datetime
import os
import re
import zipfile

import filetype
import magic


def get_file_type(dir_path):
    # for listx in os.listdir(dir_path):
    print(os.path.exists("./file_type.txt"))
    if os.path.exists("./file_type.txt"):
        os.remove("./file_type.txt")
    print(dir_path)
    if os.path.isfile(dir_path):
        print("============")
        kind = filetype.guess_extension(dir_path)
        if kind == "zip" or not kind:
            res = other_get_type(dir_path, "filename")
            kind = res
            if not res:
                kind = "未找到类型"
            return kind
        return kind
    for filepath, dirnames, filenames in os.walk(dir_path):
        for filename in filenames:
            print(os.path.join(filepath,filename))
            dir_file_path = os.path.join(filepath,filename)
            if not os.path.isfile(dir_file_path):
                continue
            try:
                kind = filetype.guess_extension(dir_file_path)
                print(kind)
                if kind == "zip" or not kind:
                    res = other_get_type(dir_file_path, filename)
                    kind = res
                    if not res:
                        kind = get_type(dir_file_path)
                        if not kind:
                            kind = "未找到类型"
                    return kind
            except Exception as e:
                print("e::::", e)
                continue


def other_get_type(file_path, file_name):
    # file_path = "geshi/dll\CLASS/31D10D6430AFB5244B20D1607D5EFDDB"
    type_info = magic.from_file(file_path)
    print("type_info", type_info)
    if "Zip" in type_info:
        tmpzip_obj = zipfile.ZipFile(file_path)
        name_list = tmpzip_obj.namelist()
        print("name_list", name_list)
        # for name in name_list:
        #     print("name", name)
        if "word/document.xml" in name_list:
            return "docx"
        if "xl/workbook.xml" in name_list:
            return "xlsx"
        if "ppt/presProps.xml" in name_list:
            return "pptx"
        return False
    else:
        with open(file_path, 'rb') as f:
            buffer_type_info = magic.from_buffer(f.read(), mime=True)
        print("buffer_type_info", buffer_type_info)
        # type_info = magic.from_file(file_path)
        if "powerpoint" in buffer_type_info:
            return "ppt"
        if "msword" in buffer_type_info:
            return "doc"
        if "Document" in buffer_type_info:
            return "doc"
        if "excel" in buffer_type_info:
            return "xls"
        if "pdf" in buffer_type_info:
            return "pdf"
        if "EMF" in type_info:
            return "emf"
        if "PHP" in type_info:
            return "php"
        if "XML" in type_info:
            return "xml"
        if "class" in type_info:
            return "class"
        if "wmf" in type_info:
            return "wmf"
        if "ISO" in type_info:
            return "iso"
        if "dex" in type_info:
            return "dex"
        if "COM" in type_info:
            return "com"
        if "JAR" in type_info:
            return "jar"
        if "portable-bitmap" in buffer_type_info:
            return "pbm"
        if "msi" in buffer_type_info:
            return "msi"


# def magic_or_file_type_main(path):
#     get_file_type("./geshi/dll/COM/BA32CB26AC790111F6762E2F5D959FD3")
#     print("结束")

def get_type(path):
    if os.path.isfile(path):
        res = os.popen("trid.exe " + path).read()
        # print(res)
        res_list = re.findall("\(\.(.*?)\)", res)
        # print("a.group()", res_list)
        file_type = "unknown"
        if res_list:
            if "NULL" in res_list.copy():
                res_list.remove("NULL")
            if len(res_list) >= 1:
                file_type = res_list[0]
        if "ELF" in res:
            file_type = "ELF"
        with open("trid.txt", "a+") as f:
            f.write(path + "::::::::::::::     " + file_type + "\n")
        return file_type
    elif os.path.isdir(path):
        for filepath, dirnames, filenames in os.walk(path):
            for filename in filenames:
                # print(os.path.join(filepath, filename))
                dir_file_path = os.path.join(filepath, filename)
                res = os.popen("trid.exe " + dir_file_path).read()
                # print(res)
                if res:
                    print(res)
                    res_list = re.findall("\(\.(.*?)\)", res)
                    # print("a.group()", res_list)
                    file_type = "unknown"
                    if res_list:
                        if "NULL" in res_list.copy():
                            res_list.remove("NULL")
                        if len(res_list) >= 1:
                            file_type = res_list[0]
                    if "ELF" in res:
                        file_type = "ELF"
                    # if file_type == "unknown" or not file_type:
                    #     file_type = get_file_type(dir_file_path)
                    #     print("file_type::::get_file_type", file_type)
                    #     if not file_type:
                    #         file_type = "unknown"
                    with open("trid.txt", "a+") as f:
                        f.write(dir_file_path + "::::::::::::::     " + file_type + "\n")

    # res = os.popen("trid.exe " + path).read()
    # print(res)

if __name__ == '__main__':
    print(datetime.datetime.now())
    path = input("请输入路径(输入q退出):")
    if os.path.exists("trid.txt"):
        os.remove("trid.txt")
    while path != "q":
        res = get_file_type(path)
        print(path)
        print(datetime.datetime.now())
        path = input("请输入路径(输入q退出)::")
    # file_type = get_file_type("./geshi/dll\COM\\1EAAA98A0E65728ACDA2781AD9176CA5")
    # print(file_type)


