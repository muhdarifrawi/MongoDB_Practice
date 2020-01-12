from flask import Flask, render_template, request, redirect, url_for
import os
import pymongo
import re

app = Flask(__name__)

MONGO_URI = "mongodb+srv://arifrawi:madgecko91@cluster0-jv1uk.mongodb.net/test?retryWrites=true&w=majority"
DATABASE_NAME = "sample_airbnb"

def get_connection():
    conn = pymongo.MongoClient(MONGO_URI)
    return conn
      
@app.route("/")
def index():
    search_terms = request.args.get('search-by')

    search_criteria = {}
    
    if search_terms is not None:
        
        search_criteria["name"] = re.compile(r'{}'.format(search_terms), re.I)
    
    conn = get_connection()
    cursor = conn[DATABASE_NAME]["listingsAndReviews"].find(search_criteria).limit(10)
    return render_template("index.template.html", results=cursor)

#"magic code" - - boilerplate
if __name__ == "__main__":
   app.run(host=os.environ.get("IP"),
      port=int(os.environ.get("PORT")),
      debug=True)
      
