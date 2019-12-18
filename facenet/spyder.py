# coding=utf-8
"""
爬取百度图片的高清原图
"""
import re
import sys
import urllib
import os
 
import requests
 
 
def get_onepage_urls(onepageurl):
    if not onepageurl:
        print('执行结束')
        return [], ''
    try:
        html = requests.get(onepageurl).text
    except Exception as e:
        print(e)
        pic_urls = []
        fanye_url = ''
        return pic_urls, fanye_url
    pic_urls = re.findall('"objURL":"(.*?)",', html, re.S)
    fanye_urls = re.findall(re.compile(r'<a href="(.*)" class="n">下一页</a>'), html, flags=0)
    fanye_url = 'http://image.baidu.com' + fanye_urls[0] if fanye_urls else ''
    return pic_urls, fanye_url
 
 
def down_pic(pic_urls,pic_name,localPath):
    if not os.path.exists(localPath):  # 新建文件夹
        os.mkdir(localPath)
    """给出图片链接列表, 下载图片"""
    for i, pic_url in enumerate(pic_urls):
        try:
            pic = requests.get(pic_url, timeout=15)
            string = pic_name + "_" + str(i + 1) + '.jpg'
            with open(localPath + '%s' % string, 'wb')as f:
                f.write(pic.content)
                print('成功下载第%s张图片: %s' % (str(i + 1), str(pic_url)))
        except Exception as e:
            print('下载第%s张图片时失败: %s' % (str(i + 1), str(pic_url)))
            print(e)
            continue
 
 
if __name__ == '__main__':
    keyword = '杨幂1920*1080'  # 关键词, 改为你想输入的词即可
   # url_init_first = r'http://image.baidu.com/search/index?tn=baiduimage&ipn=r&ct=201326592&cl=2&lm=-1&st=-1&fm=result&fr=&sf=1&fmq=1571658773043_R&pv=&ic=&nc=1&z=&hd=&latest=&copyright=&se=1&showtab=0&fb=0&width=&height=&face=0&istype=2&ie=utf-8&hs=2&sid=&word=%E8%B5%B5%E4%B8%BD%E9%A2%96%E5%9B%BE%E7%89%87'
    #url_init_first=r'http://image.baidu.com/search/index?tn=baiduimage&ipn=r&ct=201326592&cl=2&lm=-1&st=-1&fm=result&fr=&sf=1&fmq=1576424347193_R&pv=&ic=&nc=1&z=&hd=&latest=&copyright=&se=1&showtab=0&fb=0&width=&height=&face=0&istype=2&ie=utf-8&hs=2&sid=&word=%E5%91%A8%E6%9D%B0%E4%BC%A6%E5%9B%BE%E7%89%87'
    #url_init_first='http://image.baidu.com/search/index?tn=baiduimage&ipn=r&ct=201326592&cl=2&lm=-1&st=-1&fm=result&fr=&sf=1&fmq=1576424608553_R&pv=&ic=&nc=1&z=&hd=&latest=&copyright=&se=1&showtab=0&fb=0&width=&height=&face=0&istype=2&ie=utf-8&hs=2&sid=&word=%E6%9D%8E%E6%98%93%E5%B3%B0%E5%9B%BE%E7%89%87&f=3&oq=%E6%9D%8E%E6%98%93%E5%B3%B0tu&rsp=-1'
    url_init_first='http://image.baidu.com/search/index?tn=baiduimage&ipn=r&ct=201326592&cl=2&lm=-1&st=-1&fm=result&fr=&sf=1&fmq=1576424709930_R&pv=&ic=&nc=1&z=&hd=&latest=&copyright=&se=1&showtab=0&fb=0&width=&height=&face=0&istype=2&ie=utf-8&hs=2&sid=&word=%E9%B9%BF%E6%99%97%E5%9B%BE%E7%89%87'
    #url_init_first=
    url_init = url_init_first + urllib.parse.quote(keyword, safe='/')
    all_pic_urls = []
    onepage_urls, fanye_url = get_onepage_urls(url_init)
    all_pic_urls.extend(onepage_urls)
 
    fanye_count = 0  # 图片所在页数，下载完后调整这里就行
    while 1:
        onepage_urls, fanye_url = get_onepage_urls(fanye_url)
        fanye_count += 1
        print('第%s页' % fanye_count)
        if fanye_url == '' and onepage_urls == []:
            break
        all_pic_urls.extend(onepage_urls)
 
    down_pic(list(set(all_pic_urls)),'yangmi','G:\\FaceRecognition\\yangmi\\')#保存位置也可以修改