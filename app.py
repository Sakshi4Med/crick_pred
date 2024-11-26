from flask import Flask, render_template, request
import pickle
import pandas as pd
import numpy as np
import xgboost
print(xgboost.__version__)

app = Flask(__name__)

pipe = pickle.load(open('pipe.pkl', 'rb'))

teams = ['Pakistan', 'India', 'New Zealand', 'South Africa', 'Sri Lanka', 'West Indies',
         'England', 'Australia', 'Bangladesh', 'Afghanistan', 'Zimbabwe', 'Ireland', 
         'Netherlands', 'Scotland']

stadiums = ['Shere Bangla National Stadium', 'Dubai International Cricket Stadium', 'Sharjah Cricket Stadium',
            'Harare Sports Club', 'R Premadasa Stadium', 'Kensington Oval', 'Trent Bridge', 'Newlands',
            'Sydney Cricket Ground', 'Eden Park', 'National Stadium', 'Pallekele International Cricket Stadium',
            'Hagley Oval', 'New Wanderers Stadium', 'Providence Stadium', 'National Cricket Stadium',
            'Kennington Oval', 'Seddon Park', 'Bellerive Oval', 'The Village', 'Sheikh Zayed Stadium',
            'Zayed Cricket Stadium', 'Melbourne Cricket Ground', 'Civil Service Cricket Club', 'Kingsmead',
            'The Rose Bowl', "Lord's", 'Punjab Cricket Association IS Bindra Stadium', 'Gaddafi Stadium',
            'Saurashtra Cricket Association Stadium', 'Eden Gardens', 'Beausejour Stadium', 'SuperSport Park']

@app.route('/')
def index():
    return render_template('index.html', teams=teams, stadiums=stadiums)

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        batting_team = request.form['batting_team']
        bowling_team = request.form['bowling_team']
        stadium = request.form['stadium']
        current_score = int(request.form['current_score'])
        overs = float(request.form['overs'])
        wickets = int(request.form['wickets'])
        last_five = int(request.form['last_five'])

        # Calculate balls left and wickets left
        balls_left = 120 - (overs - 1) * 6
        wickets_left = 10 - wickets
        crr = current_score / overs

        input_df = pd.DataFrame({
            'batting_team': [batting_team],
            'bowling_team': [bowling_team],
            'Stadium': [stadium],
            'current_score': [current_score],
            'balls_left': [balls_left],
            'wickets_left': [wickets_left],
            'crr': [crr],
            'last_five': [last_five]
        })

        result = pipe.predict(input_df)
        predicted_target = int(result[0])

        return render_template('index.html', teams=teams, stadiums=stadiums, predicted_target=predicted_target)

if __name__ == "__main__":
    app.run(debug=True)
