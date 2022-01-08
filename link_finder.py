# ماژول های مورد نیاز
from html.parser import HTMLParser
from urllib import parse

# کلاس لینک یاب 
class LinkFinder(HTMLParser):
    # base_url="www.cnet.com"
    # page_url="www.cnet.com/videos" "/videos"
    def __init__(self,base_url,page_url):
        super().__init__()
        self.base_url=base_url
        self.page_url=page_url
        self.links=set()

    def error(self,message):
        pass 
    
    def handle_starttag(self,tag,attrs):
        if tag=='a':
            #attrs={attribute:value}
            for (attribute,value) in attrs:
                if attribute=='href':
                    url=parse.urljoin(self.base_url,value)
                    self.links.add(url)

    def page_links(self):
        return self.links

# finder=LinkFinder('www.google.com','www.google.com/videos')
# finder.feed('<html><body><a href="www.google.com/jkhhkh"><a href="www.cnet.com/go"></body>,/html>')
# print(finder.page_links())



    
