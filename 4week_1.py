import requests
from bs4 import BeautifulSoup

url = r'https://news.ebs.co.kr/ebsnews/?mainTop'

response = requests.get(url)

if response.status_code == 200:
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')
    print(soup)

else : 
    print(response.status_code)
    
    
from pprint import pprint
        
    # for i in range(19):
    #     title = soup.select_one(f'#contentsW > div.botWrap > div.Nsect02.glob_l > ul > li:nth-child({i+1}) > div > a > div > em')
    #     print(title.text)
    # #contentsW > div.botWrap > div.Nsect02.glob_l > ul > li:nth-child(2) > div > a > div > em
    # #contentsW > div.botWrap > div.Nsect02.glob_l > ul > li:nth-child(3) > div > a > div > em
    # #contentsW > div.botWrap > div.Nsect02.glob_l > ul > li:nth-child(20) > div > a > div > em
    # #contents > div > div.list_article > div.submok > ul > li:nth-child(1) > p.tit > a
    # #contents > div > div.list_article > div.submok > ul > li:nth-child(18) > p.tit > a
    # #contents > div > div.list_article > div.submok > ul > li:nth-child(18) > p.tit > a