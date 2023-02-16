import requests
import os
import re
import time
import hashlib
from urllib.request import urlretrieve
'''
爬取思路：
    由1输入的歌手名称-2确定并获取该歌手下全部歌曲id(理想状态下)-3爬取歌曲相关属性信息-4下载
        1.输入想要下载歌曲的作者名称 如 薛之谦、许嵩、陈奕迅...由歌手名称确定到该歌手歌曲列表url
        2.每首歌曲 都有唯一标识tsid 从上步url源码界面中运用正则表达式爬取歌曲总页码及歌曲tsid
        3.在歌曲播放player页面（随便播放一首歌-f12）分析获取歌曲相关信息json文件 
            ps: 千千音乐有sign的js加密 此处需要解密sign 进而爬取歌曲相关属性信息
        4.下载-视频音频压缩包图片下载用urlretrieve库即可 文件类用with open
'''
# 输入歌手名称
keywords = input("请输入歌手姓名：")
# 成功下载歌曲数
song_number = 0
 
# 创建存放歌曲/词的文件
filename1 = f'{os.getcwd()}\\songs\\{keywords}\\'
if not os.path.exists(filename1):
    os.mkdir(filename1)
filename2 = f'{os.getcwd()}\\songwords\\{keywords}\\'
if not os.path.exists(filename2):
    os.mkdir(filename2)
 
 
def main():
     # 伪装头部
    headers = {
         'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'
    }
    params = (
        ('word', keywords),
    )
     # 参数timeout=5 防止访问超时
    response = requests.get('https://music.taihe.com/search', headers=headers,params=params, timeout=5)
     # 歌曲页码数
    page_NUM = re.findall(r'<li class="number">(.*?)</li>', response.text, re.S)
    if len(page_NUM) == 0:  # 存在某歌手歌曲过少不足一页的情况
        page_num = 1
    else:
        page_num = int(page_NUM[-1])
 
     # 通过翻页获取某歌手所有歌曲id
    for i in range(1, page_num + 1):
        url_fenye = f'https://music.taihe.com/search?word={keywords}&pageNo={i}'
        response = requests.get(url=url_fenye, headers=headers, timeout=5)
        tsids = re.findall(r'<a href="/song/(.*?)"', response.text, re.S)
        set_tsids = list(set(tsids))
        set_tsids.sort(key=tsids.index)     # set_tsids去重不改变原顺序
 
         # 开始下载歌曲/词
        j = 1  # 歌曲数
         # 获取每首歌曲的tsid值
        for tsid in set_tsids:
             # 防止反爬，每隔1秒进行一次
            time.sleep(1)
            print(f'正在下载第{i}页第{j}首...')
             # 从浏览器中js解密sign，采用的是md5加密形式
            r = f"TSID={tsid}&appid=16073360&timestamp={str(int(time.time()))}0b50b02fd0d73a9c4c8c3a781c30845f"
            sign = hashlib.md5(r.encode(encoding='UTF-8')).hexdigest()
             # print(sign) # 获取到的就是每一首歌曲的sign值，下面构造params
            params = (
                ('sign', sign),
                ('appid', '16073360'),
                ('TSID', tsid),
                ('timestamp', str(int(time.time()))),
            )
             # 具体歌曲的相关属性
            song_info = requests.get('https://music.taihe.com/v1/song/tracklink',params=params, timeout=5).json()[
                 'data']
            if len(song_info) != 0:     # 部分歌曲播放链接不存在导致song_info为空的情况
                if 'path' in song_info.keys():  # VIP的歌曲只能部分听取 无意义 不下载
                    singer_name = song_info['artist'][0]['name']  # 歌手名
                    song_name = song_info['title']  # 歌名
                    song_link = song_info['path']  # 音频地址
                    lrc_link = song_info['lyric']  # 歌词地址
                else:
                    print(f'第{i}页的第{j}首为VI歌曲,无法找到下载链接！')   # 可去掉
                    j += 1
                    continue
            else:
                print("该歌曲播放链接不存在!")    # 可去掉
                pass
 
             # 下载歌曲 f'{song_name}-{singer_name}.mp3'
            if not os.path.exists(f'{filename1}{song_name}-{singer_name}.mp3'):
                urlretrieve(song_link, f'{filename1}{song_name}-{singer_name}.mp3')  # 下载歌曲
                print(song_name, '下载完成')
                global song_number  # 使变量全局化
                song_number += 1
            else:
                print(f"{song_name}已存在，下载失败！")
                pass
            j += 1
 
             # 下载歌词 f'{song_name}.lrc'
            if not os.path.exists(f'{filename2}{song_name}.lrc'):
                if lrc_link:    # 存在歌词链接即下载
                    urlretrieve(lrc_link, f'{filename2}{song_name}.lrc')  # 下载歌词
            else:
                pass
 
    print(f'共下载成功{song_number}首歌曲，请查看存放地址{filename1}')
 
 
if __name__ == '__main__':
    main()