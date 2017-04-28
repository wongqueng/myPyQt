# -*-coding:UTF-8-*-
from downloader import Downloader
import lxml.html
import  threading
from bili_db import bili_DB
BaseUrl="http://search.bilibili.com/all"

def geturl(keyword="",page="1",order="totalrank"):
    url=BaseUrl+"?keyword="+keyword+"&page="+page+"&order="+order
    print url
    return url
def parstr(num):
    if str(num).count("万"):
        int_num=num.replace("万","")
        return float(int_num)*10000
    try:
        return float(num)
    except:
        return 0
class Video:
    def __init__(self,url,title,up_name,watches,bullets,up_time):
        self.url=url.encode("utf-8")
        self.title=title.encode("utf-8")
        self.up_name=up_name.encode("utf-8").strip()
        self.watches=parstr(watches.encode("utf-8").strip())
        self.bullets=parstr(bullets.encode("utf-8").strip())
        self.up_time=up_time.encode("utf-8").strip()
        self.json={"url":url,"title":title,"up_name":self.up_name,"watches":self.watches,"bullets":self.bullets,"up_time":self.up_time}
    def __str__(self):
        return "标题:%s;观看次数:%f;弹幕:%f;上传时间:%s;up主:%s"%(self.title,self.watches,self.bullets,self.up_time,self.up_name)

count=0
def bilibiliCallBack(html,DB):
    tree=lxml.html.fromstring(html.decode('utf-8'))
    videos=tree.cssselect(".video")
    for video in videos:
        title=video.cssselect("a[se-linkid]")[0].get('title')
        up_name=video.cssselect("span[title=up主] a".decode("utf-8"))[0].text_content()
        watches=video.cssselect("span[title=观看]".decode("utf-8"))[0].text_content()
        bullets=video.cssselect("span[title=弹幕]".decode("utf-8"))[0].text_content()
        up_time=video.cssselect("span[title=上传时间]".decode("utf-8"))[0].text_content()
        url=video.cssselect("a[se-linkid]")[0].get('href')
        v=Video(url,title,up_name,watches,bullets,up_time)
        DB[url]=v
        print v
def crawler(max_threads=5):
    craw_queue=[geturl("鬼畜",str(i),"click") for i in range(1,11)]
    def process_queue():
        D = Downloader()
        DB = bili_DB()
        while True:
            try:
                url=craw_queue.pop()
            except:
                break
            else:
                html=D(url)
                bilibiliCallBack(html,DB)
    threads=[]
    while threads or craw_queue:
        for thread in threads:
            if not thread.is_alive():
                threads.remove(thread)
        while len(threads)<max_threads and craw_queue:
            thread=threading.Thread(target=process_queue)
            thread.setDaemon(True)
            thread.start()
            threads.append(thread)

crawler()


# D("http://search.bilibi li.com/all?keyword=%E9%AC%BC%E7%95%9C&page=1&order=totalrank")