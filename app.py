from jlod import database, console
import pymongo

dbi = database.connect('example').instance
client = dbi.collection('users')

host = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = host["example"]
mongoClient = mydb["users"]
#
# response = client.exportTo(mongoClient)
# console.log(response)

# for doc in mongoClient.find():
#     console.log(doc)

# client.truncate
# response = client.importFrom(mongoClient,{})
# print(response)

# client.addMany([
#     {'name': 'Rabiu', 'age': 21},
#     {'name': 'Kehinde', 'age': 22},
#     {'name': 'Nazeh', 'age': 22},
#     {'name': 'Abel', 'age': 21}
# ])


result = client.findOne({
    'name': 'kehinde',
    'age': 22
})

print(result)
# result = client.find({
#     'name': 'kehinde',
#     'age': 22
# })

# print(client.size)

#
# result = client.distinct(
#      {'name': [
#          'Abel','Nazeh'
#      ], 'age': 21}
# )

# result = client.addMany([
#     {'name': 'Ummi', 'age': 21},
#     {'name': 'Abubakar', 'age': 20}
# ])

#
# res = client.update(['age', 'name'], [23, 'Khadija'], {
#     'name': 'Aisha'
# })
# print(res)


# res = client.remove({
#     'name': [
#         'Kubra', 'Zainab'
#     ]
# })

#
# search = client.limit(1)
# print(search)
#


import pymongo
#
# myclient = pymongo.MongoClient("mongodb://localhost:27017/")
# mydb = myclient["example"]
# mycol = mydb["users"]
# # mycol.insert_one({
# #     'name': 'Aminu',
# #     'age': 24
# # })
# for x in mycol.find():
#   print(x)


# result = client.addMany(
#     {'name': 'Zainab', 'age': 20},
#     {'name': 'Kubra', 'age': 20}
# )

# resultSet = client.documents
# print(resultSet)

# client2.truncate
# client2.remove(name='Rabs')
# client2.drop

# result = client1.get('name,age,city')
# console.log(result)

# client2.add({
#     "name": 'Aisha Yahaya',
#     "city": 'Lagos',
#     "age": 23,
# })
#
# name = client.get('name,age', age=23)
# print(name)

# search = client.find(name="Rabs")
# print(search)

# client.add({
#     "name": 'Aisha Yahaya',
#     "city": 'Lagos',
#     "age": 23,
# })

# response = client.documents
# users = client.documents
# for i in users:
#     print(i)
