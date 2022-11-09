
# 导入cryptography库的相关模块和函数
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization

from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding


# 签名函数
def sign(data_file_name, signature_file_name, private_key_file_name):
    """
    签名函数使用指定的私钥Key对文件进行签名，并将签名结果写入文件中
    :param data_file_name: 待签名的数据文件
    :param signature_file_name: 存放签名结果的文件
    :param private_key_file_name: 用于签名的私钥文件
    :return: 签名数据
    """

    # 读取待签名数据
    data_file = open(data_file_name, 'rb')
    data = data_file.read()
    data_file.close()

    # 从PEM文件中读取私钥数据
    key_file = open(private_key_file_name, 'rb')
    key_data = key_file.read()
    key_file.close()

    # 从PEM文件数据中加载私钥
    private_key = serialization.load_pem_private_key(
        key_data,
        password=None,
        backend=default_backend()
    )

    # 使用私钥对数据进行签名
    # 指定填充方式为PKCS1v15
    # 指定hash方式为sha256
    signature = private_key.sign(
        data,
        padding.PKCS1v15(),
        hashes.SHA1()
    )

    # 将签名数据写入结果文件中
    signature_file = open(signature_file_name, 'wb')
    signature_file.write(signature)
    signature_file.close()

    # 返回签名数据
    return signature


if __name__ == '__main__':
    # 指定数据文件
    data_file = r'06131832-update.exe'
    # 指定签名结果文件
    signature_file = r'signature.bin'
    # 指定签名的私钥
    private_key_file = r'key-20220609-174338.pem'

    # 签名并返回签名结果
    signature = sign(data_file, signature_file, private_key_file)
    # 打印签名数据
    [print('%02x' % x, end='') for x in signature]


    """5971 07699aecedf18186b37232a00d622026fa6d431a23a79ba6cbed8779e21d9963558d798002999cdc25d00067eb9ff201580d767b755bc175fd168d28a374bebcd71020cec7879f62c61b0d228e1dae90aee3d69be71ee46eb6a06811785bca3e36984518bd3f32faf0368b637dc67451cb079034dc080344ec665fe2f4a9b55c6d1c34c9ce2b55fc2eebb0902a018d7bbae2754a21a71da7b3c1bc4b00316b2815b085ce8f6d8bf855e84e42139e1dfb78c8f578beed17f4b085920acc6e0d88cd7bc5768dfbb14be035bc364e23736a4a51097839233ce5ef7a4c49fcb0f6ef2bb27c2f8d6052adebe5385500d76f0f473758cd37d18309a424a6a04498a2b9e830e7ee3d4b98fc1a32abd36e273ac7bef16798dd2af6c38a2ade09cca43bf9aaae889f7f0fc630c919bb27623fd95ade66a5d54beea78521d65843dbb283443fc1ba5483179c56d658c2761f86f2e5883e5e0d60fb1505af5a19df758f76866aa7e9a3dc47ccd844ef28960aa869df84f1bf7bb61c7cbb64e5c30f77768f0b3f7b287bd9f736c4bbc82774ecf3eea80813b214d12292f31d5a06c17001fe44a20b3be025b6140d6c4481b063fc7d90496672d3482bb7ba28e16fc76349f6028b05168768622066628c50cc1e66ea6db875b77beff4453d968ff4cdd74e48989cff9e4dc04e1d96fe1b1c3073d6945730c436c07873605004"""

