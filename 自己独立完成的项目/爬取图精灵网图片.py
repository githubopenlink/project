import requests
import random
import lxml.etree

'''爬取图精灵网图片'''

headers={'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Mobile Safari/537.36 Edg/108.0.1462.76'}
proxies_pool=[
    {'http':'202.109.157.61:9000'},
    {'http':'222.74.73.202:42055'},
    {'http':'202.109.157.60:9000'},
    {'http':'27.42.168.46:55481'},
    {'http':'182.139.111.149:9000'}
]
proxies=random.choice(proxies_pool)

for pg in range(2,51):
    url='https://616pic.com/png/'+str(pg)+'.html' 
    resp=requests.get(url=url,headers=headers,proxies=proxies)
    resp.encoding='utf-8'
    con=resp.text
    #print(con)
    tr=lxml.etree.HTML(con)
    img_url=tr.xpath('//a[@class="img img-ys"]//img/@data-original')
    img_name=tr.xpath('//a[@class="btitle"]/text()')
    for i in range(len(img_url)):
        img_urls=img_url[i]
        img_names=img_name[i]
        new_img_urls='https:'+img_urls
        #print(new_img_urls)
        resp=requests.get(url=new_img_urls,headers=headers,proxies=proxies)
        with open('E:\\素材\\素材\\各种素材\\'+img_names+'.jpg','wb') as f:
                f.write(resp.content)
                print('下载成功')