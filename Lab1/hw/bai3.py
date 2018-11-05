from pymongo import MongoClient
uri='mongodb://admin:admin@ds021182.mlab.com:21182/c4e'

client=MongoClient(uri)

db = client.get_database()

posts = db["posts"]

new_post={
    'title': 'Cảm nhận',
    'author': 'Tuấn',
    'content': 'giáo viên nhiệt tình , lớp học hăng say',
}

posts.insert_one(new_post)