import json

import requests

if __name__ == '__main__':
    headers = {
        'User-Agent': 'Mozilla / 5.0(Windows NT 6.1; Win64; x64) AppleWebKit / 537.36(KHTML, like Gecko) Chrome / 89.0.4389.114 Safari / 537.36'
    }
    #好像post请求就直接保留url不动
    page_url = 'http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=keyword'
    kw = input("Enter keywords")
    pram = {
        'op':kw
    }
    page_pram = {
        'cname':'',
        'pid':'',
        'keyword': kw,
        'pageIndex': '1',
        'pageSize': '10',

    }
    response = requests.post(url=page_url,data=page_pram)
    page_json = response.json()
    fp = open('kfcList.json','w',encoding='UTF-8')
    json.dump(page_json,fp=fp,ensure_ascii=False)
    print("kfcjson已保存")