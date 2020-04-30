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

# client.addMany([
#     {"name": 'Aisha',"city": 'Lagos',"age": 23},
#     {"name": 'Amina',"city": 'Lagos',"age": 24},
#     {"name": 'Zainab',"city": 'Lagos',"age": 25},
#     {"name": 'Rabiu',"city": 'Lagos',"age": 23}
# ])

#
# result = client.find({})
# print(result)

# result = client.distinct()


# single conditions
# result = client.find({
#     "$and": {"name": {"$eq": "Rabie"}}
# })
# print(result)

# #multiple conditions
result = client.find({
    "$and": [{"name": {"$eq": "Rabie"}}, {"name": {"$eq": "Jhon"}}]
})
print(result)

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

# single check, by default is OR operator
# result = client.find([{"name": {"$eq": "Rabiu"}},{"age": {"$eq": 22}}])
# print(result)
#
# search = client.limit(1)
# print(search)
#
# resultSet = client.documents

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
