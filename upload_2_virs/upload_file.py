import datetime
import os
import pymysql
import paramiko
from pymysql.cursors import DictCursor

def upload_file_demo():
    # 创建SSHClient实例对象
    mysql_demo = MysqlUtil()
    ssh = paramiko.SSHClient()
    # 调用方法，标识没有远程机器的公钥，允许访问
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    # 连接远程机器 地址端口用户名密码
    ssh.connect("'192.168.1.110'", 22, "xiaoming", "123456")
    ssh.exec_command("rm -rf /home/ubuntu/test/*")
    sftp = ssh.open_sftp()
    sftp.put("./Similar.zip", "/home/ubuntu/test/Similar.zip")
    msg1, msg2, msg3 = ssh.exec_command("unzip -P 'qwertyuiopl,' /home/ubuntu/test/Similar.zip  -d /home/ubuntu/test/")
    msg1, msg2, msg3 = ssh.exec_command("ls -r /home/ubuntu/test/Similar |awk '{print i$0}' i=`pwd`'/'")
    path_list = str(msg2.read().decode()).split("\n")
    mysql_demo.delete_table()
    for path in path_list:
        if path:
            model_name = path.split("/")[-1]
            mysql_demo.insert_mysql(model_name, path)
    ssh.close()



class MysqlUtil(object):
    """Mysql operating mode"""
    def __init__(self):
        """Mysql connection info"""
        self.db_info = {
            "db_host": "192.168.1.110",
            "db_user": "systemserver",
            "db_password": "systemserver123",
            "db_port": 3306,
            "db_name": "roar_panda",
            "db_charset": "utf8"
        }
        conn = None
        cur = None
        try:
            conn = pymysql.connect(host=self.db_info["db_host"], user=self.db_info["db_user"],
                                   password=self.db_info["db_password"], port=self.db_info["db_port"],
                                   database=self.db_info["db_name"], charset=self.db_info["db_charset"])
            cur = conn.cursor()
        except Exception as e:
            print("The mysql connection is abnormal ::::: ", str(e))
            conn = None
            cur = None
        self.conn = conn
        self.cur = cur

    def delete_table(self):
        try:
            delete_sql = "truncate table deepAnalysis_familymodel"
            self.cur.execute(delete_sql)
        except Exception as e:
            return False

    def insert_mysql(self, model_name, model_path):

        try:
            now_time = datetime.datetime.now()
            insert_sql = """insert into deepAnalysis_familymodel(user_id, model_name, model_path, score, create_time) values('%s', '%s', '%s', '%s', '%s')"""% ('4', model_name, model_path, '10', now_time)
            print(insert_sql)
            a = self.cur.execute(insert_sql)
            if a:
                self.conn.commit()
        except Exception as e:
            print("insert")


if __name__ == '__main__':
    try:
        upload_file_demo()
    except Exception as e:
        print("模型升级失败")
    else:
        print("模型升级成功")