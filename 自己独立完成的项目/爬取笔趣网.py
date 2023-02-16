import requests
import random
import lxml.etree

'''
爬取笔趣阁三体小说
1 获取三体每一页的URL
2 获取每个章节URL
3 爬取文本内容
'''

headers={
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'referer': 'https://www.biqiuge8.cc/',
    'sec-ch-ua': '"Not?A_Brand";v="8", "Chromium";v="108", "Microsoft Edge";v="108"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-site',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Mobile Safari/537.36 Edg/108.0.1462.76'
}
proxies_pool=[
    {'http':'202.109.157.61:9000'},
    {'http':'222.74.73.202:42055'},
    {'http':'202.109.157.60:9000'},
    {'http':'27.42.168.46:55481'},
    {'http':'182.139.111.149:9000'}
]
proxies=random.choice(proxies_pool)

#startpage=int(input('开始页面'))
#endpage=int(input('结束页面'))

urlpage=[]
for page in range(1,12):
    if page == 1:
        url='https://m.biqiuge8.cc/chapters_21506/'
        urlpage.append(url)
    else:
        url='https://m.biqiuge8.cc/chapters_21506/{}/'.format(str(page))
        urlpage.append(url)

for i in range(len(urlpage)):
    url_str=urlpage[i]
    #print(url_str)
    
    resp=requests.get(url=url_str,headers=headers,proxies=proxies)
    #print(resp.status_code)
    resp.encoding=resp.apparent_encoding
    con=resp.text
    
    tree=lxml.etree.HTML(con)
    link=tree.xpath('//div[@class="book_last"]//a/@href')
    name=tree.xpath('//div[@class="book_last"]//a/text()')
    #print(link)

    for j in range(len(link)):
        links=link[j]
        names=name[j]
        new_link='https://m.biqiuge8.cc'+links
        #print('{}:{}'.format(new_link,names))

        response=requests.get(url=new_link,headers=headers,proxies=proxies)
        response.encoding=resp.apparent_encoding
        content=response.text

        tree=lxml.etree.HTML(content)
        txtcontent=tree.xpath('//div[@id="chaptercontent"]/text()')
        
        conlist=[x.strip() for x in txtcontent if x.strip()]
        strtxt=''.join(conlist)
        #print(strtxt)

        with open('E:\\素材\\素材\\三体小说\\'+names+'.txt','w',encoding='utf-8') as f:
            f.write(strtxt)
            print(names+':下载成功')