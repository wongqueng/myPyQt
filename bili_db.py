from pymongo import MongoClient
class bili_DB:
    def __init__(self):
        self.client = MongoClient('localhost', 27017)
        self.db = self.client["bilibili"]
    def __getitem__(self, url):
        video=self.db.videos.find_one({"_id":url})
        if video:
            return video
        else:
            raise KeyError(url+" not exist")
    def __setitem__(self, url, video):
        self.db.videos.update({"_id": url}, {"$set": {"title":video.title,"up_name":video.up_name,"watches":video.watches,"bullets":video.bullets,"up_time":video.up_time}}, upsert=True)

# db.web.insert_one({"name":"huang","age":27})
# print db.web.find({"name":"huang"}).count()
# client.close()
