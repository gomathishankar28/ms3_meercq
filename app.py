import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for, jsonify)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
from pymongo.message import query
from werkzeug.datastructures import FileStorage
from urllib.parse import urlparse
from datetime import datetime
import cloudinary
import cloudinary.uploader
if os.path.exists("env.py"):
    import env


app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)


@app.route("/")
# Home
@app.route("/home")
def home():
    return render_template("index.html")


# Register
@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        # check if username already exists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            flash("Username already exists. Please Login if you are an existing User")
            return redirect(url_for("register"))

        register = {
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password")),
            "email": request.form.get("email")
        }
        mongo.db.users.insert_one(register)
        session["user"] = request.form.get("username").lower()

        # put the new user into 'session' cookie
        
        flash("Hi {} , your Registration is Successful!".format(request.form.get("username")))
        return render_template("index.html")
    return render_template("register.html")


# Login
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # check if username exists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            # ensure hashed password matches user input
            if check_password_hash(
                existing_user["password"], request.form.get("password")):
                    session["user"] = request.form.get("username").lower()
                    flash("Welcome, {}".format(request.form.get("username")))
                    return render_template("index.html")
            else:
                # invalid password match
                flash("Incorrect Username and/or Password")
                return redirect(url_for("login"))

        else:
            # username doesn't exist
            flash("Incorrect Username and/or Password")
            return redirect(url_for("login"))

    return render_template("login.html")


# Logout
@app.route("/logout")
def logout():
    # remove user from session cookie
    flash("You have been logged out")
    session.pop("user")
    return redirect(url_for("home"))


# Electricians
@app.route("/electricians")
def electricians():
    # Retrieve all contacts whose service type = electricians
    electrician_contacts = list(mongo.db.contacts.find(
        {"service_type": "electricians"}))
    # Calculate Average rating rounded to 1 decimal.
    rating = mongo.db.reviews.aggregate(
        [{ 
            "$group":
                {
                    "_id": "$company_name",
                    "avgRating": { "$avg": "$rating" },
        }},{
                "$addFields": 
                {
                    "avgRating": { "$round": ["$avgRating", 1] },
                },
        }]
    )
    # create list of dictionaries with company name and average rating.
    ratings = list(rating)
    reviews = list(mongo.db.reviews.find())
    # To get a list of companies which has reviews available
    review_companies = [review["company_name"] for review in reviews]
    contacts = list(mongo.db.contacts.find())
    # To get a list of all companies
    all_companies = [contact["company_name"] for contact in contacts]
    # To get a list of companies which has no reviews.
    no_review_companies = list(set(all_companies) - set(review_companies))
    return render_template(
        "electricians.html", contacts=electrician_contacts, 
        count=len(electrician_contacts), reviews=reviews, ratings=ratings, 
        review_companies=review_companies, no_review_companies=no_review_companies) 


#Carpenters
@app.route("/carpenters")
def carpenters():
    # Retrieve all contacts whose service type = electricians
    carpenter_contacts = list(mongo.db.contacts.find(
        {"service_type": "carpenters"}))
    # Calculate Average rating rounded to 1 decimal.
    rating = mongo.db.reviews.aggregate(
        [{ 
            "$group":
                {
                    "_id": "$company_name",
                    "avgRating": { "$avg": "$rating" },
        }},{
                "$addFields": 
                {
                    "avgRating": { "$round": ["$avgRating", 1] },
                },
        }]
    )
    # create list of dictionaries with company name and average rating.
    ratings = list(rating)
    reviews = list(mongo.db.reviews.find())
    # To get a list of companies which has reviews available
    review_companies = [review["company_name"] for review in reviews]
    contacts = list(mongo.db.contacts.find())
    # To get a list of all companies
    all_companies = [contact["company_name"] for contact in contacts]
    # To get a list of companies which has no reviews.
    no_review_companies = list(set(all_companies) - set(review_companies))
    return render_template(
        "carpenters.html", contacts=carpenter_contacts, 
        count=len(carpenter_contacts), reviews=reviews, ratings=ratings, 
        review_companies=review_companies, no_review_companies=no_review_companies) 


# Plumbers
@app.route("/plumbers")
def plumbers():
    plumber_contacts = list(mongo.db.contacts.find(
        {"service_type": "plumbers"}))
    rating = mongo.db.reviews.aggregate(
        [{ 
            "$group":
                {
                    "_id": "$company_name",
                    "avgRating": { "$avg": "$rating" },
        }},{
                "$addFields": 
                {
                    "avgRating": { "$round": ["$avgRating", 1] },
                },
        }]
    )
    ratings = list(rating)
    reviews =list(mongo.db.reviews.find())   
    review_companies = [review["company_name"] for review in reviews]
    contacts = list(mongo.db.contacts.find())
    all_companies = [contact["company_name"] for contact in contacts]
    no_review_companies = list(set(all_companies) - set(review_companies))
    return render_template(
        "plumbers.html", contacts=plumber_contacts, count=len(plumber_contacts), 
        reviews=reviews, ratings=ratings, review_companies=review_companies, 
        no_review_companies=no_review_companies)


# Painters
@app.route("/painters")
def painters():
    painter_contacts = list(mongo.db.contacts.find(
        {"service_type": "painters"}))
    rating = mongo.db.reviews.aggregate(
        [{ 
            "$group":
                {
                    "_id": "$company_name",
                    "avgRating": { "$avg": "$rating" },
        }},{
                "$addFields": 
                {
                    "avgRating": { "$round": ["$avgRating", 1] },
                },
        }]
    )
    ratings = list(rating)
    reviews = list(mongo.db.reviews.find()) 
    review_companies = [review["company_name"] for review in reviews]
    contacts = list(mongo.db.contacts.find())
    all_companies = [contact["company_name"] for contact in contacts]
    no_review_companies = list(set(all_companies) - set(review_companies))
    return render_template(
        "painters.html", contacts=painter_contacts, 
        count=len(painter_contacts), reviews=reviews, 
        ratings=ratings, review_companies=review_companies,
         no_review_companies=no_review_companies)
 

# Gardeners
@app.route("/gardeners")
def gardeners():
    gardener_contacts = list(mongo.db.contacts.find(
        {"service_type": "gardeners"}))
    rating = mongo.db.reviews.aggregate(
        [{ 
            "$group":
                {
                    "_id": "$company_name",
                    "avgRating": { "$avg": "$rating" },
        }},{
                "$addFields": 
                {
                    "avgRating": { "$round": ["$avgRating", 1] },
                },
        }]
    )
    ratings = list(rating)
    reviews = list(mongo.db.reviews.find())
    review_companies = [review["company_name"] for review in reviews]
    contacts = list(mongo.db.contacts.find())
    all_companies = [contact["company_name"] for contact in contacts]
    no_review_companies = list(set(all_companies) - set(review_companies))
    return render_template(
        "gardeners.html", contacts=gardener_contacts, 
        count=len(gardener_contacts), reviews=reviews, 
        ratings=ratings, review_companies=review_companies, 
        no_review_companies=no_review_companies) 


# Whitegoods
@app.route("/whitegoods")
def whitegoods():
    whitegoods_contacts = list(mongo.db.contacts.find(
        {"service_type": "whitegoods"}))
    rating = mongo.db.reviews.aggregate(
        [{ 
            "$group":
                {
                    "_id": "$company_name",
                    "avgRating": { "$avg": "$rating" },
        }},{
                "$addFields": 
                {
                    "avgRating": { "$round": ["$avgRating", 1] },
                },
        }]
    )
    ratings = list(rating)
    reviews = list(mongo.db.reviews.find())
    review_companies = [review["company_name"] for review in reviews]
    contacts = list(mongo.db.contacts.find())
    all_companies = [contact["company_name"] for contact in contacts]
    no_review_companies = list(set(all_companies) - set(review_companies))
    return render_template(
        "whitegoods.html", contacts=whitegoods_contacts, 
        count=len(whitegoods_contacts), reviews=reviews, ratings=ratings, 
        review_companies=review_companies, no_review_companies=no_review_companies)  


# Cleaners
@app.route("/cleaners")
def cleaners():
    cleaner_contacts = list(mongo.db.contacts.find(
        {"service_type": "cleaners"}))
    rating = mongo.db.reviews.aggregate(
        [{ 
            "$group":
                {
                    "_id": "$company_name",
                    "avgRating": { "$avg": "$rating" },
        }},{
                "$addFields": 
                {
                    "avgRating": { "$round": ["$avgRating", 1] },
                },
        }]
    )
    ratings = list(rating)
    reviews = list(mongo.db.reviews.find())
    review_companies = [review["company_name"] for review in reviews]
    contacts = list(mongo.db.contacts.find())
    all_companies = [contact["company_name"] for contact in contacts]
    no_review_companies = list(set(all_companies) - set(review_companies))
    return render_template(
        "cleaners.html", contacts=cleaner_contacts, count=len(cleaner_contacts), 
        reviews=reviews, ratings=ratings, review_companies=review_companies, 
        no_review_companies=no_review_companies)  


# Cloudinary uploader
def upload(file):
    app.logger.info('in upload route')
    cloudinary.config(cloud_name = os.getenv('CLOUD_NAME'), api_key=os.getenv('API_KEY'), 
        api_secret=os.getenv('API_SECRET'))
    return cloudinary.uploader.upload(file, width=180, height=160)


# Add contact
@app.route("/add_contact", methods=["GET", "POST"])
def add_contact():
    if request.method == "POST":  
        company_name = request.form.get("company_name")
        service_type = request.form.get("service_type")
        contacts = list(mongo.db.contacts.find(
        {"service_type": service_type}))
        img_upload = upload(request.files['file'])
        companies = [contact["company_name"] for contact in contacts]
        # To check if the comany name already exists for that service type
        if company_name not in companies:
            contact = {
            "service_type": request.form.get("service_type"),
            "company_name": request.form.get("company_name"),
            "mobile": request.form.get("mobile"),
            "email": request.form.get("email"),
            "url": ((request.form.get("url") if(request.form.get("url")) else "N/A")),
	        "address": ((request.form.get("address") if(request.form.get("address")) else "N/A")),
            "created_by": session["user"],
            "created_date": datetime.now().strftime("%b %d %Y"),
            "company_image": img_upload["secure_url"]
            }
            mongo.db.contacts.insert_one(contact)
            # To get the base url to be redirected
            full_url = request.referrer
            parts = urlparse(full_url)
            path =  "/{}".format(request.form.get("service_type"))
            baseurl = "{}://{}{}".format(parts.scheme, parts.netloc, path)
            flash("Your new Contact Successfully Added")
            return redirect(baseurl)
        # Display error message when adding a duplicate contact under the same service type.    
        flash("company name already exists under {} service type".format(request.form.get("service_type")))
    services = mongo.db.services.find().sort("service-type", 1)
    return render_template("add_contact.html", services=services)


# Edit Contact
@app.route("/edit_contact/<contact_id>", methods=["GET", "POST"])
def edit_contact(contact_id):
    if request.method == "POST":
        
        contact = mongo.db.contacts.find_one({"_id": ObjectId(contact_id)})
        # To retreive base url to be redirected
        full_url = request.referrer
        parts = urlparse(full_url)
        path =  "/{}".format(contact["service_type"])
        baseurl = "{}://{}{}".format(parts.scheme, parts.netloc, path)
        
        edited_contact = {
            "service_type": contact["service_type"],
            "company_name": contact["company_name"],
            "mobile": request.form.get("mobile"),
            "email": request.form.get("email"),
            "address": request.form.get("address"),
            "url": request.form.get("url"), 
            "created_by": session["user"],
            "created_date": contact["created_date"],
            "company_image": contact["company_image"]
        }
        mongo.db.contacts.update({"_id": ObjectId(contact_id)}, edited_contact)
        flash("contact Successfully Updated")
        return redirect(baseurl)
    contact = mongo.db.contacts.find_one({"_id": ObjectId(contact_id)})
    services = mongo.db.services.find().sort("service-type", 1)
    return render_template("edit_contact.html", contact=contact, services=services)
    
    
# Delete Contact
@app.route("/delete_contact/<contact_id>")
def delete_contact(contact_id):
    mongo.db.contacts.remove({"_id": ObjectId(contact_id)})
    flash("contact Successfully Deleted")
    return redirect(request.referrer)


# Add Review
@app.route("/add_review/<contact_id>", methods=["GET", "POST"])
def add_review(contact_id):
    if request.method == "POST":
        contact = mongo.db.contacts.find_one({"_id": ObjectId(contact_id)})
        # To retreive the base url to be redirected
        full_url = request.referrer
        parts = urlparse(full_url)
        path =  "/{}".format(contact["service_type"])
        baseurl = "{}://{}{}".format(parts.scheme, parts.netloc, path)
        review = {
            "rating": int(request.form.get("rating")),
            "comments": request.form.get("comments"),
            "company_name": contact["company_name"],
            # To display date and time
            "date": datetime.now().strftime("%b %d %Y %H:%M:%S"),
            "created_by": session["user"]
        }
        mongo.db.reviews.insert_one(review)
        flash("Your review has been added")
        return redirect(baseurl)
    contact = mongo.db.contacts.find_one({"_id": ObjectId(contact_id)})
    services = mongo.db.services.find().sort("service-type", 1)
    return render_template("add_review.html", contact=contact, services=services,)


# Delete Review
@app.route("/delete_review/<review_id>")
def delete_review(review_id):
    mongo.db.reviews.remove({"_id": ObjectId(review_id)})
    flash("review Successfully Deleted")
    return redirect(request.referrer)


# Search
@app.route("/search", methods=["GET", "POST"])
def search():
    query = request.form.get("query")
    contacts = list(mongo.db.contacts.find({"$text": {"$search": query}}))
    if (contacts):
        for contact in contacts:
            if contact["service_type"] == "electricians":
                return redirect(url_for('electricians'))
            elif contact["service_type"] == "painters":
                return redirect(url_for('painters'))
            elif contact["service_type"] == "plumbers":
                return redirect(url_for('plumbers'))
            elif contact["service_type"] == "cleaners":
                return redirect(url_for('cleaners'))
            elif contact["service_type"] == "gardeners":
                return redirect(url_for('gardeners'))
            elif contact["service_type"] == "whitegoods":
                return redirect(url_for('whitegoods'))
            elif contact["service_type"] == "carpenters":
                return redirect(url_for('carpenters'))
    else:
        return render_template("no_results.html")


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)       