import scrapy
import json
import pickle


def pickle_save(x, file):
    with open(file, 'wb') as f:
        pickle.dump(x, f)

def pickle_load(file):
    with open(file, 'rb') as f:
        return pickle.load(f)


class MySpider(scrapy.Spider):
    name = 'my_spider'
    n_pages = 187
    
    visited_ids = []
    all_prices = []
    n_per_page = []
    

    custom_settings = {
        'LOG_ENABLED': False,
    }
    
    def start_requests(self):
        base_url =  'https://krisha.kz/arenda/kvartiry/astana/?das[live.rooms]=1&das[rent.period]=1'
        
        urls = [base_url+f'&page={i}' for i in range(1,self.n_pages+1)]
        for url in urls:
            print(url)
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        def parse_all(x, to_int=False):
            x = x.getall()
            x = map(lambda s: s.strip().replace('\xa0',''), x)
            x = filter(bool, x)
            if to_int: x = map(lambda s: int(s), x)
            x = list(x)
            return x
            
        cards = response.css("div.a-card")
        prices = cards.css("div.a-card__price::text")
        prices = parse_all(prices, True)
        ids = [x.attrib['data-id'] for x in cards]
        
        
        # print(response.url, ids)
        # print(response.url, prices)
        
        # self.all_prices += prices
        # self.visited_ids += ids
        self.n_per_page.append(len(cards))
        
        assert len(ids) == len(prices)
        for idx, p in zip(ids, prices):
            yield {'id':idx, 'price':p}
            
        print(url, len(ids))
        
    def closed(self, reason):
        print(reason)
        print(self.n_per_page)