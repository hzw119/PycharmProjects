import requests

if __name__ == '__main__':
    pic_url = 'http://img1.baidu.com/it/u=125354275,674293863&fm=26&fmt=auto&gp=0.jpg'
    pic_data = requests.get(url=pic_url).content
    with open('./watermelon.jpg','wb')as fp:
        fp.write(pic_data)
    print('over!!')