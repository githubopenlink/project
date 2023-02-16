import requests
import random
import lxml.etree
import time

url='https://www.mhua5.com/chapter-942734.html'
headers={'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Mobile Safari/537.36 Edg/108.0.1462.76'}

proxies_pool=[
    {'http':'202.109.157.61:9000'},
    {'http':'222.74.73.202:42055'},
    {'http':'202.109.157.60:9000'},
    {'http':'27.42.168.46:55481'},
    {'http':'182.139.111.149:9000'},
    {'http':'121.13.252.62:41564'},
    {'http':'112.14.47.6:52024'},
    {'http':'61.216.185.88:60808'},
    {'http':'183.236.232.160:8080'},
    {'http':'123.169.39.212:9999'},
    {'http':'112.14.47.6:52024'}
]
proxies=random.choice(proxies_pool)

resp=requests.get(url=url,headers=headers,proxies=proxies)
print(resp.status_code)
con=resp.text
#print(con)

tr=lxml.etree.HTML(con)
url_list=tr.xpath('//ul[@class="comic-list"]//img/@src')
#print(url_list)
  
for j in range(len(url_list)):
    url_lists=url_list[j]
    #print(url_lists)
    #print(len(url_lists))
    while True:
        try:            
            resp=requests.get(url=url_lists,headers=headers)
            break
        except:
            time.sleep(1)

    with open('E:/素材/素材/金瓶梅/01话/'+str(j+1)+'.jpg','wb') as f:
        f.write(resp.content)
        print('下载中')

print('end')