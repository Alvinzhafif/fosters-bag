## My Deployed App
https://fosters-bag.adaptable.app/main/

### Create a New Django Project
Before i started making the django project, i initialized the required items. Which is, the local repository, then installed the requirements, and created the environment. Finally, i initialized the django project and added the `.gitignore` file for it to be pushed into github later

### Create an App with the name 'main' on that project
For this step, first, i initialized the virtual environment again and create the main app by inputting `python manage.py startapp main` on to the terminal. Next, i updated the settings.py so that the app main is now registered on that project

### Create a URL routing configuration to access the 'main' App
Now, i can create a file named `urls.py inside` of my projects(main) directory. Then, i imported `import path` from the django library, this will be used for routing the url to the appropriate view function that will be made afterwards. Next, i imported `import show_main` this will be used to take a request and turn it into a response. For my current project, it will be for rendering the main app. Then, i inputted the name for my app `main` and create the path of the url pattern to display my `main` app later 

### Create a model on the 'main' app 
Now, i head over to the `models.py` file, and then i imported the models from django. This will be used for making the necessary components, which are the attributes. Next, i made a class that can hold the mandatory attributes. Those attributes include, name, amount, and description.

### Create a function in 'views.py' that returns an HTML template containing your application name, your name, and your class.
For this step, i head over to the `views.py` file. Then, i imported render from django for rendering HTML with the given data, then i created the function show_main. This function will be used to handle the HTTP request and returns the content of the displayed content. After adding the necessary dictionary elements into the function, i add `return render(request, 'main.html', context)` this will be used for rendering the html request, displayed content, and the main html itself.

### Create a routing in 'urls.py' to map the function in 'views.py' to an URL
Before launching the app in `Adaptable.io` we need to configure the URL routing so that the website can properly display the content that we wanted. So here, i came back to the urls.py but, different from the first time now i opened it inside of my `Assignment_2` directory instead of the `main` project directory. From there, i added another import, which is `from django.urls import path, include`. This will be used to define the url pattern and to include another URL configuration. then i defined the url of my `main` app by creating the path for it, and include the configuration of the url from the `main` directory previously

###  Deploy your app to Adaptable so it can be accessed through the internet
Finished!, but actually not yet. For my app to be accessed through the internet i need to deploy it first into `Adapatble.io`. So first, i go into the website and then login with my git account. Then, i pressed the new app button and connect it to this repository. Next, i chose Python App Template and PostgreSQL as my deployment template and database respectively. Finally, i edit the start command and added my current python version. And then my app is ready and finally can be accessed through the internet.

### Create a diagram explaining the flow of client requests to a Django web app and its response. Also in the diagram, explain the connections between urls.py, views.py, models.py, and the HTML file(s).
<img src="/assets/image.png">


### What is the purpose of a virtual environment? Can we create a Django web app without a virtual environment?
A virtual environment is used to isolate packages for different projects. This will be useful when encountering with projects that have lots of dependencies, such as Django itself. It is highly recommended to use a virtual environment when creating a new Django project as it can prevent global installation or random directory installation of files on your computer. And the answer is yes, you can create a django project or web app without virtual environment but it will cause the troubles mentioned before

### What is MVC, MVT, and MVVM? Explain the differences between the three.
MVC(Model-View-Controller), MVT(Model-View-Template), and MVvM(Model-View-ViewModel) are all architectural design patterns that are used for seperating the concerns of an application. In MVC the model and view interact directly, this however, can lead to tight coupling and resulting in difficulty on extending the app. In MVT the model and view interact through template, the template that contains an HTML code for the view file and renders the HTML files data. While in the MVVM, the model and view interact through the view model. In this model the view does not interact directly with the model, but it can receives data from the model.
### What is the difference between POST form and GET form in Django?
**POST** and **GET** form are the only HTTP methods to use when dealing with forms in **Django**<br />

**POST** in general, should be used anytime we want to change anything in the database. A positive difference between **POST** and **GET** is that, **POST** encodes the datas so that it can send for transmission. This also affect that, the data values will not be visible. Another one is that the **POST** method doesnt have any restriction in data types, which mean it can send any form of data. An example of a **POST** form request is logging in into a website. When users logs in into a website they will usually need to enter their passwords or other kinds of private informations, such as bank accounts, credit card numbers ot more. By using **POST** their datas would be secured and encoded so it would not be vulnarable.<br />

**GET** on the other hand bundles the data into a string to compose an URL. This also means that **GET** can only use one form of data types, which is strings. The composed string will contain adresses to the object that is requested. An example of a **GET** form request would be searching an item in an online shop or searching something up on a search engine. This will involve in requesting the address of the requested object, as for searching up items in an online shop we will be redrected to the shop page conbtaining the item we requested, same with searching up articles or news in a search engine.
###  What are the main differences between XML, JSON, and HTML in the context of data delivery?
Before Knowing the differences, what is `XML`, `JSON`, and `HTML` in general?<br /> 

`XML` stands for extensible mark-up language. `XML` is designed for carrying out data, this is also one of the reason why `XML` can process difficult datas such as, trees and graphs.
`XML` focuses on generality, usability, and simplicity. `XML` is configured such that its design focuses on documents, despite that, many web services still uses `XML`. This is due to the fact that, `XML` can representate arbitrary data structures<br />

`JSON`or JavaScript Object Notation is a lightweight format for storing and is commonly used for sending datas from a server to a webpage. `JSON` is known to be "self-describing" and easy to understand, this is because `JSON` is represents its datas as a dictionary styled key and value pairs. `JSON` is also very efficient when it comes to parsing, which makes it the perfect candidate for data delivery. <br />

Hyper Text Markup-Language a.k.a `HTML` is a markup language used for creating web pages. Every webpage, is constructed by a `HTML` as the language will provide the display for the website. `HTML` is used to define structures and add interactivity to the web page.<br />

But in terms of data delivery are the three of this the same?, the answer is no. While `XML` and `JSON` shares the same functionality which is data transmission. `HTML` is used for describing and displaying the data 

### Why is JSON often used in data exchange between modern web applications?
`JSON` is often used as it excels in 4 categories. First is its easy in terms of readability and parsing. Since `JSON` uses a test-based format, it is easier for us to read the program and for the machine to write the program as well. this can be beneficial, as it will help in parsing for any platform or programming language. Secondly is that `JSON` is lightweight and efficient so that the perfomance of transmitting over minimal bandwith is very optimum. Thirdly, is the Language-independece capability. This allows `JSON` to be used by any programming language there is, which allows easy exchange between either systems or applications. And finally is it is widely supported by any programming language. This makes it easy to fund the library and data when it comes to working with json datas.

### Create a form input to add a model object to the previous app.
Before making the form i implemented a skeleton for avoiding code redundancy and any other possible problems. First i opened my local directory in an `IDE` for me it's `visual studio code`. Next, i opened the `root` directory or the common directory where the requirements and others are placed in it. Then i created a folder named `templates` and added a file named `base.html` inside of it. Inside of the file i added an `HTML` code that serves as the base for my web page. Then, i head over to my `settings.py` in my `Assignment_2` folder and edited the `TEMPLATES` line so it can detect the base html structure. Next, i went to my `main` folder and edited my `main.html` file, so that it implements the basic structure.<br />

Now i can make the forms. First, i head over to the `main` folder and created a new file named `forms.py` this will serve as the base for the form like structure that accepts and saves inputs. Then, i imported a few components namely, `ModelForm` and `Product`. `Product` is invoked form the `models.py` file which contains every data and their data type that will be displayed in the web page later on. Secondly, in the `views.py` file inside of the `main folder`, i imported a few components that will be used to make the function for saving the content of the inputted form into the web page. Those imported components involve, `HttpResponseRedirect` for processing responses, `reverse` for retrieving the `URL` detail, `ProductForm` which is the class used for creating the form, and finally the `Product` for implementing the data and necessary datatypes. Next, still in the same file i created a function for saving and adding  the data into the webpage after the form is inputted. The function is called `create_product` and everytime the post is pressed the content of the form is saved and return the render request so the webpage can be rendered. Next, i head over to my  `show_main` function in `views.py` and added an extra statement for processing the data and fecthing the products objects.
Then, i open the `urls.py` file inside of the `main` folder and import the recently created `create_product` function and add it to the path in the in `urlpatterns`. Next, in the `templates` sub directory next to `main.html` i created a new `HTML` file named `create_product.html` that implements a `django` `POST` method and implement a table display. For the finishing touch, i went over to the `main.html` and added a few lines of code that implemented the `create_product.html` for it to be displayed on the web page.

###  Add 5 views to view the added objects in HTML, XML, JSON, XML by ID, and JSON by ID formats and create the URLS for each of them
The HTML view has been made on the previous step but what about the others?, well for `XML` i head over to the `views.py` file again and import some necessary components and created a new function `show_xml` with a request parameter. Then, i added a return statement to it as an XML. Then, on the `urls.py` i imported that function and add it to the `urlpatterns` for it to be routed into the `URL`. Then, i repeated the same steps for the `JSON` difference is just in the functions name. Next for the `ID` formats, it is basically the same with the previous ones. But change the data variabel and change it with `data = Product.objects.filter(pk=id)`. This allows the use of id's when searching up the items based on an `ID` address.

### Access the five URLs in point 2 using Postman, take screenshots of the results in Postman, and add them to README.md.







