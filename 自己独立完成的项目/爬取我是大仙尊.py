import requests
import lxml.etree as le

headers={'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Mobile Safari/537.36 Edg/108.0.1462.76'}
for page in range(1,39):
    url='https://m2.ddyueshu.com/wapbook/2911-'+str(page)+'.html'
    #print(url)

    resp=requests.get(url=url,headers=headers)
    resp.encoding=resp.apparent_encoding
    con=resp.text
    #print(con)

    tr=le.HTML(con)
    chatpterlink=tr.xpath('//div[@class="book_last"]//a/@href')
    chatptername=tr.xpath('//div[@class="book_last"]//a/text()')
    #print(chatptername)

    for i in range(len(chatpterlink)):
        chatpterlinks=chatpterlink[i]
        chatpternames=chatptername[i]
        chatpter_url='https://m2.ddyueshu.com'+chatpterlinks
        #print(chatpter_url)

        resps=requests.get(url=chatpter_url,headers=headers)
        resps.encoding=resps.apparent_encoding
        cont=resps.text
        #print(cont)

        trs=le.HTML(cont)
        txt_content=trs.xpath('//div[@id="chaptercontent"]//text()')
        #print(txt_content)

        conlist=[x.strip() for x in txt_content if x.strip()]
        constr=''.join(conlist)
        #print(type(constr))

        with open('E:/素材/素材/我是大仙尊/'+chatpternames+'.txt','w',encoding='utf-8') as f:
            f.write(constr)
            print('{}:{}'.format(chatpternames,chatpter_url),':下载中')

print('save end')  