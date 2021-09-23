from flask import Flask, request, render_template
import requests
import sklearn
import pickle
import pandas as pd
from  sklearn.preprocessing import StandardScaler

app = Flask(__name__)
model = pickle.load(open("flight_dt_new.pickle", "rb"))

@app.route('/',methods=['GET'])
def Home():
    return render_template('index.html')

standard_to = StandardScaler()
@app.route('/predict',methods=['POST'])
def predict():
    if request.method == 'POST':
        stops = int(request.form["stops"])
        Destination = request.form["Destination"]
        if(Destination=="Cochin"):
            Cochin = 1
            Delhi = 0
            Hyderabad = 0
            Kolkata = 0
            New_Delhi = 0 
        elif(Destination=="Delhi"):
            Cochin = 0
            Delhi = 1
            Hyderabad = 0
            Kolkata = 0
            New_Delhi = 0 
        elif(Destination=="Hyderabad"):
            Cochin = 0
            Delhi = 0
            Hyderabad = 1
            Kolkata = 0
            New_Delhi = 0  
        elif(Destination=="Kolkata"):
            Cochin = 0
            Delhi = 0
            Hyderabad = 0
            Kolkata = 1
            New_Delhi = 0 
        elif(Destination=="New_Delhi"):
            Cochin = 0
            Delhi = 0
            Hyderabad = 0
            Kolkata = 0
            New_Delhi = 1
        else:
            Cochin = 0
            Delhi = 0
            Hyderabad = 0
            Kolkata = 0
            New_Delhi = 0 
        #Source Station
        Source = request.form["Source"]
        if(Source=="Chennai"):
            Chennai = 1
            Delhi = 0
            Kolkata = 0 
            Mumbai = 0
        elif(Source=="Delhi"):
            Chennai = 0
            Delhi = 1
            Kolkata = 0 
            Mumbai = 0
        elif(Source=="Kolkata"):
            Chennai = 0
            Delhi = 0
            Kolkata = 1
            Mumbai = 0
        elif(Source=="Mumbai"):
            Chennai = 0
            Delhi = 0
            Kolkata = 0 
            Mumbai = 1
        else:
            Chennai = 0
            Delhi = 0
            Kolkata = 0 
            Mumbai = 0
        #AirLine
        airline = request.form["airline"]
        if(airline=="Air_India"):
            Air_India = 1
            GoAir = 0
            IndiGo = 0
            Jet_Airways = 0
            Jet_Airways_Business = 0
            Multiple_carriers = 0
            Multiple_carriers_Premium_economy = 0
            SpiceJet = 0
            Trujet = 0
            Vistara = 0
            Vistara_Premium_economy = 0
        elif(airline=="GoAir"):
            Air_India = 0
            GoAir = 1
            IndiGo = 0
            Jet_Airways = 0
            Jet_Airways_Business = 0
            Multiple_carriers = 0
            Multiple_carriers_Premium_economy = 0
            SpiceJet = 0
            Trujet = 0
            Vistara = 0
            Vistara_Premium_economy = 0
        elif(airline=="IndiGo"):
            Air_India = 0
            GoAir = 0
            IndiGo = 1
            Jet_Airways = 0
            Jet_Airways_Business = 0
            Multiple_carriers = 0
            Multiple_carriers_Premium_economy = 0
            SpiceJet = 0
            Trujet = 0
            Vistara = 0
            Vistara_Premium_economy = 0
        elif(airline=="Jet_Airways"):
            Air_India = 0
            GoAir = 0
            IndiGo = 0
            Jet_Airways = 1
            Jet_Airways_Business = 0
            Multiple_carriers = 0
            Multiple_carriers_Premium_economy = 0
            SpiceJet = 0
            Trujet = 0
            Vistara = 0
            Vistara_Premium_economy = 0
        elif(airline=="Jet_Airways_Business"):
            Air_India = 0
            GoAir = 0
            IndiGo = 0
            Jet_Airways = 0
            Jet_Airways_Business = 1
            Multiple_carriers = 0
            Multiple_carriers_Premium_economy = 0
            SpiceJet = 0
            Trujet = 0
            Vistara = 0
            Vistara_Premium_economy = 0
        elif(airline=="Multiple_carriers"):
            Air_India = 0
            GoAir = 0
            IndiGo = 0
            Jet_Airways = 0
            Jet_Airways_Business = 0
            Multiple_carriers = 1
            Multiple_carriers_Premium_economy = 0
            SpiceJet = 0
            Trujet = 0
            Vistara = 0
            Vistara_Premium_economy = 0
        elif(airline=="Multiple_carriers_Premium_economy"):
            Air_India = 0
            GoAir = 0
            IndiGo = 0
            Jet_Airways = 0
            Jet_Airways_Business = 0
            Multiple_carriers = 0
            Multiple_carriers_Premium_economy = 1
            SpiceJet = 0
            Trujet = 0
            Vistara = 0
            Vistara_Premium_economy = 0
        elif(airline=="SpiceJet"):
            Air_India = 0
            GoAir = 0
            IndiGo = 0
            Jet_Airways = 0
            Jet_Airways_Business = 0
            Multiple_carriers = 0
            Multiple_carriers_Premium_economy = 0
            SpiceJet = 1
            Trujet = 0
            Vistara = 0
            Vistara_Premium_economy = 0
        elif(airline=="Trujet"):
            Air_India = 0
            GoAir = 0
            IndiGo = 0
            Jet_Airways = 0
            Jet_Airways_Business = 0
            Multiple_carriers = 0
            Multiple_carriers_Premium_economy = 0
            SpiceJet = 0
            Trujet = 1
            Vistara = 0
            Vistara_Premium_economy = 0
        elif(airline=="Vistara"):
            Air_India = 0
            GoAir = 0
            IndiGo = 0
            Jet_Airways = 0
            Jet_Airways_Business = 0
            Multiple_carriers = 0
            Multiple_carriers_Premium_economy = 0
            SpiceJet = 0
            Trujet = 0
            Vistara = 1
            Vistara_Premium_economy = 0
        elif(airline=="Vistara_Premium_economy"):
            Air_India = 0
            GoAir = 0
            IndiGo = 0
            Jet_Airways = 0
            Jet_Airways_Business = 0
            Multiple_carriers = 0
            Multiple_carriers_Premium_economy = 0
            SpiceJet = 0
            Trujet = 0
            Vistara = 0
            Vistara_Premium_economy = 1
        else:
            Air_India = 0
            GoAir = 0
            IndiGo = 0
            Jet_Airways = 0
            Jet_Airways_Business = 0
            Multiple_carriers = 0
            Multiple_carriers_Premium_economy = 0
            SpiceJet = 0
            Trujet = 0
            Vistara = 0
            Vistara_Premium_economy = 0
        #Departure Date & Time
        Deep_Time = request.form["Deep_Time"]
        Journey_day = int(pd.to_datetime(Deep_Time, format="%Y-%m-%dT%H:%M").day)
        Journey_month = int(pd.to_datetime(Deep_Time, format="%Y-%m-%dT%H:%M").month)

        # Departure Time
        Dep_hour = int(pd.to_datetime(Deep_Time, format ="%Y-%m-%dT%H:%M").hour)
        Dep_min = int(pd.to_datetime(Deep_Time, format ="%Y-%m-%dT%H:%M").minute)

        # Arrival Time
        Arrival_Time = request.form["Arrival_Time"]
        Arrival_hour = int(pd.to_datetime(Arrival_Time, format ="%Y-%m-%dT%H:%M").hour)
        Arrival_min = int(pd.to_datetime(Arrival_Time, format ="%Y-%m-%dT%H:%M").minute)

        prediction = model.predict([[stops,Cochin,Delhi,Hyderabad,Kolkata,New_Delhi, Chennai,Delhi,Kolkata,Mumbai,
         Air_India,GoAir,IndiGo,Jet_Airways,Jet_Airways_Business,Multiple_carriers,Multiple_carriers_Premium_economy,SpiceJet,
         Trujet,Vistara,Vistara_Premium_economy,
         Journey_day,Journey_month,Dep_hour,Dep_min,Arrival_hour,Arrival_min]])

        output = round(prediction[0],2)
        if(output<0):
            return render_template('index.html',prediction_text="Sorry We can not Predict Flight Fare")
        else:
            return render_template('index.html',prediction_text="Your Flight price is Rs. {}".format(output))

    else:
        return render_template('index.html')

if __name__=="__main__":
    app.run(debug=True)








            

        
        
        




    

