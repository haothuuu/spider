from bs4 import BeautifulSoup
import requests 
import os 
from tomorrow import threads



class Meizitu():

    def __init__(self):
        self.all_url = set()
        self.path = None
    
    def add_url(self,url):
        self.add_url.add(url)


    def get_max_page(self,url):
        html = self.request(url)
        soup = BeautifulSoup(html.text,'lxml')
        max_page = soup.find('div',class_ = 'navigation').find_all('li')[-3].get_text()
        return max_page
    
    def get_all_a(self,page_url):
               
        page_html = self.request(page_url)
        page_soup = BeautifulSoup(page_html.text,'lxml')
        all_a = page_soup.find('ul',class_ = 'wp-list clearfix').find_all('h3')
        return all_a
        
    def get_url_data(self,a):
        url_data = {}
        
        url_data['href'] = a.a.get('href')
        url_data['title'] = a.get_text()

        return url_data

    def get_img_urls(self,url_data):
        html = self.request(url_data['href'])
        html_soup = html_soup = BeautifulSoup(html.text,'lxml')
        img_urls=html_soup.find('div',id = 'picture').find_all('img')
        return img_urls
        
    def mkdir(self,url_data):
        path = 'C:\\GIRLS\\quanluo\\'+ str(url_data['title'].encode('ISO-8859-1'))
        path = path.strip()
        path = path.rstrip("\\")
        isExists = os.path.exists(path)
        if not isExists:
            print 'create a directory named' + path
            os.makedirs(path)            
        else:
            print 'the dirtory has been created named ' + url_data['title'].encode('ISO-8859-1')
            
        os.chdir(path)        
        print 'start saving' + str(url_data['title'].encode('ISO-8859-1'))
    

    @threads(500)    
    def save_img(self,img_urls):
        count = 1
        for img_url in img_urls:
            
            img_url_real = img_url['src']
            img_name = img_url['alt'].encode('ISO-8859-1')
            img = self.request(img_url_real)
            print 'now is saving no.'+str(count)
            f = open(img_name+'.jpg','ab')
            f.write(img.content)
            f.close()
            count = count +1
            
    
    def request(self,url):
        headers = {'User-Agent':"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/2.2.0.1207/1 Safari/537.1"}
        content = requests.get(url,headers = headers)
        return content
    

        
        
    
