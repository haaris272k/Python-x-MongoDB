from a_connect import collection, db, client

"""------------PART-5 Retrieving Documents (Data) from Collection------------"""

"""A - Retrieving a single document"""
# find_one() used to retrieve a single document,
# Based on the query (like age=24, name="John" or any other field)
# In the below example, we are retrieving a document where the name is "John" and age is 24
document1 = collection.find_one({"name": "John", "age": 24})
print("Retrieving a single document:", document1)


"""B - Retrieving multiple documents"""
# find() used to retrieve multiple documents
# We have to iterate through the result of find() to retrieve all the documents
# In the below example, we are retrieving all the documents where the name is "John"
documents = collection.find({"name": "John"})
for result in documents:
    print("Retrieving multiple documents:", result)

"""---------------------------------- Note ----------------------------------"""

# We can fetch the information from a document by hiding the ones we don't want.
# This is done by using 1 and 0 in the find() method.
# 1 means we want the field and 0 means we don't want the field.
# In the below example, we are retrieving all the documents where the name is "John" but,
# we are not fetching the age
document2 = collection.find_one({"name": "John"}, {"age": 0})
print("Retrieving a single document with name John, without age:", document2)

"""-------------------------------------------------------------------------"""
