import pymongo

myclient = pymongo.MongoClient("mongodb://127.0.0.1:27017")

dblist = myclient.list_database_names()

if 'test' in dblist:
    print('The database exists')

mydb = myclient["test"]

colList = mydb.list_collection_names()
if 'customers' in colList:
    mycol = mydb['customers']
    print('The collection exists')


# Find the first document in the customers collection:
firstRecord = mycol.find_one()
print(firstRecord)

# Find all records from customer collection
for record in mycol.find():
    print(record)

# Return only the names and addresses, not the _ids
for record in mycol.find({},{"_id":0, "first_name": 1, "address": 1}):
    print(record)

# When finding documents in a collection, you can filter the result by using a query object.
# The first argument of the find() method is a query object, and is used to limit the search

myquery = {"address.city":"Boston"}

mydoc = mycol.find(myquery)

for record in mydoc:
    print(record)

# To make advanced queries you can use modifiers as values in the query object.
# E.g. to find the documents where the "age" field is lesser than 40, use the leser than modifier : { "$lt" : 40 };

myquery = { "age": { "$lt" : 40 } }

mydoc = mycol.find(myquery)

for record in mydoc:
    print(record)

# To find only the documents where the "first_name" starts with letter 'J", use the regular expression {"$regex": "^J"}

myquery = { "first_name": {"$regex": "^J" } }

mydoc = mycol.find(myquery)

for record in mydoc:
    print(record)

# Use the sort() method to sort the result in ascending or descending order.
# The sort() method takes one parameter for "fieldname" and one parameter for "direction" (ascending is the default direction)

mydoc = mycol.find().sort("first_name")

for record in mydoc:
    print(record) 

# Now in descending order
mydoc = mycol.find().sort("first_name",-1)

for record in mydoc:
    print(record) 


# To delete one document, we use the delete_one() method.
# The first parameter fo the delete_one() method is a query object defining which document to delete

# myquery = {"address.city":"Boston"}
# mycol.delete_one(myquery)

# To delete more than one document, use the delete_many() method.
# The first parameter of the delete_many() method is a query object defining which document to delte

# myquery = { "fist_name": { "$regex": "^J" } }
# countofRecordDeleted = mycol.delete_many(myquery)
# print(countofRecordDeleted.deleted_count, "documents deleted.")

# To delete all documents in a collection, pass an empty query object to the delete_many() method:
# countofRecordDeleted = mycol.delete_many({})
# print(countofRecordDeleted.deleted_count, " documents deleted.")

# You can delete a table or collection as is called in MongoDB, by using the drop() method
# mycol.drop()

# You can update a record, or document as it is called in MongoDB, by using the update_one() method.
# The first parameter of the update_one() method is query object defining which document to update.
# The second parameter is an object defining the new values of the document.

# Change the adderess 'address': 'street': '22 School st' to 'address': 'street': '21 School st'

myquery = { "address.street" : "22 School st" }
newValues = { "$set" : {"address.street" : "21 School st" } }

mycol.update_one(myquery, newValues)

for document in mycol.find():
    print(document)

# To update all documents that meets the criteria of the query use the update_man() method
# myquery = { "first_name" : { "$regex" : "^J" } }
# newValues = { "$set" :  "XYX" }

# updatedDocCount = mycol.update_many(myquery, newValues)
# print(updatedDocCount.modified_count, "documents updated")

# To limit the result in MongoDB, use the limit() method
# The limit() method takes one parameter, a number defining how many documents to return
# Limit the result to only return 5 documents:
myresult = mycol.find().limit(5)
for document in myresult:
    print(document)