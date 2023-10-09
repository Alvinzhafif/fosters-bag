## My Deployed App
https://fosters-bag.adaptable.app/main/

### Create a New Django Project
<hr>

Before I started making the Django project, I initialized the required items. Which is, the local repository, then installed the requirements, and created the environment. Finally, I initialized the Django project and added the `.gitignore` file for it to be pushed into GitHub later

### Create an App with the name `main` on that project
<hr>

For this step, first, I initialized the virtual environment again and created the main app by inputting `python manage.py startapp main` onto the terminal. Next, I updated the settings.py so that the app main is now registered on that project

### Create a URL routing configuration to access the 'main' App
<hr>

Now, I can create a file named `urls.py` inside of my project's (main) directory. Then, I imported the `import path` from the Django library, this will be used for routing the URL to the appropriate view function that will be made afterward. Next, I imported `import show_main` which will be used to take a request and turn it into a response. For my current project, it will be for rendering the main app. Then, I inputted the name for my app `main` and created the path of the URL pattern to display my `main` app later 

### Create a model on the 'main' app 
<hr>

Now, I head over to the `models.py` file, and then I import the models from Django. This will be used for making the necessary components, which are the attributes. Next, I made a class that can hold the mandatory attributes. Those attributes include name, amount, and description.

### Create a function in 'views.py' that returns an HTML template containing your application name, your name, and your class.
<hr>

For this step, I head over to the `views.py` file. Then, I imported render from Django for rendering HTML with the given data, then I created the function show_main. This function will be used to handle the HTTP request and return the content of the displayed content. After adding the necessary dictionary elements into the function, I add `return render(request, 'main.html', context)` this will be used for rendering the html request, displayed content, and the main html itself.

### Create a routing in 'urls.py' to map the function in 'views.py' to an URL
<hr>

Before launching the app in `Adaptable.io` we need to configure the URL routing so that the website can properly display the content that we wanted. So here, I came back to the urls.py but, different from the first time now I opened it inside of my `Assignment_2` directory instead of the `main` project directory. From there, I added another import, which is `from Django. urls import path, include`. This will be used to define the URL pattern and to include another URL configuration. then I defined the URL of my `main` app by creating the path for it, and including the configuration of the URL from the `main` directory previously

###  Deploy your app to Adaptable so it can be accessed through the internet
<hr>

Finished!, but not yet. For my app to be accessed through the internet I need to deploy it first into `Adapatble.io`. So first, I go into the website and then log in with my git account. Then, I pressed the new app button and connected it to this repository. Next, I chose Python App Template and PostgreSQL as my deployment template and database respectively. Finally, I edited the start command and added my current Python version. Then my app is ready and finally can be accessed through the internet.

### Create a diagram explaining the flow of client requests to a Django web app and its response. Also in the diagram, explain the connections between urls.py, views.py, models.py, and the HTML file(s).
<hr>

<img src="/assets/image.png">


### What is the purpose of a virtual environment? Can we create a Django web app without a virtual environment?
<hr>

A virtual environment is used to isolate packages for different projects. This will be useful when encountering projects that have lots of dependencies, such as Django itself. It is highly recommended to use a virtual environment when creating a new Django project as it can prevent global installation or random directory installation of files on your computer. The answer is yes, you can create a Django project or web app without a virtual environment but it will cause the troubles mentioned before

### What is MVC, MVT, and MVVM? Explain the differences between the three.
<hr>

MVC(Model-View-Controller), MVT(Model-View-Template), and MVVM (Model-View-ViewModel) are all architectural design patterns that are used for separating the concerns of an application. In MVC the model and view interact directly, this, however, can lead to tight coupling and result in difficulty in extending the app. In MVT the model and view interact through the template, a template that contains an HTML code for the view file and renders the HTML file data. While in the MVVM, the model and view interact through the view model. In this model, the view does not interact directly with the model, but it can receive data from the model.
### What is the difference between POST form and GET form in Django?
<hr>

**POST** and **GET** forms are the only HTTP methods to use when dealing with forms in **Django**< br />

**POST** in general, should be used anytime we want to change anything in the database. A positive difference between **POST** and **GET** is that, **POST** encodes the data so that it can be sent for transmission. This also affects that, the data values will not be visible. Another one is that the **POST** method doesn't have any restriction in data types, which means it can send any form of data. An example of a **POST** form request is logging in to a website. When users log in to a website they will usually need to enter their passwords or other kinds of private information, such as bank accounts, credit card numbers and more. By using **POST** their data would be secured and encoded so it would not be vulnerable.<br />

**GET** on the other hand bundles the data into a string to compose a URL. This also means that **GET** can only use one form of data types, which is strings. The composed string will contain adresses to the object that is requested. An example of a **GET** form request would be searching an item in an online shop or searching something up on a search engine. This will involve in requesting the address of the requested object, as for searching up items in an online shop we will be redrected to the shop page conbtaining the item we requested, same with searching up articles or news in a search engine.
###  What are the main differences between XML, JSON, and HTML in the context of data delivery?
<hr>

Before Knowing the differences, what is `XML`, `JSON`, and `HTML` in general?

`XML` stands for extensible mark-up language. `XML` is designed for carrying out data, this is also one of the reason why `XML` can process difficult datas such as, trees and graphs.
`XML` focuses on generality, usability, and simplicity. `XML` is configured such that its design focuses on documents, despite that, many web services still uses `XML`. This is due to the fact that, `XML` can representate arbitrary data structures<br />

`JSON`or JavaScript Object Notation is a lightweight format for storing and is commonly used for sending datas from a server to a webpage. `JSON` is known to be "self-describing" and easy to understand, this is because `JSON` is represents its datas as a dictionary styled key and value pairs. `JSON` is also very efficient when it comes to parsing, which makes it the perfect candidate for data delivery. <br />

Hyper Text Markup-Language a.k.a `HTML` is a markup language used for creating web pages. Every webpage, is constructed by a `HTML` as the language will provide the display for the website. `HTML` is used to define structures and add interactivity to the web page.<br />

But in terms of data delivery are the three of this the same?, the answer is no. While `XML` and `JSON` shares the same functionality which is data transmission. `HTML` is used for describing and displaying the data 

### Why is JSON often used in data exchange between modern web applications?
<hr>

`JSON` is often used as it excels in 4 categories. First is its easy in terms of readability and parsing. Since `JSON` uses a test-based format, it is easier for us to read the program and for the machine to write the program as well. this can be beneficial, as it will help in parsing for any platform or programming language. Secondly is that `JSON` is lightweight and efficient so that the perfomance of transmitting over minimal bandwith is very optimum. Thirdly, is the Language-independece capability. This allows `JSON` to be used by any programming language there is, which allows easy exchange between either systems or applications. And finally is it is widely supported by any programming language. This makes it easy to fund the library and data when it comes to working with json datas.

### Create a form input to add a model object to the previous app.
<hr>

Before making the form i implemented a skeleton for avoiding code redundancy and any other possible problems. First i opened my local directory in an `IDE` for me it's `visual studio code`. Next, i opened the `root` directory or the common directory where the requirements and others are placed in it. Then i created a folder named `templates` and added a file named `base.html` inside of it. Inside of the file i added an `HTML` code that serves as the base for my web page. Then, i head over to my `settings.py` in my `Assignment_2` folder and edited the `TEMPLATES` line so it can detect the base html structure. Next, i went to my `main` folder and edited my `main.html` file, so that it implements the basic structure.<br />

Now i can make the forms. First, i head over to the `main` folder and created a new file named `forms.py` this will serve as the base for the form like structure that accepts and saves inputs. Then, i imported a few components namely, `ModelForm` and `Product`. `Product` is invoked form the `models.py` file which contains every data and their data type that will be displayed in the web page later on. Secondly, in the `views.py` file inside of the `main folder`, i imported a few components that will be used to make the function for saving the content of the inputted form into the web page. Those imported components involve, `HttpResponseRedirect` for processing responses, `reverse` for retrieving the `URL` detail, `ProductForm` which is the class used for creating the form, and finally the `Product` for implementing the data and necessary datatypes. Next, still in the same file i created a function for saving and adding  the data into the webpage after the form is inputted. The function is called `create_product` and everytime the post is pressed the content of the form is saved and return the render request so the webpage can be rendered. Next, i head over to my  `show_main` function in `views.py` and added an extra statement for processing the data and fecthing the products objects.
Then, i open the `urls.py` file inside of the `main` folder and import the recently created `create_product` function and add it to the path in the in `urlpatterns`. Next, in the `templates` sub directory next to `main.html` i created a new `HTML` file named `create_product.html` that implements a `django` `POST` method and implement a table display. For the finishing touch, i went over to the `main.html` and added a few lines of code that implemented the `create_product.html` for it to be displayed on the web page.

###  Add 5 views to view the added objects in HTML, XML, JSON, XML by ID, and JSON by ID formats and create the URLS for each of them
<hr>

The HTML view has been made on the previous step but what about the others?, well for `XML` i head over to the `views.py` file again and import some necessary components and created a new function `show_xml` with a request parameter. Then, i added a return statement to it as an XML. Then, on the `urls.py` i imported that function and add it to the `urlpatterns` for it to be routed into the `URL`. Then, i repeated the same steps for the `JSON` difference is just in the functions name. Next for the `ID` formats, it is basically the same with the previous ones. But change the data variable and change it with `data = Product.objects.filter(pk=id)`. This allows the use of id's when searching up the items based on an `ID` address.

### Access the five URLs in point 2 using Postman, take screenshots of the results in Postman, and add them to README.md.
<hr>

#### 1. Accessing json
<img src="/assets/pic1.png"><br />
#### 2. Accessing xml
<img src="/assets/pic2.png"><br />
#### 3. Accessing html
<img src="/assets/pic3.png"><br />
#### 4. Accessing json by id
<img src="/assets/pic4.png"><br />
#### 5. Accessing xml by id
<img src="/assets/pic5.png"><br />

### What is `UserCreationForm in Django?` Explain its advantages and disadvantages.
<hr>

`UserCreationForm` is a command in Django that is used for creating users in the web application. The `UserCreationForm` has three main fields, the `username` field for the user to input their username of the account, the `password1` field for the account's password, and the `password2` field which is commonly used for confirming the inputted password. 
The advantage of using `UserCreationForm` is its ability for user validation. Those validations come in many forms, an example would be when creating a blank form, the user will be asked to fill in every field before the form can be submitted. Another feature is that it can validate various amounts of inputs, such as Emails. In the Email field, when the user inputs a string without the `@gmail.com` suffix, the form will automatically decline the submission and point out the error. An Email is a string of typed data, but can the form validate other types of data? The answer is yes, it can validate other data types such as integers, decimals, and many more.
The disadvantage of using `UserCreationForm` is that it uses the Django form class, it's not actually a downside, but since we are creating it in a separate Python file we need to import the whole module. This will cause restrictions on the class which can affect your form.

### What is the difference between authentication and authorization in the Django application? Why are both important?
<hr>
both authentication and authorization are important in Django, authentication can be used for verifying if the user is really who they are and authorization can be used to determine what kind of access that user has.<br />
the difference between both are the following, <br />
Authentication: used for authenticating the user, Works through passwords, pins, or any other security information, takes place first, is visible to the user, and is changeable by the user<br />     
Authorization: used for authorizing the user's access, Works through the settings that are implemented in the code, takes place after authentication, and is not visible and changeable for the user           

### What are `cookies` on a website? How does Django use cookies to manage user session data?
<hr>

`cookies` are small pieces of information stored in the client's browser. Generally, it is used for storing the user's data temporarily or permanently. Cookies have an expiry date which will make the data they hold be removed when the time has passed, Django provides a method for setting and fetching `cookies`.<br />
Django uses `cookies` by containing a special session id to identify each browser and each of its associated session with the site, by default the actual session is stored in the database. This is way safer compared to storing data in `cookies`, as the data in cookies has a possibility to be accessed by hackers or any malicious user.

### Are  `cookies` secure to use? Is there potential risk to be aware of?
<hr>

`cookies` itself do not pose any security risk, but it can be used by malicious users as a method to exploit your personal datas. A great potential risk would be, that `cookies` can introduce you to dangerous websites and a very rare case it could introduce you to malware as well. This could happen if your `cookies` was exposed to cyber criminals.<br />
In conclusion the biggest threat that `cookies` poses is a security risk, like i mentioned before is not the cookie itself that is dangerous but the possibilities of malicious user exploiting it. Currently the most advanced `cookies`
is the one used in marketing, the `cookies` for this category has the ability to track the users over time. Those tracking can come from many sources, counting ad impressions, views and clicks, even limiting pop ups and ad sequence. This `cookies` are the one that can do user profiling / tracking of website preferences

###  Implement registration, login, and logout functions to allow users to access the previous application.
<hr>

#### 1. Create a registration<br />
before i start this step, i activated my virtual environmen first to make it easier to test the web page later on, for activating it i go to the local repository on my command prompt and use the command `enc\Scripts\activate.bat` on the cmd. Now onto the first step, i went over to my `views.py` file, this file plays a crucial lore as every function such as create product is located inside here. Next i imported a few components, `redirect`, `UserCreationForm`, and `messages`. The `redirect` will be used for redirecting us to the webpaage once the form has been saved, the `UserCreationForm` will be used for creating the forms easily as it is a built in form from Django itself, and `messages` will be used to display a message once we have succesfully filled the form. Next i created a function called `register` that will be used for creating a registration, the function will have a `request` parameter as it will process and pass the user's input, next i call the `UserCreationForm()` function and make an if else statement for assuring that the user fills in the correct and necessary datas, if the user fills in the correct datas the form will be saved, a message of successfully creating the account will be shown, and we will be redirected back to the page.<br />
Next, i created a new `HTML` file in the main/templates folder, then i created a statement so that this file inherits the `base.html` file. Next i added the title in the `meta` block, created a class named login for my container, and created the title of the registration page. Next, i created the form element with the method `'POST'` for creating the registration form, then added a CSRF(cross-site-request-forgery) for anticipating against CSRF attacks,  then i make the form results into an HTML table for generating the necessary HTML `form` fields, next i created the submit button with the label "Daftar" for the user to submit their account request. Then i made the if statement for generating the message when the account is successfully created. And finally, i add the path to `urls.py` so the file can be accessed. 
#### 2. Create a login function<br />
for this step i went back to the `views.py` file, i imported the built in function `authenticate` and `login`, this two functions will be used for authenticating the user and for logging the user in. Then i editted the `login_user` function, and added the variable `user` that serves as the authentication process of the account. Next, i made an if else statement depending on the output of the authentication, if the login credentials are fullfilled the account will be logged in and we will be redirected to the web page, if otherwise, a message of "wrong username or password" will be shown. <br />
next i made a new `HTML` file named `login.html` in the `templates` folder inside of the `main` folder. Then i created a statement so that this file inherits the `base.html` file. Next i added the title of Login and, and creted a class named login for my container, and created the title of the Login page. Then, i created the form element with the method `'POST'` for creating the login form, then added a CSRF(cross-site-reqest-forgery) for anticipating against CSRF attacks, the i make the form in an `HTML` table like form for generating the necessary HTML `login` field, next inside of the table i created the lable `Username: `, `Password: `, and blank on the third one as the last would only be used for the login button. For the username field i added the input type of `text` as it is a string text and redirect the inputted username back to the `authenticate` function for authenticating the username, and likewise the password field with the input password, as the display is intended to be in a password like form where the text will be depicted as dots after its inputted. and redirect the inputted password to the `authenticate` function for authenticating the password. if the login crednetials are not fullfilled whether it is a false username or false password the meesage of "wrong username or password" is shown, Then i added the link path with the text for those who have not created an account yet will be redirected to the registration form. Then i head over to the `urls.py` once again for registrating the path link to the login form webpage.
#### 3. Create a logout function<br />
for this step i went back to the `views.py` file, i imported the built in function `logout` function, this function will be used for logging out from the web page and redirected to the login page. Then i added the function `logout_user` for logging out from the account and redirects the user to the login page. Then, inside of the `templates` subdirectory inside of the `main` folder, i head over to the `main.html` and added the code for producing the logout button right after the table of products. Then i added the url path to the function for listing the function into the web page.

### Create two user accounts with three dummy data entries for each account using the model previously created in the application.
<hr>

for this step i run the server from the command prompt, i ran the command for activating the virtual environment `env\Scripts\activate.bat` command in the cmd, then i visited the local host web to access my web page. There i made two accounts and added three items respectively in both accounts.

###  Connect Item model with User
<hr>

For this step i opened my `models.py` file inside of the `main` subdirectory, and imported the `user` function from the library. Next from the `Product` model that already existed i added a newline of code that implements a `ForeignKey` structure where each of the data inputted will be related to only the associated user. Next in the `create_product` function i added a new line of code that will prevent the form from saving the products data into the database, instead we assign that product to the user so that each of the product will only belong to the associated user. Then, added the new element `name` inside of the showmain for showing the current user's name inside of the webpage. For the changes to be saved i went over to my cmd, head to the directory of the local project and then, activate the virtual environment again by using the command `env\Scripts\activate.bat`. After that i run the command `Python manage.py makemigrations` to commit the changes inside of the `models.py` file. Since no default values are added for the `user` field the env will warn us as the database needed to store some default values, to fix that the environment will provide an option of provide a default value. To resolve the issue we can simply select that option, and after that we can do `Python manage.py migrate` to commit the changes and access the renewed web page that can have two seperate items for each account.

### Display the information of the logged-in user, such as their username, and applying cookies, such as last login, on the main application page.
<hr>

for this step we need to implement `cookies`, for the displaying the information of the logged-in user we can simply add the element name in to the `show_main` function that contains the data of who is the person/user's name that is logging in into the website. To add `cookies` i head over to the `views.py` file and imported three functions from the library, `datetime` (for displaying the date and time when the users logged in into the account), 'Httpresponseredirect`for redirecting or forwarding the URL, and  `reverse` for retrieving the `url`. Next, inside of `login_user` funnction in the if statement i added a response object for showing the contents for the main web page. Then i set a cookie that can track the last login of the user. Then inside of the `show_main` function i added the element last login to track the request using a `cookie`, then i modify the `logout` function as well, and added the same response object to show the contents of the main web page and added the line `response.delete_cookie` to delete the last login cookie when the user logs out. Then inside of the `main.html` file, i added the line last log in to display the last time the user logged in into the web page 

### Explain the purpose of some CSS element selector and when to use it.
<hr>

`CSS` are used for styling your webpage such as creating custom positioning of the text, recoloring the text, styling images, and many more. `CSS` uses selectors to identify which part of the HTML that you want to style, there are a few selectors that `CSS` implements, such as select by id, select by class, select universally, and many more. Select by id can be used when you are only trying to modify one unique element, such as a text for the title of the webpage, to create an id we can use the pund sign `#` and add the unique id name after it before making the content of the `CSS` file. Select by class can be used when you are trying to style one whole class of an attribute, to create the class select we can add the dot sign `.` and the specific class name we want to style. And select universally is used when we want to edit the whole html page, such as for changing the whole webpage's text color or for positioning the contents, to crete a universal select we can add the asterisk sign `*` before filling out the content of the `CSS` styling file

###  Explain some of the HTML5 tags that you know.
<hr>

There are many `HTML5` tags that can be used, each with their own unique specifications. A few of their examples would be the `<img>`, `<hr>`, `<p>`, `<h>`, and `<table>`. the `<img>` tag is used to specify an image, this is commonly used for adding images to the webpage for a banner,background,and any other image needs for the webpage. the `<hr>` is used for specifying a horizontal break line, usually it is used in blogs for seperating paragraphs and adding neatness to the webpage. The `<p>` tag is used for specifying a paragraph, in which every sentence inside of the tag until it reaches the end `</p>` will be considered as a paragraph. The `<h>` tag is used to specify a heading, it is commonly used for titles and to mark important points of the webpage. The `<h>` tag is followed by a number ranging from 1-6, ranked from smallest to biggest. the `<table>` tag is used for specifying tables, this tables is usually used to display data in a neat order or in a tabular like form on the webpage.

### What are the differences between margin and padding?
<hr>

`padding` is the space between the content and the border of an element. `padding` is valuable in making additional space inside an element, keeping it at a set distance from other aspects of a website. Using `padding` is extremely beneficial when you need to separate text boxes and images while also keeping them aligned.<br>
`margin` on the other hand is the space around the border of an element. `margin` surrounds an element and informs the web browser on how many spaces should be left between the element and the external margin of the webpage. `margins` can also be used to set distance between two distinct elements.<br>
The difference between `margin` and `padding` is that, `padding` represents the amount of inner space that element has, while `margin` is the amount of whitespace surrounding that element. `margin` are also usually unable to be set automatically, while for `padding` it is possible to set it automatically. and lastly, `margin` would not be affected by styling from another element, while `padding` can be affected 

###  What are the differences between the CSS framework Tailwind and Bootstrap? When should we use Bootstrap rather than Tailwind, and vice versa?
<hr>

`Bootstrap` is a`CSS` framework that is used for building responsive and mobile-first projects on the web, `Bootstrap` is a component based framework, which means it comes with prebuilt components and includes other utilities for layering displays,spacing etc.<br>
`Tailwind` is a `CSS` framework that is used for building utility-first framework for builidng rapidly custom user interfaces. Unlike other frameworks `Tailwind` is low-level, which means it offers you collection of classes that can be implemented to your `HTML` or webpage directly without touching `CSS`.<br>
The `Bootstrap` framework compels the developer to follow a certain template like structure. The developer themselves could overwrite the  `Bootstrap` framework but that would result in redundance as there is not realky any need to use the given framework. This can lead to similarity in `Bootstrap` framework developer's website, as all the websites may have different colors, backgrounds, and layouts but their frame concept might be similar.<br>
While using `Tailwind` allows the developer to customize the web page as they please, in `Tailwind` there are no restrictions to using and following a certain given template. In `Tailwind` the developer can edit their web page from scratch as each and every aspects of the framework is customizeable by the developer

### Explain how you implemented the checklist above
<hr>

Here are the changes i made:
<img src="/assets/pic6.png"><br />
<img src="/assets/pic7.png"><br />
<img src="/assets/pic8.png"><br />
<img src="/assets/pic9.png"><br />

In a nutshell the changes i made is adding backgrounds,text colors, and card display using `Bootstrap`. The `CSS` files are then stored inside of the new `static` folder located inside of the `main` folder.

### Explain the difference between asynchronous programming and synchronous programming.
<hr>

`Asynchronous` programming is a non blocking architecture, which means the execution of a program is not dependant on another. This also implies that multiple tasks can run simultaneously.<br>
`Synchronous` programming is a blocking architecture, which means the execution of a program is dependant on the other. A task must be answered before it can successfully iterate through the next task<br>
In addition towards their difference is listed as follows:
* Asynchronous is multi-thread, which means operations or programs can run in parallel.
* Synchronous is a single-thread, so only one operation or program will run at a time.
* Asynchronous is non-blocking, which means it will send multiple requests to a server.
* Synchronous is blocking — it will only send the server one request at a time and wait for that request to be answered by the server.
* Asynchronous increases throughput because multiple operations can run at the same time.
* Synchronous is slower and more methodical.

### In the implementation of JavaScript and AJAX, there is an implemented paradigm called the event-driven programming paradigm. Explain what this paradigm means and give one example of its implementation in this assignment.
<hr>

an `Event-driven programming paradigm` is a method of programming where the flow of the program is determined by the events that occur throughout the program. This means that the code will not execute a program without an event occurring, making the program itself more responsive as it is not running constantly.<br>
An example of its implementation in this assignment is the `create_product`form made using `AJAX`, the form will wait for the user to input the required fields then after pressing submit the program will be executed and the item will appear on the web page.

### Explain the implementation of asynchronous programming in AJAX.
<hr>

`AJAX` stands for Asynchronous JavaScript and XML, `AJAX` itself executes the data transfer in the background which makes the necessity of reloading a web page for executing a command unnecessary. `AJAX` implements Asynchronous programming by making asynchronous requests to the `HTTP` server, in addition the `JavaScript` in `AJAX` has the `async` and `await` command. Both of this command will make the program wait for an input and then be executed after, while also making the web page still accessible without the necessity of refreshing the web page.

### In this semester, the implementation of AJAX is done using the Fetch API rather than the jQuery library. Compare the two technologies and write down your opinion which technology is better to use.
<hr>

Before we can compare both technologies it is best to know what is `Fetch API` and `JQuery library`.<br>
`Fetch API` is an `AJAX-JavaScript` implementation that provides an interface for accessing and manipulating parts of the protocol, those parts can be requests or responses.<br>
`JQuery library` is an `AJAX-JavaScript` implementation that provides the same features as `Fetch API` however, it is older and more native to `JavaScript`.<br>
the difference of both implementation are as follows:
* the `Fetch API` is a more modern and advanced version of the `JQuery library` so performance-wise it is better.
* in terms of community `JQuery library` is more popular, this implies there are tons of library Plugins made by the community.
<br>
In my opinion using `Fetch API` is better as it is more modern and suited to modern web pages. However if a web page is already made using a `JQuery` implementation there's no need for changing it into `Fetch API` as it is still customizeable and not out-of-date for the modern web page.

### Explain how you implemented the checklist above step-by-step (not just following the tutorial).
1. First i implemented the following code into the `views.py` file
   ```
    def get_product_json(request):
    product_item = Product.objects.filter(user=request.user)
    return HttpResponse(serializers.serialize('json', product_item))
    ```
   This is a new function that is added to get the `product` using `JSon`, then i filter the the products so that the products displayed in the web page will be seperated for each users
   respecitvely. And `HttpResponse` is used for serializing the `Django` into `JSon` and retrieving it as a response.

2. Next, i implemented an add product function using `AJAX` in `views.py` file
```
  @csrf_exempt
  def add_product_ajax(request):
    if request.method == 'POST':
        name = request.POST.get("name")
        price = request.POST.get("price")
        description = request.POST.get("description")
        amount = request.POST.get("amount")
        type = request.POST.get("type")
        rarity = request.POST.get("rarity")
        user = request.user

        new_product = Product(name=name, price=price, description=description, user=user, type=type, rarity=rarity, amount=amount)
        new_product.save()

        return HttpResponse(b"CREATED", status=201)

    return HttpResponseNotFound()
```
    this function implements `AJAX` for adding the products into the web page, if the request is post every fields data will then be retrieved and made into the product using the `      
  `new_product` statement, and if the request is post then the HttpCreated response is returned. If the request is not post a 404 Not Found error message is shown.
  After adding the function i head over to my `urls.py` in the `main` subdirectory and added the url routing to the `get_product` and the `add_product_ajax` function as well 
3. Now i need to modify the `main.html` file in the the `templates` directory in side of the `main` directory
 




