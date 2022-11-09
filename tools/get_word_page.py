import datetime
import hashlib
import mimetypes

import filetype
import magic
import os
import re
import zipfile

class FileInfo:
    def __init__(self, file_path):
        self.file_path = file_path

    def generate_hash(self, file_info, hash_style):
        if hash_style == "md5":
            md5 = hashlib.md5()
            md5.update(file_info)
            sign = md5.hexdigest()
            sample_md5 = sign.upper()
            sample_md5 = str(sample_md5)
            return sample_md5
        elif hash_style == "sha1":
            sha1 = hashlib.sha1()
            sha1.update(file_info)
            sign = sha1.hexdigest()
            sample_sha1 = sign.upper()
            sample_sha1 = str(sample_sha1)
            return sample_sha1
        elif hash_style == "sha256":
            sha256 = hashlib.sha256()
            sha256.update(file_info)
            sign = sha256.hexdigest()
            sample_sha256 = sign.upper()
            sample_sha256 = str(sample_sha256)
            return sample_sha256

    def get_file_hash(self, file_path):
        with open(file_path, "rb") as f:
            file_info = f.read()
        print("文件的sha1:   ", self.generate_hash(file_info, "sha1"))
        print("文件的sha256:   ", self.generate_hash(file_info, "sha256"))
        print("文件的md5:   ", self.generate_hash(file_info, "md5"))

    def get_file_type(self, dir_path):
        # for listx in os.listdir(dir_path):
        if os.path.exists("./file_type.txt"):
            os.remove("./file_type.txt")
        if os.path.isfile(dir_path):
            print("文件的MIMETYPE为：", mimetypes.guess_extension(dir_path))
            print("文件的大小为：", os.stat(dir_path).st_size)
            print("文件的最近修改时间为：", datetime.datetime(os.path.getmtime(dir_path)))
            kind = filetype.guess_extension(dir_path)
            if kind == "zip" or not kind:
                kind = self.other_get_type(dir_path, "filename")
                if not kind:
                    kind = self.get_type(dir_path)
                    if not kind:
                        kind = self.get_type(dir_path)
                        if not kind:
                            kind = "未找到类型"
                return kind
            return kind
        for filepath, dirnames, filenames in os.walk(dir_path):
            for filename in filenames:
                dir_file_path = os.path.join(filepath, filename)
                if not os.path.isfile(dir_file_path):
                    continue
                try:
                    kind = filetype.guess_extension(dir_file_path)
                    if kind == "zip" or not kind:
                        kind = self.other_get_type(dir_file_path, filename)
                        if not kind:
                            kind = self.get_type(dir_file_path)
                            if not kind:
                                kind = self.get_type(dir_file_path)
                                if not kind:
                                    kind = "未找到类型"
                    with open("file_type.txt", "a+") as f:
                        f.write(dir_file_path + ":::::::::   " + kind.upper() + "\n")
                except Exception as e:
                    print("e::::", e)
                    continue

    def other_get_type(self, file_path, file_name):
        # file_path = "geshi/dll\CLASS/31D10D6430AFB5244B20D1607D5EFDDB"
        type_info = magic.from_file(file_path)
        if "Zip" in type_info or "Microsoft OOXML" in type_info:
            tmpzip_obj = zipfile.ZipFile(file_path)
            name_list = tmpzip_obj.namelist()
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
            # type_info = magic.from_file(file_path)
            if "powerpoint" in buffer_type_info:
                return "ppt"
            if "msword" in buffer_type_info:
                return "doc"
            if "Document" in buffer_type_info:
                return "doc"
            if "vnd.ms-office" in buffer_type_info:
                return "xls"
            if "excel" in buffer_type_info:
                return "xls"
            if "pdf" in buffer_type_info:
                return "pdf"
            if "msi" in buffer_type_info:
                return "msi"
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

    # def magic_or_file_type_main(path):
    #     get_file_type("./geshi/dll/COM/BA32CB26AC790111F6762E2F5D959FD3")
    #     print("结束")

    def get_type(self, path):
        if os.path.isfile(path):
            res = os.popen("./trid " + path).read()
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
                        # with open("trid.txt", "a+") as f:
                        #     f.write(dir_file_path + "::::::::::::::     " + file_type + "\n")

        # res = os.popen("trid.exe " + path).read()
        # print(res)


if __name__ == '__main__':
    file_obj = FileInfo("")
    print(file_obj.get_file_hash("/home/yuebao/test/zw_test/cert-20220609-174338.crt"))
    print(file_obj.get_file_type("/home/yuebao/test/zw_test/cert-20220609-174338.crt"))



