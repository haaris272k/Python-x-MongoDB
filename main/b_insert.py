from a_connect import collection, db, client

"""------------PART-3 Inserting Document (Data) into Collection------------"""

"""A - Inserting a single document"""
# Creating a document
document = {"name": "John", "age": 24, "address": "New York"}
# insert_one() used to insert a single document
collection.insert_one(document)

"""B - Inserting multiple documents"""
# Creating multiple documents
# A list of dictionaries is created to store multiple documents
documents = [
    {"name": "John", "age": 25, "address": "New York"},
    {"name": "Larry", "age": 26, "address": "California"},
    {"name": "Steve", "age": 27, "address": "Texas"},
    {"name": "John", "age": 38, "address": "Florida"},
    {"name": "Peter", "age": 29, "address": "New Jersey"},
]
# insert_many() used to insert multiple documents
collection.insert_many(documents)
print("Documents inserted successfully")

"""-------------------------------- Note ---------------------------------"""

"""Note - Every document must have a unique _id field which acts as 
a primary key(Object_ID). If the _id field is not specified, then MongoDB 
will add one unique _id field for each document. The user can specify 
the _id field manually,as well."""

# Example
# Creating a document
document = {"_id": 7, "name": "John", "age": 30, "address": "New York"}
# Inserting the document into the collection
collection.insert_one(document)

"""---------------"PART-4 View the databases and collections---------------"""

# List all the databases
print("List of all the databases:", client.list_database_names())
# List all the collections
print("List of all the collections:", db.list_collection_names())

"""-------------------------------------------------------------------------"""
