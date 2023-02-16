import urllib.request
import lxml.etree
import random
import requests

proxies_pool=[
    {'http':'202.109.157.61:9000'},
    {'http':'222.74.73.202:42055'},
    {'http':'202.109.157.60:9000'},
    {'http':'27.42.168.46:55481'},
    {'http':'182.139.111.149:9000'}
]
proxies=random.choice(proxies_pool)
mainurl='https://vidhub.top/voddetail/159655.html'
headers={
    'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Mobile Safari/537.36 Edg/108.0.1462.76'
}

request=urllib.request.Request(url=mainurl,headers=headers)
handle=urllib.request.ProxyHandler(proxies=proxies)
opener=urllib.request.build_opener(handle)
response=opener.open(request)
content=response.read().decode('utf-8')

tree=lxml.etree.HTML(content)
link=tree.xpath('//div[@class="scroll-content"]/a/@href')
name=tree.xpath('//div[@class="scroll-content"]//span/text()')

baseurl='https://vidhub.top'
for i in range(len(link)):
    vlink=link[i]
    vname=name[i]
    vurl=baseurl+vlink
    
urllist=[]
for i in range(1,3):
    if i == 1:
        for j in range(1,26):
            url='https://vidhub.top/vodplay/159655-1-'+str(j)+'.html'
            urllist.append(url)
    elif i == 2:
        for n in range(1,28):
            url='https://vidhub.top/vodplay/159655-2-'+str(n)+'.html'     
            urllist.append(url)      

for x in range(len(urllist)):
    new_url=urllist[x]

    resp=requests.get(url=new_url)
    #resp.encoding='utf-8'
    con=resp.content
    
    with open('E:\\素材\\素材\\进击的巨人\\'+vname+'.mp4','wb') as f:
        f.write(con)
        print(vname+':下载中')