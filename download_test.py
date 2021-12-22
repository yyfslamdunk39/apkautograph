import time

import pandas as pd
import requests
from download import download_url
import random

DATABASE_CONFIG={
    "type":"mysql",
    "config":{
        "host":"192.168.92.34",
        "port":3306,
        "user":"zttest",
        "password":"ztgame123",
        "db":"xt_phone_ztgame_original",
        "charset":"utf8"
    }
}

useragent_pool = [
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/14.0.835.163 Safari/535.1",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11",
    "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:6.0) Gecko/20100101 Firefox/6.0",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv:2.0.1) Gecko/20100101 Firefox/4.0.1",
    "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50",
    "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; 360SE)",
    "Opera/9.80 (Windows NT 6.1; U; en) Presto/2.8.131 Version/11.11",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; SE 2.X MetaSr 1.0; SE 2.X MetaSr 1.0; .NET CLR 2.0.50727; SE 2.X MetaSr 1.0)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; The World)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Maxthon 2.0)"
]



list = download_url(DATABASE_CONFIG)
"list = list(tuple_url)"
df = pd.DataFrame(list, columns=["name", "url"])
print (df)
wandoujia = "wandoujia"
vivo = "vivo"
for i in range(len(df)):
        if wandoujia in df.at[i, 'url'] or vivo in df.at[i, 'url']:
            df.at[i, 'url'] = df.at[i, 'url'].replace("'}", "")
            a = "http://"
            df.at[i, 'url'] = a + df.at[i, 'url']
            print("Downloading file:%s" % df.at[i, 'name'])
            print("Downloading file:%s" % df.at[i, 'url'])
            useragent = random.choice(useragent_pool)
            hd = {'user-agent': useragent}
            print(hd)
            r = requests.get(df.at[i, 'url'], stream=True, headers=hd)
            # download started
            with open(df.at[i, 'name'] + ".apk", 'wb') as f:
                for chunk in r.iter_content(chunk_size=10240 * 2048):
                    if chunk:
                        f.write(chunk)
                        print("chunk")
            print("%s downloaded!\n" % df.at[i, 'name'])
            time.sleep(60)
        else:
            print("false")

print('download over')