import requests
from bs4 import BeautifulSoup

def scraping(r):
    soup = BeautifulSoup(r.content, "html.parser")
    
    categories = soup.find_all("h3")
    category = []
    for cat in categories:
        item = cat.text
        category.append( item )
        
    tables = soup.find_all("table")
    
    weapon = []
    cnt = 0
    for t in tables:
        words = t.find_all("td", attrs={"class":"style_td",
                                "style":"text-align:center; width:120px;"})
    
        wep = []
        for word in words:
            item = word.text
            #print( item )
            wep.append(item)
        weapon.append(wep)
        #print("-------------------")
        #print( weapon )
        
        
    weapon = weapon[4:15]
    weapon = [x for x in weapon if x]
    
    for i in range( len(weapon) ):
        if i == 0:
            continue
        weapon[i].insert(0, category[i-1])
    return weapon



r = requests.get('https://h1g.jp/cod_mw_ps4/?.50%20GS')
work = scraping(r)

print(work)


