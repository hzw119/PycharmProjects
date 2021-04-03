import json

import requests
if __name__ == '__main__':
    headers = {
        'User-Agent': 'Mozilla / 5.0(Windows NT 6.1; Win64; x64) AppleWebKit / 537.36(KHTML, like Gecko) Chrome / 89.0.4389.114 Safari / 537.36'
    }
    page_url = 'http://scxk.nmpa.gov.cn:81/xk/itownet/portalAction.do?method=getXkzsList'
    idList = []

    for page in range(1,6):
        page = str(page)
        page_pram = {
            'on':'true',
            'page':page,
            'pageSize':'15',
            'productName':'',
            'conditionType':'1',
            'applyname':'',
            'applysn':'',
        }
        response = requests.post(page_url,page_pram)
        page_json = response.json()
    #获取到json数据后，分析组成元素，并获取ID


        for id in page_json["list"]:
            idList.append(id["ID"])

    # print(idList)
    AllJsons = []
    detail_url = 'http://scxk.nmpa.gov.cn:81/xk/itownet/portalAction.do?method=getXkzsById'
    for id in idList:
        data = {
            'id':id
        }
        detail_json = requests.post(url=detail_url,data=data,headers=headers).json()
        AllJsons.append(detail_json)
    print(AllJsons)

    fp = open('makeup_detailList.json','w',encoding='UTF-8')
    json.dump(AllJsons,fp=fp,ensure_ascii=False)





    # fp = open('Makeup.json','w',encoding='UTF-8')
    # json.dump(page_json,fp=fp,ensure_ascii=False)
    # print("success")