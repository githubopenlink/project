import requests
from lxml import etree

'''爬取顶点小说网武神主宰'''

#获取源代码
url='https://www.ddyueshu.com/5_5034/'
headers={'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 Edg/108.0.1462.76'}
resp=requests.get(url=url,headers=headers,timeout=1)
resp.encoding='gbk'
content=resp.text

#解析
tree=etree.HTML(content)
txtname=tree.xpath('//div[@id="list"]//dd/a/text()')
txtlink=tree.xpath('//div[@id="list"]//dd/a/@href')

#拼接并获取各章节url
baseurl='https://www.ddyueshu.com'
for i in range(len(txtname)):
    new_txt_name=txtname[i]
    new_txt_link=txtlink[i]
    #newurl=baseurl+new_txt_link
    #print('{}:{}'.format(newurl,new_txt_name))
    
    #获取各章节的响应
    respose=requests.get(url=baseurl+txtlink[i],headers=headers)
    respose.encoding='gbk'
    html=respose.text
    
    #解析各章节响应文本
    tr=etree.HTML(html)
    con=tr.xpath('//*[@id="content"]/text()')
    #用list推导式去除文本中制表符和空格 制表符
    conlist=[x.strip() for x in con if x.strip()]
    #list转str
    constr=''.join(conlist)

    #下载保存文本
    with open('E:\\素材\\素材\\武神主宰\\'+new_txt_name+'.txt','w',encoding='utf-8') as f:
        f.write(constr)
    #跟踪下载进度
    if len(txtname) == len(txtname):
        print('下载完成')
    else:
        print(txtname[i]+':正在下载中')