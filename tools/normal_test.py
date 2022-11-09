import requests
from gevent import monkey
# monkey.patch_all(ssl = False)

STATIC_GENE_IP = ["192.168.122.1:34276"]
GENE_DETECT_URL = "/gene?timeout=120"
FAMILY_URL = "/analysis/familyjudge/?timeout=120"
FDFS_URL = "http://192.168.122.207/{}"
IocLoginAPI = "/user/newlogin/"
# IocDataAPI = "/api/checkmd5/?md5=%s&token=%s"
API_CHEEK = "checkmd5"
API_DETECT = "md5_detection_view"
API_BEHAVIOR = "md5_behavior_view"
API_DETAIL = "md5_detail_view"
IocIP = "https://taishi.roarpanda.com:9300"
WaitTime = 60
IocUser = "rongpan"
IocPassword = "eae6b57da0c885e923ccbf13e5d1c1dd6ff7aa358724ae8984bf0df47e00bb74"
IocLoginData = {"username": IocUser,
                "password": IocPassword}
IocMethod = "ioc"
static_docker_image_1 = "roarpanda/gene_engine:v3.1.1"
static_docker_image_2 = "ana-gene:v1.1.0"


def get_token():
    s = requests.session()
    url = IocIP + IocLoginAPI
    try:
        res = s.post(url, data=IocLoginData)
        print(url)
        token = res.json().get("token", "-1")
    except Exception as e:
        s.close()
        print("token::::::::", e)
        return None, "-1"
    print('-------token--------', token, '=--------------tokmen-----')
    return s, token

get_token()

def get_api(md5, api):
    try:
        session, token = get_token()
        print(token)
        url = IocIP + '/api/%s/?md5=%s&token=%s' % (api, md5, token)
        result = session.get(url, timeout=20).json()
        # TODO 做个判断 状态码
        print("get_api:::::::::::::::::", result)
        return result
    except Exception as e:
        print(e)
        return None


def get_detail(md5):
    result = get_api(md5, API_DETAIL)
    print("get_detail:::::::::::::::::", result)

    # print(result)
    if not result:
        return None
    if 'status' in list(result[0].keys()) and result[0]['status'] == '0':
        return None
    return result[0]

# print("aaa")
# get_detail("833E330440590DD19AB9E7456783281A")

