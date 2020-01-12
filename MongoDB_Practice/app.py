import pymongo

MONGO_URI = "mongodb+srv://arifrawi:madgecko91@cluster0-jv1uk.mongodb.net/test?retryWrites=true&w=majority"
DATABASE_NAME = "sample_airbnb"

conn = pymongo.MongoClient(MONGO_URI)

results = conn[DATABASE_NAME]["listingsAndReviews"].find().limit(5)
for each_result in results: 
    print("Name:", each_result["name"])
    print("Beds:", each_result["beds"])