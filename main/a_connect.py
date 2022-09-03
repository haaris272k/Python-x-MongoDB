import pymongo

"""PART - 1 - Connecting to MongoDB"""
# With the use of 'connection string' we can connect to the database
# The connection string is a standard URI format
# Here we are connecting to the local database server
client = pymongo.MongoClient("mongodb://localhost:27017/")


"""PART - 2 - Creating a Database and Collection"""
# Creating a database
db = client["TestDB"]
# Creating a collection
collection = db["TestCollection"]

print("Database and Collection created successfully")
