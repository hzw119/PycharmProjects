
import requests
if __name__ == "__main__":
    request_url = 'https://www.sogou.com/web?'
    kw = input("Enter keywords")
    pram = {
        'query':kw
    }
    headers = {
        'User-Agent':'Mozilla / 5.0(Windows NT 6.1; Win64; x64) AppleWebKit / 537.36(KHTML, like Gecko) Chrome / 89.0.4389.114 Safari / 537.36'
    }
    response = requests.get(url=request_url,params=pram,headers=headers)
    page_text = response.text
    fileName = kw + '.html'
    with open(fileName,'w',encoding='UTF-8')as fp:
        fp.write(page_text)
    print(fileName+"保存成功")



