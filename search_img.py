from icrawler.builtin import GoogleImageCrawler

def search_img(name_req):
    
    google_crawler = GoogleImageCrawler(storage={'root_dir': '/Users/aleksandrarefev/Downloads/TelegramBotPython/img'})

    name = 'ава ' + name_req

    google_crawler.crawl(keyword=name, max_num=3)