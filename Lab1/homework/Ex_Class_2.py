from pymongo import MongoClient
uri = "mongodb://admin:admin@ds021182.mlab.com:21182/c4e"

client = MongoClient(uri)

get_db = client.get_default_database()


collect_1 = get_db["post"]

ngon_tinh_1 = {
    "title": "Tôi muốn",
    "author": "Nam Nguyễn",
    "content": "Sau 1 lần anh bị các e giết khi đang say giấc nồng.. Anh thấy dân làng chúng ta cần chung tay tiêu diệt sói Tuấn Anh và Quân... Đừng để bị chúng lừa dối nhưng người nông dân chất phác như anh chẳng hạn :)) "
    }

collect_1.insert_one(ngon_tinh_1)

