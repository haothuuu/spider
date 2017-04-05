import meizitu


class SpiderMain(object):
    
    def __init__(self):
        self.mzitu = meizitu.Meizitu()
    
    
    
    def craw(self,root_url):
        max_page = self.mzitu.get_max_page(root_url)
        for page in range(1, int(max_page)+1):
            page_url = 'http://www.meizitu.com/tag/quanluo' + '_4_' +str(page)+'.html'
            all_a = self.mzitu.get_all_a(page_url)
            
            
            for a in all_a:
                url_data = self.mzitu.get_url_data(a)
                #print url_data
                #print a.get_text().encode('ISO-8859-1')
                img_urls = self.mzitu.get_img_urls(url_data)
                self.mzitu.mkdir(url_data)
                self.mzitu.save_img(img_urls)
        
    
    
    
if __name__ == "__main__":
    root_url = "http://www.meizitu.com/tag/quanluo_4_1.html"
    obj_spider = SpiderMain()
    obj_spider.craw(root_url)
