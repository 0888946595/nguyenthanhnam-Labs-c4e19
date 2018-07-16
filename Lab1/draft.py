from pymongo import MongoClient
import matplotlib
from matplotlib import pyplot
matplotlib.use("TkAgg")
uri = "mongodb://admin:admin@ds021182.mlab.com:21182/c4e"

#Connect to database
client = MongoClient(uri)

#Get database
db = client.get_default_database()

#Creat collection
search = db.customers

#Tìm kiếm ,phân loại và đếm 
count_eve = 0
count_wom = 0
count_ads = 0

'''C1: Anh Quân kiểm tra giúp em cách này với ạ !!! Hình như em sử dụng sai hàm find() nên cách này ko ra được kết quả !!!'''
# searchs = search.find()
# for i in range(6969):
#     if searchs[i]['ref'] == "events" :
#         count_eve+=1
#     elif searchs[i]['ref'] == "wom":
#         count_wom+=1
#     elif searchs[i]['ref'] == "ads":
#         count_ads+=1
#     else:
#         continue

'''C2:sử dụng hàm count() '''
count_ads = search.find({"ref": "ads"}).count()
count_eve = search.find({"ref": "events"}).count()
count_wom = search.find({"ref":"wom"}).count()

print("events: {0} , ads : {1} , won: {2}".format(count_eve,count_ads,count_wom))



""" Vẽ Hình:"""
#Tên + tỉ lệ
labels = ["ads","events","wom"]
values = [count_ads,count_eve,count_wom]

#Thêm màu
colors = ["red","blue","green"]

#Sử dụng pie chart trong thư viện matplotlib
pyplot.pie(values,
           labels=labels,
           colors=colors)

#Diều chỉnh tỉ lệ 2 trục
pyplot.axis("equal")

#Show to screen ^^
pyplot.show()
