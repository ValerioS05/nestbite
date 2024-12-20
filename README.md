# NestBite Readme
**NestBite** is a web based app built with Django, designed primarily as a booking system for restaurant tables.<br>Its user friendly and intuitive design make it easy to interact and explore.<br>To learn more about NestBite have a look at the README!  


## Readme content
- This Readme is organized by sections for a total of 11. 
    - Sections :
        - From 1 to 4 and 11 - Everything about this sections is in this page.
        - For section 5  and section from 6 to 10:
            - Please follow the links provided below.  

 **Happy exploring!**
1. [About NestBite](#about-nestbite)
2. [User Stories / Agile workflow](#user-stories)
3. [Features](#features)
4. [UI/UX Design](#uiux)
- Separate section for 5.
5. [Project structure](./project_structure.md)
    - [Wire frames / Skeleton](./project_structure.md#wireframes--skeleton)
    - [Models](./project_structure.md#models)
    - [Views](./project_structure.md#views)
    - [Forms](./project_structure.md#forms)
    - [Urls](./project_structure.md#urls)
    - [Templates](./project_structure.md#templates)
    - [Assets](./project_structure.md#assets)  

- Separate section for 6. to 10.  
    - [Go to 6-10 section ](./6to10section.md)
    6. [Testing / Validation](./6to10section.md#tests)
    7. [Technologies](./6to10section.md#technologies-used)
    8. [Languages](./6to10section.md#languages-used)
    9. [Deployment](./6to10section.md#deployment)
    10. [Bugs and Fixes](./6to10section.md#bugs-and-fixes)
11. [Credits](#credits)  


## Devices Mockups
### Laptop view
![laptop mockup](/static/images/readme_images/lapmock.png)


### Tablet and Mobile view
||||
|--|--|--|
|![tablet mockup](/static/images/readme_images/tabmock.png)||![mobile mockup](/static/images/readme_images/mobmock.png)|

## Link to main page.

[NestBite Homepage](https://nestbite-5dd11ab0ac7f.herokuapp.com/)



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
## Features
### General Features
- Responsive Design
    - **NestBite** is fully responsive and optimized for various devices and sizes of screens. Provides a smooth and accessible experience on you favourite device.
        ||||
        |--|--|--|
        |![Responsive main page mobile](/static/images/readme_images/mainsec.png)| ![Responsive main page tablet](/static/images/readme_images/respons.png)|![Responsive main page large screen](/static/images/readme_images/respons2.png)|
        | ![Responsive booking page mobile](/static/images/readme_images/respbook3.png)|![Responsive booking page tablet](/static/images/readme_images/respbook2.png)|![Responsive booking page larger screen](/static/images/readme_images/respbook.png)|
        |![Responsive contact us form mobile](/static/images/readme_images/respons4.png)|![Responsive contact us form larger screens](/static/images/readme_images/respons5.png)||
        |![Responsive booking details mobile](/static/images/readme_images/respdet2.png)|![Responsive booking detail Larger screen](/static/images/readme_images/respdet.png)|In here we have how the navbar gets on mobile devices/less large screens.![Responsive navbar non collapsed](/static/images/readme_images/responsenav.png)|

    - **Email service**: When submitting message forms the form is sent directly to the nestbite mail address.
        ||||
        |--|--|--|
        |Contact form![Mail Showcase 1](/static/images/readme_images/mail.png)|Emails received with subject![Mail showcase 2](/static/images/readme_images/mailreceived.png)|Review form with booking reference.![Mail showcase 3](/static/images/readme_images/mailreview.png)|

    - **Fast loading times**: Efficiently designed to quickly load pages facilitating smooth navigation through the site.
    - **Intuitive** navigation: Minimalist design and clear navigation options.
    The layout allows the User to easy find the section they need most, as making reservations, view bookings and contacting support.
    - **Interactive Visual Feedbacks**: Buttons and other elements provide clear clues making the UI more engaging.
    - **Efficient booking system**: User can quickly reserve one table or multiple tables, filter restaurants and receive immediate feedbacks.
    - **User friendly forms**: Forms provide real time feedbacks, preventing errors with the help of clear labels.
    - **Personalized experience**: Logged in users have access to `Your Bookings` page showing only personal bookings.
    - **Clear, Info messages**: The system provides messages for most of the interaction with the site (Login,Sign out, bookings, errors) acting as a real time guide.
    - **Security and privacy**: Personal data remain private.
    - **Role based access**: the site layout differ depending on the status of the users.
    - **Pagination and sorting**: For large lists the site/admin site is organized with paginations and sortings optimizing the overall.
- See below for more details about features!
### Future features
- Real time availability - User can literally see which tables are free and which not.
- Booking History - Admin can access booking history for analysis.
- Profile Customization - As a profile a User can upload picture and add more details for the profile.
- Loyalty Rewards - If User booked with NestBite a certain times can get lower prices for next reservation.
- Dynamic menus - User can actually select menus when booking a table.
- Additional filters - Sort by rating or diet. Or for bookings with the reference number for example.
- Booking reminder - Email is sent when booking is close to start.
- Multi language support - Selection of language/s.
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
- In terms of UX the general idea like the Interface was to make the User don't feel overwelmed.
-  NestBite offer a desgin that makes the User interact and reach the desired point with only few clicks.  
The site can be navigated with a keyboard giving different possibilities to the User.
- What makes NestBite stand out is the fact that the user is never left hanging clueless.
The design is straight forward:
    - Good naming on redirections buttons/links  
        ![Naming on navbar](/static/images/readme_images/naming.png)
    - Naming on url paths consistent with the actual page.
    - Headings consistent with the active page.
    - Feedbacks when errors or successfull interactions.
    - Validation and authorization
    - Uniqueness and personal for example:
        - Reviews and ratings
            ![Ratings and message in booking form](/static/images/readme_images/ratingrev.png)
        - Reference Number  
            ![Reference Number](/static/images/readme_images/bookref.png)
        - Private:
            - No one can have access to your profile (except for admin(s)).
            - Reviews are personal.
            - Confirmation when registering.
    - The User can navigate easy thanks to the navbar and the many redirection anchors throughout the page, it is quite impossible to get stuck even for first time Users.

    - In NestBite the UX is taken care of giving also the chance to leave a message with the Contact Us form / Message in the Booking Form. If a person got any issue or any queries is always possible to contact administration with these forms.
        |Description| Image|
        |--|--|
        |Contact Us page| ![Contact Us form with message](/static/images/readme_images/contact.png)|
        |Message in Booking Form|![Message in the booking form](/static/images/readme_images/message.png)|
    - If the User is not registered Can still browse the site in the Home page or browse the Restaurants pages, to have an insight of what is NestBite.
    If you are not registered Nestbite give you feedbacks about it, letting you know that certain actions require registration and validation.  
        ![Non registered feedback](/static/images/readme_images/registerfeed.png)
    - The Booking system:
        - When the user is making a reservation, the system is always aware of what is going on. 
        - User can filter restaurants and bookings with the help of widgets.
            |Description|Image|
            |--|--|
            |Filtering restaurants by maximum `capacity` or working `hours`.|![Filter for restaurants](/static/images/readme_images/filter1.png)|
            |Filter Bookings by date|![Filter for bookings](/static/images/readme_images/filter2.png)|
            - Every filter has a `clear` button to reduce time consuming deleting/updating filters.
        - If the booking fails, there's nothing to worry about, NestBite gives many feedbacks helping you out to complete the forms.
        - Table already booked? I provide the User with feedbacks and different but similar options for different Tables.
        - Succesfull bookings are saved in Your Bookings page:
            - For Users : 
            Users can see all `their` bookings but not others. So the page in not overpopulated with useless informations.
            - For administration/staff. The `Your Bookings` acts as a database, displaying every booking made. This could cause trouble if we have too many bookings. 
            Nothing to worry about bacause you can filter the bookings reducing the amount of displayed items.
    - For Administration only:
        - The Admin panel also gives all you need to create, delete and update any of the data available from the models. We also have some restrictions here for example on capacities and uniqueness. The panel is not overwelmed in general. The only side that could be a bit "too much" to get through is the Restaurant panel.
            - The amount of `Tables` and `Restaurants` can get as bigger as you can imagine.
            Fortunately you can sort both of these items giving you more specif data to work on.
        - From the admin panel you can give access to actual staff member and sort them out as you need, and this goes for any of the model. All of them got a sort options that can go from names to dates or status, making the admin life quite easier.
        - One of the jobs needed to be completed manually is the setup of Restaurants and Tables. Beeing a risky factor only the people that have access to this panels can work on this datas, keeping the layout and datas safe and well processed to pass to the actual site.
        - Only administration can give staff status as it should be in most of the enviroments.
            |Description|Image|
            |--|--|
            |Table sort|![Sorting Tables by restaurant](/static/images/readme_images/tabfilt.png)|
            |Restaurant sort|![Sorting restaurant by name](/static/images/readme_images/restfilt.png)|
            |Booking sort|![Sorting booking by date](/static/images/readme_images/bookfilt.png)|
            |Email sort|![Sorting email by verification](/static/images/readme_images/emailfilt.png)|
            |User sort|![Sorting users by status](/static/images/readme_images/userfilt.png)|  


## Credits
- Favicon created with Favicon.io
- Fonts from Google Fonts
- Images taken from Unsplash.
- Logo from Free logo design.
- Wireframes from [Wireframe.cc](https://wireframe.cc/)
- Icons from fontawesome.
- ERD diagrams from [Drowio.com](https://www.drawio.com/)
- Starting Template offered by Code Institute.
    - (Some of the settings code were taken from the course, like the mail settings and featured image settings.)

Featured images  
Image by <a href="https://pixabay.com/users/eelffica-52436/?utm_source=link-attribution&utm_medium=referral&utm_campaign=image&utm_content=190817">Eelffica</a> from <a href="https://pixabay.com//?utm_source=link-attribution&utm_medium=referral&utm_campaign=image&utm_content=190817">Pixabay</a>

Image by <a href="https://pixabay.com/users/gioelefazzeri-16466931/?utm_source=link-attribution&utm_medium=referral&utm_campaign=image&utm_content=5356682">Gioele Fazzeri</a> from <a href="https://pixabay.com//?utm_source=link-attribution&utm_medium=referral&utm_campaign=image&utm_content=5356682">Pixabay</a>

Image by <a href="https://pixabay.com/users/divily-110719/?utm_source=link-attribution&utm_medium=referral&utm_campaign=image&utm_content=2931846">Stefan</a> from <a href="https://pixabay.com//?utm_source=link-attribution&utm_medium=referral&utm_campaign=image&utm_content=2931846">Pixabay</a>

## [Back to top](#nestbite-readme)




    