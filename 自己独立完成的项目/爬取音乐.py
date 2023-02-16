import requests
import lxml.etree
import urllib.request

'''爬取九酷音乐'''

url='https://www.9ku.com/music/t_w_hits.htm'
res=requests.get(url=url,timeout=1)
res.encoding='utf-8'
con=res.text

tr=lxml.etree.HTML(con)
name=tr.xpath('//div[@class="songList clearfix"]//li/a/text()')
link=tr.xpath('//div[@class="songList clearfix"]//li/a/@href')

for i in range(len(name)):
    newname=name[i]
    newlink=link[i]
    newlinks='https://www.9ku.com'+newlink

    urllib.request.urlretrieve(url=newlinks,filename='E:/素材/素材/音乐/'+newname+'.mp3')
    print(newname+':下载中')