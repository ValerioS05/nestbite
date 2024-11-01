# NestBite Readme

**NestBite** is a web based app built with Django, designed primarily as a booking system for restaurant tables.<br>Its user friendly and intuitive design make it easy to interact and explore.<br>To learn more about NestBite have a look at the README!


## Devices Mockups
### Laptop view
![laptop mockup](/static/images/readme_images/lapmock.png)


### Tablet and Mobile view
||||
|--|--|--|
|![tablet mockup](/static/images/readme_images/tabmock.png)||![mobile mockup](/static/images/readme_images/mobmock.png)|

## Link to main page.

[NestBite Homepage](https://nestbite-5dd11ab0ac7f.herokuapp.com/)

## Readme content
1. [About NestBite](#about-nestbite)
2. [User Stories / Agile workflow](#user-stories)
3. UI/UX Design
4. Features
5. Project structure
  - Models
  - Views
  - Forms
  - Urls
  - Templates
  - Assets
6. Testing / Validation
7. Deployment
11. Technologies
12. Languages
13. Bugs and Fixes
14. Credits

## About NestBite
- NestBite is a web based app built with `Django`, is simulate a restaurant table reservation system.  
This project was created as 4th part of my portfolio building under the guidance and teaching of Code Institue.  
The choise for this project is made by the fact that I actually work in this enviroment and  
it was a fun idea to replicate my experience in an application built by me.
- The development for this project was much different from the previous projects made.  
With the introduction of Agile Workflow and many different aspects to integrate to the aquired knowledge,  
made the development of this project a great challenge and also a great achivement for my personal growth.

## User Stories
### Agile Workflow
- As mentioned before the introduction of Agile made my routine differ from the past.  
I researched in advance what a person using this kind of application would like to be able to do, what they would look for in this enviroment.  
The kind of people that I question where from different backgrounds 
    - Collegues from hospitality.
    - Friends in university(Computer Science).
    - Real life customers.
    - People that are first time users.
    - Also I question myself to understand better what would be the optimal conclusion for all the answers that I received and how to proceed.
- My `user stories` are stored openly in my `Github project section`.
I created a board where I stored in the first column my `Epics` (general collection of user stories divided by category), and three more columns To Do, In progress, Done respectively.
The process of creating more specific user stories was to take one Epic and divide it in smaller sections, making clearer the scope and easier to follow through with the actual project development.
- Each of the `Epics` is numbered , this made it easier to keep track of the user stories added in the To Do list that on their own have as well a combination of numbers:
    - My first epic is named User Account Management (Epic 1).
    - The User stories for that category are named after the number 1, taking into account the first user story that is named U.S. 1.1 Account creation.
    - 1 Epic(first) and 1 U.S. (first U.Story) and so on.

    |Epic|User Story|
    |--|--|
    |![Epic](/static/images/readme_images/epics1.png)|![User Story](/static/images/readme_images/1us.png)|

    - Check my [Github](https://github.com/users/ValerioS05/projects/2) User stories to understant better!

    ### In depth Epics and User Stories
    #### Epic 1 : User Account Management
    - This Epic covers stories related to user registration, login, profile management.
        - User Stories:
            - U.S. 1.1
            As a user, I want to create an account so that I can make reservations.

            - U.S 1.2
            As a user, I want to login to my account so that I can access my reservation/profile

            - U.S. 1.3
            As a user , I want to reset my password (or forgotten)

            - U.S. 1.4
            As a user , I want to update my profile information so I can update my details

        - Using the User default from Django in combination con Allauth it was made possible to let user create their account.  
        Everything related with login/logout any kind of form reguarding registration originated with the help of Allauth.
        Logging to your account will make possible for you to create/delete/update your bookings,  
        also using the default User model I implemented a form where the User can update their details if needed.
        The registration is completed in two steps:
            - First complete the form handed to you in NestBite.  
                |Description|Image|
                |--|--|
                |Register/Login Buttons|<img src="static/images/readme_images/registerlogin.png" alt="register/login buttons"/>|  
                |Sign In Button|<img src="static/images/readme_images/signin.png"  alt="sign in form"/>|
                |Sign Up Form|<img src="static/images/readme_images/signup.png"  alt="sign up button"/>  |
        
        


        - Second you will receive an Email for confirmation.
            - This second step is a good way to avoid spam.
            - Email is set up with a Gmail account `Nestbite@gmail.com` created for the project purpose only.
            - Settings using backend mail and Heroku keys/values(previously only in the env.py file).  
            - The actual code for the settings was provided/learned from :Diploma in Full Stack Software Development learning path.  
            - Once you are registered/logged in you can see the logout and profile buttons.  

            <img src="static/images/readme_images/buttonsregistered.png" alt="registered user buttons"/>  
            
            - NestBite Email.  
            
            <img alt="NestBite Email" src="static/images/readme_images/nestbiteemail.png" width="600">

    #### Epic 2 : Reservation System
    - This Epic covers stories related to reservation-related features (guest/owners/admin).
        - User Stories:
            - U.S. 2.1
            As a user, I want to search for available tables by date and time so I can choose a suitable one for me.

            - U.S. 2.2
            As a user , I want to receive confirmation so I can have proof of my reservation.

            - U.S. 2.3
            As a user, I want to be able to view/manage my reservation so I can cancel if I need to.

            - U.S. 2.4
            As a user, I want to be able to add notes to my reservation so I can leave special requests/needs

            - U.S. 2.5
            As a owner, I want to set available time slots and table so I can control the flow of people (no overbooking , no booking for same table)
        
            - U.S. 2.6
            As a owner , I want to be able to access reservations so I can view, modify or cancel.  
        - Making a reservation/booking is one of the most crucial NestBite's features.
        Many things needs to be accounted for, as the user stories specify.
            - Date and time for the booking, simple at first look in the webpage, quite intricated at the back.
                <img src="static/images/readme_images/datetime.png" alt="date and time selection">  
            User can choose date and time using inputs as widgets. Many restrictions are added for example:
                - Working hours of the actual restaurant, already existing booking , date and times restrictions like, nothing can be booked in the past or in the too distant future.
                - There is a maximum stay(3hrs) and a minimum(1 hr) restriction.
                - Booking can be made/updated/canceled 2 hours in advance, this goes for real life situations where last minute changes are not very liked by anyone.  
                - The reservation system give also the chance to leave a message for the related booking for any special request or any other issue/request.
                - The system provide also feedbacks to the user, and it's quite many.
                    - Feedbacks for:
                        - Succesfull booking.
                        - Unsuccesfull: 
                            - Already existing bookings at that time/date for that table(s).
                            - Time/Date restrictions.
                            - Missing inputs
                    - I decided to also add a feedback to let the user know that there are tables available with similar prices / timing making easier the reselection.
                - Once the table(s) is booked the user will be able to see the booking saved in `Your Bookings` page.
                From there the user is able to delete/view/update the booking, obviously following the same restrictions as for the booking.
                #### Feedbacks

                |Description|Image|
                |--|--|
                |Successful Booking|![Successful Booking](static/images/readme_images/success.png)|
                |Restriction Feedback 1|![Restriction Feedback 1](/static/images/readme_images/no1.png)|
                |Restriction Feedback 2| ![Restriction Feedback 2](/static/images/readme_images/no2.png)|
                |Restriction Feedback 3|![Restriction Feedback 3](/static/images/readme_images/no3.png)|
                | Restriction Feedback 4| ![Restriction Feedback 4](/static/images/readme_images/no4.png)|
                | Booking Reserved| ![Booking Reserved](/static/images/readme_images/booking.png)|
                | Booking Detail| ![Booking detail](/static/images/readme_images/bookdet.png)|
   
    #### Epic 3 : Admin Panel
    - This Epic covers stories related to managing the admin panel(accounts ,approvals, settings..).
        - User Stories:
            - U.S. 3.1
                As an Admin, I want to be able to see and mofify registrations, so I can manage my users.

            - U.S 3.2
                As an Admin, I want to be able to see and manage my restaurants so I can ensure is up to date and best quality.

            - U.S 3.3
                As an admin, I want to be able to see the site settings so I can modify them if needed.  
        - The admin panel is also very important for whoever will manage the overall.
        From the admin panel we have access to:
            - Accounts
                - Email Addresses:
                    - From here we can see verified or non email adresses and username.
                    - The verification is connected directly to the Users panel/model
                    - Is also possible to delete.

                    |Description|Image|
                    |--|--|
                    |Email Addresses in Accounts|![Email addresses panel](/static/images/readme_images/address.PNG)
                    
            - Authentication and Authorization 
                - Users  
                    - From this part of the admin panel we have access to:
                    - Username and Email Address
                    - First Name and Last Name
                    - Staff Status
                    - We can also delete Users.
                        - When deleting users, their booking will be canceled and anything related except for their reviews.
                    
                    |Description|Image|
                    |--|--|
                    |Users in Authentication and Authorization|![Users admin panel](/static/images/readme_images/users.png)|
            - Booking
                - Bookings
                    - In the booking we got a bit more infos:
                    - We have a line of text to start where is specified reference number, name on booking, and date
                    - Username
                    - Tables booked
                    - Customer name
                    - Email
                    - Date
                    - Start and End time
                    - Message
                    - Reference Number
                    - Canceled

                    |Description|Image|
                    |--|--|
                    |Bookings List|![bookings list](/static/images/readme_images/bookingsadmin.png)|
                    |Bookings panel 1|![Bookings admin panel](/static/images/readme_images/bookadmin1.png)|
                    |Bookings panel 2|![Bookings admin panel](/static/images/readme_images/bookadmin2.png)|                   
            - Restaurants
                - Restaurants
                    - In here we have:
                    - Name
                    - Capacity
                    - Opening and Closing time

                    |Description|Image|
                    |--|--|
                    |Restaurants in Restaurants|![Restaurant admin panel](/static/images/readme_images/rest.png)|
                    |Restaurant Detail|![Restaurant Detail](/static/images/readme_images/restdet.png)|                 
                - Tables
                    - Tables panel contains:
                    - Table Number
                    - Capacity
                    - Price
                    - Restaurant (property of)

                    |Description|Image|
                    |--|--|
                    |Tables List|![Tables list](/static/images/readme_images/tables.png)|
                    |Tables Details|![Tables details](/static/images/readme_images/tabdet.png)|    
      
    #### Epic 4 : UX/UI
    - This Epic covers stories related to UX and UI.
        - User Stories:

            - U.S. 4.1
            As user, I want the site to be mobile-friendly(mobile first) and responsive so that I can access it from any of my devices.

            - U.S 4.2
            As a user, I want the page to load quickly so I can smoothly make reservations.

            - U.S 4.3
            As a user, I want the site to be organized and easy to understand at first impact so I can use the site properly even if is the first time

            - U.S 4.4
            As a user, I want to filter options for restaurants to be easy to use so that I can find a restaurant with my preferences.

            - U.S 4.5
            As a user, I want forms inputs to give validations and feebacks so that I can correct mistakes before submitting.

            - U.S 4.6
            As a user, I want a contact page/button so that i can reach for support.
        - Last aspect of my epics was the User Interface and the User Experience.  
        Last for the only reason that first this project needed a skeleton to work on,  
        before style and other aspects needed to be implemented later in case I would change the structure overtime.
        - NestBite offers a mobile friendly interface, as well as other devices and screen sizes.
            - See [Mockups](#devices-mockups)
        
        - Pages in general are quick to load thanks to the small load of datas that every page has.  
        Only the Restaurant_detail template takes slightly longer to load,  
        due to the high definition images.
        - As per the User Experience we can see that filters were added for the restaurants, and all is just 1 click away to the preferred choice.
        - NestBite offers in general a good amount of feedbacks (missing inputs, error and constrictions) so the User is never left hanging around not knowing what is going on. 
            - See [Feedbacks](#feedbacks) images to get a better idea how the site helps the User. To help out also the User can't input anything that would make the form fail or give errors that are not accepted as a "positive" data.  

## UI/UX
### User Interface
- The UI for this project came from a minimalist idea.  
    Every person that I questioned about what they would like in a booking system told me that,  
    everytime they use an app on their mobiles or website they get overwelmed of informations, most of the time not relevant to what they want to achieve.  
    So the plan for NestBite was to make it look nice and easy even trying to not over fill the user. 
    - The palette is a simple grey scale, loads of breathing space and good contrast between sections.
    Giving vibes of classy and not to heavy for the eyes of any user.
    
        |Description|Image|
        |--|--|
        |Main Colors 1| ![First Color Used](/static/images/readme_images/pale1.png)|
        |Main Colors 2| ![Second Color Used](/static/images/readme_images/pale2.png)|
        |Main Colors 3| ![Third Color Used](/static/images/readme_images/pale3.png)|
 
    - The index/home page appears more colorfull due to small feature images added in the main section.
    ![Feature images](/static/images/readme_images/featimg.png)  
    - Some more color were added to action buttons (update and delete bookings(yellow and red respectively)) giving a color feedback and meaning to that buttons.

        |Description|Image|
        |--|--|
        |Visual feedbacks on buttons| ![Visual feedback on buttons](/static/images/readme_images/colorfeed.png)|
    - Throughout all the pages NestBite is consistent.  
    We can always see our footer and navigation bar and a main section that always follow the same color patterns, dark > light > dark. 
    Good contrast with dark font on light background and reverse.
        |Description|Image|
        |--|--|
        |Navigation Bar | ![Navigation Bar](/static/images/readme_images/navbar.png)|
        |Main Section| ![Main Sectin](/static/images/readme_images/mainsec.png)|
        |Footer| ![Footer](/static/images/readme_images/footer.png)|
    - For the fonts I opted for `Italianno` on attention cathing text(Headings, brand ,..) and `Playfair Display` for the rest of the text.
        |Description|Image|
        |--|--|
        |Main Font| ![Main font](/static/images/readme_images/font2.png)|
        |Second Font| ![Second font](/static/images/readme_images/font1.png)|
    - Same goes for the logo used as first impact image, grey scale of colors, the font is light on dark background that surround the text over an low light image.
    The logo and most of the items in the pages are surrounded by a quite dark box-shadow giving a feeling of depth.
        ![Logo](/static/images/readme_images/logordme.png)
    - I would like to say that under the UI aspect NestBite is quite balanced, with the help of a base template followed that smaller templates made the development much easier.  
    Also the use of Bootstrap was a great help on pagination,sizes and general structure. In this case it made possible that the css would be quite a small amount adding only few touches to colors and effects and some smaller details.
    - A `different CSS` file was created for the templates obtained at the setup of `Allauth (Accounts templates)`, the base was kept the same so the new templates would follow the same patterns.
        ![Different template and stylesheet](/static/images/readme_images/difftemp.png)
    - I opted for the use of Icons instead of plain text to keep the user out of too much reading, the icons that I used for the project are:
        |Description|Image|
        |--|--|
        | Stars for ratings|![Star icon](/static/images/readme_images/star.png)|
        |Clock for time 1|![Clock Item 1](/static/images/readme_images/clock.png)|
        |Clock for time 2 (Widget)|![Clock Item 2](/static/images/readme_images/widclock.png)|
        | Phone for Phone numbers|![Phone icon](/static/images/readme_images/phone.png)|
        | User Icon for the profile|![User icon](/static/images/readme_images/prof.png)|
        | Burger Icon for the collapsed navigation bar|![Collapsed Navbar icon](/static/images/readme_images/burg.png)|
    - To mention that I `didn't use` icons for `Social medias`(Facebook and Instagram in this case), even if it would be a great addition to have them, I thought that the actual text gave more feelings than the usual icons that we always see.  
    ![Social Media](/static/images/readme_images/social.png)
    - Most of the clickable items have effects when interacted with, can be more brightness or a change of colors/font all to give the user more visual feedbacks.
        |Description|Image|
        |--|--|
        |Effects on clickable item 1: Addeed some brightnees when interaction happens.|![Effects on clickable item 1](/static/images/readme_images/interact3.png)|
        |Effects on clickable item 2: Reversed palette when interacted with.|![Effects on clickable item 2](/static/images/readme_images/interactbut.png)|
        |Effects on clickable item 3: As previous item with different palette.|![Effects on clickable item 3 (after)](/static/images/readme_images/interactbut1.png)![Effect on same item (before)](/static/images/readme_images/interactbut2.png)|
        |Effects on clickable item 4: Same as item 1.|![Effects on clickable item 4](/static/images/readme_images/interactbut3.png)|
        |Effects on clickable item 5: When interacted with, the button reverses it's palette but keeps the feeback color on border to keep consistency.|![Effects on clickable item 5](/static/images/readme_images/interactbut4.png)|
        |Effects on clickable item 6: Same as previous item|![Effects on clickable item 6](/static/images/readme_images/interactbut5.png)|
        |Effects on clickable item 7: When interacted with it stays mainly the same, I added some shadow on the item.|![Effects on clickable item 7](/static/images/readme_images/restdeteff.png)|
### User Experience
- In terms of UX the general idea as for the Interface was to make the User don't feel overwelmed.
-  NestBite offer a desgin that makes the User interact and reach the desired point with only few clicks. The site can be navigated with a keyboard giving different possibilities to the User.
- What makes NestBite stand out is the fact that the user is never left hanging clueless.
The design is straight forward:
    - Good naming on redirections buttons/links
    - Naming on url paths consistent with the actual page.
    - Headings consistent with the active page.
    - Feedbacks when errors or successfull interactions.
    - Validation and authorization
    - Uniqueness and personal for example:
        - Reviews and ratings
        - Reference Number
        - Private:
            - No one can have access to your profile (except for admin(s)).
            - Reviews are personal.
            - Confirmation when registering.
    - The User can navigate easy thanks to the navbar and the many redirection anchors throughout the page, it is quite impossible to get stuck even for first time Users.
    - In NestBite the UX is taken care of giving also the chance to leave a message with the Contact Us form / Message in the Booking Form. If a person got any issue or any queries is always possible to contact administration with these forms.
    - If the User is not registered Can still browse the site in the Home page or browse the Restaurants pages, to have an insight of what is NestBite.
    If you are not registered Nestbite give you feedbacks about it, letting you know that certain actions require registration and validation.
    - The Booking system:
        - When the user is making a reservation, the system is always aware of what is going on. 
        - User can filter restaurants and bookings with the help of widgets.
        - If the booking fails, there's nothing to worry about, NestBite gives many feedbacks helping you out to complete the forms.
        - Table already booked? I provide the User different but similar options for different Tables.
        - Succesfull bookings are saved in Your Bookings page:
            - For Users : 
            Users can see all `their` bookings but not others. So the page in not overpopulated with useless informations.
            - For administration/staff. The Your Bookings acts as a database, displaying every booking made. This could cause trouble if we have too many bookings. 
            Nothing to worry about bacause you can filter the bookings reducing the amount of displayed items.
            













    