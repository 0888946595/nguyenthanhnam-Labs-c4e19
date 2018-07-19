# 1. download webpage 
from urllib.request import urlopen
from bs4 import BeautifulSoup
import pyexcel
url = "http://dantri.com/"
    # # 1.1 Open a connection
    # conn = urlopen(url)
    # # 1.2 Read data
    # data = conn.read()
    # print(data)
    # # 1.3 Decode
    # html = data.decode("utf-8")
    # print (html)
html_content = urlopen(url).read().decode("utf-8")

# f = open("dantri.html", "wb")
# f.write(html_content)
# f.close()

# save to file
    # import urllib.request
    # check = urllib.request.urlretrieve(url, "dantri.html")
# 2. Extract ROI (Region Of interest)
# html, xml, xhtml
soup = BeautifulSoup(html_content, "html.parser")
ul = soup.find("ul", "ul1 ulnew")
# print(ul.prettify())

# 3. Extract info 
li_list = ul.find_all("li")

d = []
for li in li_list:
    a = li.h4.a 
    title = a.string
    href = url + a["href"]
    print(href)
    d.append({"title": title,
             "href": href})
# print(title)
# print(href)




# 4. Save data to excel

pyexcel.save_as(records = d, dest_file_name = "dantri_list.xlsx" )
    