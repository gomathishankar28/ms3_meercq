# **Testing**

## Table of Contents

- [Smoke Testing](#smoke-testing)
- [Code Testing](#code-testing)
- [User stories Testing](#user-stories-testing)
- [Functional Testing](#functional-testing)
- [Responsiveness Testing](#responsiveness-testing)
- [Performance Testing](#performance-testing)
- [Accessibility Testing](#accessibility-testing)
- [Best Practices and SEO Results](#best-practices-and-seo-results)
- [Issues found and fixed during Coding](#issues-found-and-fixed-during-coding)
- [Enhancements](#enhancements)

## **Smoke Testing**

Following testcases were tested as part of smoke testing.

> 1. To  Check if the Website launches with a Home page when given the URL of the site. > Tested Pass
> 2. To Check for broken links for all the navigation menus. –Tested Pass
> 3. To Check if “search” button on the landing page displays the desired results based on the search –Tested Pass
> 4. To check if clicking on each image in "about"section displays the contact cards for the appropriate service
> 5. To check if the Add_contact button in services page invokes a Add Contact Form –Tested Pass
> 6. To check if the Edit contact button on each contact card invokes the "Edit contact form" with details on the form to be edited –Tested Pass
> 7. To check if clicking on delete contact button on each contact card deletes the  –Tested Pass
> 8. To check if the user reviews collapsible is displayed under each contact - Tested Pass.
> 9. To check if clicking on Add_review button on each contact invokes the "Add review form".
> 10. To check if the website launches with a home page on all  different devices as per the wireframe. –Tested Pass

## **Code Testing**

### **Results from HTML Validator**

HTML was validated with [W3C Validator](https://validator.w3.org/) by direct input. Results came out good except for few errors because of the use of  jinja templating which cannot be corrected.


### **Results from  W3C CSS**

CSS was validated with [W3C CSS](https://jigsaw.w3.org/css-validator/) by direct input.Results came out good


### **Results from Jshint**

Js files were validated with [Jshint](https://jshint.com/). No Errors found

   1. Warnings for variables with let or const declaration according to ECMAScript 6 features

              Fixed by adding /*jshint esversion: 6 */ at the top of every js file.

## **User Stories Testing**


   1. ***As a prospective customer to the website, I want to easily navigate the site, so that I can easily find the details about MeerCQ so that I am assured about their service.***

         > As the Website is launched, On the Top left is the Navigation bar which is categorized to show different details about the website that the customer is looking for.
         
   2. ***As a prospective customer to the website, I want to precisely know what services are offered so that I have enough information to avail their service***

         > This is acheieved by a Hero Banner displayed on the Hero image of the Landing page talking about what MeerCQ is all about and what can it offer.
         >
   3. ***As a prospective customer to the website, I should be able to search based on keywords so that I can get the desired information quickly***

         > This is acheived by providing a search bar on the Hero image of the Landing page.Search can be based on services, usernames who created contacts or Company name.
         >
   4. ***As a prospective customer, I would like to receive suggestions in the search field so that I can narrow down my search easily.***

         > This is acheieved by providing an auto complete option from materialise framework. By typing an alphabet suggests a list of services having that particular letter in them.
         >
   5. ***As a prospective customer, I should be able to avail the contacts of services from a list as well as through visual tiles so that this information is easily accessible.***

         > This is acheieved by dropdown nav menu which lists down all the available services for which contacts are available. And also the About section has image tiles for each service which on hovering displays the name of the service.
         >
   6. ***As a new customer to the website, I want to know for what kind of services, the contact details are provided.***

         > This is again acheieved by dropdown nav menu which lists down all the available services for which contacts are available. And also the About section has image tiles for each service which on hovering displays the name of the service.
         >
   7. ***As a new customer, I want to know the contact details of service providers based on the service type chosen, so that I do not see contacts of services that I do not need.***

         > This is acheived by creating a seperate view for each service and rendering a seperate html page for each service called.
         >
   8. ***As a new customer to website, I want to know how many contacts are available under each service.***

         > This is acheived by displaying "Available contacts" for each service on top of the contacts cards listed on the page.
         >
   9. ***As a customer to the website, I want to know the name of the person/company as part of the contact details.***

         > This is acheieved by creating a contact card and displaying the company anme as te card -title.
         >
   10. ***As a customer, I would like to know the address of the company so that I have the physical location to reach in case of any issues.***

          > This is acheieved by creating a contact card and displaying the address information as part of card content.
          >
   11. ***As a customer, I would like to know the mobile number in order to contact and fix an appointment..***

          > This is acheieved by creating a contact card and displaying the mobile number as part of card content.
          >
   12. ***As a customer, I would like to know the email ID of the Service provider for future correspondences and invoice sharing.***

          > This is acheieved by creating a contact card and displaying the emailID as part of card content.
          >
   13. ***As a customer who has experience with a particular service provider, I would like to provide a rating so that I can quantify my recommendation to other users.***

          > This is acheieved by creating a Add Review form and enable the user to give the rating and comments for a service provider.
          >
   14. ***As a customer, I would like to see an average rating for each contact that would help me to choose a better professional service provider.***

          > This is acheieved by creating a contact card and displaying the Average Rating as part of the card content.
          >
   15. ***As a Prospective customer I want to add a new contact to a particular service when I find a new reliable contact so that the other users can profit from my experience.***

          > This is acheieved by creating a Add Contact form and enable the user to give the contact details for the chosen service type.
          >
   16. ***As a prospective customer to the website, I want to edit all the contact details of the service provider so that the other users have the latest information about the service provider.***

          > This is acheieved by creating a Edit Contact form and enable the user to update the contact details chosen to edit.
          >
   17. ***As a prospective customer to the website, I want provide feedback /comments about each service provider so that it helps other users to choose the best contact from the available list.***

          > This is acheieved by creating a "user Reviews" collapsible element which when collapsed shows the rating and comments added by all users for that service provider.
          >
   18. ***As an Administrator to the website, I want to delete a contact which is fake, never exists or stopped providing any service.***

          > This is acheived by placing "Delete" button on the contact card as part of card action.
          >
   19. ***As an administrator I want to provide the option of user log in so that changes done to contacts are tracked.***

          > This is acheived by Login Form which asks for a valid username and password.
          >
   20. ***As an administror, the system should allow new contacts to be added only by registered user so that there is accountability on the records created.***

          > This is acheived by Register Form which asks for a  username, password and email details for user to get registered which is then stored in DB.
          >
   21. ***As an Administrator, I would like to restrict only the logged in users to edit a contact or add a comment so that unauthorized/ untraceable changes are prevented.***

          > This is acheived by displaying the Edit contact, add review button on the contact card to be visible only when the user is logged in .Otherwise no buttons are seen.
          >
   22. ***As an administrator, only registered users with a valid password should be allowed to log in so that unauthorized changes can be prevented.***

          > This is acheived by using Check password hash method.
          >
   23. ***As an administrator, both unregistered and registered users should be able to view the contact of service providers and the user reviews so that the display of information is not restricted for unregistered users.***

          > This is acheived by search bar on Landing page which will help any user to search for contacts without logging in.
          >
   24. ***As an administrator, I should allow registered users to log out so that unauthorized accesses are prevented.***

          > This is acheived by an Logout option on Nav menu which is visible only for logged in users.
          >
   25. ***As an administrator, I would like to have field level validations on the contact entry so that incorrect or incomplete information is avoided.***

          > This is acheived by using Materialize framework's Validate method.
          >

   ## **Functional Testing**

   Functional testing was done by testing induvidual features of the website to see if they meet their intended purpose.

   1. **Brand-Title**

         * Checked to see if the Click on the Title takes you to the Home page.
   2. **Navigation Bar**

         * Checked to see if the navigation links are highlighted according to the active page.
         * At the launch, Home link of the nav bar has to be higlighted with a relatively dark background color.
   3. **Home Page**

         ***Call out Section***

         * checked to see if the main hero banner is visible on all size screens
         * Checked to see if the hero text is visible on medium and large screens and hidden on small screens.
         * Checked to see if the input field in the search bar of the hero image triggers an autocomplete on text input.
         * Checked to see if the search for a particular servce displays the corresponding contacts cards.
         * Checked to see if the no results page is displayed when there are no contacts found relavent to th search option.

         ***About section***

         * Checked to see if the hovering on each service image displays the name of that service.
         * Checked to see if clicking on particular service displays corresponding service page with contact cards.
   4. ***Services Section***

         * checked to see if choosing "Electricians" from service dropdown displays a service page with contacts whose service type is electricians.
         * checked to see if choosing "Carpenters" from service dropdown displays a service page with contacts whose service type is Carpenters.
         * checked to see if choosing "Plumbers" from service dropdown displays a service page with contacts whose service type is Plumbers.
         * checked to see if choosing "Gardeners" from service dropdown displays a service page with contacts whose service type is Gardeners.
         * checked to see if choosing "Painters" from service dropdown displays a service page with contacts whose service type is Painters.
         * checked to see if choosing "Whitegoods" from service dropdown displays a service page with contacts whose service type is Whitegoods.
         * checked to see if choosing "Cleaners" from service dropdown displays a service page with contacts whose service type is Cleaners.
         * checked to see if  the total number of Available contacts is displayed for each service and tallies with the number of contact cards listed for that service..
   5. ***Add New Contact***

         * Checked to see if this button is visible only for users who are logged in.
         * Checked to see if cliking on "Add New Contact" invokes the Add new contact form.
         * Checked to see if the company name field when left empty prompts an error.
         * Checked to see if the mobile number field takes only numbers as input if not prompts an error.
         * Checked to see if the email field displays an error for an invalid input.
         * Checked to see there is no error prompted for address and website fields when left empty.
         * Checked to see if clicking on back button takes you to the previous service page.
         * checked to see if clicking on ADD button displays a flash message when contact is successfully added.
         * Checked to see if the new contact card is displayed under the corresponding service page.
         * Checked to see if "N/A" is displayed for address and website details of the contact card when left empty while adding the details.
         * Checked to see if the Available Contacts" gets updated accordingly.
   6. ***Edit Contact***

         * Checked to see if this button is visible only for users who are logged in.
         * Checked to see if hovering on Edit Icon displays a tool tip "Edit Contact".
         * Checked to see if cliking on "Edit Contact" button inside each card invokes the Edit contact form.
         * Checked to see if all the details of the contact chosen to edit are displayed automatically on the Edit form.
         * Checked to see if the company name field when left empty prompts an error.
         * Checked to see if the mobile number field takes only numbers as input if not prompts an error.
         * Checked to see if the email field displays an error for an invalid input.
         * Checked to see there is no error prompted for address and website fields when left empty.
         * Checked to see if clicking on back button takes you to the previous service page.
         * checked to see if clicking on Update button displays a flash message when contact is successfully updated.
         * Checked to see if the contact card is displayed  with the updated details under the corresponding service page.
         * Checked to see if "N/A" is displayed for address and website details of the contact card when left empty while adding the details.
   7. ***Delete Contact***

         * Checked to see if this button is visible only for admin user.
         * Checked to see if hovering on Delete Icon displays a tool tip "Delete Contact".
         * checked to see if clicking on Delete button displays a flash message when contact is successfully deleted.
         * Checked to see if the contact card is removed under the corresponding service page.
         * Checked to see if the Available Contacts" gets updated accordingly.
   8. ***Add Review***

         * Checked to see if this button is visible only for users who are logged in.
         * Checked to see if hovering on comments Icon displays a tool tip "Add Review".
         * Checked to see if cliking on "Add Review" inside each card invokes the Add Review form.
         * Checked to see if the company name and service type of the chosen contact gets populated automatically in the form
         * Checked to see if the comments field when left empty prompts an error.
         * Checked to see if the rating field displays a drop down containing numbers from 1 to 5.

   9.***User Reviews***

   * Checked to see if this section is visible for both registered and unregistered users.
   * Checked to see if all the reviews pertaining to the service provider/company are listed in an collapsible view
   * Checked to see if the number of stars displayed is corresponding to the number given in the rating field.
   * Checked to see if the correct name of the user who added that review is displayed.

   10. ***Login***

          * Checked to see if clicking on Login from nav menu invokes the Login form.
          * Checked to see if there is an error message  username/password  combination is invalid.
   11. ***Register***

          * Checked to see if clicking on Register from nav menu invokes the Register form.
          * Checked to see if the username accepts a combination of alphabets and numbers and a maximum of 15 characters.
          * Checked to see if the password accepts a combination of alphabets and numbers and a maximum of 15 characters.
          * Checked to see if the email field displays an error for an invalid emailid input.
   12. ***Logout***

         * checked to see if Clicking on Logout from nav menu displays a flash message to the user for successfully logging out.

   ## **Responsiveness Testing**

     ***Devices Testing***

      Website was tested using Chrome Dev tools in the following devices to check if the pages are rendered well.The results are satisfying<br>

   1. Galaxy Fold.<br>
   2. Moto G4<br>
   3. Pixel 2<br>
   4. Pixel 2xl<br>
   5. iphone5<br>
   6. iphone 6/7/8<br>
   7. iphone 6/7/8 plus<br>
   8. iphone x<br>
   9. surface Duo<br>
   10. ipad<br>
   11. ipad pro.<br>

   ***BrowserTesting***

   Website was tested in browsers listed below and results were satisfying.

   1. Chrome<br>
   2. Edge.<br>
   3. Opera<br>
   4. Safari<br>
   5. Firefox<br>

      ***Operating System Testing***

      Website was tested in different OS listed below and results were satisfying.

      1. Windows 10<br>
      2. Mac OS.<br>
      3. iOS.<br>
      4. Android<br>

      ## **Performance Testing**

      Performance has been tested using the Lighthouse tool of Google Chrome. The results are shown below.

      > ![Perfomance Results](https:/workspace/ms3_meercq/static/images/testing/performance.jpg?raw=true)
      >

      ## **Accessibility Testing**

      The website's accessibility was also tested using Lighthouse. The result are shown below.

      > ![Accessibility](https:/workspace/ms3_meercq/static/images/testing/accessibility.jpg)
      >

      ## **Best Practices and SEO Results**

      > ![BestPractices](https:/workspace/ms3_meercq/static/images/testing/best_practices.jpg)
      >

      > ![SEO](https:/workspace/ms3_meercq/static/images/testing/SEO.jpg)
      >

      Spelling was checked thoroughly using [W3C Spell Checker](https://www.w3.org/2002/01/spellchecker). The results are satisfying.

      ## **Issues found and fixed during Coding**

      1. Nav bar with dropdown menu "services" would collapse to show the list of all services either on main navbar on large screens or on the sidenav on small screen but not on both.

         > **Solution** - There could actually be only one list emelent  with  dropdown-trigger class with data-target referring to the drop down content. But I had 2 initially, one for the main nav bar and other one for the sidenav.Later it was replaced with a collapsible for a sidenav as shown below.

                <ul class="collapsible">
                            <li>
                                <a class="collapsible-header">Services<i class="fas fa-caret-down right"></i></a>
                                <div class="collapsible-body">
                                    <ul id="" class="">
                                        <li><a href="{{ url_for('electricians') }}">Electricians</a></li>
                                        <li class="divider"></li>
                                        <li><a href="{{ url_for('plumbers') }}">Plumbers</a></li>
                                        <li class="divider"></li>
                                        <li><a href="{{ url_for('carpenters') }}">Carpenters</a></li>
                                        <li class="divider"></li>
                                        <li><a href="{{ url_for('painters') }}">Painters</a></li>
                                        <li class="divider"></li>
                                        <li><a href="{{ url_for('gardeners') }}">Gardeners</a></li>
                                        <li class="divider"></li>
                                        <li><a href="{{ url_for('whitegoods') }}">Whitegoods</a></li>
                                        <li class="divider"></li>
                                        <li><a href="{{ url_for('cleaners') }}">Cleaners</a></li>
                                    </ul>
         
      2. Redirecting to the corresponding service page from the Edit contact form and Add Review form errored out when 
      "return redirect(request.referrer)" was used because the route app for them involved the contactid as part of the URL.

         > **solution** - Fixed by using the urlparse method to identify the baseurl and then appending it with corresponding service type which would give the url to be redirected.
                
                 from urllib.parse import urlparse
                 @app.route("/edit_contact/<contact_id>", methods=["GET", "POST"])
                 def edit_contact(contact_id):
                 if request.method == "POST":
                    full_url = request.referrer
                    parts = urlparse(full_url)
                    path =  "/{}".format(request.form.get("service_type"))
                    baseurl = "{}://{}{}".format(parts.scheme, parts.netloc, path)
                    edited_contact = {
                        "service_type": request.form.get("service_type"),
                        "company_name": request.form.get("company_name"),
                        "mobile": request.form.get("mobile"),
                        "email": request.form.get("email"),
                        "url": ((request.form.get("url") if(request.form.get("url")) else "N/A")),
	                    "address": ((request.form.get("address") if(request.form.get("address")) else "N/A")),
                        "rating": request.form.get("rating"),
                        "created_by": session["user"]
        }
        mongo.db.contacts.update({"_id": ObjectId(contact_id)}, edited_contact)
        flash("contact Successfully Updated")
        return redirect(baseurl)
         
      3. Average Rating for a company was always being displayed as None, though there were ratings available for the company.

         > **solution** - This was because the Rating value received from the add review form was inserted as string in the DB and average function performed on a string returned None. Fixed by parsing the rating value to integer.

                "rating": int(request.form.get("rating"))
         
      4. User Reviews was being displayed only for the first contact card/first company displayed under every service, though other company also had user reviews

         > **Solution**  - Fixed by converting the reviews object to a list.

                reviews = list(mongo.db.reviews.find())
      5. To calculate the average rating rounded to 1 decimalbased n the rating from users.Had to use to $round.Was trying to use it directly to avgRating field.But it errored out.

         > **Solution**  - Had to use $addfields function to use round function as follows.

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
      

      ## **Enhancements**


         1. Initially the contact card section was designed to have only contact details like company name, moble number, email, address and website details. 

            > **Enhancement 1** - Then as per my partner's advise, Average rating and contact creation date details and user review colapsible were displayed as part of the contact card.
            >
         2. Initially there was no image upload feature as part of this project. My mentor Nishant kumar had suggested to have an image upload feature if possible

            > **Enhancement 2** - Added an image upload feature to addcontact form so that the contact card will also have an picture of the company displayed as part of the contact card.This was acheived using Cloudinary API
            >
         3. Initially each service page would display all the contact cards.

            > **Enhancement 3** - Thought it would be nice to display the total number of available contacts on the top, so that the user can know how many contacts does he have without counting the cards being displayed.
            >
         4. Initially User reviews section just had the start rating, user name and user comments displayed

            > **Enhancement 4** - As per the advise of my partner, added a timestamp for each user rating and also added a delete review button which would be accessible only to the user who created that review. That way it is easy for user to delete his own review and add a new one if needed.
            >   
         5. Initially the search bar on the Landing page did not have any autocomplete feature .

            >**Enhancement 5** - For ease of use for the user, added an autocomplete feature to the search field.
      

         ## **Known Bugs and yet to be Fixed**

         