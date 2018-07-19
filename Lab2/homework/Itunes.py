from urllib.request import urlopen
from bs4 import BeautifulSoup
from youtube_dl import YoutubeDL
import pyexcel

url = "https://www.apple.com/itunes/charts/songs/"

html_content = urlopen(url).read().decode("utf-8")

choose = BeautifulSoup(html_content, "html.parser")
data = choose.find("section", "section chart-grid")

div_search = data.find("div", "section-content")
ul_search = div_search.find("ul")


li_list = ul_search.find_all("li")

songs = []

for li in li_list:
    singgle = {}
    singgle["name"] = li.h3.string
    singgle["artist"] = li.h4.string
    print (singgle)
    songs.append(singgle)
    
pyexcel.save_as(records = songs, dest_file_name = "appstore.xlsx" )



option = {
    'default_search': 'ytsearch',
    'max download': 1
}

dl = YoutubeDL(option)

se_download = []

for li in li_list:
    search = {}
    search_name = li.h3.string
    search_artist = li.h4.string
    print (search)
    se_download.append(search)
dl.download (se_download)

    