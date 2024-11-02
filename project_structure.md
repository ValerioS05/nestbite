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
    - __str_ _(): Returning a readable string.
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
- Location: nestbite/booking/models.py
- Review relationships:
    - ForeignKey to booking (set to Null if the booking is no longer available).
    - ForeignKey to restaurant.
    - ForeignKey to user.
- Methods used:
    - __str_ _():
        - Represents the review showing its details.
- To mention is that this model is not registered to the admin panel, is not essential to the admin to view directly from it. Also it could result redundant.
    - An email is actually set up, receiving reviews and it is accessible from there.

## Views 
### Restaurant views.py
- This view is basically divided in three main section:
    - The displaying/rendering of the index page that serves as the home page.
        - Parameters: 
        - request - represents the incoming request from the User.
    - The RestaurantList
        - A view for displaying a list of restaurants with filtering and pagination added to it.
        - Attributes: 
            - template_name - Specify the name of the template used to render the list.
            - context_object_name - Used to contain the name used in the template in this case (restaurants) containing the list of restaurant objects.
            - paginated_by - Define the number of restaurants displayed per page in this case (3).
        - Methods used:
            - get_queryset(self):
                - it calls the restaurant_filter function to define filtering based on the user input in this case capacity and working hours.
            - restaurant_filter(request):
                - This function handles the logic behind the filtering. Takes as parameter (request) obtaining the parameters for the queryset from the url.
                - It initially gets the restaurant objects , followed by capacity and the opening time. The Time filtering was a bit challenging due to the fact that in the url the representation of the time is a string. Using the strptime() method the system parse the string into a datetime object. If no hours is present then the value is set to none.
    - The restaurant_detail
        - This view renders the details of the specified restaurant using the restaurant_detail.html template.
        - Takes as parameter (request, pk). 
            - pk to retrieve the restaurant. (raises a 404 if restaurant is not found.)

### Booking views.py
- The Booking view file is quite larger than the previous showcase.
    - Divided between logic/utility and view functionality.
        -  View functions:
            - create_booking(request,restaurant_id)
            Handles the creation of a new booking for the specified restaurant, it renders the booking form and redirection to the booking list when the form is succesfully submitted. If the form is not succesfully submitted the function rises errors rendered in the form itself.
            - update_booking(request,booking_id)
            Retrieving the existing booking specified , checks authorization and processes the form updating the details(if valid).
            - booking_list(request)
            Display the list of bookings for the current user rendering the booking_list.html template.
            - booking_detail(request, booking_id)
            Display the deatails of the specified booking and handles the reviews, checking user authorization and allowing them to submit the review if they didn't already.
            - cancel_booking(request,booking_id)
            The purpose of this function is deleting the specified booking (if user is authorized).
            - delete_finished_booking(booking_id)
            Delets bookings after is done. It is automatic so the system is not redundant and overpopulated with non pertinent bookings.
            The bookings are deleted after 2 hours after the end_time.
        - Logic/Utility Functions
            - check_timings(booking,restaurant,form)
            The purpose of this function is to validate the booking timings. (beeing within working hours and min/max stay of the customer.)
            How it works: It compares the booking to the restaurant ensuring that the booking is starting 1 hour before closing time(for obvious reasons).
            It also validates that the duration of the booking is between 1 and 3 hours. This decision was made because:
                - 1 - The booking needs a minimum time even if hypotetically the Customer leaves that remaining time is "paid" for.
                - 2 - The 3 Hours booking is a way to don't give the user the chance to book all the restaurant for the all day "paying" the same amount.
                    Giving the case a User can do multiple bookings. Not much logic to it , it's just showcasing timeslots.
            - overlapping_bookings(booking,form,current_booking)
                - One of the most important function, this helps to keep check on overlapping bookings for the selected tables and specified timings.
                A good thing that this function does is giving the chance to the user to explore different options if a overlap is found.
                The logic here is to filter the booking objects to fint overlaps between the start time or end time of the current booking.
            - handle_booking_form(request,form,restaurant,booking)
                - As the function name, this handles the form submition for creating or updating. 
                If the form is valid, it either updates or creates a new booking based on the booking parameter, calling the check_timings and overlap functions for validation. If the overall is good, it saves the booking to the database.
### Myprofile views.py
- Very smaller view file. It is in a separate app (myprofile) meant to User interaction not directly affecting the system reservation logic.
    - profile_view(request)
        The purpose of this view is to display the profile page (profile.html) with the actual user details.
    - profile_edit(request)
        As per name the view allows the logged user to edit the profile details (name, email) if the form is valid(if the form is not valid it renders the error messages).
    - contact_us(request)
        - Allows the user logged in to send a message to the nestbite email, quite simple. The form extracts the user details that will be sent with the mail(send_mail function).
## Forms
### Booking forms.py
- Here we have forms related to the booking app.
    - BookingForm:
        - The purpose of this form is to allow the user to create booking for tables in a specified restaurant. As the name says the form is based on the booking model and its fields.
        - There are some features in this form:
            - The multiple choice field a list of tables selectable with checkboxes.
            The __init_ _ method was initialized to get the tables for the selected restaurants by queryset.
            This method does important actions like identify the restaurant id filtering the tables.
            Create the list of tables displaying some pertinent details.
            - Meta:
            Specifing the booking as model for this form I included fields like , customer name , date, timings and a optional message.
            - Widgets were used to customize the form, date picker for booking_date and time picker for both the start and end time.
            Some validation was added over the timings for closing and opening hours of the specified restaurant.
    - ReviewForm:
        - Allows the user to leave a review, this form provides a rating from 1 to 5 and an optional message.
        - Meta: Specifing the Review model, I included rating and message.
        - In here widgets were used as well, RadioSelect for radio buttons displayed with stars and the actual "value" of the button. Also a textarea was user for the message.
### Myprofile forms.py
- In this file we have 2 forms as well. These two forms handles user interaction like profile update and contact form.
    - ProfileForm:
        - The profileForm gives the user the chance to update thier profile informations based on the built-in User model, that's the reason why the User is able to modify the username, first and last name plus the email. This form is a very basic form to edit basic informations trying to don't expose sensitive datas.
    - ContactForm:
        - This is a simple form to submit a message intended for customer experience (customer service and  feedbacks).
        - **Important** to say is that the form is not linked to the database bacause it stores input temporarily.
        - The message is in a form of a Textare widget giving the user multiple lines where to right(complaints!!!) to nestbite administration.
        - The form is processed and emailed to the site email very straightforward.
## Urls
- These urlpatterns configures the primary url routes for nestbite(nest_bite project).
    |Urls|Description|
    |--|--|
    |![Nestbite main urls image](/static/images/nest_structure_images/nesturl.png)| In these paths we have connection to : /accounts/,/admin/,/booking/,/myprofile/, the /''/ is including the restaurant because it focuses as the main entry point for the site. We can also see the connection to summernote enabling the customization.|
    |![Restaurant urls image](/static/images/nest_structure_images/urlrest.png)|In the Restaurant urls we can see the /''/ that sets the index page as homepage for the site, we have the path to the restaurant_list  using class based view. Same for the restaurant_detail, in this case we have an identifier specifing which restaurant to see <int:pk> primary key expected as an integer.|
    |![Booking urls image](/static/images/nest_structure_images/urlbook.png)|The empty path here define the main route for the /booking/ linked to the booking_list view. The /create/ is the path to the create_booking view get the restaurant id as integer. We can see the booking_detail that is set as the booking_id, followed bycancel_booking and update_details.|
    |![Myprofile urls image](/static/images/nest_structure_images/urlprurl.png)|My profile url pattern is quite small, covers the profile viewing ,editing and concting page. The empty path is set as main entrance for the profile, followed by the /edit/ and the /contact/ paths. These routes are user related actions within the myprofile.|
- Examples:  
![Url showcase 1](/static/images/nest_structure_images/urlex.png)    
![Url showcase 2](/static/images/nest_structure_images/urlex1.png)  
![Url showcase 3](/static/images/nest_structure_images/urlex2.png)  
![Url showcase 4](/static/images/nest_structure_images/urlex3.png)  
![Url showcase 5](/static/images/nest_structure_images/urlex4.png)  
- As we can see the urls follow a specific pattern depending on what we are trying to reach or achieve.

## Templates
|||
|--|--|
|![Templates organization picture](/static/images/nest_structure_images/templates.png)|As we can see from the image. My templates are organized inside the templates folder. The First templates created were the ones left outside of folders also for importance. This was to keep track of the organization that was idealized. We have first the base template that is the base that will be inherited from all the other templates. In this template we have the main items to form a webpage, such as the metadatas with the addition of navigation bar and footer. This made possible a fast deployment of the other templates keeping everything consistent and organized. The accounts templates also inherited this base template. The main base.html contains also a message display that will be exported to every template avoiding redundancy.|

- Main section export using the block content.  
![Export showcase from base.html main section](/static/images/nest_structure_images/Mainexport.png)  
- Message export example.  
![Export showcase from base.html messages](/static/images/nest_structure_images/messageexport.png)

- All the other are constructed using content blocks filled with HTML and Bootstrap. 
- This was the actual first time using Bootstrap in this exstensive way.

- The booking folder contains temlates meant to structure the display of reservation related content. 
    - booking_detail.
    - booking_form.
    - booking_list.
    - cancel_booking
    - update_booking_form.
- The profile folder as for the booking one, contains templates devoted to user interaction structures.
    - contact_us.
    - profile.
    - update_profile.
- Account templates.
    - These templates were already set and nothing that I created. 
    - Some of these templates were modified mainly the /account/base.html, this was bacause I wanted even the furthest templates to inherit the same structure as the main base and also the same styles etc...
    - I opted to leave the account templates inside their original folder, this has been chosen like this because I preferred keepin the created by me templates distant from what I didn't actually built.
    - Social account templates as the others that I didn't mention were untouched.

### Dynamic templates
- The templates are structured in a way that dynamically changes elements based on the status of the User
    - If the user is a first timer the template realizes that with the help of ({% if user.is_authenticated %}) the user can access only few elements.
    - It can be certain items like the links in the navigation bar, or the buttons in the restaurant pages to start making bookings.  

|Image| Description|
|--|--|
|![Registered user showcase](/static/images/nest_structure_images/registered.png)| This is displayed for registered user from the template logic|
|![Non registered user showcase](/static/images/nest_structure_images/nonregistered.png)| This is the case the user is not registered/logged in|


    
