# @author :Jiaqi Ding
# @time   :2018/11/12 20:19
# @file   :FilmDownload.py
# @IDE    :PyCharm

import requests
from bs4 import BeautifulSoup


def get_page(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 '
                      '(KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',
        'Host':'movie.douban.com'
            }
    r = requests.get(url,headers = headers)
    return r

def get_pictures_url(url,number):
    r = get_page(url)
    Number = 0 + number * 25
    if r.status_code == 200:
        soup = BeautifulSoup(r.content)
        pictures_url = soup.find_all('div',class_="item")
        for pictures in pictures_url:
            Number += 1
            try:

                with open('top250.txt','a') as f:
                    print('正在存储top第{}'.format(Number))
                    f.write('TOP排名：' + str(Number) + '\n')
                    f.write('源网页：' + pictures.find('a',class_="")['href'] + '\n')
                    f.write('海报地址：' + pictures.find('img', class_="")['src'] + '\n')

                    f.write('片名：' + pictures.find('img', class_="")['alt'] + '\n')
                    f.write(pictures.find('div', class_="bd").p.get_text()[29:40] + '\n')
                    f.write('一句话介绍：' + str(pictures.find('span', class_='inq').string) + '\n\n\n')
                    f.flush()
                    print("%s已存储" % pictures.find('img', class_="")['alt'])


            except:
                print('Fail download')

if __name__ == "__main__":
    for i in range(11):
        get_pictures_url("https://movie.douban.com/top250?start={}&filter=".format(i * 25), i)
    print('-------------------------------------')
    print('数据保存完毕')