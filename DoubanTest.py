import json

import requests

if __name__ == '__main__':
    headers = {
        'User-Agent': 'Mozilla / 5.0(Windows NT 6.1; Win64; x64) AppleWebKit / 537.36(KHTML, like Gecko) Chrome / 89.0.4389.114 Safari / 537.36'
    }
    pram = {
        'type': '13',
        'interval_id': '100:90',
        'action': '',
        'start': '0',
        'limit': '20',
    }
    page_url = 'https://movie.douban.com/j/chart/top_list'
    response = requests.get(url=page_url,params=pram,headers=headers)

    #保存为text文件
    # page_text = response.text
    # with open('DoubanText.txt','w',encoding='UTF-8')as fp:
    #     fp.write(page_text)
    # print("text已保存")

    #保存为json文件
    list_data = response.json()
    fp = open('./DoubanList.json','w',encoding="UTF-8")
    json.dump(list_data,fp=fp,ensure_ascii=False)

    print("保存成功")
