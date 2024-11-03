# Build / Test / Deployment 
- In this section we will speak about the following points.
6. Testing / Validation
7. Deployment
8. Technologies
9. Languages
10. Bugs and Fixes


## Validation / Testing 
### Validation
For validation many tools were used:
- [W3C Markup](https://validator.w3.org/)/[CSS Validators](https://jigsaw.w3.org/css-validator/)
- [JSHint](https://jshint.com/)
- [Python Linter CI](https://pep8ci.herokuapp.com/#)
- [Lighthouse tool (Dev Tools)](https://developer.chrome.com/docs/lighthouse/overview/)
- [Wave (WebAim)](https://wave.webaim.org/)
### Lighthouse tests
|||||
|--|--|--|--|
|![Lighhouse Check 1](/static/images/6t010_images/light1.png)||![Lighhouse Check 2](/static/images/6t010_images/light2.png)||
|![Lighhouse Check 3](/static/images/6t010_images/light3.png)||![Lighhouse Check 4](/static/images/6t010_images/light4.png)||
|![Lighhouse Check 5](/static/images/6t010_images/light5.png)||![Lighhouse Check 6](/static/images/6t010_images/light6.png)||
|![Lighhouse Check 7](/static/images/6t010_images/light7.png)||![Lighhouse Check 8](/static/images/6t010_images/light8.png)||
|![Lighhouse Check 9](/static/images/6t010_images/light9.png)||![Lighhouse Check 10](/static/images/6t010_images/light10.png)||
|![Lighhouse Check 11](/static/images/6t010_images/light11.png)||||
- In the restaurant_detail.html the performance is a bit lower due to the image and the page takes a bit longer to load. Also the best practices was effected because my device was connected to cloudinary pages and cookies were retrieved. Using a different device the Best Practices is higher.

### HTML validation
The Html was taken from the source code once the page was rendered in the browser.
|||||
|--|--|--|--|
|![Html validation 1](/static/images/6t010_images/htm.png)||![Html validation 2](/static/images/6t010_images/htm1.png)||
|![Html validation 3](/static/images/6t010_images/htm2.png)||![Html validation 4](/static/images/6t010_images/htm3.png)||
|![Html validation 5](/static/images/6t010_images/htm4.png)||![Html validation 6](/static/images/6t010_images/htm5.png)||
|![Html validation 7](/static/images/6t010_images/htm6.png)||![Html validation 8](/static/images/6t010_images/htm7.png)||
|![Html validation 9](/static/images/6t010_images/htm8.png)||||

### Css validation
![ Css validation 3](/static/images/6t010_images/cssval3.png)
|||
|--|--|
|![Css validation 1](/static/images/6t010_images/cssval.png)|![Css validation 2](/static/images/6t010_images/cssval1.png)|

### Wave
In here I checked the contrast in the pages if they would achieve good results overall.  
![Contrast in page](/static/images/6t010_images/contrs.png)

### Python
All the files have been passed through the Python Linter offere by Code Insitute.
![Python in Python linter](/static/images/6t010_images/linter.png)

### Tests
For this project for the testing side, in addition to manual testing we have some automated test.
#### Auto tests
The location of these tests is related to their app of origin.
Tests about booking is in the booking app. 
nestbite/booking/test_booking.py
Test for myprofile
nestbite/myprofile/test_myprofile.py
Tests for restaurants
nestbite/restaurants/test_restaurant.py

To run the tests in the app I used the `python manage.py test` command using test cases.

Resulting as this:
![Running Tests](/static/images/6t010_images/test.png)
Tests were built as failing tests and rewriting until arriving to the point that the test would pass.
|||
|--|--|
|Here is an example of a completed test. I recreated booking datas used in a real booking. Some print messages were added for debugging. In here we log the test user, we try to send a POST request with the details of the booking.|![booking test](/static/images/6t010_images/bookingtest.png)|
#### Booking test
What we are trying to check in this test is that the booking was created and everything macthes.
- Booking created for the correct user and the user is associated to the booking.
- The table is correctly linked to the booking.
- Correct timings were followed.  

#### Myprofile test
For test_myprofile similar logic was used. I set up a test user.
- What I was trying to check is that the user could update his datas like name and email.
- In this tests I also checked the contact us form section. Asserting the mail outbox and the message.

#### Restaurant test
For the restaurant the logic was to setup a restaurant and its datas.
- In here I recreated the addition of a new restaurant checking if it was created succesfully.
- The second test is directed to the filtering actions, in this case by capacity(75). I checked if the restaurant object was with a capacity of 75 and in this case if the return was the "Restaurant One"(created momentarily).

### Manual testing
As the title say NestBite is been manually tested from first to last page.
#### Homepage
|Element tested|Test Result|Note|
|--|--|--|
|NestBite Brand Btn|ok|Used to redirect to Homepage|
|Navigation Bar Items(registered)|ok|All the items are redirecting to the right place.|
|Navigation Bar Items(non registered)|ok|All Items works in the right way.|
|Browse Restaurants Btn|ok|Redirects the user to the right place|
|Social Links|ok|Even though social media pages are not set up, the links redirect to the correct social media platform,|  
#### Restaurants list page
|Element tested|Test Result|Note|
|--|--|--|
|Filters|ok|Both capacity and Time correctly filters the restaurants based on input.|
|Clear Buttons|ok|Both buttons clear the input field|
|Displayed list of restaurants|ok|Every item is associated to the correct restaurant id.|
|Pagination Buttons|ok|Both buttons redirect the page correctly|

#### Restaurant detail page
|Element tested|Test Result|Note|
|--|--|--|
|Make reservation|ok|Sends the user to the booking form.|
|Back To restaurant|ok|Redirect the user to the restaurant list.|
|Restaurant fields|ok|The restaurant fields are loaded correctly depending on restaurant id|

#### Booking form page
|Element tested|Test Result|Note|
|--|--|--|
|Name input|ok|Restriction to only characters works correctly displaying error message|
|Date picker|ok|Display correct error if date doesn't meet requirements|
|Start/End Time pickers|ok|Display correct error if timing is not met|
|Tables Select|ok|Displayed correctly as intended form is not submitted if a table is not selected|
|Textarea|ok|No issue with textarea|
|Book now Btn|ok|Submit the details if succesfully compiled datas, else herror handling manages it|

#### Booking list page
|Element tested|Test Result|Note|
|--|--|--|
|Date filter|ok|Works correctly as espected.|
|Filter and Clear filter|ok|Both buttons do what they are supposed to do.|
|View Details Btn|ok|When pressed redirect correctly to the booking details.|
|Cancel Booking|ok|When pressed redirect correctly to the delete booking form.|
|Update Btn|ok|Also works correctly redirecting to the update form.|

#### Booking details page
|Element tested|Test Result|Note|
|--|--|--|
|Booking details|ok|The page display correctly the booking details|
|Ratings in review|ok|Displayed correctly and the given value is correctly selected.|
|Message |ok|Works as intended.|
|Submit review btn|ok|Correctly submit the review.|
|Update Booking btn|ok|Redirect correctly to the update form.|
|Back btn|ok|Redirect correctly to the booking list page.|

#### Update Booking page
|Element tested|Test Result|Note|
|--|--|--|
|Form fields|ok|All acts correctly with no issue.|
|Update booking btn|ok|Correctly updates the booking.|
|Back btn|ok|Correctly redirect to the booking list page.|

#### Cancel Booking page
|Element tested|Test Result|Note|
|--|--|--|
|Page|ok|Display correctly minimal booking datas.|
|Confirm Deletion btn|ok|Correctly eliminates the booking.|
|Back btn|ok|Correctly redirect to booking list page.|

#### Contact Us page
|Element tested|Test Result|Note|
|--|--|--|
|Form|ok|Displayed correctly the textarea.|
|Send Message btn|ok|Correctly start the send email action.|

#### Profile page
|Element tested|Test Result|Note|
|--|--|--|
|Page|ok|Displayed correctly the info of the current user.|
|Edit btn|ok|Correctly redirect to edit form.|

#### Edit profile page
|Element tested|Test Result|Note|
|--|--|--|
|Form|ok|Displayed as intended the form.|
|Save btn|ok|Works as expected saving the new details|
|Back btn|ok|Redirect correctly.|
#### Accounts template
- For this pages , I many times create , delete , reset accounts, logged in and logged out. Everything works as intended also the logic is not beeing touched from these accounts.

## Technologies Used
- For this project many technologies were used
    - [Django](https://docs.djangoproject.com/en/5.1/)
        - Primary framework to build this app in python.
    - [DjDatabase](https://pypi.org/project/dj-database-url/)
    - [PsycoPg2](https://www.psycopg.org/docs/)
        - These two are used for database configuration and interaction to PostgreSql and Heroku
    - [Cloudinary](https://cloudinary.com/documentation)
        - Used to integrate/manage assets like images(much more can be done).
    - [Allauth](https://docs.allauth.org/en/latest/)
        - For authentication like for logins emails and passwords.
    - [Summernote](https://summernote.org/getting-started/)
        - Editor.
    - [Gunicorn](https://docs.gunicorn.org/en/stable/)
        - Used to serve the application to production.
    - [Whitenoise](https://whitenoise.readthedocs.io/en/latest/django.html)
        - A middleware for static file management. 
    - [Bootstrap 5](https://getbootstrap.com/docs/5.0/getting-started/introduction/)
        - Css framework used to style and layout.
        - Bounded with [Popper.js](https://popper.js.org/docs/v2/)
    - [Font Awesome](https://fontawesome.com/)
        - Used to add icons.
    - [Google Fonts](https://fonts.google.com/knowledge)
        - Loads the fonts used on this project.
