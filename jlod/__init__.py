import os
import json
import ast
import string
import random
from json import JSONDecodeError
from os import path


class Database:
    db = None
    db_path = None
    db_collection = None
    db_default_path = 'jlod/databases'
    db_dictionary = None
    DBManager = None

    def __init__(self, db_path=db_default_path, dbi=db, collection=db_collection):
        if db_path.__eq__(self.db_default_path):
            self.db_path = self.db_default_path
        else:
            self.db_path = db_path
        self.db = dbi
        self.db_collection = collection
        self.DBManager = DatabaseManager(self.db_collection)
        self.db_dictionary = {
            "documents": [
            ]
        }

    @property
    def instance(self):
        return Database(self.db_path, self.db)

    def connect(self, db_name=None):
        db_connection = False
        if not str(db_name).endswith('.db'):
            self.db = self.db_path + '/' + db_name + '.db'

        try:
            if db_name is not None:
                if not os.path.exists(self.db):
                    os.makedirs(self.db)
                    console.log('Database [' + db_name + '] created at [' + self.db_path + ']')
                    db_connection = True
                else:
                    db_connection = True
            else:
                db_connection = False
                console.log('Oops! Unable to find database ' + db_name)

        except FileNotFoundError and OSError:
            console.log('Oops! Unable to initialize local database ' + db_name + ' at ' + self.db_path)
            return db_connection
        else:
            return Database(self.db_path, self.db)

    def collection(self, collection_name=""):
        if collection_name is not None:

            if not collection_name.endswith('.collection'):
                collection_name = collection_name + '.collection'

            col = self.db + '/' + collection_name
            self.db_collection = col
            open(col, 'a+')  # create collection

            if path.exists(col):
                return Database(self.db_path, self.db, col)
            else:
                console.log('Unable to create collection' + collection_name)
                return None
        else:
            print('Oops! No collection provided')

    def override(self, obj: dict):
        document: dict
        if dict is not None:
            documentId = self.DBManager.generateId()
            obj.__setitem__('id', documentId)
            dictionary = self.db_dictionary.get('documents')
            dictionary.append(obj)
            self.DBManager.write(self.db_dictionary)
            return True
        else:
            print('No data found!')
            return False

    def add(self, obj: dict):
        document: dict
        if dict is not None:

            if os.path.getsize(self.db_collection) == 0:
                self.override(obj)
            else:
                document = self.DBManager.read()
                documentId = self.DBManager.generateId()
                obj.__setitem__('id', documentId)
                document.append(obj)
                dictionary = {
                    'documents': document
                }
                self.DBManager.write(dictionary)
            return True
        else:
            print('No data found!')
            return False

    def addMany(self, documents: []):
        try:
            for document in documents:
                self.add(document)
            console.log(str(len(documents)) + ' documents added')
        except:
            return False
        else:
            return True

    @property
    def documents(self):
        document: dict
        document = self.DBManager.read()
        return document

    @property
    def count(self):
        document: dict
        document = self.DBManager.read()
        return document.__len__()

    @property
    def truncate(self):
        self.DBManager.truncate()
        return True

    @property
    def drop(self):
        try:
            os.remove(self.db_collection)
        except FileNotFoundError:
            print("Collection " + self.db_collection + "  not found ")
        else:
            return True

    @property
    def size(self):
        self.DBManager = DatabaseManager(self.db_collection)
        return self.DBManager.getSize()

    def removeAll(self):
        self.DBManager.truncate()

    def update(self, search=[], replacement=[], conditions=dict):

        document: dict
        document = self.DBManager.read()
        if conditions.__len__() <= 0:
            document = self.DBManager.read()
        else:
            document = self.DBManager.search(conditions)

        index = 0
        for doc in document:
            for s in search:
                if s in doc:
                    print(str(s) + ':' + str(replacement[index]))
                    doc[s] = replacement[index]
                    index = index + 1

        for doc in document:
            print(doc.get('id'))

    def remove(self, conditions: dict):
        try:
            if conditions.__len__() <= 0:
                self.truncate
            else:
                document = self.DBManager.read()
                resultSet = self.DBManager.search(conditions)
                for doc in resultSet:
                    document.remove(doc)
                dictionary = {
                    'documents': document
                }
                self.DBManager.write(dictionary)

        except():
            return False
        else:
            return True

    def get(self, key: str, conditions: dict):
        document: dict
        resultSet = []
        if conditions.__len__() <= 0:
            document = self.DBManager.read()
        else:
            document = self.DBManager.search(conditions)

        if key.__ne__("") and key is not None:
            if key.__ne__("*"):
                if str(key).__contains__(','):
                    keys = str(key).split(',')
                    for doc in document:
                        for key in keys:
                            if key in doc.keys():
                                resultSet.append(doc[key])
                else:
                    for doc in document:
                        if key in doc.keys():
                            resultSet.append(doc[key])
            else:
                resultSet = document
            return resultSet
        else:
            return document

    def distinct(self, conditions: dict):
            if conditions is not None:
                document = self.DBManager.search(conditions)
            else:
                document = self.DBManager.read()
            resultSet = []
            for x in document:
                if x not in resultSet:
                    resultSet.append(x)
            return(resultSet)

            
    def exportTo(self, mongo_collection: classmethod, conditions={}):
        self.DBManager = DatabaseManager(self.db_collection)
        try:
            import pymongo
            documents: dict
            if conditions.__len__() > 0:
                documents = self.DBManager.search(conditions)
            else:
                documents = self.DBManager.read()
            mongo_collection.insert_many(documents)
        except ImportError:
            console.log('Oops! Unable to find MangoDB')
            return False
        else:
            return True

    def importFrom(self, mongo_collection: classmethod, conditions: dict):
        self.DBManager = DatabaseManager(self.db_collection)
        doc: dict
        try:
            import pymongo
            documents: dict
            if conditions.__len__() > 0:
                documents = mongo_collection.find({}, conditions)
            else:
                documents = mongo_collection.find({}, conditions)
            for doc in documents:

                if '_id' in doc.keys():
                    doc.pop('_id')
                if 'id' in doc.keys():
                    doc.pop('id')
                if doc.__len__() > 0:
                    self.add(doc)
        except ImportError as error:
            console.log('Oop! Unable to find MangoDB')
            return [error]
        else:
            return self.DBManager.read()

    def findOne(self, conditions: dict, limit=0):
        self.DBManager = DatabaseManager(self.db_collection)
        if conditions:
            documents = self.DBManager.search(conditions)
        else:
            documents = self.DBManager.read()

        print(documents)  # this is the dictionary to work with

    def find(self, conditions: dict, limit=0):
        self.DBManager = DatabaseManager(self.db_collection)
        if conditions:
            documents = self.DBManager.search(conditions)
        else:
            documents = self.DBManager.read()

        if limit != 0:
            limitedDocuments = []
            limiter = 0
            if documents.__len__() >= limit:
                for doc in documents:
                    if limiter < limit:
                        limitedDocuments.append(doc)
                        limiter = limiter + 1
                return limitedDocuments
            else:
                return documents
        else:
            if conditions:
                return self.DBManager.search(conditions)
            else:
                return documents


class DatabaseManager:
    db_collection = None

    def __init__(self, collection=db_collection):
        self.db_collection = collection

    def generateId(self):
        return ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(30))

    def getSize(self):
        st = os.stat(self.db_collection)
        return st.st_size

    def truncate(self):
        collection = open(self.db_collection, 'r+')
        collection.truncate()
        collection.close()

    def write(self, document: dict):
        collectionWriter = open(self.db_collection, 'w')
        collectionWriter.write(str(document))
        collectionWriter.close()

    def read(self):
        try:
            collectionReader = open(self.db_collection, 'r')
            document = collectionReader.read()
            if document.__ne__(''):
                document = document.replace("'", "\"")
                document = json.loads(document)
            else:
                document = {
                    "documents": [
                    ]
                }
        except JSONDecodeError as error:
            return [error]
        else:
            return document.get('documents')
    


    def search(self, conditions: dict, ):
        document = self.read()
        resultSet = []
        for doc in document:
            for s in conditions.items():
                key = str(s[0])
                value = str(s[1])
                if str(value).__contains__('[') and str(value).__contains__(']'):
                    values = ast.literal_eval(value)
                    for val in values:
                        if key in doc:
                            if str(doc[key]).lower() == val.lower():
                                if doc not in resultSet:
                                    resultSet.append(doc)
                else:
                    if str(doc[key]).lower() == value.lower():
                        if doc not in resultSet:
                            resultSet.append(doc)

        return resultSet


class Console:
    def log(self, msg):
        print(msg)


console = Console()
database = Database()
