#pymongo is module in python to handle mongodb database
import pymongo
from pymongo import MongoClient

#take this urel from mongodb website after creation of cluster
cluster= MongoClient("mongodb+srv://k2p1020:@cluster0-bjlzs.mongodb.net/test?retryWrites=true&w=majority")
#cluster-->db--->collection
#cluster-->School--->Student
db=cluster["School"]
collection=db["Student"]
#write data to be insert in json format
json1={"_id":"1","Name":"ketan","Age":"19","Std":"12","Marks":"92","Gender":"Male"}
json2={"_id":"2","Name":"lav","Age":"19","Std":"12","Marks":"82","Gender":"Male"}
json3={"_id":"3","Name":"darshana","Age":"19","Std":"12","Marks":"99","Gender":"Female"}
#insert data using insert_many() method
#insert_one() method use to insert only one document in collection of db
collection.insert_many([json1,json2,json3])

#to find doccument in collection having id 3 and print it
results=collection.find({"_id":"3"})
print(results)
#above command will give output as:<pymongo.cursor.Cursor object at 0x0000012BB102C100>
#to get name of searched document
for result in results:
    print(result["Name"])
#above loop may give error like connection loss due to more time requirement to search and find 
#this can be solved by adding 0.0.0.0/0 neetwork in below path
#*Your Mongo cluster* -> Security -> Network Access -> IP Whitelist -> Add IP Address


#to delete onne document in collection
#to many delete_many()
collection.delete_one({"_id":"0"})

#to update one document in collection
#collection.update_one({condition},{"$set":{to be update/addnew}})
collection.update_one({"_id":"3"},{"$set":{"Name":"Darshika"}})

#count number of documents in collection
count=collection.count_documents()
print("Number of documents in collection are:",count)