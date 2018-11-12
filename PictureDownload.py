# @author :Jiaqi Ding
# @time   :2018/11/13 0:06
# @file   :PictureDownload.py
# @IDE    :PyCharm

import requests
import urllib.request
from lxml import etree


def main(start):
    url = 'https://movie.douban.com/top250?start=' + str(start) + '&filter='
    data = requests.get(url)
    html = etree.HTML(data.text)
    res = html.xpath('//img/@src')
    for i in range(0, len(res)):
        urllib.request.urlretrieve(res[i],
                                   filename="./movie/" + str(start + i) + ".jpg")  # filename=(自己要存图片的目录)，后面加的是图片的命名
        print(str(start + i) + ".jpg")

if __name__ == '__main__':
    for i in range(10):
        main(start=i * 25)