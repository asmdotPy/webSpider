import threading 
from queue import Queue
from Spider import Spider
from domain import *
from osengine import *

# تعریف مقادیر ثابت 
HOME_PAGE='https://www.instagram.com'
PROJECT_NAME=get_domain_name(HOME_PAGE)
DOMAIN_NAME=get_domain_name(HOME_PAGE)
QUEUE_FILE=PROJECT_NAME+'/queue.txt'
CRAWLED_FILE=PROJECT_NAME+'/crawled.txt'
NUMBER_OF_THREADS=1

# ایجاد ابجکت از کلاس صف برای مالتی تردینگ
queue=Queue()

# اولین خزنده وب
Spider(PROJECT_NAME,HOME_PAGE,DOMAIN_NAME)


#ایجاد تابع برای انجام همزمان تابع ورک
def create_workers():
    for _ in range(NUMBER_OF_THREADS):
        t=threading.Thread(target=work)
        # با قرار دادن مقدار ترو در صورت پایان برنامه تمام ترد ها از بین می روند
        t.daemon=True 
        t.start()

#ایجاد تابع اصلی برای عملیات خزندهدر حلفه بینهایت 
def work():
    while True:
        url=queue.get()
        try:
            Spider.crawl_page(threading.current_thread().name,url)
        except Exception as e:
            with open('error.txt','a+') as f:
                f.writelines(str(e))
            pass 
        queue.task_done()

# هر لینکی که در داخل فایل کیو داخل فولدر پروژه است یک کار جدید است 
def create_jobs():
    for link in file_to_set(QUEUE_FILE):
        # وارد کردن لینک داخل صف ترد
        queue.put(link)
    # مدیریت ترد ها برای عدم تداخل کار
    queue.join()
    crawl()

#اگر در فایل کیو داخل فولدر پروژه لینکی وجود داشته باشد ان را بررسی می کند 
def crawl():
    queued_links=file_to_set(QUEUE_FILE)
    if len(queued_links)>0:
        print(str(len(queued_links))+' links in queue')
        create_jobs()
        

create_workers()
crawl()