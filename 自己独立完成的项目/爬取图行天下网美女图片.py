import requests
import lxml.etree
import urllib.request as ulr

for i in range(1,7):
    url='https://www.photophoto.cn/all/xingganchangtuimeinv-0-0-0-4-0-0-0-'+str(i)+'.html'
    resp=requests.get(url=url)
    resp.encoding='utf-8'
    content=resp.text

    tr=lxml.etree.HTML(content)
    img=tr.xpath('//div[@class="Masonry-item"]//a/img/@src')

    for j in range(len(img)):
        imgc=img[j]
        imgs='https:'+imgc
        #print(imgs)

        #解决文件名重名覆盖问题
        if i == 1:
            ulr.urlretrieve(url='https:'+img[j],filename='E:\素材\素材\美女图\美女图{}.jpg'.format(j))
            print('{}:下载中'.format(j))
        elif i == 2:
            ulr.urlretrieve(url='https:'+img[j],filename='E:\素材\素材\美女图\美女图_{}.jpg'.format(j))
            print('_{}:下载中'.format(j))
        elif i == 3:
            ulr.urlretrieve(url='https:'+img[j],filename='E:\素材\素材\美女图\美女图-{}.jpg'.format(j))
            print('-{}:下载中'.format(j))
        elif i == 4:
            ulr.urlretrieve(url='https:'+img[j],filename='E:\素材\素材\美女图\美女图:{}.jpg'.format(j))
            print(':{}:下载中'.format(j))
        elif i == 5:
            ulr.urlretrieve(url='https:'+img[j],filename='E:\素材\素材\美女图\美女图0{}.jpg'.format(j))
            print('0{}:下载中'.format(j))
        elif i == 6:
            ulr.urlretrieve(url='https:'+img[j],filename='E:\素材\素材\美女图\美女图00{}.jpg'.format(j))
            print('00{}:下载中'.format(j))
        else:
            print('下载完成')