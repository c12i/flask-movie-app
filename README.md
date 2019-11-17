# Flask Movie App

####  A movie watchlist application.
![alt text](app.gif)


## Author
[Collins Muriuki](https://github.com/collinsmuriuki), 9/10/2019.

## Description
Application makes use of the movie database API (tmdb)

## Features
Here are the features in summary:
* App displays popular movies, upcoming movies and latest movies
* User can search and review any movie.

## Requirements
* This program requires python3.+ (and pip) installed, a guide on how to install python on various platforms can be found [here](https://www.python.org/)
    * Once python is installed, install the folowing external libraries provided in the requirements.txt file using pip
    * Example: 
        * **`pip install flask`**
* PostgresSQL was also used in this project as the database client, however fell free to use whichever cliet you prefer.
    * To download postgres, follow this [link](https://www.postgresql.org/download/)

## Installation and Set-up
To view the app, open the live site link provided below on the README.
Here is a run through of how to set up the application:
* **Step 1** : Clone this repository using **`git clone https://github.com/collinsmuriuki/flask-movie-app.git`**, or downloading a ZIP file of the code.
* **Step 2** : The repository, if downloaded as a .zip file will need to be extracted to your preferred location and opened
* **Step 3** : Go to the project root directory and install the virtualenv library using pip an afterwards create a virtual environment. Run the following commands respectively:
    * **`pip install virtualenv`**
    * **`virtualenv virtual`**
    * **`source virtual/bin/activate`**
        * Note that you can exit the virtual environment by running the command **`deactivate`**
* **Step 4** : Download the all dependencies in the requirements.txt using **`pip install -r requirements.txt`**
* **Step 5** : Go to the [the movie database (TMDB) API](https://www.themoviedb.org/) WEBSITE, sign up for a free account and generate an API key. 
    * Create a .sh (shell)file in your root directory called **start.sh** and store the API key like so **`export API_KEY="<your-key>"`**
    * On the same file write down the command **`python3 manage.py server`** 
* **Step 6** : If you are using postgresql, run the server on a separate terminal tab/window using **postgres**
    * Then on another terminal tab/window, run the command **psql** to enter the postgresql shell
    * Create a database called **'watchlist'** by typing the command  **`CREATE DATABASE watchlist;`**
    * Set a password for your database by running this command **`ALTER USER <username> WITH PASSWORD "<new_password>";`**
    * Now go back to the project directory, in the **config.py** file, set your **SQLALCHEMY_DATABASE_URI** in the Config class following the following format:
    **`SQLALCHEMY_DATABASE_URI="postgresql+psycopg2://<username>:<password>@localhost/watchlist"`**
    * Side note: you will notice that on the TestConfig class, the database uri is linked to a test database, you can create one for testing purposes, otherwise, ignore.
* **Step 7** : On your terminal, run the following command, **`chmod +x start.sh`** to make the shell file from **step 5** executable
    * You can now launch the application locally by running the command **`./start.sh`** 
    * Open your preferred browser and view the app by opening the link **http://127.0.0.1:5000/**.

## IMPORTANT
* **NOTE**: For deployment purposes, on the **manage.py** file, be sure to change from **"development"** config options to **"production"** like so: **`app = create_app("production")`**
* **NOTE**: If you cloned this project before 17/11/2019, the default config options in the **manage.py** file were set to **"production"**, be sure to switch to **"development"** like so: **`app = create_app("development")`**

## Known Bugs
* **Styling bug**: There seems to be an inconsistent arrangement of movie thumbnails on landing page as well as search results page.

## Technologies Used
* Python 3.7.4
* Flask 1.1.1
* HTML  
* CSS
* Bootstrap 3.3.7

## Support and contact details
You can provide feedback or raise any issues/ bugs through the following means:
* murerwacollins@gmail.com

## Live Site link
You can view the live application by following this [link](https://movie-app95.herokuapp.com/).

## License
#### [*GNU License*](LICENSE)

