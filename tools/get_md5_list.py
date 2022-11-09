import json
import os
import hashlib



class GetSampleInfo:
    def __init__(self):
        #self.dir_name = "./dt100/"
        self.dir_name = "./"
        self.file_num = sum([os.path.isfile(self.dir_name + listx) for listx in os.listdir(self.dir_name)])

    def hash_md5(self, file):
        md5 = hashlib.md5()
        if isinstance(file, str):
            md5.update(file.encode())
        else:
            md5.update(file)
        return md5.hexdigest()


    def get_hash_list(self):
        hash_list = []

        for listx in os.listdir(self.dir_name):
            print(listx)
            if not os.path.isfile("./" + listx):
                continue
            with open(self.dir_name + listx, "rb") as f:
                file_info = f.read()
            file_md5 = self.hash_md5(file_info)
            hash_list.append(file_md5.upper())
        return hash_list



if __name__ == '__main__':
    obj = GetSampleInfo()
    hash_list = obj.get_hash_list()
    print(hash_list)
    with open("./hash_list.txt", "w") as f:
        f.write(json.dumps(hash_list))


