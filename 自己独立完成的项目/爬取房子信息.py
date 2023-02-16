import urllib.request
import random
import lxml.etree
import xlwt

proxies_pool=[
    {'http':'202.109.157.61:9000'},
    {'http':'222.74.73.202:42055'},
    {'http':'202.109.157.60:9000'},
    {'http':'27.42.168.46:55481'},
    {'http':'182.139.111.149:9000'}
]
proxies=random.choice(proxies_pool)
url='https://m.ke.com/wh/loupan/dongxihu'
headers={
    'Host': 'm.ke.com',
    'Referer': 'https://wx.fang.ke.com/',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Mobile Safari/537.36 Edg/108.0.1462.76'
}

request=urllib.request.Request(url=url,headers=headers)
handle=urllib.request.ProxyHandler(proxies=proxies)
opener=urllib.request.build_opener(handle)
response=opener.open(request)
content=response.read().decode('utf-8')

tree=lxml.etree.HTML(content)
name=tree.xpath('//div[@class="description"]//span/text()')
alt=tree.xpath('//div[@class="location"]//span/text()')
price=tree.xpath('//div[@class="price"]//span/text()')
tags=tree.xpath('//div[@class="tags"]//text()')

print(type(alt))
print(type(name))
print(type(price))
print(type(tags))

book=xlwt.Workbook(encoding='utf-8',style_compression=0)
sheet=book.add_sheet('武汉新房信息表',cell_overwrite_ok=True)
col=('小区名','属性','优势','价格')

for i in range(4):
    sheet.write(0,i,col[i])

for i in range(4):
    data=name[i]
    for j in range(len(name)):
        sheet.write(i+1,j,data[j])
book.save('E:\素材\素材\武汉新房信息表.xls')