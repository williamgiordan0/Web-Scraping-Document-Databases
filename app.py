from flask import Flask, render_template, jsonify, redirect
#import pymongo
from flask_pymongo import PyMongo
import scrape_mars

# create instance of Flask app

app = Flask(__name__)
#conn = 'mongodb://localhost:27017' 

#client = pymongo.MongoClient(conn)
#db = client.mars_database

# Use flask_pymongo to set up mongo connection
app.config["MONGO_URI"] = "mongodb://localhost:27017/mars"
mongo = PyMongo(app)

#  create route that renders index.html template
@app.route("/")
def index():
    print("root route")
    #mars = [data for data in db.mars.find()]
    mars = mongo.db.mars.find_one()
    return render_template("index.html", mars=mars)

@app.route("/scrape")
def scraper():
    print("scrape route")
    #mars = db.mars
    mars = mongo.db.mars
    mars_data = scrape_mars.scrape()
    mars.update({}, mars_data, upsert=True)
    return redirect("/", code=302)

if __name__ == "__main__":
    app.run(debug=True)