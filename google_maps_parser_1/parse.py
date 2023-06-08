from selenium import webdriver
from parsel import Selector
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options



#def get_data()


#chromedrive_path = '/usr/bin/chromedriver' # use the path to the driver you downloaded from previous steps
#driver = webdriver.Chrome(chromedrive_path)

chrome_options = Options()
chrome_options.add_argument('--proxy-server=http://ipaddress:port')
service = Service(executable_path='/home/skienbear/Рабочий стол/made/project/google-maps-scraper/build/')
driver = webdriver.Chrome(service = service,options=chrome_options)

url = 'https://www.google.com/maps/search/Ступино аптеки,+Russia/@54.8903165,38.0762222,13z'
driver.get(url)

page_content = driver.page_source

response = Selector(page_content)

results = []

for el in response.xpath('//div[contains(@aria-label, "Results for")]/div/div[./a]'):
    results.append({
        'link': el.xpath('./a/@href').extract_first(''),
        'title': el.xpath('./a/@aria-label').extract_first('')
    })

print(response.xpath('//div[contains(@aria-label, "Results for")]/div/div[./a]'))
driver.quit()
