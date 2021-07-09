# [MeerCQ](https://gomathishankar28.github.io/ms3_meercq/)

This is a website that provides contact details of variety of services like electricians, plumbers,
carpenters, painters, gardeners, whitegoods and cleaners in Meerhoven in one place. As the name suggests, MeerCQ( which means Meerhoven people seek you) 
is a platform where people can find the contact of a professional for all the chores at home without any hassle.
**MeerCQ** is an educational project that serves as the **Milestone Project 3** for the **Full-Stack Software Developer programme** powered by **Code Institute**.

## **Table of Contents**
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

## **Demo** 



# **Introduction**

MeerCQ gathers recommendations shared in public conversations on social media. It aims to create contact listings for
 recommended pros, so that the customers can easily see referrals from across social media, in one handy location.
 Customers can find a professional to contact for small jobs in and around the house.

The reason to promote this business model is because when there is a problem with any of the service at home,
it is very difficult to find an appropriate contact on time. Users refer to google and find some available contact which will not ensure 
a reliable service. MeerCQ aims at collecting the details and contacts  for such services based on experience from other users which 
ensures a reliable service.

The site enables the registered users to create, Read, Update and Delete (CRUD) contacts. The site also provides a platform to share
the user reviews for each contact, based on which the customers can choose a best contact professional from the list of available contacts.


## **Business Goals**
*   To target the expat community who are looking for handyman professionals for their home needs.

*   To evince interest in customers who wants to find contacts for all home services in one place.

*   To bring this offering to all the expats who are new to this place and doesn't have any contacts to reach to in case of a problem at home.

*   Provide a single, standard way to find the contact of professionals for all the basic home services.

*   To comprehensively list the available contacts under each service type.

*   Build a brand image for contact directory for all home services in Meerhoven

*   Clearly communicate the contact information for every company under each service type.

## **user Goals**

As a customer, I would like 

*   To know what kind of information, MeerCQ can Provide. 

*   To know the list of services for which contacts is provided

*   To know the name, contact number, address,emailID of each contact for further communication

*   To see the user reviews for each company,so that i can pick the best choice up. 

##  **User stories**
*   As a prospective customer to the website, I want to easily navigate the site, so that I can easily find the details about MeerCQ so that I am assured about their service. 

*   As a prospective customer to the website, I want to precisely know what services are offered so that I have enough information to avail their service

*   As a new customer to the website, I want to know for what kind of services, the contact deatils are provided.

*   As a new customer to the website, I want to know the contact details based on the service type chosen.

*   As a new customer to website, I want to know how many contacts are available under each service.

*   As a customer to the website, I want to know the name of the person/company as part of the contact deatils

*   As a customer, I would like to know the address of the company so that I have a place to reach incase of any issue..

*   As a customer, I would like to know the mobile number in order to contact and fix an appointment.

*   As a customer, I would like to know the emailID of the contact for future communication and invoice sharing.

*   As a customer, I would like to see a rating for each contact that would help me to choose a better contact profesional.

*   As a Prospective customer I want to add a new contact to the service when I find a new reliable contact and wishes to suggest the same to others.

*   As a prospective customer to the website, I want to edit a contact when the address or mobile number changes.

*   As a  prospective customer to the website, I want to edit a contact to add review comments wich helps other users to choose the best contact from the available list.

*   As a  admin to the website, I want to delete a contact which is fake, never exists or stopped providing any service.

## **UX**
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

## **Strategy**
Build brand awareness for a directory of handyman contacts in the neighbourhood
Through this website , clearly communicate the services for which contacts are available
Provide an easy option for users to quickly look for a contact for a particular service
Maintain all contact information in one place.
Aim to increase the number of reliable contacts for different services based on customer reviews.

## **Scope**
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

## **Structure**

The website was designed to deliver an intuitive experience with a consistent information flow.

**Interaction design**

The interface responds to the user actions as expected. The scroll behavior is standard and the buttons respond instantly when actioned. In order to increase the sense of interaction, subtle effects of zooming in,  highlighting and transition effects are used wherever appropriate.

**Information architecture**

The content is organized and segregated into sections from top to bottom. The navigation bar is also categorized accordingly.

## **Skeleton**

**Wireframe mockups**

Please find attached Wireframe for Home page , place order form and acknowledgement page for Large, medium and Small devices. 

**Wirefame mockups**

[Home]()

[services]()

[Login]

[Register]

[Add New Contact]

[Edit Contact]

[Add Review]

### Database Schema

<img src="assets/documentation/doc-images/dbschema.png" width="900" height="300" alt="database schema">

* The site contains **four** collections which are stored in MongoDB. The **users** collection stores the user's username and password which enables the user to create an account and have a profile page. The **services** collection stores all the different type of services that it provides contacts for.The **contacts** collection that stores all the contact details for a company like service type, mobile number, email, website, address etc. The **Reviews** section stores the rating, user comments for each company name.


### Sitemap
* The sitemap was created using [Balsamiq wireframes](https://balsamiq.com/)

* A link to the [Sitemap can be found here](assets/documentation/wireframes/MS3-sitemap-wireframe.pdf)

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

## **Features**
Each page in the website features a responsive navigation bar on the right with conventional placing of Brand Name on the top left. Each page has a footer with copyright information, contact details of the Desi Wagon and links to social media.

### **Home**
The Home page features 3 sections areas apart from the header and footer.


### **Carousel**
This is the  first section (call out section)- which features a carousel of 3 images which talks about, what this Desi Wagon does, What they deliver and a call to action for placing the orders respectively.

### **Schedule**
This is second section of the Home page. This section elaborates on the delivery schedule of the Desi Wagon. The wagon is scheduled to visit 1 city a day, accounting to 5 different cities in a week. This section showcases a table that would detail the scheduled visits of the wagon on each week day including the visit timing. This is displayed in a table for large and medium screens. However table is not advised as a good UX for smaller screens, so this section is displayed as an accordion in smaller screens for better reponsiveness, good UX and readability. Also, to indicate the wagon’s location on any given weekeday, there is a flashing wagon in the schedule for better interpretation.

### **Location**
This is third section of the Home page. The wagon visits 5 cities in a week and this section gives the address details of each location at which the wagon will be stationed. This is achieved with the help of Google Maps API. This section contains 2 columns on large and medium screens(col-lg-6, col-md-6) on which the first column displays the map with markers on 5 different cities this wagon would visit every week. The second column displaying a card with details of address, landmark , timings and day when each marker is clicked for better usability. This is done in smaller screen with 2 (col-12) columns.

### **Place order**
This page presents a form to the user which helps them to send in their grocery list in advance. An email will be sent to Desi wagon and copy of it will be sent to the user as well.
The form has the following fields.
1.  **Name** - Text input field for the name of the user initiating the request.
2.  **Email** - Text input field for the mail ID of the user. a copy of their grocery list is sent to this mail ID.
3.  **Mobile** - Number input field for the Mobile number of the user.
4.  **Location** -  A drop down box showing 5 cities the Wagon visits.
5.  **Address**  - Text Input field which auto populates the address on choosing a specific location from the above field.
6.  **Groceries** - A drop down that contains a list of Indian groceries grouped under four different categories like fruits, vegetables, wholegrains and spices ,for the users to choose from.
7.  **Quantity** - A drop down that contains numbers from 1 to 10.
8.  **Add to List** - Button that adds the grocery item and quantity to the grocery list
9.  **Dynamic InputElement** - An readonly input element conatining the added grocery item along with Quantity and a span element beside it for delete option ("X") 
10. **TextArea** - A hidden text area where the final list of all grocery items along with quantity is created. The value of this field is used to send email via emailJS.
11. **Submit** - A submit button which sends an email with the username and thier grocery list to desiwagon and a copy of it is send to the user as well.
    This is acheived by using EmailJs API.

### **Acknowledgement**
This page is seen on successful completion of placing the order. It displays a Thank you image from Desi Wagon to the user for placing the order with them. It also contains text to say that order has been received successfully and the user needs to check the schedule to pick the order. A link to the schedule is also provided for convenience.

### **Footer**
The footer displays the following:
*   copyright information 
*   additional details to say that they are closed on weekends and timings they ar availale on weekdays.
*   Contact Information  with mobilenumber, e-mail and country details.
*   links Social media like facebook, linkedln, twitter , instagram and pinInterest.

##  **Existing Features**

*   **Title** - Allows the user to easily recognise the brand of “Desi Wagon”. If the user clicks on the logo, it will return the users to the “Home” section as they would expect.
*   **Navigation Bar** - Allows the user to easily navigate the website's sections and find what they are looking for with ease 
*   **Landing Page** - Allows the user to know about Desiwagon. carousel with 3 slides showing who they are, what they offer and a CTA button to place the order respectively.
*   **Schedule** - Allows user to know the Schedule of the wagon for a week.
*   **Location** - Allows the user to know the  the address details of the stationed wagon.
*   **Place Order** - Allows the user to place prior orders for their groceries. Also enables the user to send an email to desiwagon with their grocery list.
*   **Acknowledgement** - Provides the user with an acknowledgement message on successful placement of the order
*   **Footer**  -   Allows user to access contact info and Social links.

## **Features to be implemented in future**
*   A google sign in to place the  order for user validation.
*   Auto populate items based on order history.
*   Autocomplete option for form fields in place_order form.
 
 ## Technologies Used
- This project is primarily built using HTML5 semantic markup, CSS stylesheets, Javascript, Python, Flask and MongoDB.
- [Flask](https://flask.palletsprojects.com/en/2.0.x/)
    - Flask was used as the main python framework in the building of this project.
- [jQuery](https://jquery.com/)
    - This framework was used to create some of the site's interactive functions.
- [Gitpod](https://gitpod.io)
    - This project was built using Gitpod as the IDE.
- [Github](https://github.com/)
    - Github was used for online version control and storing files and documents.
- [Heroku](https://id.heroku.com/)
    - Heroku was used as a cloud based platform to deploy this site.
- [Google fonts](https://fonts.google.com/) 
    - The font styles used on this website were chosen from Google fonts.
- [Materializecss](https://materializecss.com/)
   - Various aspects of this website were structured using Materialize.
   - Materialize was used to make this website responsive
- [Fontawesome](https://fontawesome.com/)
    - The icons used on this page were found in Fontawesome.
- [MongoDB](https://www.mongodb.com/)
    - MongoDB Atlas was used as the database for the creation of this project.
- [Jinja](https://jinja.palletsprojects.com/en/3.0.x/)
    - Jinja was used for templating.
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
- [Favicon.io](https://favicon.io/) 
    - This was used to create the site's favicon.
- [Am I Responsive](http://ami.responsivedesign.is/)
    - This was used to test the responsiveness of the site and also to create the mock-up image presented at the start of this document.
- [Beautifier.io](https://beautifier.io/)
    - Beautifier.io was used to format all javascript files in this project.
- [Dbdiagram.io](https://dbdiagram.io/home)
    - Dbdiagram.io was used to create the Database Schema presented in this document.
- [StackOverflow](https://stackoverflow.com/)
    - Stack Overflow was used as a general reference resource. 

## Testing
Testing information can be found here in the separate [TESTING.md file](TESTING.md)

## Deployment
This project was developed using [Gitpod IDE](https://gitpod.io) and pushed to Github using the in-built terminal. However, because Github can only host static websites it was necessary to deploy this project to Heroku because it is a compatible hosting platform for a back-end focused site like MotherFolklore. 

This project was deployed using Heroku and stored in GitHub.

Before deploying the website to Heroku, the following three must be followed to allow the app to work in Heroku:
1. Create requirements.txt file that contains the names of packages being used in Python. It is important to update this file if other packages or modules are installed during project development by using the following command:

    - pip freeze --local > requirements.txt

2. Create Procfile that contains the name of the application file so that Heroku knows what to run. If the Procfile has a blank line when it is created remove this as this may cause problems.

3. Push these files to GitHub.
Once those steps are done, the website can be deployed in Heroku using the steps listed below:

### Deployment Steps

1. Log into Heroku.
2. Click the New button.
3. Click the option to create a new app.
4. Enter the app name in lowercase letters.
5. Select the correct geographical region.

### Set environment variables:

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
5. key: SECRET_KEY, value: (This is a custom secret key set up for configuration to keep client-side sessions secure).


### Enable automatic deployment:

1. Click the Deploy tab
2. In the Automatic deploys section, choose the branch you want to deploy from then click Enable Automation Deploys.


### Connect app to Github Repository

1. Click the deploy tab and connect to GitHub.
2. Type the name of the repository into the search bar presented.
3. Click the Code dropdown button next to the green Gitpod button.
4. When the correct repository displays click the connect button.



### Making a clone to run locally

It is important to note that this project will not run locally unless an env.py file has been set up by the user which contains the IP, PORT, MONGO_DBNAME, MONGO_URI and SECRET_KEY which have all been kept secret in keeping with best security practices. 

1. Log into GitHub.
2. Select the [respository](https://github.com/AideenM12/MotherFolklore-MS3).
3. Click the Code dropdown button next to the green Gitpod button.
4. Download ZIP file and unpackage locally and open with IDE. Alternatively copy the URL in the HTTPS box.
5. Open the alternative editor and terminal window.
6. Type 'git clone' and paste the copied URL.
7. Press Enter. A local clone will be created.

Once the project been loaded into the IDE it is necessary to install the necessary requirements which can be done by typing the following command.

    -pip install -r requirements.txt

### How to Fork the respository.

1. Log into GitHub.
2. In Github go to (https://github.com/AideenM12/MotherFolklore-MS3).
3. In the top right hand corner click "Fork".
