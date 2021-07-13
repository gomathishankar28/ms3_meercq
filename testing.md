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
1.	To  Check if the Website launches with a Home page when given the URL of the site. > Tested Pass
2.	To Check for broken links for all the navigation menus. –Tested Pass
3.	To Check if “search” button on the landing page displays the desired results based on the search –Tested Pass
4.	To check if clicking on each image in "about"section displays the contact cards for the appropriate service
5.	To check if the Add_contact button in services page invokes a Add Contact Form –Tested Pass
6.  To check if the Edit contact button on each contact card invokes the "Edit contact form" with details on the form to be edited –Tested Pass
7.  To check if clicking on delete contact button on each contact card deletes the  –Tested Pass
8.  To check if the user reviews collapsible is displayed under each contact - Tested Pass.
9.  To check if clicking on Add_review button on each contact invokes the "Add review form".
10.  To check if the website launches with a home page on all  different devices as per the wireframe. –Tested Pass

##  **Code Testing**
### **Results from HTML Validator**
HTML was validated with [W3C Validator](https://validator.w3.org/) by direct input. Results came out as follows.

> ![HTMLValidator results for Home page](https://github.com/gomathishankar28/ms2_desi_wagon/blob/e73bba2942c61209e9600d41068fe3a600950920/assets/images/Testing/HTMLValidationresults1.jpg?raw=true)

> ![HTMLValidator results for Place order](https://github.com/gomathishankar28/ms2_desi_wagon/blob/e73bba2942c61209e9600d41068fe3a600950920/assets/images/Testing/HTMLValidatorresults2.jpg?raw=true)

### **Results from  W3C CSS**
CSS was validated with [W3C CSS](https://jigsaw.w3.org/css-validator/) by direct input.Results came out as follows.

> ![CSS validator Results](https://github.com/gomathishankar28/ms2_desi_wagon/blob/e73bba2942c61209e9600d41068fe3a600950920/assets/images/Testing/CSSValidationresults.jpg?raw=true)

### **Results from Jshint**
Js files were validated with [Jshint](https://jshint.com/). Only 3 warnings occured which were handled as follows.
1. Unused variables for function names.

        Because jshint is only reading that file and doesn't know about the file which is calling this function. and it thinks the function is being unused and hence the error.
2. Warning: Do not use 'new' for side effects.
        
        No fix as the code has been copied for google maps documentation site.

3. Warnings for variables with let or const declaration according to ECMAScript 6 features

        Fixed by adding /*jshint esversion: 6 */ at the top of every js file.

##  **User Stories Testing**
1.  ***As a prospective customer to the website, I want to easily navigate the site, so that I can easily find the details about MeerCQ so that I am assured about their service.***
    >   As the Website is launched, On the Top left is the Navigation bar which is categorized to show different details about the website that the customer is looking for.

2.  ***As a prospective customer to the website, I want to precisely know what services are offered so that I have enough information to avail their service***
    >   This is acheieved by a Hero Banner displayed on the Hero image of the Landing page talking about what MeerCQ is all about and what can it offer. 

3.  ***As a prospective customer to the website, I should be able to search based on keywords so that I can get the desired information quickly***
    >   This is acheived by providing a search bar on the Hero image of the Landing page.Search can be based on services, usernames who created contacts or Company name.

4.  ***As a prospective customer, I would like to receive suggestions in the search field so that I can narrow down my search easily.***
    >   This is acheieved by providing an auto complete option from materialise framework. By typing an alphabet suggests a list of services having that particular letter in them.

5.  ***As a prospective customer, I should be able to avail the contacts of services from a list as well as through visual tiles so that this information is easily accessible.***
    >   This is acheieved by dropdown nav menu which lists down all the available services for which contacts are available. And also the About section has image tiles for each service which on hovering displays the name of the service.

6.  ***As a new customer to the website, I want to know for what kind of services, the contact details are provided.***
    >   This is again acheieved by dropdown nav menu which lists down all the available services for which contacts are available. And also the About section has image tiles for each service which on hovering displays the name of the service.

7.  ***As a new customer, I want to know the contact details of service providers based on the service type chosen, so that I do not see contacts of services that I do not need.***
    >   This is acheived by creating a seperate view for each service and rendering a seperate html page for each service called.

8.  ***As a new customer to website, I want to know how many contacts are available under each service.***
    >   This is acheived by displaying "Available contacts" for each service on top of the contacts cards listed on the page.

9.  ***As a customer to the website, I want to know the name of the person/company as part of the contact details.***
    >   This is acheieved by creating a contact card and displaying the company anme as te card -title.

10. ***As a customer, I would like to know the address of the company so that I have the physical location to reach in case of any issues.***
    >   This is acheieved by creating a contact card and displaying the address information as part of card content.

11. ***As a customer, I would like to know the mobile number in order to contact and fix an appointment..***
    >   This is acheieved by creating a contact card and displaying the mobile number as part of card content.

12. ***As a customer, I would like to know the email ID of the Service provider for future correspondences and invoice sharing.***
    >   This is acheieved by creating a contact card and displaying the emailID as part of card content.

13. ***As a customer who has experience with a particular service provider, I would like to provide a rating so that I can quantify my recommendation to other users.***
    >   This is acheieved by creating a Add Review form and enable the user to give the rating and comments for a service provider.

14. ***As a customer, I would like to see an average rating for each contact that would help me to choose a better professional service provider.***
    >   This is acheieved by creating a contact card and displaying the Average Rating as part of the card content.

15. ***As a Prospective customer I want to add a new contact to a particular service when I find a new reliable contact so that the other users can profit from my experience.***
    >   This is acheieved by creating a Add Contact form and enable the user to give the contact details for the chosen service type.

16. ***As a prospective customer to the website, I want to edit all the contact details of the service provider so that the other users have the latest information about the service provider.***
    >   This is acheieved by creating a Edit Contact form and enable the user to update the contact details chosen to edit.

17. ***As a prospective customer to the website, I want provide feedback /comments about each service provider so that it helps other users to choose the best contact from the available list.***
     >   This is acheieved by creating a "user Reviews" collapsible element which when collapsed shows the rating and comments added by all users for that service provider.

18. ***As an Administrator to the website, I want to delete a contact which is fake, never exists or stopped providing any service.***
    >   This is acheived by placing "Delete" button on the contact card as part of card action.

19. ***As an administrator I want to provide the option of user log in so that changes done to contacts are tracked.***
    >   This is acheived by Login Form which asks for a valid username and password.

20. ***As an administror, the system should allow new contacts to be added only by registered user so that there is accountability on the records created.***
    >   This is acheived by Register Form which asks for a  username, password and email details for user to get registered which is then stored in DB.

21. ***As an Administrator, I would like to restrict only the logged in users to edit a contact or add a comment so that unauthorized/ untraceable changes are prevented.***
    >   This is acheived by displaying the Edit contact, add review button on the contact card to be visible only when the user is logged in .Otherwise no buttons are seen.

22. ***As an administrator, only registered users with a valid password should be allowed to log in so that unauthorized changes can be prevented.***
    >   This is acheived by using Check password hash method.

23. ***As an administrator, both unregistered and registered users should be able to view the contact of service providers and the user reviews so that the display of information is not restricted for unregistered users.***
    >   This is acheived by search bar on Landing page which will help any user to search for contacts without logging in.

24. ***As an administrator, I should allow registered users to log out so that unauthorized accesses are prevented.***
    >   This is acheived by an Logout option on Nav menu which is visible only for logged in users.

25. ***As an administrator, I would like to have field level validations on the contact entry so that incorrect or incomplete information is avoided.***
    >   This is acheived by using Materialize framework's Validate method.

##  **Functional Testing**
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

4.  ***Services Section***  
    * checked to see if choosing "Electricians" from service dropdown displays a service page with contacts whose service type is electricians. 
    * checked to see if choosing "Carpenters" from service dropdown displays a service page with contacts whose service type is Carpenters.
    * checked to see if choosing "Plumbers" from service dropdown displays a service page with contacts whose service type is Plumbers.
    * checked to see if choosing "Gardeners" from service dropdown displays a service page with contacts whose service type is Gardeners.
    * checked to see if choosing "Painters" from service dropdown displays a service page with contacts whose service type is Painters.
    * checked to see if choosing "Whitegoods" from service dropdown displays a service page with contacts whose service type is Whitegoods.
    * checked to see if choosing "Cleaners" from service dropdown displays a service page with contacts whose service type is Cleaners.
    * checked to see if  the total number of Available contacts is displayed for each service and tallies with the number of contact cards listed for that service..

5.   ***Add New Contact***
     * Checked to see if the company name field when left empty prompts an error.
     * Checked to see if the mobile number field takes only numbers as input if not prompts an error.
     * Checked to see if the email field displays an error for an invalid input.
     * Checked to see there is no error prompted for address and website fields when left empty.
     * Checked to see if clicking on back button takes you to the previous service page.
     * checked to see if clicking on ADD button displays a flash message when contact is successfully added to database.
     * Checked to see if the new contact card is displayed on the service page after hitting the ADD button.
     * Checked to see if "N/A" is displayed for address and website details of the contact card when left empty while adding the details.

6.  ***Edit Contact***

7. ***Delete Contact***

8. ***Add Review***

9.***User Reviews***

10. ***Login***

11. ***Register***

12. ***Logout***

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

>  ![Perfomance Results](/workspace/ms3_meercq/static/images/testing/performance.jpg?raw=true)

## **Accessibility Testing**

The website's accessibility was also tested using Lighthouse. The result are shown below.
>  ![Accessibility](/workspace/ms3_meercq/static/images/testing/accessibility.jpg)

## **Best Practices and SEO Results**
>  ![BestPractices](/workspace/ms3_meercq/static/images/testing/best_practices.jpg)

>  ![SEO](/workspace/ms3_meercq/static/images/testing/SEO.jpg)

Spelling was checked thoroughly using [W3C Spell Checker](https://www.w3.org/2002/01/spellchecker). The results are satisfying.

## **Issues found and fixed during Coding**

1. Blinking Truck icon used in the schedule section was hugging the city name. Just Setting margin and padding did not help
    > **Solution** - Span Element by default has display property set to inline.Fixed by changing the Span element display property to inline block for the margin values to take effect.

2. Schedule table did not render well on small and medium screens
    > **solution** - Fixed by using accordions for smaller and medium screens.

3. Image of the city on map-info section did not render well on the small screen.
    >**solution** - Fixed by setting the "display: none; " for smaller screens so that image is not displayed for small screens and is seen only on medium and large screens.

4. Every new grocery item added was not added in the new line'.
    >**Solution**  - Fixed by creating a break element (BR) and appending it to the input element.

5. When a grocery item was deleted, an empty line would be created in its place
    >**solution** - When the grocery tem is being deleted , only the item and the delete icon was being removed.Fixed by removing the break element(BR) along with input element.

6. All Markers on the map were not displayed when map was loaded.
    >**solution** - Fixed by changing the latitude value for the center attribute of the map object.

7. No alerts or error message generated when the form input doesn't match th required pattern.
    >**solution** - Fixed by adding an invalid event listener and adding the following code and similar code for other form elements.
    
        name.addEventListener("invalid", function (event) {
            if ((!(name.value)) || (this.validity.patternMismatch)) {
                alert ("name cannot be empty and should only contain letters. e.g. John");
            }
            else {
             return false;
            }
        });

8.  Initially when the grocery list is empty, there would be an alert to notify that. But when the grocery items are added to the list
     and when all of them are deleted, there was no alert and it allowed the form to submit with empty grocerylist.
    >**solution** -  Fixed by adding a function CheckList() which displays an alert to notify that "grocery list cannot be empty" and disabled the
     submit button to prevent it from submitting with an empty grocery list. Submit button is enabled when an item is added again to the grocery list.

        function checkList() {
        let groceryItem = document.getElementsByClassName("inputlist");
        if (groceryItem.length === 0) {
            alert ("Grocery List cannot be empty.Please add atleast 1 item to the list"); 
            document.getElementById("submit-btn").disabled = true; // To prevent the form with empty grocery list being submitted.
        }
        else {
            return true;
        }
    }

9.  There were lot of small issues related to margin,padding,width,height of the image,font-size etc
    >**solution** - Fixed by adding media queries accordingly.

## **Enhancements**
1. Initially the Schedule section was designed to have a table for all screens displayed. As my mentor Nishant kumar suggested that table is not a preferred UX design for small screens and I was asked to find an alternative.
    >**Enhancement 1** - Found accordion as an alternative from Bootstrap documentation .
2. Map-info  window would just show  cityname, address, landmark , timings and day of the visit of the wagon when clicked on each marker. As my mentor Nishant kumar suggested to have the map-info window's height equal to the height of the map on large screens for better presentation
    >**Enhancement 2** - Added an image of the city to the map-info window so that the height of the map-window matches the height of the map on large screens.
3. Place order form initially had an text area which requires user to manually enter the grocery item and quantity in it. Nishant kumar suggested additional features to increase the use javascript in the project.
    >**Enhancement 3** - Created a drop down for grocery items and quantity and then created a list when the user clicks an "Add to List" button.
    
    >**Enhancement 4** - Added a delete button enabling the user to delete an item from the list.

## **Known Bugs and yet to be Fixed**
1. Every item of the grocery list sent  does not appear in a newline in the **email**. I suspect the whitespace gets removed before being handled by emailjs for security reasons.