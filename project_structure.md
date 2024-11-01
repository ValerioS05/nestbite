# NestBite structure
## Wireframes / Skeleton
- As starting point for the NestBite's structure I will do a showdown of wireframes.  
Created mostly before starting the project, and some were created after ideas came through.
- An important thing to mention is that NestBite follows same pattern regarding the main structure and this will not change in any template.  
**Header** > **Main section** > **Footer** 
    |Description|Wireframe|Final result|
    |--|--|--|
    |Home page (index): The home page as you can see is structured with a navigation bar as header, followed below by the NestBite logo. Under the logo we have the feature section and below it a action button. At the end of the page we have the footer containing brand name , copyright and social media links|![Home page wire frame](/static/images/nest_structure_images/wirehome.png)|The final result doesn't differ much from the wireframe, we still have the navigation bar and the footer as was designed from the start. In the main section we have the feature section that offers small images pertinent to the paragraph underneath it. The main difference from the original wireframe is the bottom side of the main section. The button is surrounded by a dark container containing some text to give directions to the user|
    |Restaurants page (restaurants): In here we have a "list" of the restaurants that are inserted in the database, as usual with navbar and footer, the main section starts with a heading relative to the actual page. Underneath the heading we can see a list of restaurant. Every restaurant contained in a box. The restaurants are paginated 3 by 3. We miss the action button in this page but is replaced that the actual containers in the list that acts as redirection element.|![Restaurants page wire frame](/static/images/nest_structure_images/wirerestlist.png)| The main difference here is the addition of filters, the more detailed restaurant element. The filters were added to provide an easier navigation for the user and a way to sort out in base of their needs. The restaurant elements contains the main details of the relative restaurant(name,address,phone,capacity,working hours).|
    |Restaurant details (restaurant_detail): In the wireframe here we got same base as before with a main section composed of the usual heading followed by the details of the restaurant and the action buttons (book/back)|![restaurant detail wire frame](/static/images/nest_structure_images/wirerestdet.png)|The final result is exactly the same as the wireframe, Heading with the restaurant's name, followed by the relative infos. Underneath a picture of the restaurant. At the bottom we have the owner's name(small addition) and 2 buttons, first is `make a reservation` second is `back to restaurants`|
    |Booking form page (booking_form): In this wireframe we can see in the main section the consistent heading and below it the form to complete to make the reservation. Under the form a single submit button.|![Booking page wireframe](/static/images/nest_structure_images/wirebook.png)|The final result didn't change from the framework structure. I only added some widget to help the user but the structure is quite the same.|
    |Your Bookings page (booking_list): This main section contains under the heading a filter first(decided to be on top due to the chance of having too many bookings and the filter would be too hard to reach). Under the filter we have the reservations and close to the reservations right side we can see the action buttons.|![Booking list wire frame](/static/images/nest_structure_images/wirebooklist.png)|Here the final result is a bit different. The buttons instead of being outside the booking container are inside. This made easier to paginate and also made more sense. Instead of having 1 button for 3 different actions, I splitted them in 3 buttons for each action (view, delete, update).|
    |Booking details page (booking_detail): In this main section we have basically all the booking's details inside a container. Under the container an action button.|![booking details pwire frame](/static/images/nest_structure_images/wirebookdet.png)|The final result as the previous page is different of what was in my mind before. The main difference is that I added a way to the user to submit a review, a simple form with radio buttons and a message area. Also I added 2 more buttons(Submit.., Update.. , back to..)|
    |Update booking page (update_booking): Initially thought to use the same structure as the booking form.|![Update booking wire frame](/static/images/nest_structure_images/wirebook.png)|Keeps the same structure as the wire frame with the exception of having 2 buttons instead of 1 (update.., back to..).|
    |Contact Us page (contact_us): This wire frame shows in the main section a heading followed by a simple container meant to display simple text with underneath the message. Usual button under the message area.|![Contat us wire frame](/static/images/nest_structure_images/wirecont.png)|Resulted same structure until the end of the project.|
    |Profile page (profile):This page was added after the start of the project, the wireframe contains simply the user detail inside a container followed by a edit button.|![Profile page wire frame](/static/images/nest_structure_images/wire%20prof.png)|No changes to the structure|
    |Edit profile page(update_profile): Follows the same structure as the profile page, differs only on the way the details are displayed, instead of having simple text the details are replaced by a form. The form is followed by 2 buttons (save,cancel). To mention is that the cancel button is not meant to delete the profile.|![Update profile wire frame](/static/images/nest_structure_images/wireupda.png)|As said before the profile templates were added way after the start so the structure is not changed in the final result.|
    |Account templates (login,logout,..): As this templates were provided I only imported the base that I used for the previous wire frames(header,main section block, footer).|![Account template wireframes](/static/images/nest_structure_images/wirelog.png)|The structure of these templates may differ on the main section, depending on what the user is trying to do. (Reset password,register, login..)|
    |Base structure (base):As you probably noticed and as said before, the base structure follows always the same structure, Header > Main section > Footer|![base wire frame](/static/images/nest_structure_images/wirebase.png)|Consistency!! |
- Across all templates, the structure is aligned with mobile responsiveness and different screen sizes. The structure may differ on some elements but not their relative position. For example the feature image instead of beeing displayed vertically in mobile view, in bigger screens they will be displayed horizontally.
This Skeleton structure was essential in ensuring that the site was visually consistent,user friendly and appealing.

## Models
 - For the NestBite project I used 4 custom models and the Django Default User models
 - As follow I will showcase my models and their descriptions.
    |Description| ERD Model |
    |--|--|
    |Restaurant model: This model represent a restaurant. Stores it's details as represented in the image. I tried to take the main points of a real life restaurant to better represent it.|![restaurant model diagram](/static/images/nest_structure_images/modrest.png)|
    |Table Model: The model represents individual tables within a restaurant, tracking table details like capacity, its price and unique table number.|![Table model diagram](/static/images/nest_structure_images/modtable.png)|
    |Booking Model: The booking models represents a booking reservetion, This model is associated with many datas, User,Tables,various details about time ,date and customer details.|![Table model diagram](/static/images/nest_structure_images/modbook.png)|
    |Review Model: Allows the user to review a restaurant based on their booking experience. Each review is linked to a specific booking and the restaurant itself.|![Review model diagram](/static/images/nest_structure_images/modreview.png)|
    |Default User Model|[Documentation to Django User Model](https://docs.djangoproject.com/en/5.1/ref/contrib/auth/)|
### Models details and connections
#### The restaurant model
- The Restaurant model is the main entity in this system, each restaurant is essential for informations and organization.
- Location: nestbite/restaurants/models.py
- Restaurant relationships:
    - One-to-many with User model - Owner.
    - One-to-many with Table model - A restaurant can have multiple Tables.
    - One-to-many with Review - Each restaurant can have multiple Reviews.
    - Related to Booking via Tables.
- Methods used:
    - average_rating(): Used to calculate average of rating field from the Review model.
    - __str__(): Returning a readable string.
- Meta:
    - ordering by name, created and capacity.
#### The Table model
- The table model follows directly the Restaurant model representing individual tables within a restaurant.
- Location: nestbite/restaurants/models.py
- Table relationships:
    - ForeignKey to Restaurant
    - Many-to-many with Booking - A single table can belong to multiple bookings and reverse.
- Methods used:
    - clean():
        - Added validation to it:
            - Table capacity is positive.
            - Total restaurant capacity is not exceeded when adding a table.
            - Table_number is unique within each restaurant
    - save():
        - Used to override the save method applying the clean() above.
    __str__(): Returning a representation of each table.

#### The Booking model
- The Booking model handles many aspects:
    - Reservation data.
    - User bookings.
    - Timings.
    - Additional infos like message and booking_reference
- Location: nestbite/booking/models.py
- Booking relationships:
    - ForeignKey to User
    - Many-to-many with Table - Each booking can reserve multiple tables.
    - One-to-many with Review - A booking can have multiple reviews.
- Methods used:
    - clean(): as the previous explanation in the Table model this add validation to the instance.
        - Booking in the past
        - Ensures booking are scheduled at least 2 hours in advance.
        - Limiting booking to a year max in the future (No point booking for the 3024!)
    - generate_booking_reference():
        - Generates 10 alphanumeric characters
    - save():
        - add check on reference number if already provided it will not be regenerated.
    - total_price():
        - Calculates the total price for the booking , if 2 or more tables it will summ the prices of each table to retrieve the total.
    - cancel():
        - Gives the user the right to cancel the booking only if 2 hours in advance (We don't like surprises!)
    - __str_ _():
        - Represents booking showing details as a string.
#### The Review model
- The Review model allows the User to reate their experience with a restaurant based on a specific booking(reviews are accessible only through bookings).
The review is linked with a restaurant,a booking and the User.
- Review relationships:
    - ForeignKey to booking (set to Null if the booking is no longer available).
    - ForeignKey to restaurant.
    - ForeignKey to user.
 




    
