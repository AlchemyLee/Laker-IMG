import requests
from bs4 import BeautifulSoup
import os  
ul = 'https://nba.hupu.com/players/lakers'
html = requests.get(ul).text
#main_url = 'https://www.zhihu.com'
#print(html)
soup = BeautifulSoup(html, 'lxml')  #使用LXML解析器解析html；
img_ul = soup.find_all('td', {'class':'td_padding'})   #找到所有div模块下的image类，图片就在这个类里面。
os.makedirs('./爬图片/', exist_ok=True)    #新建文件夹
for ul in img_ul:    
    imgs = ul.find_all('img')    
    # print(imgs)    
    for img in imgs:        
        url = img['src']        
        img_name = url.split('/')[-1]        
#        req = requests.get(main_url+url, stream=True)    
        req = requests.get(url, stream=True)
        with open('./爬图片/%s' % img_name, 'wb') as f:            
            for chunk in req.iter_content(chunk_size=100):                
                f.write(chunk)        
        print('Saved %s' % img_name)
