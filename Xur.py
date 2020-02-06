from bs4 import BeautifulSoup
from urllib.request import urlopen
from datetime import *



title = """

`/oooooooo+/`/ooooooooo/-    `/+ooooo+/ 
   .dMMMh.     -sMMMMm          hMmo.   
    sMMM+        -mMMMs`      `sNo`     
    oMMM+         `sMMMd-    /mh.       
    oMMM+           :mMMN+ -dm/         
    oMMM+            `hMMMdNs`          
    oMMM+              +MMMN:           
    oMMM+             .hNmMMMs`         
    oMMM+           `oNy``sMMMm-        
    oMMM+          :mm:    /NMMN+       
    oMMM+        .yNo       .dMMMh.     
    sMMMo      `oNm-          yMMMN/    
`/+sNMMMNs//./sNMMmo/.     `:/yMMMMMdo/`

    #Created by Deviant-Fox 

        """
        
"""
A basic webscraping program to scrape info from the website and display what is for
sell in Destiny 2 by XUR. written to see what weekday it is so it can display the 
right info. 

TO-DO:
    - find a way to display a countdown in the ELIF statement to the Friday of that
        week
    - 
"""

today = date.today()
weekday = today.weekday()
TuesWedThurs = [1,2,3]
MonFriSatSun = [0,4,5,6]


Xur_page = 'https://xur.wiki/'
page = urlopen(Xur_page)
html = page.read()
page.close()
SoupPage = BeautifulSoup(html, "html.parser")

if weekday in MonFriSatSun:
    try:
        ExoticItems = SoupPage.findAll("div",{'hero_item_container'})
        Location = SoupPage.find("div", class_ = 'location')
        ExoticsName = [item.find(class_ = 'hero_item_name').get_text() for item in ExoticItems]
        ExoticsType = [item.find(class_ = 'hero_item_type').get_text() for item in ExoticItems]
        Xur_loc = Location.find(class_ = 'location_name').get_text()
        location_text = Location.find(class_ = 'location-text-here').get_text()
        
        print(title + "\n" + "_"*110)

        print(f"Xur has been located on {Xur_loc}.")
        print(location_text +"\n\nHis Inventory\n"+ "_" * 110)

        print(f"EXOTIC WEAPON: {ExoticsName[0]} | {ExoticsType[0]} \n\n {ExoticsName[1]} | {ExoticsType[1]} "
              f"\n\n {ExoticsName[2]} | {ExoticsType[2]}  \n\n {ExoticsName[3]} | {ExoticsType[3]}")
    
    except AttributeError:
        pass




elif weekday in TuesWedThurs:
    print(title)
    #reminder to find a way to display a countdown and a except error for
    #keyboard interrupt 
    print("-Xur has Vanished for the time being. Check back Friday")
        


   

    



