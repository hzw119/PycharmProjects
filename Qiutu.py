import requests
import re
import os

if __name__ == '__main__':
    page_url = 'https://www.qiushibaike.com/imgrank/'
    headers = {
        'User-Agent': 'Mozilla / 5.0(Windows NT 6.1; Win64; x64) AppleWebKit / 537.36(KHTML, like Gecko) Chrome / 89.0.4389.114 Safari / 537.36'
    }
    #创建文件夹操作
    if not os.path.exists('./qiutuLib'):
        os.mkdir('./qiutuLib')
    #获取url所对应的源代码html数据
    page_text = requests.get(url=page_url,headers=headers).text

    #根据获取的源代码解析出图片的url地址
    #利用正则表达式，观察得到正则表达解析式，利用re.findall(待处理的爬取的源代码文本，正则化处理式子，re.S寻找单条结果)
    ex = '<div class="thumb">.*?<img src="(.*?) alt=.*?</div>'
    img_src_list = re.findall(ex,page_text,re.S)
    # print(img_src_list)
    #获取到图片的链接list后，进一步得到图片名，根据链接获取图片的content，再把图片存到定好的文件夹中
    for img_src in img_src_list:
        img_src = 'https:'+img_src
        print(img_src)
        img_content = requests.get(url=img_src,headers=headers).content
        img_name = img_src.split('/')[-1]
        # print(img_name) #打印文件名，没有问题
        #持久化存储 fp.write
        img_path = './qiutuLib/'+img_name
        print(img_path)
        # with open(img_path,'wb') as fp:
        #     fp.write(img_content)
        #     print(img_name+"下载成功!!!")






# <div class="thumb">
#
# <a href="/article/124202466" target="_blank">
# <img src="//pic.qiushibaike.com/system/pictures/12420/124202466/medium/NW4U7ZKSOWWTOZ33.jpg" alt="糗事#124202466" class="illustration" width="100%" height="auto">
# </a>
# </div>

# <div class="thumb">
#
# <a href="/article/124197930" target="_blank">
# <img src="//pic.qiushibaike.com/system/pictures/12419/124197930/medium/N6HLJXIBTEOBB0EA.jpg" alt="糗事#124197930" class="illustration" width="100%" height="auto">
# </a>
# </div>
