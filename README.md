# Abstract
This tutorial details step by step how to make a flask API based prediction model based on 
Linear regression that predicts the total charges of an inpatient discharge based on historical data and factors that influence this cost. 
This project is designed by keeping end user in mind and provides an intuitive and simple user interface.

# Dataset
We have obtained this data from Statewide Planning and Research Cooperative System (SPARCS). SPARCS is a comprehensive all payer data reporting system established in 1979 as a result of cooperation between the healthcare industry and government of United States of America.
The dataset contains de-identified data for inpatient discharges from hospitals based in the state of New York. The dataset contains discharge level details on patient characteristics, diagnoses, treatments, services, and charges for each hospital inpatient stay and outpatient (ambulatory surgery, emergency department, and outpatient services) visit. This dataset contains 34 columns and 1 million rows detailing every aspect of patient discharge.
Link to dataset: https://health.data.ny.gov/Health/Hospital-Inpatient-Discharges-SPARCS-De-Identified/82xm-y6g8

# To run this code

To run this application you need to have Flask installed in your system. Flask is a web development framework for Python that can be installed as a Python module. It has many cool features like URL routing and a template engine. You can install Flask by following this tutorial.
Steps to run this application:
Assuming you have ran the model creation code and a model.joblib file is created. The next step is to run the app.py file. My preferred way to execute this is to use an IDE such as VS Code. Using such IDE is helpful as most of them have built in terminal integration, a debugger and an output window along with syntax highlighting.

This application has seven Input fields that has the various parameters mentioned in their respective drop down menu. After selecting the parameters click submit to view the predicted price. You can also see the raw input that goes to the prediction engine.

Follow this tutorial for more details: https://medium.com/@himancodes/hospital-charges-prediction-application-using-flask-21d7eb687da9

About me: https://himanshu-ops.github.io/index.html

Kindly reach out to me on this email: hbcan9@gmail.com for any concerns and clarifications.
