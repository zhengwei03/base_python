# coding=utf-8
# import pymysql
import pandas as pd


class EventImport(object):

    def __init__(self, excel_path):
        # self.conn = pymysql.Connect(host="127.0.0.1", user="root", password="user@1346", database="test",
        #                            port=3306, charset='utf8')
        # self.conn = pymysql.Connect(host="127.0.0.1", user="apt_user", password="apt_user123", database="apt",
        #                             port=3306, charset='utf8')
        # self.cursor = self.conn.cursor()
        # self.insert_event_sql = "insert into apt_event (title, event_type, summary, text_date, image_src, organization_name, source_url, target, annx, destination_country, source_country) values (%s,99,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        self.excel_path = excel_path
        self.static_path = {"img": "/static/img/cover_img/", "pdf": "/static/files/"}
        self.ioc_type = {0: "MD5", 1: "SHA1", 2: "SHA256", 3: "IP", 4: "Domain", 5: "URL", 6: "C&C-IP", 7: "C&C-Domain",
                         8: "C&C-URL", 9: "Email", 10: "RC4 Key", 11: "XOR Key", 12: "CAST-128 Key", 13: "RSA key",
                         14: "PATH"}

    def read_data(self, base_rowid, max_columnid, sheet_name, exclude_columnid):
        data_list = []
        df = pd.read_excel(self.excel_path, sheet_name=sheet_name)
        max_row_id = df.shape[0]
        while base_rowid < max_row_id:
            row_list = []
            for column_id in range(max_columnid + 1):
                if column_id in exclude_columnid:
                    continue
                row_data = df.iloc[base_rowid, column_id]
                row_list.append(row_data)
            base_rowid += 1
            data_list.append(row_list)
        return data_list

    def handle_base_info(self, sheet_name="基本信息"):
        data_list = self.read_data(0, 14, sheet_name, exclude_columnid=[0, 4, 6, 14])
        for event in data_list:
            title = event[0]
            found_time = self.handle_value(event[1])
            apt_name = event[2]
            src_country = event[3]
            if apt_name == "unknown":
                continue
            # apt_id = self.handle_apt_name(apt_name, src_country)
            target_country = event[4]
            target = event[5]
            summary = event[6]
            source_url = event[7]
            organization_name = event[8]
            print(title, found_time, apt_name, src_country, target_country, target, summary, source_url, organization_name )
            # img_filename = self.handle_file_path("img", event[9])
            # pdf_filename = self.handle_file_path("pdf", event[10])
            # res = self.cursor.execute(self.insert_event_sql, (
            # title, summary, str(found_time), img_filename, organization_name, source_url, target, pdf_filename,
            # target_country, src_country))
            # event_id = self.cursor.lastrowid
            # self.cursor.execute("insert into apt_event_relation(event_id, apt_id) values(%s,%s)", (event_id, apt_id))
            # self.conn.commit()

    def handle_ioc_info(self, sheet_name="IOC信息"):
        data_list = self.read_data(1, 17, sheet_name, exclude_columnid=[0])
        for ioc in data_list:
            if not pd.isna(ioc[0]):
                event_title = ioc[0]
                apt_name = self.handle_value(ioc[1])
                if not apt_name:
                    continue
                print("event_title:::::::::::", event_title)
                print("apt_name:::::::::::", event_title)
                # event_result = self.cursor.fetchone()
                # if not event_result:
                #     continue
                # event_id = event_result[0]
                # self.cursor.execute("select id from apt_info where apt_name=%s", apt_name)
                # apt_result = self.cursor.fetchone()
                # if not apt_result:
                #     continue
                # apt_id = apt_result[0]
            for index, row_info in enumerate(ioc[2:]):
                if not pd.isna(row_info):
                    type = self.ioc_type.get(index)
                    print("row::::::::::::::::::::", type, row_info)
            # self.conn.commit()

    def handle_file_path(self, static_type, col_data):
        file_path = ""
        if not pd.isna(col_data):
            file_path = self.static_path.get(static_type) + col_data
        return file_path

    def handle_apt_name(self, apt_name, src_country):
        self.cursor.execute(
            "select id, apt_id, organization_apt_name, main_name from apt_another_name where organization_apt_name='%s'" % apt_name)
        result = self.cursor.fetchone()
        self.cursor.execute("select * from apt_info where apt_name='%s'" % apt_name)
        result2 = self.cursor.fetchone()
        if result:
            apt_id = result[1]
            if apt_id == 10000:
                if not result2:
                    self.cursor.execute("insert into apt_info (apt_name, country) values (%s, %s)",
                                        (apt_name, src_country))
                    print("APTname：", apt_name, "现在的country::", src_country, '：：：：直接插入')
                    apt_id = self.cursor.lastrowid
                else:
                    apt_id = result2[0]
                    if result2[5] == "unknown":
                        self.cursor.execute("update apt_info set country=%s where id=%s", (src_country, apt_id))
                        self.conn.commit()
                        print("APTname：", apt_name, "之前的country::::", result2[5], "现在的country::", src_country,
                              '：：：：已修改')
                    elif result2[5] != "unknown" and apt_name != "unknown":
                        self.cursor.execute("update apt_info set country=%s where id=%s", (src_country, apt_id))
                        self.conn.commit()
                        print("APTname：", apt_name, "之前的country::::", result2[5], "现在的country::", src_countryi,
                              '：：：：已修改')
                    elif result2[5] != "unknown" and apt_name == "unknown":
                        # self.cursor.execute("update apt_info set country=%s where id=%s", (apt_id, src_country))
                        # self.conn.commit()
                        print("APTname：", apt_name, "之前的country::::", result2[5], "现在的country::", src_country,
                              '：：：：未修改')
                    else:
                        print("APTname：", apt_name, "之前的country::::", result2[5], "现在的country::", src_country,
                              '：：：：未修改')

                self.cursor.execute("update apt_another_name set apt_id=%s where id=%s", (apt_id, result[0]))
                self.conn.commit()
            else:
                if result2:
                    if result2[5] == "unknown":
                        self.cursor.execute("update apt_info set country=%s where id=%s", (src_country, apt_id))
                        self.conn.commit()
                        print("APTname：", apt_name, "之前的country::::", result2[5], "现在的country::", src_country,
                              '：：：：已修改')

                    elif result2[5] != "unknown" and apt_name != "unknown":
                        self.cursor.execute("update apt_info set country=%s where id=%s", (src_country, apt_id))
                        self.conn.commit()
                        print("APTname：", apt_name, "之前的country::::", result2[5], "现在的country::", src_country,
                              '：：：：已修改')
                    elif result2[5] != "unknown" and apt_name == "unknown":
                        # self.cursor.execute("update apt_info set country=%s where id=%s", (apt_id, src_country))
                        # self.conn.commit()
                        print("APTname：", apt_name, "之前的country::::", result2[5], "现在的country::", src_country,
                              '：：：：未修改')
                    else:
                        print("APTname：", apt_name, "之前的country::::", result2[5], "现在的country::", src_country,
                              '：：：：未修改')
                    self.cursor.execute("update apt_another_name set apt_id=%s where id=%s", (apt_id, result[0]))
                    self.conn.commit()
                else:
                    self.cursor.execute("insert into apt_info (apt_name, country) values (%s, %s)",
                                        (apt_name, src_country))
                    print("APTname：", apt_name, "现在的country::", src_country, '：：：：直接插入')
                    apt_id = self.cursor.lastrowid


        else:
            if not result2:
                print(apt_name, "::::::正常APT插入：：：：：：")
                self.cursor.execute("insert into apt_info (apt_name, country) values (%s, %s)", (apt_name, src_country))
                apt_id = self.cursor.lastrowid
                self.cursor.execute(
                    "insert into apt_another_name (apt_id, organization_apt_name, main_name) values (%s,%s,%s)",
                    (apt_id, apt_name, apt_name))
                self.conn.commit()
            else:
                print(apt_name, "::::::::更新apt_info 数据：：：：：")
                apt_id = result2[0]
                print(result2[5], '--------------------')
                if result2[5] == "unknown":
                    self.cursor.execute("update apt_info set country=%s where id=%s", (src_country, apt_id))
                    self.conn.commit()
                    print("APTname：", apt_name, "之前的country::::", result2[5], "现在的country::", src_country, '：：：：已修改')
                elif result2[5] != "unknown" and apt_name != "unknown":
                    self.cursor.execute("update apt_info set country=%s where id=%s", (src_country, apt_id))
                    self.conn.commit()
                    print("APTname：", apt_name, "之前的country::::", result2[5], "现在的country::", src_country, '：：：：已修改')
                elif result2[5] != "unknown" and apt_name == "unknown":
                    # self.cursor.execute("update apt_info set country=%s where id=%s", (apt_id, src_country))
                    # self.conn.commit()
                    print("APTname：", apt_name, "之前的country::::", result2[5], "现在的country::", src_country, '：：：：未修改')

                else:
                    print("APTname：", apt_name, "之前的country::::", result2[5], "现在的country::", src_country, '：：：：未修改')

        return apt_id

    def handle_value(self, value):
        if pd.isna(value):
            value = None
        elif value == "unknown":
            value = ""
        return value


if __name__ == '__main__':
    for i in range(1, 6):
        event_import = EventImport(excel_path="./apt_{}.xlsx".format(str(i)))
        event_import.handle_base_info()
    # event_import.handle_ioc_info()
    # conn = pymysql.Connect(host="127.0.0.1", user="apt_user", password="apt_user123", database="apt",
    #                                port=3306, charset='utf8')
    # cursor = conn.cursor()
#
# cursor.execute("select * from apt_info where apt_name='%s'"%"APT37")
# result = cursor.fetchone()
# print(result)
#     df = pd.read_excel(r"E:\python_test\apt_demo.xlsx", sheet_name="IOC信息")


