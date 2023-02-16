import lxml.etree
import urllib.request

url='http://c.biancheng.net/tkinter/project-case.html'
response=urllib.request.urlopen(url=url)
content=response.read().decode('utf-8')
tree=lxml.etree.HTML(content)
re1=tree.xpath('//div[@id="contents"]//a/text()')
re2=tree.xpath('//div[@id="contents"]//a/@href')

for i in range(len(re1)):
    name=re1[i]
    link=re2[i]
    new_url='http://c.biancheng.net'+link
    print(new_url,name)

'''后面怎么下载下来,因为网页中既有图片也有表格,还有文本'''