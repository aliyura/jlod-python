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
# })
# print(result)

#single check, by default is OR operator
# result = client.find([{"name": {"$eq": "Rabiu"}},{"age": {"$eq": 22}}])
# print(result)


result= client.sort({},{"age":1})
print(result)
