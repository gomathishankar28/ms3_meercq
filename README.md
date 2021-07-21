# [MeerCQ](https://gomathishankar28.github.io/ms3_meercq/)

This is a website that provides contact details of variety of services like electricians, plumbers,
carpenters, painters, gardeners, whitegoods and cleaners in Meerhoven in one place. As the name suggests, MeerCQ( which means Meerhoven people seek you) 
is a platform where people can find the contact of a professional for all the chores at home without any hassle.
**MeerCQ** is an educational project that serves as the **Milestone Project 3** for the **Full-Stack Software Developer programme** powered by **Code Institute**.

## Table of Contents
  - [Demo](#demo)
  - [Introduction](#introduction)
  - [UX](#ux)
    - [Business Goals](#business-goals)
    - [User Goals](#user-goals)
    - [User Stories](#user-stories)
    - [Strategy](#strategy)
    - [Scope](#scope)
    - [Structure](#structure)
    - [Skeleton](#skeleton)
    - [Surface](#surface)
  - [Features](#features)
  - [Technologies Used](#technologies-used)
  - [Testing](#testing)
  - [Deployment](#deployment)
  - [Credits](#credits)
  - [Acknowledgements](#acknowledgements)

## Demo 
[Live Website](https://meercq.herokuapp.com/)

![AmIResponsive](https://github.com/gomathishankar28/ms3_meercq/blob/master/static/images/readme/amiresponsives.jpg?raw=true)

### Introduction

MeerCQ gathers recommendations shared in public conversations on social media. It aims to create contact listings for
 recommended pros, so that the customers can easily see referrals from across social media, in one handy location.
 Customers can find a professional to contact for small jobs in and around the house.

The reason to promote this business model is because when there is a problem with any of the service at home,
it is very difficult to find an appropriate contact on time. Users refer to google and find some available contact which will not ensure 
a reliable service. MeerCQ aims at collecting the details and contacts  for such services based on experience from other users which 
ensures a reliable service.

The site enables the registered users to create, Read, Update and Delete (CRUD) contacts. The site also provides a platform to share
the user reviews for each contact, based on which the customers can choose a best contact professional from the list of available contacts.


### Business Goals
*   To target the expat community who are looking for handyman professionals for their home needs.

*   To evince interest in customers who wants to find contacts for all home services in one place.

*   To bring this offering to all the expats who are new to this place and doesn't have any contacts to reach to in case of a problem at home.

*   Provide a single, standard way to find the contact of professionals for all the basic home services.

*   To comprehensively list the available contacts under each service type.

*   Build a brand image for contact directory for all home services in Meerhoven

*   Clearly communicate the contact information for every company under each service type.

### user Goals

As a customer, I would like 

*   To know what kind of information, MeerCQ can Provide. 

*   To know the list of services for which contacts is provided

*   To know the name, contact number, address,emailID of each contact for further communication

*   To see the user reviews for each company,so that i can pick the best choice up. 

##  User stories
*   As a prospective customer to the website, I want to easily navigate the site, so that I can easily find the details about MeerCQ so that I am assured about their service.

*   As a prospective customer to the website, I want to precisely know what services are offered so that I have enough information to avail their service.

*   As a prospective customer to the website, I should be able to search based on keywords so that I can get the desired information quickly.

*   As a prospective customer, I would like to receive suggestions in the search field so that I can narrow down my search easily.

*   As a prospective customer, I should be able to avail the contacts of services from a list as well as through visual tiles so that this information is easily accessible.

*   As a new customer to the website, I want to know for what kind of services, the contact details are provided.

*   As a new customer, I want to know the contact details of service providers based on the service type chosen, so that I do not see contacts of services that I do not need.

*   As a new customer to website, I want to know how many contacts are available under each service.

*   As a customer to the website, I want to know the name of the person/company as part of the contact details.

*   As a customer, I would like to know the address of the company so that I have the physical location to reach in case of any issues.

*   As a customer, I would like to know the mobile number in order to contact and fix an appointment.

*   As a customer, I would like to know the email ID of the Service provider for future correspondences and invoice sharing.

*   As a customer who has experience with a particular service provider, I would like to provide a rating so that I can quantify my recommendation to other users.

*   As a customer, I would like to see an average rating for each contact that would help me to choose a better professional service provider.

*   As a Prospective customer I want to add a new contact to a particular service when I find a new reliable contact so that the other users can profit from my experience.

*   As a prospective customer to the website, I want to edit all the contact details of the service provider so that the other users have the latest information about the service provider.

*   As a prospective customer to the website, I want provide feedback /comments about each service provider so that it helps other users to choose the best contact from the available list.

*   As an Administrator to the website, I want to delete a contact which is fake, never exists or stopped providing any service.

*   As an administrator I want to provide the option of user log in so that changes done to contacts are tracked.

*   As an administror, the system should allow new contacts to be added only by registered user so that there is accountability on the records created.

*   As an Administrator, I would like to restrict only the logged in users to edit a contact or add a comment so that unauthorized/ untraceable changes are prevented.

*   As an administrator, only registered users with a valid password should be allowed to log in so that unauthorized changes can be prevented.

*   As an administrator, both unregistered and registered users should be able to view the contact of service providers and the user reviews so that the display of information is not restricted for unregistered users.

*   As an administrator, I should allow registered users to log out so that unauthorized accesses are prevented.

*   As an administrator, I would like to have field level validations on the contact entry so that incorrect or incomplete information is avoided.
 

## UX
### Ideal client
#### The ideal client for this business is:
*   Residing in the Netherlands.
*   Has good social contacts across the neighbourhood.
*   Wants to create a directory of contacts for handyman professionals.
*   English speaking.

#### Visitors to this website are searching for:
*   Contacts of Handyman professionals for different services.
*   A contact who is reliable and is referred by their neighbours
*   All handyman contacts in and around the neighbourhood for all services in one place
*   A place where they can add new contacts, edit existing contacts
*   An option to write reviews for each contact.

#### This Website is the best way to help the user and the owner because:
Be it any place , for an expat, finding a handyman professional for any service is extremely difficult as people are not aware about reliable contacts. All they could do is search in google for any available contact. Currently this is being done via watsapp where the expat community in neighbourhood form a group and then share contacts when there is a need. This website will serve as a single point of reference for all the home needs.

### Strategy
Build brand awareness for a directory of handyman contacts in the neighbourhood
Through this website , clearly communicate the services for which contacts are available
Provide an easy option for users to quickly look for a contact for a particular service
Maintain all contact information in one place.
Aim to increase the number of reliable contacts for different services based on customer reviews.

### Scope
**Functional requirements:**
*   A Navigation bar to guide the user experience across the website;
*   An About section to tell what MeerCQ is all about and list of services for which contact are available.
*   A Service section to show the contacts under each service
*   An Option to Login so the members of the site who have the previlige to add new contacts, edit existing contact and add reviews.
*   An option to Register for new users.


**Content requirements:**

*   Content categorization based on Login, Register, quick search for contacts, About, Services to display contacts,
*   Use of Text and images to make things easy to understand.
*   A search bar on the hero image for a quick search option.
*   A collapsible dropdown for the "services" nav menu to list down the all the available services.
*   A list of items that can be ordered along with their corresponding quantity.
*   A card to display the contact details.
*   An collapsible to display user reviews.
*   Buttons to Add, edit and delete contacts.

### Structure

The website was designed to deliver an intuitive experience with a consistent information flow.

**Interaction design**

The interface responds to the user actions as expected. The scroll behavior is standard and the buttons respond instantly when actioned. In order to increase the sense of interaction, subtle effects of zooming in,  highlighting and transition effects are used wherever appropriate.

**Information architecture**

The content is organized and segregated into sections from top to bottom. The navigation bar is also categorized accordingly.

### Skeleton

**Wireframe mockups**

Please find attached Wireframe for Home page , place order form and acknowledgement page for Large, medium and Small devices. 

**Wirefame mockups**
Wireframe mockups for Home, Login, Register, Add New Contact, Edit Contact, Add Review for small, meidium and Large screens have been given below.

[SMALL screen](https://github.com/gomathishankar28/ms3_meercq/blob/master/static/images/wireframes/Small.pdf)

[MEDIUM screen](https://github.com/gomathishankar28/ms3_meercq/blob/master/static/images/wireframes/Medium.pdf)

[LARGE screen](https://github.com/gomathishankar28/ms3_meercq/blob/master/static/images/wireframes/Large.pdf)



### Database Schema

![Database Schema](https://github.com/gomathishankar28/ms3_meercq/blob/master/static/images/readme/database_schema.jpg?raw=true)


* The site contains **four** collections which are stored in MongoDB. The **users** collection stores the user's username and password which enables the user to create an account and have a profile page. The **services** collection stores all the different type of services that it provides contacts for.The **contacts** collection that stores all the contact details for a company like service type, mobile number, email, website, address etc. The **Reviews** section stores the rating, user comments for each company name.

## **Surface**

**Colors**

In factories, the Color BLUE often marks equipment to be repaired. So I have decided to use the colour Blue predominantly across the website. Blue (navy) is considered the perfect pick as it reflects trust, confidence and stability which are considered the most important triats for bulding contacts.

**Typography**

Two fonts were used for this project, Akaya Telivigala', cursive, and sans-serif with a sans-serif being fallback font. The cursive style fonts are a well-known typography choice, and are particularly popular on the web. Cursive writing fonts can give the website a more personal feel and approach media.


**Media**

The hero image displays a picture of handyman with all the tools..
All the other images used throughout the website are relative to our service.
All images have been resized and compressed in order to boost the UX flow.

**Iconography**

Icons like plus, pen,star, comments, back arrow have been used throughout the website to improve the efficiency of UX.

## Features
Each page in the website features a responsive navigation bar on the right with conventional placing of Brand Name on the top left. Each page has a very simple footer with just the copyright information.

**Home**

The Home page features 2 sections areas apart from the header and footer.


**Hero image with qucik search bar**

This is the  first section (call out section)- which features a handyman professional with the tools. Upon which is placed a "Call out text" describing the purpose of the website. It also features a search bar that enables the user to quickly find a contact for a service.

**About**

This is second section of the Home page. This section elaborates the purpose  and the uses of this website. It also higlights the services for which the contacts are available.

### **Services**
This page displays the following:

***Cards*** for each company containing  information such as Average Rating, company name, created date, mobile number, address, email, website if any etc. based on one of the 7 services chosen. 

***Add New Contact*** Button to enable registered users to add new contact under a service.

***Edit Contact*** Button to enable registered users to edit existing contact such as mobile number, address or email.

***Delete Contact*** Button for the admin to delete any obsolete contacts.

***Add Review***Button to enable registered users to give rating and comments for a company based on their experience with that contact.

***User Reviews*** To view the rating and user comments added by users along with the timestamp against each company.

**Login**

This page is used for the registered users to login and thereby perform operations like adding new contact, editing existing contact, deleting a contact(only for admin user), adding user reviews etc. This page contains a form with 2 input fields 1. username and 2. password. It also has a link to "Register" page for New users to register


**Register**

This page is used for first time users or new users who wish to register themselves. It contains a form with 3 input fields such as username, password and email. It also provides a link to Login to enable the user to login once they are registered.


### **Footer**

The footer displays the copyright information and social media links 

##  **Existing Features**

*   **Title** - Allows the user to easily recognise the brand of “MeerCQ”. If the user clicks on the logo, it will return the users to the “Home” section as they would expect.
*   **Navigation Bar** - Allows the user to easily navigate the website's sections and find what they are looking for with ease 
*   **Landing Page** - Allows the user to know the purpose of MeerCQ. 
*   **Search bar** which gives the user a quick search option.
*   **About** - Allows user to know about MeerCQ and the services for which contacts are provided.
*   **Contact Cards** - Used to display contact information for a company under each service.
*   **Add New Contact** - Allows the user to add new contact under each service type. 
*   **Edit Contact** - Allows the user to edit existing Contact information.
*   **Delete Contact** - Allows admin to delete an absolete contact.
*   **Add Review**  - Allows user to give a rating and add comments about a contact based on theor experience.
*   **Footer**  -   Allows user to access contact info and Social links.

## **Features to be implemented in future**

 
 ## **Technologies Used**

 ### **Languages**
*   HTML
*   CSS
*   Javascript
*   python

### **Libraries & Frameworks**
- [Materializecss](https://materializecss.com/)
   - Various aspects of this website were structured using Materialize.
   - Materialize was used to make this website responsive
- [Fontawesome](https://fontawesome.com/)
    - The icons used on this page were found in Fontawesome.
- [Flask](https://flask.palletsprojects.com/en/2.0.x/)
    - Flask was used as the main python framework in the building of this project.
- [jQuery](https://jquery.com/)
    - This framework was used to create some of the site's interactive functions.
- [Google fonts](https://fonts.google.com/) 
    - The font styles used on this website were chosen from Google fonts.

### **Tools**
- [Gitpod](https://gitpod.io)
    - This project was built using Gitpod as the IDE.
- [Github](https://github.com/)
    - Github was used for online version control and storing files and documents.
- [Heroku](https://id.heroku.com/)
    - Heroku was used as a cloud based platform to deploy this site.
- [MongoDB](https://www.mongodb.com/)
    - MongoDB Atlas was used as the database for the creation of this project.
- [Jinja](https://jinja.palletsprojects.com/en/3.0.x/)
    - Jinja was used for templating.
- [Cloudinary API](https://cloudinary.com/blog/creating_an_api_with_python_flask_to_upload_files_to_cloudinary)
    - for uploading company_images
- [Balsamiq](https://balsamiq.com/)
    - The wireframes and sitemap for this project were created using Balsamiq.
 -[Freeformatter- CSS beautifier](https://www.freeformatter.com/css-beautifier.html)
    - This was used to format the CSS stylesheet.
- [Freeformatter- HTML formatter](https://www.freeformatter.com/html-formatter.html)
    - This was used to format each HTML page
- [PEP8online](http://pep8online.com/)
    - PEP8 online was used to make sure all python code was pep8 compliant.
- [Google DevTools](https://developers.google.com/web/tools/chrome-devtools) 
    - Google Dev Tools was extensively used throughout the project for various styling and testing purposes. Its lighthouse feature was used as one of the main testing tools for this project.
- [CSS-Tricks](https://css-tricks.com/)
    - This was used as a general reference resource.
- [JSHint Validator](https://jshint.com/)** 
    - For detecting errors and potential problems in your **JavaScript code.**
- [Lighthouse](https://developers.google.com/web/tools/lighthouse)** 
    - For testing the **performance of the website.**
- [Am I Responsive](http://ami.responsivedesign.is/)
    - This was used to test the responsiveness of the site and also to create the mock-up image presented at the start of this document.
- [Beautifier.io](https://beautifier.io/)
    - Beautifier.io was used to format all javascript files in this project.
- [QuickDBD](https://app.quickdatabasediagrams.com/)
    - QuickDBD was used to create the Database Schema presented in this document.

### **Media**

- [WallpaperAccess](https://wallpaperaccess.com) for the hero image.
- [BusinessPartner](https://businesspartner.com) - for electrician image
- [Thumbtack](https://thumbtack.com)- for plumber image
- [Stockvault](https://stockvault.net)- for carpenter image.
- [DepositPhotos](https://depositphotos.com)- for cleaner image.
- [ecoticias](https://ecoticias.com)- for gardener image.
- [Homebli](https://hombli.com)- for painter image.
- [StlitsIreland](https://stiltsireland.net)- for Whitegoods image.
- [Econations](https://eco-nations.com)- for No results found image.

## Cloudinary API

1. Create an account by clicking on sign up for free account on [Cloudinary](https://cloudinary.com/)
2. While creating an account using email and password., Make sure to edit the Cloud name of your choice.
3. Authorize the verification email from cloudinary.
4. clicking on Configure SDK  button gives the values of the environmental variables like cloud_name, api_key, api_secret_key.
5. login to Gitpod workspace.
6. Set default for all the environmental variables.Also make sure to add them to Heroku(under settings->reveal config vars) as well.
7. Install cloudinary using the below command.

        pip3 install cloudinary.
        pip3 freeze --local > requirements.txt
8. Make sure to import the following packages

        from werkzeug.datastructures import FileStorage
        import cloudinary
        import cloudinary.uploader
9.  Add  the following attribute to the form element having the input file class 

        <form enctype="multipart/form-data" class="col s12" method="POST" action="{{ url_for('add_contact') }}">

10. Add the following input element through which file upload can be done.

        <div class="input-field col s12">
                    <i class="fas fa-images prefix white-tex"></i>
                    <input class="file-upload" type="file" name="file" id="fileid" class="validate" required>
                  </div>
11. Add the following code to app.py

            def upload(file):
                app.logger.info('in upload route')
                cloudinary.config(cloud_name = os.getenv('CLOUD_NAME'), api_key=os.getenv('API_KEY'), 
                api_secret=os.getenv('API_SECRET'))
            return cloudinary.uploader.upload(file, width=200, height=160)

12. To the form that is being submitted  with the file. add the code below.

            def add_contact():
                 if request.method == "POST":  
                    img_upload = upload(request.files['file'])
                    contact = {
                        "company_image": img_upload["secure_url"]
                    }
                    mongo.db.contacts.insert_one(contact)

## Testing
Testing information can be found here in the separate [TESTING.md file](/workspace/ms3_meercq/testing.md)

## Deployment
This project was developed using [Gitpod IDE](https://gitpod.io) and pushed to Github using the in-built terminal. However, because Github can only host static websites it was necessary to deploy this project to Heroku because it is a compatible hosting platform for a back-end focused site like MeerCQ. 

This project was deployed using Heroku and stored in GitHub.

### 3 steps to be done in workspace before deploying
Before deploying the website to Heroku, the following three must be followed to allow the app to work in Heroku:

1. Create requirements.txt file that contains the names of packages being used in Python. It is important to update this file if other packages or modules are installed during project development by using the following command:

    - pip freeze --local > requirements.txt

2. Create Procfile that contains the name of the application file so that Heroku knows what to run.The file should contain the following:

        web: python app.py

    Make sure Procfile does not have any blank line follwing the above line when it is created.


3. Push these files to GitHub.
Once those steps are done, the website can be deployed in Heroku using the steps listed below:

**Deployment Steps**

1. Log into Heroku.
2. Click the New button.
3. Click the option to create a new app.
4. Enter the app name in lowercase letters.
5. Select the correct geographical region.

**Set environment variables**

Navigate to the settings tab and then click the Reveal Config Vars button and add the following:

1. key: IP, value: 0.0.0.0
2. key: PORT, value: 5000
3. key: MONGO_DBNAME, value: (the name of the database that is being used for the project)
4. key: MONGO_URI, value:
 * This can be found in MongoDB by navigating  to the clusters section of your MongoDB account.
 * Click the cluster where the database is located.
 * Click the connect button.
 * Select the connect you application button.
 *  Copy the link provided to your application and ensure you have substituted the password and dbname with the correct values).
5. key: SECRET_KEY, value: (This is a custom secret key set up for configuration to keep client-side sessions secure.Randomkeygen was used to generate a secret key).


**Enable automatic deployment**

1. Click the Deploy tab
2. In the Automatic deploys section, choose the branch you want to deploy from then click Enable Automation Deploys.


**Connect app to Github Repository**

1. Click the deploy tab and connect to GitHub.
2. Type the name of the repository into the search bar presented.
3. Click the Code dropdown button next to the green Gitpod button.
4. When the correct repository displays click the connect button.



### **Making a clone to run locally**

It is important to note that this project will not run locally unless an env.py file has been set up by the user which contains the IP, PORT, MONGO_DBNAME, MONGO_URI and SECRET_KEY which have all been kept secret in keeping with best security practices. 

1. Log into GitHub.
2. Select the [respository](https://github.com/gomathishakar28/ms3_meercq).
3. Click the Code dropdown button next to the green Gitpod button.
4. Download ZIP file and unpackage locally and open with IDE. Alternatively copy the URL in the HTTPS box.
5. Open the alternative editor and terminal window.
6. Type 'git clone' and paste the copied URL.
7. Press Enter. A local clone will be created.

Once the project been loaded into the IDE it is necessary to install the necessary requirements which can be done by typing the following command.

    -pip install -r requirements.txt

### **How to Fork the respository**

1. Log into GitHub.
2. In Github go to (https://github.com//gomathishakar28/ms3_meercq).
3. In the top right hand corner click "Fork".

### **Credits**
* **Content**

	* [Zoofy](https://zoofy.nl/)  as a general inspiration.

* **Media**

    * [WallpaperAccess](https://wallpaperaccess.com) for the hero image.
    * [BusinessPartner](https://businesspartner.com) - for electrician image
    * [Thumbtack](https://thumbtack.com)- for plumber image
    * [Stockvault](https://stockvault.net)- for carpenter image.
    * [DepositPhotos](https://depositphotos.com)- for cleaner image.
    * [ecoticias](https://ecoticias.com)- for gardener image.
    * [Homebli](https://hombli.com)- for painter image.
    * [StlitsIreland](https://stiltsireland.net)- for Whitegoods image
    * [BeFunky](https://www.befunky.com/ )** for **resizing and editing images**.
    * [TinyPNG](https://tinypng.com/)** for **Compressing images**. 


* **Code**

	* [Materialize](https://materializecss.com/) for navbar, collapsible, cards, form input fields

	* [W3Schools](https://www.w3schools.com/) as a general source.

    * [geekforgeeks](https://www.geekforgeeks.com/) for $group function in pymongo

    * [stackoverflow](https://stackoverflow.com/) for aggregate and $round function to calculate average rating in pymongo

    * [Githubgist](https://gist.github.com/) as reference for collapsible menu on side nav.

    * [Cloudinary](https://cloudinary.com/blog/creating_an_api_with_python_flask_to_upload_files_to_cloudinary) as a reference to upload company images on add_contact form.

    * [code Institute](https://learn.codeinstitute.net/courses/course-v1:CodeInstitute+IFD101+2017_T3/courseware/03d3f6524ad249d9b33e3336d156dfd0/3b2af8636ea54a4d9dc45126f7498633/) for login, register and delete views.

    

	
### **Acknowledgements**
    
* **My mentor: Nishant kumar** by giving lot of inputs and useful tips to improve.
* **The Slack community** of Code Institute for a peer code review.
* **My Family and Friends** who provided their honest feedback by testing the website across different devices and different OS.
