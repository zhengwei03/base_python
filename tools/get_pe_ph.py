import hashlib
import os, string, shutil, re
import pefile  ##记得import pefile

file_path = r"C:\Users\RP\Desktop\tools\wt0609_update.exe"
# with open("pe_info.txt", "wb") as f:
#     f.write(open("./dwt/ori/PE/0F4AF56EBB29683D025E8A8E85E98F20", 'rb').read())

def test1():
    pe = pefile.PE(file_path)
    print(pe)
    # info = pe.DOS_HEADER
    # print(hex(23117))
    # print(info.dump_dict())
    with open(file_path, "rb") as f:
        print(f.read())
    # print(pe.DOS_HEADER.dump_dict())
    # offset = 0
    # for key, value in info.items():
    #     if key == "Structure":
    #         continue
    #     offset += value.get("Offset")
    # print(offset)
    # print(pe)
    # for sect in pe.sections:
    #     print(sect)
        # print(generate_hash(hex(sect.Characteristics).encode(), "sha256"))
        # print(sect.get_hash_sha256())
        # break
        # print(sect.Name.decode().replace("\x00", ''))
        #
        # print(sect.get_hash_md5())
        # print(sect.get_hash_sha256())


def test2():
    pe = pefile.PE(file_path)
    print(file_path)

    for section in pe.sections:
        print(section)


def test3():
    pe = pefile.PE(file_path)
    print(file_path)

    for importeddll in pe.DIRECTORY_ENTRY_IMPORT:
        print(importeddll.dll)
        ##or use
        # print pe.DIRECTORY_ENTRY_IMPORT[0].dll
        for importedapi in importeddll.imports:
            print(importedapi.name)
        ##or use
        # print pe.DIRECTORY_ENTRY_IMPORT[0].imports[0].name


def generate_hash(file_info, hash_style):
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



test1()










