from urllib.parse import urlparse

# در یافت نام دامین از یک لینک ادرس طولانی 
# get domain name (example.com) from name.name.name.example.com
def get_domain_name(url):
    try:
        # netloc network location part
        url=urlparse(url).netloc
        results=url.split('.')
        return results[-2]+'.'+results[-1]
    except:
        return ''

# link 1 : https://docs.python.org --> python.org

get_domain_name('https://docs.python.org/3/library/urllib.request.html')

# urlparser : ParseResult(scheme='https', netloc='docs.python.org', path='/3/library/urllib.request.html', params='', query='', fragment='')
# netloc : docs.python.org
# result : ['docs', 'python', 'org']
# python.org