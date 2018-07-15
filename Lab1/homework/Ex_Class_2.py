from pymongo import MongoClient
import matplotlib
matplotlib.use("TkAgg")
from matplotlib import pyplot


link = "mongodb://admin:admin@ds021182.mlab.com:21182/c4e"

client = MongoClient(link)

get_db = client.get_default_database()

customers = get_db["customers"]

events = get_db.customers.count({"ref": "events"})
wom = get_db.customers.count({"ref": "wom"})
ads = get_db.customers.count({"ref": "ads"})

labels = ["events", "wom", "ads"]
colors = ["red", "gold", "green"]
explode = [0, 0.1, 0.1, 0.1]

pyplot.pie(labels=labels, colors=colors, explode=explode)
pyplot.axis("equal")

pyplot.show()