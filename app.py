import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env


app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)


@app.route("/")
@app.route("/home")
def home():
    return render_template("index.html")


@app.route("/services")
def services():
    services = mongo.db.services.find()
    return render_template("services.html", services=services)


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

        # put the new user into 'session' cookie
        session["user"] = request.form.get("username").lower()
        flash("Hi {} , your Registration is Successful!".format(request.form.get("username")))
        return render_template("login.html")
    return render_template("register.html")


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

@app.route("/logout")
def logout():
    # remove user from session cookie
    flash("You have been logged out")
    session.pop("user")
    return redirect(url_for("home"))


@app.route("/electicians")
def electricians():
    electrician_contacts = mongo.db.contacts.find(
        {"service_type": "electricians"})
    return render_template("electricians.html", contacts=electrician_contacts, count=electrician_contacts.count())   


@app.route("/carpenters")
def carpenters():
    carpenter_contacts = mongo.db.contacts.find(
        {"service_type": "carpenters"})
    return render_template("carpenters.html", contacts=carpenter_contacts, count=carpenter_contacts.count()) 


@app.route("/plumbers")
def plumbers():
    plumber_contacts = mongo.db.contacts.find(
        {"service_type": "plumbers"})
    return render_template("plumbers.html", contacts=plumber_contacts, count=plumber_contacts.count()) 


@app.route("/painters")
def painters():
    painter_contacts = mongo.db.contacts.find(
        {"service_type": "painters"})
    return render_template("painters.html", contacts=painter_contacts, count=painter_contacts.count()) 


@app.route("/gardeners")
def gardeners():
    gardener_contacts = mongo.db.contacts.find(
        {"service_type": "gardeners"})
    return render_template("gardeners.html", contacts=gardener_contacts, count=gardener_contacts.count()) 


@app.route("/whitegoods")
def whitegoods():
    whitegoods_contacts = mongo.db.contacts.find(
        {"service_type": "whitegoods"})
    return render_template("whitegoods.html", contacts=whitegoods_contacts, count=whitegoods_contacts.count()) 


@app.route("/cleaners")
def cleaners():
    cleaner_contacts = mongo.db.contacts.find(
        {"service_type": "cleaners"})
    return render_template("cleaners.html", contacts=cleaner_contacts, count=cleaner_contacts.count()) 


@app.route("/add_contact", methods=["GET", "POST"])
def add_contact():
    if request.method == "POST":
        contact = {
            "service_type": request.form.get("service_type"),
            "company_name": request.form.get("company_name"),
            "mobile": request.form.get("mobile"),
            "email": request.form.get("email"),
            "url": request.form.get("url"),
	        "address": request.form.get("address"),
            "rating": request.form.get("rating"),
            "created_by": session["user"]
        }
        mongo.db.contacts.insert_one(contact)
        flash("Your new Contact Successfully Added")
        return redirect(url_for('home', _anchor='services-section'))

    services = mongo.db.services.find().sort("service-type", 1)
    ratings = ["1", "2", "3", "4", "5"]
    return render_template("add_contact.html", services=services, ratings=ratings)


@app.route("/edit_contact/<contact_id>", methods=["GET", "POST"])
def edit_contact(contact_id):
    if request.method == "POST":
        edited_contact = {
            "service_type": request.form.get("service_type"),
            "company_name": request.form.get("company_name"),
            "mobile": request.form.get("mobile"),
            "email": request.form.get("email"),
            "address": request.form.get("address"),
            "url": request.form.get("url"),
            "rating": request.form.get("rating"),
            "created_by": session["user"]
        }
        mongo.db.contacts.update({"_id": ObjectId(contact_id)}, edited_contact)
        flash("contact Successfully Updated")
        return redirect(url_for('home', _anchor='services-section'))

    contact = mongo.db.contacts.find_one({"_id": ObjectId(contact_id)})
    services = mongo.db.services.find().sort("service-type", 1)
    ratings = ["1", "2", "3", "4", "5"]
    return render_template("edit_contact.html", contact=contact, services=services, ratings=ratings)
    
    
@app.route("/delete_contact/<contact_id>")
def delete_contact(contact_id):
    mongo.db.contacts.remove({"_id": ObjectId(contact_id)})
    flash("contact Successfully Deleted")
    return redirect(url_for("electricians"))


@app.route("/search", methods=["GET", "POST"])
def search():
    query = request.form.get("query")
    contacts = list(mongo.db.contacts.find({"$text": {"$search": query}}))
    return render_template("services.html", contacts=contacts)


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
        