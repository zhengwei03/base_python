# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-
import socket
import struct
# from rest_framework_jwt.settings import api_settings
import re

# jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
# jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER
# jwt_decode_handler = api_settings.JWT_DECODE_HANDLER
#
# from ...user.models import *
# from ...wrappers.utils import SystemLog
# from ...wrappers.return_msg import *
# from ...wrappers import path, status_code

# user_logger = SystemLog("SelfUser")


def ip_to_int(ip):
    nn = socket.ntohl(struct.unpack("I", socket.inet_aton(ip))[0])
    return nn


def int_to_ip(ip_int):
    mm = socket.inet_ntoa(struct.pack('I', socket.htonl(ip_int)))
    return mm

#
# def handle_token(request, group_id_list):
#     method = request.method
#     if method == "GET":
#         token = request.query_params.get("token")
#     elif method == "POST":
#         token = request.data.get("token")
#     if not token:
#         user_logger.error("lost token!!!!!")
#         return ParamsLostMsg, 0, 0
#     try:
#         payload = jwt_decode_handler(token)
#         user_id = payload.get('user_id')
#         user_group = UserGroup.objects.get(user_id=user_id)
#         group_id = user_group.group_id
#     except Exception as e:
#         user_logger.error(e)
#         return OperationErrorMsg, 0, 0
#     if group_id not in group_id_list:
#         return AuthLostOutMsg, 0, 0
#     return 1, user_id, group_id
#



def check_mobile(phone_number):
    if not phone_number:
        return False
    if not re.match("^1[3456789]\d{9}$", str(phone_number)):
        return False
    return True

print(check_mobile("18877788888"))


def check_username(user_name):
    if not user_name:
        return False
    if not re.match('^[a-zA-Z0-9][\w@\-]{5,16}$', str(user_name)):
        return False
    return True


def check_mail(mail):
    if not mail:
        return False
    if not re.match(r"^[a-z0-9][\w\.\-]*@[a-z0-9\-]+(\.[a-z]{2,5}){1,2}$", str(mail)):
        return False
    return True


import datetime
# from user.models import SelfReportSettings, SelfReportInfo
from django.db.models import Max

period_date = {"month": 31, "quarter": 92, "halfyear": 183}
#
# def check_report_status(setting_id):
#     '''将过期未发送的已生效定制化报告服务状态改成漏发'''
#     now_time = datetime.datetime.now()
#     days_time = 0
#     setting_obj = SelfReportSettings.objects.filter(id=setting_id)
#     if not setting_obj:
#         return
#     setting_obj = setting_obj[0]
#     if setting_obj.deadline < now_time:
#         setting_obj.settings_status = -1
#         setting_obj.save()
#     else:
#         report_obj = SelfReportInfo.objects.filter(self_report_id=setting_obj.id)
#         # if report_obj:
#         # report_obj = report_obj.aggregate(Max('report_times'))
#         # print(report_obj)
#         # now_times = int(report_obj[0].now_times) + 1
#         # now_times = int(report_obj.get("report_times__max"))
#         # period = int(period_date[setting_obj.period])
#         now_times = len(report_obj)
#         period = int(period_date[setting_obj.period])
#         cycle = int(setting_obj.cycle)
#         days = (period // cycle) * now_times
#         before_days = (period // cycle) * (now_times - 1)
#         back_days = (period // cycle) * (now_times + 1)
#         if now_times == setting_obj.report_all_times:
#             days = period
#         time = setting_obj.create_time + datetime.timedelta(days=days)
#         before_time = setting_obj.create_time + datetime.timedelta(days=before_days)
#         back_time = setting_obj.create_time + datetime.timedelta(days=back_days)
#         if before_time < now_time < time:
#             setting_obj.settings_status = "2"
#             setting_obj.save()
#         elif time < now_time < back_time:
#             setting_obj.settings_status = "1"
#             setting_obj.save()
#         elif back_time < now_time:
#             setting_obj.settings_status = "0"
#             setting_obj.save()
#
#
#
#
# import base64
# import Crypto.PublicKey.RSA
# import Crypto.Cipher.PKCS1_v1_5
# import Crypto.Random
# import Crypto.Signature.PKCS1_v1_5
# import Crypto.Hash
#
#
#
#
# # def rsaEncrypt(info):
# #     # 生成公钥、私钥
# #     # print(datetime.datetime.now())
# #     # (pubkey, privkey) = rsa.newkeys(2048)
# #     # print(privkey)
# #     info = bytes(info.encode('utf-8'))
# #     # print(info)
# #     with open("user/functions/public.pem", "rb") as f:
# #         pubkey = f.read()
# #     cipher_public = Crypto.Cipher.PKCS1_v1_5.new(Crypto.PublicKey.RSA.importKey(pubkey))
# #     cipher_text = cipher_public.encrypt(info)
# #     print(cipher_text, "===========================")
# #     return cipher_text
# #
# #
# # # rsa解密
# # def rsaDecrypt(info):
# #     # 私钥解密
# #     # if isinstance(info, bytes):
# #     info = base64.b64decode(info)
# #     with open("user/functions/private.pem", "rb") as f:
# #         private = f.read()
# #     cipher_private = Crypto.Cipher.PKCS1_v1_5.new(Crypto.PublicKey.RSA.importKey(private))
# #     text = cipher_private.decrypt(info, Crypto.Random.new().read)  # 使用私钥进行解密
# #     text = text.decode("utf-8")
# #     return text
#
#
# # rsa加密
# def rsaEncrypt(info):
#     # 生成公钥、私钥
#
#     info = bytes(info, encoding="utf-8")
#     length = len(info)
#     print("-------------------enodelenth-------------", length)
#
#     default_length = 245
#     with open("user/functions/public.pem", "rb") as f:
#         pubkey = f.read()
#     # print("公钥:\n%s\n私钥:\n:%s" % (pubkey, privkey))
#     # 明文编码格式
#     cipher_public = Crypto.Cipher.PKCS1_v1_5.new(Crypto.PublicKey.RSA.importKey(pubkey))
#     if length < default_length:
#         return base64.b64encode(cipher_public.encrypt(info))
#         # 需要分段
#     offset = 0
#     res = []
#     while length - offset > 0:
#         if length - offset > default_length:
#             res.append(cipher_public.encrypt(info[offset:offset + default_length]))
#         else:
#             res.append(cipher_public.encrypt(info[offset:]))
#         offset += default_length
#     byte_data = b''.join(res)
#     return byte_data.decode('utf-8')
#
# # rsa解密
# def rsaDecrypt(info):
#     # 私钥解密
#     info = base64.b64decode(info)
#     length = len(info)
#     print("-------------------decodelenth-------------", length)
#     default_length = 256
#     with open("user/functions/private.pem", "rb") as f:
#         private = f.read()
#         # private = Crypto.Cipher.PKCS1_v1_5.new(Crypto.PublicKey.RSA.importKey(private))
#     cipher_private = Crypto.Cipher.PKCS1_v1_5.new(Crypto.PublicKey.RSA.importKey(private))
#     if length < default_length:
#         text = cipher_private.decrypt(info, Crypto.Random.new().read)
#         return b''.join(text)
#     # 需要分段
#     offset = 0
#     res = []
#     while length - offset > 0:
#         if length - offset > default_length:
#             res.append(cipher_private.decrypt(info[offset:offset + default_length], Crypto.Random.new().read))
#         else:
#             res.append(cipher_private.decrypt(info[offset:], Crypto.Random.new().read))
#         offset += default_length
#     text = b''.join(res)
#     text = text.decode("utf-8")
#     return text
#
#
#
