from jlod import database

dbi = database.connect('example').instance
client = dbi.collection('users')

# Logical Operators
#  $and
#  $or
#
# Operators
#  $eq
#  $ne
#  $gt
#  $gte
#  $lt
#  $le
#  $in
#  $nin

# result = client.find({"name":"Rabiu"})
# print(result)

# single conditions
# result = client.find({
#     "$and": {"age": {"$gte": 22}}
# })
# print(result)

# #multiple conditions
# result = client.find({
#     "$and": [{"name": {"$eq": "Rabiu"}}, {"age": {"$eq": 22}}]
#     'name': 'kehinde',
#     'age': 22
# })

# print(client.size)

#
# result = client.sort(
#     {}, {"name":1, "age":1}, limit=5
# )
# print(result);
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
# print(result)
# 

#single check, by default is OR operator
# result = client.find([{"name": {"$eq": "Rabiu"}},{"age": {"$eq": 22}}])
# print(result)
#
# search = client.limit(1)
# print(search)
#

# result = client.addMany(
#     {'name': 'Zainab', 'age': 20},
#     {'name': 'Kubra', 'age': 20}
# )

# resultSet = client.documents
# print(resultSet)

# client2.truncate
# client2.remove(name='Rabs')
# client2.drop

# result = client.get(['name','city'])
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
