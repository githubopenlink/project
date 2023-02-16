import requests
import lxml.etree

wyurl='https://www.qianyege.com/54/54075/'
headers={'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 Edg/108.0.1462.76'}

response=requests.get(url=wyurl,headers=headers,timeout=1)
print(response.status_code)
response.encoding='gbk'
content=response.text

tree=lxml.etree.HTML(content)
name=tree.xpath('//div[@id="list"]//dd/a/text()')
link=tree.xpath('//div[@id="list"]//dd/a/@href')

baseurl='https://www.qianyege.com'
for i in range(len(name)):
    txtname=name[i]
    txtlink=link[i]
    print(len(name))
    resp=requests.get(baseurl+link[i],headers=headers,timeout=1)
    resp.encoding='gbk'
    html=resp.text
    
    tr=lxml.etree.HTML(html)
    txtlist=tr.xpath('//*[@id="content"]/text()')
    txtstr=''.join(txtlist)

    with open('E:\\素材\\素材\\剑道第一仙\\'+txtname+'.txt','w',encoding='utf-8') as f:
        f.write(txtstr)
        print(txtname+':下载中')