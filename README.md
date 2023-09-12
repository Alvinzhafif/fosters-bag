# Create a New Django Project
Before i started making the django project, i initialized the required items. Which is, the local repository, then installed the requirements, and created the environment. Finally, i initialized the django project and added the .gitignore file for it to be pushed into github later
# Create an App with the name 'main' on that project
For this step, first, i initialized the virtual environment again and create the main app by inputting 'python manage.py startapp main' on to the terminal. Next, i updated the settings.py so that the app main is now registered on that project
# Create a URL routing configuration to access the 'main' App
Now, i can create a file named urls.py inside of my projects(main) directory. Then, i imported 'import path' from the django library, this will be used for routing the url to the appropriate view function that will be made afterwards. Next, i imported 'import show_main" this will be used to take a request and turn it into a response. For my current project, it will be for rendering the main app. Then, i inputted the name for my app('main') and create the path of the url pattern to display my 'main' app later 
# Create a model on the 'main' app 
Now, i head over to the models.py file, and then i imported the models from django. This will be used for making the necessary components, which are the attributes. Next, i made a class that can hold the mandatory attributes. Those attributes include, name, amount, and description.
# Create a function in 'views.py' that returns an HTML template containing your application name, your name, and your class.
For this step, i head over to the views.py file. Then, i imported render from django for rendering HTML with the given data, then i created the function show_main. This function will be used to handle the HTTP request and returns the content of the displayed content. After adding the necessary dictionary elements into the function, i add "return render(request, 'main.html', context)" this will be used for rendering the html request, displayed content, and the main html itself.
# Create a routing in 'urls.py' to map the function in 'views.py' to an URL
Before launching the app in "Adaptable.io" we need to configure the URL routing so that the website can properly display the content that we wanted. So here, i came back to the urls.py but, different from the first time now i opened it inside of my "Assignment_2" directory instead of the 'main' project directory. From there, i added another import, which is "from django.urls import path, include". This will be used to define the url pattern and to include another URL configuration. then i defined the url of my 'main' app by creating the path for it, and include the configuration of the url from the 'main' directory previously
#  Deploy your app to Adaptable so it can be accessed through the internet
Finished!, but actually not yet. For my app to be accessed through the internet i need to deploy it first into "Adapatble.io". So first, i go into the website and then login with my git account. Then, i pressed the new app button and connect it to this repository. Next, i chose Python App Template and PostgreSQL as my deployment template and database respectively. Finally, i edit the start command and added my current python version. And then my app is ready and finally can be accessed through the internet.
<br />
<br />
<br />
<br />
<img src="/assets/image.png">

