#from _typeshed import HasFileno
from os import readlink
import flask
import pandas as pd
import numpy as np
from joblib import dump, load
import csv


with open(f'modelpredictorengine.joblib', 'rb') as f:
    model = load(f)



app = flask.Flask(__name__, template_folder='templates')



@app.route('/', methods=['GET', 'POST'])
def main():
    if flask.request.method == 'GET':
        return (flask.render_template('main.html'))

    if flask.request.method == 'POST':
        hospitalcounty = flask.request.form['hospitalcounty']
        agegroup = flask.request.form['agegroup']
        gender = flask.request.form['gender']
        lengthofstay = flask.request.form['lengthofstay']
        admissiontype = flask.request.form['admissiontype']
        paymentmethod = flask.request.form['paymentmethod']
        totalcosts = flask.request.form['totalcosts']

            
        if hospitalcounty == "Allegany":
            hospitalcounty = 2
        elif hospitalcounty == "Cattaraugus":
            hospitalcounty = 5
        elif hospitalcounty == "Chautauqua":
            hospitalcounty = 7
        elif hospitalcounty == "Erie":
            hospitalcounty = 15
        else:
            hospitalcounty = 27

        if agegroup == "70 or Older":
            agegroup = 5
        elif agegroup == "50 to 69":
            agegroup = 4
        elif agegroup == "30 to 49":
            agegroup = 3
        elif agegroup == "18 to 29":
            agegroup = 2
        else:
            agegroup = 1
        
        if gender == "F":
            gender = 1
        elif gender == "M":
            gender = 2
        else:
            gender = 3
        
        if admissiontype == "Urgent":
            admissiontype = 6
        elif admissiontype == "Elective":
            admissiontype = 1
        elif admissiontype == "Emergency":
            admissiontype = 2
        elif admissiontype == "Newborn":
            admissiontype = 3
        elif admissiontype == "Trauma":
            admissiontype = 5
        else:
            admissiontype = 4
        
        if paymentmethod == "Medicare":
            paymentmethod = 6
        elif paymentmethod == "Medicaid":
            paymentmethod = 5
        elif paymentmethod == "Private Health Insurance":
            paymentmethod = 8
        elif paymentmethod == "Blue Cross/Blue Shield":
            paymentmethod = 1
        elif paymentmethod == "Self-Pay":
            paymentmethod = 9
        else:
            paymentmethod = 7

        input_variables = pd.DataFrame([[hospitalcounty, agegroup, gender, lengthofstay, admissiontype, paymentmethod, totalcosts]],
                                       columns=['hospitalcounty', 'agegroup', 'gender', 'lengthofstay', 'admissiontype',
                                                'paymentmethod', 'totalcosts'],
                                       dtype='float',
                                       index=['input'])

        predictions = np.round(model.predict(input_variables)[0])
        print(predictions)

        return flask.render_template('main.html', original_input={'hospitalcounty': hospitalcounty, 'agegroup': agegroup, 
                                                                  'gender': gender, 'lengthofstay': lengthofstay, 'admissiontype': admissiontype, 
                                                                  'paymentmethod': paymentmethod, 'totalcosts': totalcosts},
                                     result=predictions)


if __name__ == '__main__':
    app.run(debug=True)
