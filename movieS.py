# coding = utf-8
import urllib
import urllib.request
import re
import os
from bs4 import BeautifulSoup
s = '喜剧'
#文件保存目录
saveUrl = 'D:\\share'
#对中文进行处理不可统一处理 分开处理后拼接
s = urllib.parse.quote(s)
url = 'https://movie.douban.com/tag/'+s+'?start=0&type=T'
data = urllib.request.urlopen(url).read()
data = data.decode('utf-8')
bs = BeautifulSoup(data)
#得到标签共xx页
bs.find('span',class_='thispage')
num = bs.find('span',class_='thispage')['data-total-page']
#得到每个电影的容器
trs = bs.find_all('tr',class_='item')
for tr in trs:
    #得到图片url
    ima = tr.find('img')
    picSrc = ima['src']
    #得到影片名字
    movieName = tr.find('div').find('a').find('span').string
    #拼接保存目录与影片名字得到目录
    dirname = os.path.join(saveUrl,movieName)
    #对目录中的空格和特殊字符进行处理
    spname = dirname.split()
    dirname = ''.join([x for x in spname])
    #去除/否则多以及目录
    dirname = dirname.replace('/','')
    #创建文件夹
    if not os.path.exists(dirname):
            print(dirname)
            os.makedirs(dirname)
    #保存文件 二进制写打开方式
    with open(dirname+'/ss.jpg','wb') as f:
        data = urllib.request.urlopen(picSrc).read()
        f.write(data)
        

