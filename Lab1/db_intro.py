from pymongo import MongoClient
uri = "mongodb://protector:admin123@ds235431.mlab.com:35431/c4e19-lab"

# 1: connect database
client = MongoClient(uri)

# 2: Get database
db = client.get_default_database()

# 3: Creat Collection (tạo ra các tủ)
games = db['games']
study = db['study']

# # 4: Creat Document
# new_x = {
#     "name": "Study",
#     "description": "Hoc"
# }
# # 5: Insert Document into Collection
# games.insert_one(new_x)

# get all documents
all_study = study.find()

print(all_study[0])


