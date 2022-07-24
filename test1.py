import pymongo

client = pymongo.MongoClient("mongodb+srv://ineuron:bikram5012013@cluster0.t2uiqfd.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)

d = {
    "name": "bikram",
    "email": "bikramjit@abc.com",
    "surname": "lahiry"
}
db1 = client['mongotest']
coll= db1['test1']
coll.insert_one(d)