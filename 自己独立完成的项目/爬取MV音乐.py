import requests
import lxml.etree
import urllib.request

'''爬取超跑音乐网MV'''

for page in range(1,4):
    url='https://www.avimv.com/play/7_'+str(page)+'.html'
    headers={'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 Edg/108.0.1462.76'}
    resp=requests.get(url=url,headers=headers,timeout=1)
    resp.encoding='utf-8'
    con=resp.text

    tr=lxml.etree.HTML(con)
    video=tr.xpath('//div[@class="pic"]/a/@href')
    name=tr.xpath('//div[@class="name"]/a/text()')
    
    for i in range(len(name)):
        videos=video[i]
        names=name[i]
        newurl='https://www.avimv.com'+videos

        urllib.request.urlretrieve(url=newurl,filename='E:\\素材\\素材\\日韩音乐MV\\'+names+'.avi')
        print(names+':下载中')