from flask import Flask
from .config import DevConfig

# Initializing application
app = Flask(__name__, instance_relative_config = True) #We pass in instance_relative_config which allow us to connect to the instance/folder when the app instance is created.
# Setting up configuration
app.config.from_object(DevConfig)     #We then use app.config.from_object() method to set up configuration and pass in the DevConfig subclass.
app.config.from_pyfile('config.py')   #The app.config.from_pyfile('config.py') connects to the config.py file and all its contents are appended to the app.config.
from flask_bootstrap import Bootstrap
# Initializing Flask Extensions
bootstrap = Bootstrap(app)
from app import views
from app import error



#CONFIGURATIONS
#Applications need some kind of configuration. 
#There are different settings you might want to change depending on the application environment like toggling the debug mode, setting the secret key, and other such environment-specific things.

#CONFIGURING FROM FILES
#Configuration becomes more useful if you can store it in a separate file, ideally located outside the actual application package. 
#This makes packaging and distributing your application possible via various package handling tools (Deploying with Setuptools) and finally modifying the configuration file afterwards.