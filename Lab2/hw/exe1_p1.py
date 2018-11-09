from urllib.request  import urlopen #(Thư viện)
from bs4 import BeautifulSoup
from collections import OrderedDict

#1. Connect to the page
url='https://www.apple.com/itunes/charts/songs'
connection = urlopen(url)

#2. Download the page content
raw_data=connection.read()
page_content=raw_data.decode("utf8")

with open("itunes.html", "wb") as f:
    f.write(raw_data)

#3 Find ROI
soup=BeautifulSoup(page_content, "html.parser")
ul=soup.find("section","section chart-grid")

#4 Extract data
li_list=ul.find_all("li")
topchart_list=[]
for li in li_list:
    title=li.h3.a.string
    artist=li.h4.a.string

    topchart=OrderedDict({
        "title":title,
        "artist":artist
    })
    topchart_list.append(topchart)
print(topchart_list)

#5 Save data
import pyexcel
pyexcel.save_as(records=topchart_list, dest_file_name="topchart.xlsx")