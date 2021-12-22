import pymysql

def download_url(config):
    data_config = config
    if data_config["type"] == "mysql":
        conn = pymysql.connect(**data_config["config"])
        cursor = conn.cursor()
        sql = 'select name , substring_index(substring_index(download_info, ":", -1),"//",-1)as url from res_apkinfos order by page_index'
        cursor.execute(sql)
        list = cursor.fetchall()
        conn.commit()
        cursor.close()
        conn.close()
        return  list

