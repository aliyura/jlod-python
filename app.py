from jlod import database

dbi = database.connect('example').instance
client = dbi.collection('users')

result = client.documents
print(result)
