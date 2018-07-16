from pymongo import MongoClient
import matplotlib
matplotlib.use("TkAgg")
from matplotlib import pyplot


link = "mongodb://admin:admin@ds021182.mlab.com:21182/c4e"

client = MongoClient(link)

get_db = client.get_default_database()

customers = get_db["customers"]

events = get_db.customers.find({"ref": "events"}).count()
wom = get_db.customers.find({"ref": "wom"}).count()
ads = get_db.customers.find({"ref": "ads"}).count()

labels = ["events", "wom", "ads"]
values = [events,wom,ads]
colors = ["red", "gold", "green"]

pyplot.pie(values, labels=labels, colors=colors)
pyplot.axis("equal")
pyplot.show()