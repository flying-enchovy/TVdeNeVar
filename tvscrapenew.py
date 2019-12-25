from bs4 import BeautifulSoup as soup
from urllib.request import urlopen,Request
import datetime

class Program:
  def __init__(self, isim, time, kanal):
    self.isim = isim
    self.time = time
    self.kanal = kanal
Urller=[
    'https://www.tvyayinakisi.com/kanal-d-tv-yayin-akisi',
    'https://www.tvyayinakisi.com/show-tv-yayin-akisi',
    'https://www.tvyayinakisi.com/star-tv-yayin-akisi',
    'https://www.tvyayinakisi.com/fox-yayin-akisi',
    'https://www.tvyayinakisi.com/atv-yayin-akisi'
]
Kanallar=[
    'Kanal D',
    'Show Tv',
    'Star Tv',
    'Fox Tv',
    'Atv Tv'
]
Programlar=[]
for i in range(0,len(Urller)):
    req = Request(Urller[i], headers={'User-Agent': 'Mozilla/5.0'})
    webpage = urlopen(req)
    webpage_raw = webpage.read()
    webpage.close()
    page_soup = soup(webpage_raw, "html.parser")
    box = page_soup.find("div",{"class":"active"})
    Time= datetime.datetime.now().time()
    for program in box.ul.findAll("li"):
        if(Time.hour*60+Time.minute>=int(program["data-start"][-8:-6])*60+int(program["data-start"][-5:-3]) and Time.hour*60+Time.minute<=int(program["data-end"][-8:-6])*60+int(program["data-end"][-5:-3])):
            Programlar.append(Program(program.find("p",{"class":"name"}).get_text(),Time.hour*60+Time.minute-(int(program["data-start"][-8:-6])*60+int(program["data-start"][-5:-3])),Kanallar[i]))
            print(Programlar[i].__dict__)


