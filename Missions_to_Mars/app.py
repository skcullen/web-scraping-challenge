from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape_mars

# Create Flask
app = Flask(__name__)

#get connection
mongo = PyMongo(app, uri="mongodb://localhost:27017/mars_data")

@app.route("/")
def home():
    mmdata = mongo.db.mmdata.find_one()
    return render_template("index.html", mdata=mmdata)

@app.route("/scrape")
def scrape():
    mmdata = mongo.db.mmdata
    m_data = scrape_mars.scrape()
    mmdata.update({}, m_data, upsert=True)
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)