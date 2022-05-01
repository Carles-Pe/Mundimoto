Mundimoto Webapp:

(NOTE): This version does not contain the virtual environment due to storage limitations, some packages require to be installed:
(FULL VERSION):  https://drive.google.com/file/d/1NTKZByU7_I-4Eon5EhjryMZ7HTzpeS4a/view?usp=sharing 

Hi, we present to you our 36 hour project where we decided to combine webapps with machine learning:

- The platform consists on an app (for now...) that allows to control the database

- The posgresql database backup file can by found by the name of mundimoto.sql

- This project was made in a virtual environment that can be activated via:
    (this-folder)# source ../bin/activate
    
- In order to start the webapp, the following command must be introduced:
    (this-folder/mundimoto)# python3 manage.py runserver
    
- Keep in mind that the postgres deamon must be active in order to work:
    # sudo service start postgresql
    # sudo -u postgres psql
    #> psql mundiauto < mundiauto.sql
    
    
Which by default will be connected to the port 5432 of the localhost
    
Regarding the models involved:

We decided to add a feature to the "add a version" section, where, by setting sell_price to "-1", a prediction is requested to the application, that will respond via an HttpRequest.
The prediction is performed using an XGBoost-Regressor that has been proven to be one among the most robust algorithms in machine learning. The lack of data may influece the accuracy of the fitting 


This project has been a very interesting opportuinty to learn more about AI machine learning and the processes involved in the developement of a webapp.
Due to the short ammount of time, some functionalities were left to implement, such as:
    - Apply a Deep-Learing model to see its effectiveness
    - Improving the accuracy of the predictor model
    - The use of external data, such as web-scrapping in order to obtain more data
    - Some photo recognition AI to match similar models of motorbikes
    
