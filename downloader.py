import urlparse
import urllib2
import random
import time
from datetime import datetime, timedelta
import socket
import requests
class Downloader:
    def __init__(self,delay=5,uesr_agent="Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; rv:11.0) like Gecko",proxies=None,num_retries=1,cache=None):
        self.throttle = Throttle(delay)
        self.uesr_agent=uesr_agent
        self.proxies=proxies
        self.num_retries=num_retries
        self.cache=cache
    def __call__(self, url):
        result=None
        if self.cache:
            try:
                result=self.cache[url]
            except KeyError:
                pass
            else:
                if self.num_retries>0 and 500<result['code']<600:
                    result=None
        if result is None:
            self.throttle.wait(url)
            proxy=random.choice(self.proxies) if self.proxies else None
            headers={'Uesr-agent':self.uesr_agent}
            result=self.download(url,headers,proxy,self.num_retries)
        return result

    def download(self,url,headers,proxy,num_retries,data=None):
        html = requests.get(url,headers=headers,proxies=proxy)
        return html.content




class Throttle:
    """Throttle downloading by sleeping between requests to same domain
    """

    def __init__(self, delay):
        # amount of delay between downloads for each domain
        self.delay = delay
        # timestamp of when a domain was last accessed
        self.domains = {}

    def wait(self, url):
        """Delay if have accessed this domain recently
        """
        domain = urlparse.urlsplit(url).netloc
        last_accessed = self.domains.get(domain)
        if self.delay > 0 and last_accessed is not None:
            sleep_secs = self.delay - (datetime.now() - last_accessed).seconds
            if sleep_secs > 0:
                time.sleep(sleep_secs)
        self.domains[domain] = datetime.now()