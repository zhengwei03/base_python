#!/usr/bin/env python3

# 导入cryptography库的相关模块和函数
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization

from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding

from cryptography.exceptions import InvalidSignature

# 验证函数
def verify(data_file_name, signature_file_name, public_key_file_name):
    """
    验证函数使用指定的公钥对签名结果进行验证
    :param data_file_name: 原始数据文件
    :param signature_file_name: 签名验证文件
    :param public_key_file_name: 用于验证的公钥文件
    :return: 成功返回True, 失败返回False
    """

    # 读取原始数据
    data_file = open(data_file_name, 'rb')
    data = data_file.read()
    data_file.close()

    # 读取待验证的签名数据
    signature_file = open(signature_file_name, 'rb')
    signature = signature_file.read()
    signature_file.close()

    # 从PEM文件中读取公钥数据
    key_file = open(public_key_file_name, 'rb')
    key_data = key_file.read()
    key_file.close()

    # 从PEM文件数据中加载公钥
    public_key = serialization.load_pem_public_key(
        key_data,
        backend=default_backend()
    )

    # 验证结果，默认为False
    verify_ok = False

    try:
        # 使用公钥对签名数据进行验证
        # 指定填充方式为PKCS1v15
        # 指定hash方式为sha256
        public_key.verify(
            signature,
            data,
            padding.PKCS1v15(),
            hashes.SHA256()
        )
    # 签名验证失败会触发名为InvalidSignature的exception
    except InvalidSignature:
        # 打印失败消息
        print('invalid signature!')
    else:
        # 验证通过，设置True
        verify_ok = True

    # 返回验证结果
    return verify_ok


if __name__ == '__main__':
    data_file = r'data.bin'
    signature_file = r'signature.bin'
    public_key_file = r'Key_pub.pem'

    verify_ok = verify(data_file, signature_file, public_key_file)
    if verify_ok:
        print('verify ok!')
    else:
        print('verify fail!')