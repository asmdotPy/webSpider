import os

#هر وبسایتی که خزیده می شود با نام پروژه مجزا ذخیره سازی خواهد شد

#ایجاد فولدر سایت
#directory="cnet" www.cnet.com
def create_project_directory(directory):
    if not os.path.exists(directory):
        print('Creating project '+directory)
        os.makedirs(directory)

#ایجاد فایل های خزیده شده یا در نوبت خزیدن
# base_url="wwww.cnet.com"
#project_name="cnet"
def create_data_files(project_name,base_url):
    queue=project_name+'/queue.txt'
    crawled=project_name+'/crawled.txt'
    if not os.path.isfile(queue):
        with open(queue,'w',encoding="utf-8") as f:
            f.write(base_url+'\n')
    if not os.path.isfile(crawled):
        with open(crawled,'w',encoding="utf-8") as f:
            f.write('')

# تبدیل اطلاعات فایل به مجموعه ست
#file_name="cnet/queue.txt"
# results=('www.cnet.com','www.cnet.com/books')
def file_to_set(file_name):
    results =set()
    with open(file_name,'rt',encoding="utf-8") as f:
        for line in f:
            results.add(line.replace('\n',''))
    return results

# تبدیل اطلاعات مجموعه ست به فایل
#links = set
#path='cnet/crawled.txt'
def set_to_file(links,path):
    with open(path,'w',encoding="utf-8"):
        pass
    for link in sorted(links):
        with open(path,'a',encoding="utf-8") as file:
            file.write(link+'\n')

# create_project_directory('cnet')
# create_data_files('cnet','www.cnet.com')

