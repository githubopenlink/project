import requests
import random
import lxml.etree
import time
import os

url='https://www.mhua5.com/comic-jinpingmei.html'
headers={'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Mobile Safari/537.36 Edg/108.0.1462.76'}
proxies_pool=[
    {'http':'202.109.157.61:9000'},
    {'http':'222.74.73.202:42055'},
    {'http':'202.109.157.60:9000'},
    {'http':'27.42.168.46:55481'},
    {'http':'182.139.111.149:9000'},
    {'http':'121.13.252.62:41564'},
    {'http':'112.14.47.6:52024'},
    {'http':'61.216.185.88:60808'},
    {'http':'183.236.232.160:8080'},
    {'http':'123.169.39.212:9999'},
    {'http':'112.14.47.6:52024'}
]
proxies=random.choice(proxies_pool)

#获取每一章节的url
res=requests.get(
    url=url,
    headers=headers,
    #proxies=proxies,
    #timeout=3
)
#print(res.status_code)
res.encoding=res.apparent_encoding
con=res.text
#print(con)

tr=lxml.etree.HTML(con)
piclink=tr.xpath('//ul[@class="clearfix"]//a/@href')
picname=tr.xpath('//ul[@class="clearfix"]//a/text()')
#print(piclink)
#print(picname)

baseurl='https://www.mhua5.com'
for i in range(len(picname)):
    link=piclink[i]
    name=picname[i]
    newlink=baseurl+link
    #print('{}:{}'.format(newlink,name))

    os.makedirs('E:\\素材\\素材\\金瓶梅\\'+ str(name))

    #获取每一章节里面的每一张图片的url
    cont=requests.get(
        url=newlink,
        headers=headers,
        #proxies=proxies,
        #timeout=3
    ).text

    tr=lxml.etree.HTML(cont)
    url_list=tr.xpath('//ul[@class="comic-list"]//img/@src')
    #print(url_list)

    for j in range(len(url_list)):
        url_lists=url_list[j]
        #print(url_lists)
        #print(len(url_lists))
        
        conts=requests.get(
            url=url_lists,
            headers=headers,
            #proxies=proxies,
            #timeout=3
        ).content


        # 1 怎么解决漫画内容放在不同的章节文件夹中
        # 2 怎么解决其中个别url请求错误的情况下继续其他url的请求

        with open('E:/素材/素材/金瓶梅/'+str(name)+'/'+str(j+1)+'.jpg','ab') as f:
            f.write(conts) 
            time.sleep(1)
            print('下载成功') 
             