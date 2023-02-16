import requests
import lxml.etree

url='https://c.runoob.com/front-end/854/'
resp=requests.get(url=url)
resp.encoding=resp.apparent_encoding
con=resp.text

tr=lxml.etree.HTML(con)
txt=tr.xpath('//div[@class="card-body"]//text()')
#print(txt,end='\n')
txtlist=[x.strip() for x in txt if x.strip()]
txtstr=''.join(txtlist)
#print(txtstr,end='\n')
#怎么才能把爬取出的字符串换行,达到网页中显示的效果
with open(r'E:\素材\素材\常用正则表达式.txt','w',encoding='utf-8') as f:
    f.write(txtstr)
    f.write('\n\n')
    print('保存成功')