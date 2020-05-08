from flask import Flask, render_template, jsonify, redirect
import pymongo
import scrape_mars

# create instance of Flask app

app = Flask(__name__, template_folder='./')
conn = 'mongodb://localhost:27017' 

client = pymongo.MongoClient(conn)
db = client.mars_database

#  create route that renders index.html template
@app.route("/")
def index():
    mars = [data for data in db.mars.find()]
    return render_template("index.html", mars = mars[0])

@app.route("/scrape")
def scrape():
    mars = db.mars
    mars_data = scrape_mars.scrape()
    mars.update({}, mars_data, upsert=True)
    return redirect("/", code=302)

if __name__ == "__main__":
    app.run(debug=True)



#If code above does not run properly, run this code below
# from flask import Flask, render_template
# from flask_pymongo import PyMongo
# import scrape_mars
# app = Flask(__name__)
# # Use flask_pymongo to set up mongo connection
# app.config["MONGO_URI"] = "mongodb://localhost:27017/mars_app"
# mongo = PyMongo(app)
# # Or set inline
# # mongo = PyMongo(app, uri="mongodb://localhost:27017/mars_app")
# @app.route("/")
# def index():
#     mars = mongo.db.mars.find_one()
#     return render_template("index.html", mars=mars)
# @app.route("/scrape")
# def scrape():
#     mars = mongo.db.mars
#     mars_data = scrape_mars.scrape_all()
#     mars.replace_one({}, mars_data, upsert=True)
#     return "Scraping Successful!"
# if __name__ == "__main__":
#     app.run()


       