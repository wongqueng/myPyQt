import pymongo

client=pymongo.MongoClient('localhost',27017)
db=client["bilibili"]
# db["videos"].drop()
cursor= db["videos"].find().sort("watches", pymongo.DESCENDING)
for i in cursor:
    print str(i["watches"])+"  "+i["title"]+"  "+i["_id"]
# client.close()
