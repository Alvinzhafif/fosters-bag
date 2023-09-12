# > Create a New Django Project
Before i started making the django project, i initialized the required items. Which is, the local repository, then installed the requirements, and created the environment. Finally, i initialized the django project and added the .gitignore file for it to be pushed into github later
# > Create an App with the name 'main' on that project
For this step, first, i initialized the virtual environment again and create the main app by inputting 'python manage.py startapp main' on to the terminal. Next, i updated the settings.py so that the app main is now registered on that project
# > Create a URL routing configuration to access the 'main' App
First, i created main.html. This will be where i will develop the main display of my website, now i edit my urls.py file where i will import the necessary components and then list the 'main' app so there will be an existing url to the app. Finally, i imported the include for including my app and add the path for my 'main' app
# > Create a model on the 'main' app 
Now, i head over to the models.py file, and then i imported the models from django. This will be used for making the necessary components, which are the attributes. Next, i made a class that can hold the mandatory attributes. Those attributes include, name, amount, and description.
# > Create a function in views.py that returns an HTML template containing your application name, your name, and your class.
For this step, i head over to the views.py file. Then, i imported render from django for rendering HTML with the given data, then i created the function show_main. This function will be used to handle the HTTP request and returns the content of the displayed content. After adding the necessary dictionary elements into the function, i add "return render(request, 'main.html', context)" this will be used for rendering the html request, displayed content, and the main html itself.
