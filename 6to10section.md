# Build / Test / Deployment 
- In this section we will speak about the following points.
6. Testing / Validation
7. Technologies
8. Languages
9. Deployment
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
    - [GitPod](https://www.gitpod.io/docs/introduction/getting-started)
        - Used for development enviroment for my workspace.
## Languages used
- [Python](https://www.python.org/doc/)
    - The code itself is written in python handling the core functionalities.
- [Html](https://developer.mozilla.org/en-US/docs/Web/HTML)
    - Html templates and structures.
- [Css](https://developer.mozilla.org/en-US/docs/Web/CSS)
    - To style and visually organize the content of this project. (With the help of Bootstrap)
- [Javascript](https://developer.mozilla.org/en-US/docs/Web/JavaScript)
    - To handle some of the front-end functionalities. 
- [Sql](https://developer.mozilla.org/en-US/docs/Glossary/SQL)
    - Not directly written, but was used to interact with the database.
## Deployment.
NestBite is hosted in:
- Heroku
- GitHub
- Postgres database
- Built with Gitpod

### Deployment on Gitpod

- Go to the [Github](https://github.com/) page.
- Access the Repository
- Select Settings
- On the left side you need to get into Pages
- You will see Build and deployment.
- Under the Branch select main
- Click save
- When correctly executed, the page will indicate the succesful deployment and the link related to the repository.

### Deployment on Heroku
- Ensure that all your dependencies are listed in the requirements.txt file by running the command: pip3 freeze > requirements.txt in your Python terminal. This will add all your requirements to the requirements.txt file.
- Visit the [Heroku](https://www.heroku.com/) website, sign up by clicking the button in the top right corner, then log in/sign up.
- Click on New in the top right corner and select Create new app.
- Choose a unique name for your app related to your project, set your region to for example "Europe"(you can choose the region that you are in), and click Create app.
- Go to the Settings tab, then click Reveal Config Vars under Config Vars.
    - In here you will set up all your keys and values for example secret keys and and password.(This will keep your vars safe.)
- Scroll down to the Buildpacks section, click Add buildpack, and select Python. (My build pack is heroku/python)
- Scroll back up and go to the Deploy tab. Under Deployment method, select GitHub, search for your GitHub repository by name, and select the correct one.
- Scroll down to Automatic deploy, choose the main branch so that any changes pushed to GitHub will automatically update the Heroku app.
- Scroll down to Manual deploy and click Deploy Branch. Once the deployment is complete, click on View to open a new tab and display your deployed app.
- `Important` to mention is that the actual deployed version needs to have the debug setting set to False. This will keep any important detail safe.

### PostgresSql from Code Institute
- In here I followed the form implemented in the course by Code institute to create my database and receive its link.
- Initially I created a env.py (make sure is added to the .gitignore file to keep your details safe).
- Import in the env.py file the `os` system.
- I set the database Url using os.environ.setdefault("database_url", "mydatabase_url")
- Installed DjDatabase , Psycopg2 and added them to the requirements.txt.
- Import os and dj_database_url in the settings.py of your app, connect the settings to the env.py importing it.
    -     if os.path.isfile('env.py'): import env.
- Connect the Environment variable to the DATABASE_URL that is in the env.py.
    #### Connect Database to Heroku
    - Go to Settings in your Heroku and click on Reveal config vars.
    - Add a new Config Var with key of DATABASE_URL and as a value the PostgreSql (you can also find the url in your previously set env.py file.).
    - Press add when is set up.
    - `To note` is that sometimes you can have already an url set up by heroku to PostgreSql. You can remove it and replace it with your own.
    - To remove it press on Resources and delete the Add-on ,once done return to settings and follow the steps above.
### Cloudinary
- Install Cloudinary from your terminal and add it to your requirements.
- SignUp/Log in  to Cloudinary.
- In the dashboard copy the url (CLOUDINARY_URL)
- As we did for the database you need to add the url to the env.py file(check PostgreSql section above.)
- Add cloduinary and cloudinary_storage(storage needs to be directly under the django.contrib.staticfiles) to your INSTALLED_APPS in the settings
- Import ClodinaryField from cloudinary.models and is ready to use.
- Remember to migrate the new added field (`python manage.py makemigrations  -->  python3 manage.py migrate`).
- Commit and deploy!


