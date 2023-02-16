import requests
import random
import lxml.etree as le
import xlwt

proxies_pool=[
    {'http':'202.109.157.61:9000'},
    {'http':'222.74.73.202:42055'},
    {'http':'202.109.157.60:9000'},
    {'http':'27.42.168.46:55481'},
    {'http':'182.139.111.149:9000'}
]
proxies=random.choice(proxies_pool)

headers={
    'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Mobile Safari/537.36 Edg/108.0.1462.76'
}

#url='https://m.ke.com/wh/loupan/p_whesscblhhv/'

url='https://m.ke.com/wh/loupan/'
resps=requests.get(url=url,headers=headers,proxies=proxies)
print(resps.status_code)
resps.encoding=resps.apparent_encoding
cont=resps.text

tr=le.HTML(cont)
page_link=tr.xpath('//div[@class="shell-resblock-card"]/a/@href')
#print(page_link)

title_data=[]
advantage_data=[]
price_data=[]
size_s_data=[]
type_s_data=[]
structure_data=[]
address_data=[]

for x in range(len(page_link)):
    link=page_link[x]
    new_link='https://m.ke.com'+link
    #print(new_link)
    #print(len(page_link))

    resp=requests.get(url=new_link,headers=headers,proxies=proxies)
    #print(resp.status_code)
    resp.encoding=resp.apparent_encoding
    con=resp.text

    tr=le.HTML(con)
    title=tr.xpath('//div[@class="title-wrapper resblock-name-line"]/h1/text()')
    advantage=tr.xpath('//div[@class="tag-wrapper"]/span/text()')
    price=tr.xpath('//*[@class="price-value item"]/text()')
    size_s=tr.xpath('//div[@class="address-value item"]/text()')[0]
    type_s=tr.xpath('//div[@class="address-value item"]/text()')[1]
    structure=tr.xpath('//div[@class="address-value item"]/text()')[2]
    address=tr.xpath('//div[@class="address-open-date"]/a/text()')
    
    title_data.append(title)
    advantage_data.append(advantage)
    price_data.append(price)
    size_s_data.append(size_s)
    type_s_data.append(type_s)
    structure_data.append(structure)
    address_data.append(address)

#print(advantage_data)
    
book=xlwt.Workbook(encoding='utf-8',style_compression=0)
sheet=book.add_sheet('武汉新房信息表',cell_overwrite_ok=True)
col=['名称','优势','均价','面积','户型','结构','地址']
  
#写入每一列
for i in range(7):
    sheet.write(0,i,col[i])

#写入每一行
for n in range(len(title_data)):
    sheet.write(n+1,0,title_data[n]) 
    sheet.write(n+1,1,advantage_data[n]) 
    sheet.write(n+1,2,price_data[n]) 
    sheet.write(n+1,3,size_s_data[n]) 
    sheet.write(n+1,4,type_s_data[n]) 
    sheet.write(n+1,5,structure_data[n]) 
    sheet.write(n+1,6,address_data[n]) 

book.save('E:\素材\素材\武汉新房信息表.xls')

print('save end')