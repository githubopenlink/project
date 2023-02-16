import requests
import json

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36'
}

headers1 = {
    'Accept': 'application/json, text/plain, */*',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Connection': 'keep-alive',
    'Cookie': '_ga=GA1.2.1500987479.1595755923; _gid=GA1.2.568444838.1596065504; Hm_lvt_cdb524f42f0ce19b169a8071123a4797=1595755923,1596065505; Hm_lpvt_cdb524f42f0ce19b169a8071123a4797=1596076178; kw_token=P5XA2TZXG9',
    'csrf': 'P5XA2TZXG9',
    'Host': 'www.kuwo.cn',
    'Referer': 'http://www.kuwo.cn/search/list?key=%E5%A4%95%E9%98%B3%E7%BA%A2',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36'
}

headers2 = {
    'Accept': 'application/json, text/plain, */*',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Connection': 'keep-alive',
    'Cookie': '_ga=GA1.2.1500987479.1595755923; _gid=GA1.2.568444838.1596065504; Hm_lvt_cdb524f42f0ce19b169a8071123a4797=1595755923,1596065505; Hm_lpvt_cdb524f42f0ce19b169a8071123a4797=1596078189; _gat=1; kw_token=IJATWHHGI8',
    'csrf': 'IJATWHHGI8',
    'Host': 'www.kuwo.cn',
    'Referer': 'http://www.kuwo.cn/search/list?key=%E6%A2%A6%E7%9A%84%E5%9C%B0%E6%96%B9',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36',

}

key_name = input('请输入你要查找的歌曲名称：')
num = input('请输入你要查看歌曲列表第几页：')

url2 = 'http://www.kuwo.cn/api/www/search/searchMusicBykeyWord?key={}&pn={}&rn=30&httpsStatus=1&reqId=da11ad51-d211-11ea-b197-8bff3b9f83d2e'.format(key_name,num)

response = requests.get(url2,headers=headers2)  #访问歌曲列表
print(response.text)
response.encoding = response.apparent_encoding  #这个apparent_encoding就是让系统根据页面来判断用何种编码
response = response.json()  # 得到josn字典dict
music_list = response["data"]["list"]  #得到歌曲列表
print("共计" + str(len(music_list)) + "结果： ")
all_singers = []  #放置所有歌手人名
names = []    #放置歌曲名字
all_rid = []    #放置所有rid，rid是网页所需参数
a = 0
for music in music_list:
    #print(music)
    singer = music["artist"]  # 歌手名
    name = str(a) + "  " + music["name"]  # 歌曲名

    rid = music["musicrid"]     #取出rid，之后要对这个字符串进行切割
    index = rid.find('_')
    rid = rid[index + 1:len(rid)]

    all_singers.append(singer)  #将对应信息放到列表中
    names.append(name)
    all_rid.append(rid)
    a = a + 1
infs = dict(zip(names, all_singers))
infs = json.dumps(infs, ensure_ascii=False, indent=4, separators=(',', ':'))
infs = infs.replace('"', ' ')
infs = infs.replace(':', '——————')
print(infs)

order = input("请输入歌曲前的序号：")

musicrid = all_rid[int(order)]
url1 = 'http://www.kuwo.cn/url?format=mp3&rid={}&response=url&type=convert_url3&br=128kmp3&from=web&t=1596078536164&httpsStatus=1&reqId=01528151-d212-11ea-b197-8bff3b9f83d2'.format(musicrid)

res = requests.get(url1,headers=headers1)  #访问歌曲列表
res.encoding = res.apparent_encoding
res = res.json()  # dict
res_url = res["url"]  #取出歌曲下载url地址

music = requests.get(res_url,headers=headers).content
with open(names[int(order)]+'.mp3','wb') as f:
    f.write(music)