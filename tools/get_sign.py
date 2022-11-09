import hashlib
import os
import time


class SignOperate:
    def __init__(self, path):
        self.path = path

    def get_sign(self):
        try:
            cmd = "osslsigncode verify %s | grep 'Signature verification: ok'|wc -l" % self.path
            print(cmd)
            res = os.popen(cmd)
            print(res)
            time.sleep(1)
            return res
        except Exception as e:
            print(e)
            return False

    def create_sign(self, certs_file, key_file, sign_file_out):
        try:
            cmd = "osslsigncode sign -certs {certs_file} " \
                  "-key {key_file} -t http://timestamp.globalsign.com/scripts/timestamp.dll -in " \
                  "{sign_file} -out {sign_file_out}".format(**{"certs_file": certs_file, "sign_file": self.path,
                                                               "sign_file_out": sign_file_out, "key_file": key_file})
            res = os.popen(cmd)
            print(res)
            return res
        except Exception as e:
            print(e)
            return False

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


if __name__ == '__main__':
    a = SignOperate("./total.py")
    # a.get_sign()
    # a.create_sign('cert-20220609-174338.crt', 'key-20220609-174338.pem', 'first_sign_total.py')
