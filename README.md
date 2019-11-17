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
* **Step 6** : On your terminal, run the following command, **`chmod +x start.sh`** to make the shell file executable
    * You can now launch the application locally by running the command **`./start.sh`** 
    * Open your preferred browser and view the app by opening the link **http://127.0.0.1:5000/**.

## Known Bugs
* Inconsistent arragngement of movie thumbnails (styling bug)

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

