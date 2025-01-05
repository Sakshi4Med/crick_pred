# T20 Cricket Score Predictor

## **Overview**
This project aims to predict the final score of a T20 cricket innings based on live match conditions using machine learning models. 
By leveraging the Ball-by-Ball IT20 dataset, the application provides an estimated target score, considering factors like current score, overs completed, wickets lost, and runs in last five overs.

## **Dataset**
The project uses the **[Ball-by-Ball IT20 dataset](https://www.kaggle.com/datasets/jamiewelsh2/ball-by-ball-it20)** from Kaggle.

## **Live Project**
Access the deployed application here:  
[T20 Cricket Score Predictor](https://t20-score-prediction-mc92.onrender.com)

## Key Features of the Dataset:
- **Detailed Match Information**: Covers runs, dismissals, and more.
- **Comprehensive Coverage**: Includes players and teams.

## **Features**
- **Live Input**: Dynamic predictions based on user-provided inputs.
  Predict scores based on user inputs like batting team, bowling team, stadium, current score, overs completed, wickets lost, and runs scored in the last 5 overs.
- **Real-Time Score Prediction**: Machine learning model predicts the final score dynamically.
- **User-Friendly Interface**: A sleek web UI for easy use.

## **Techstack**
1. Programming Language - Python
2. Web Framework - Flask, Gunicorn (used as a WSGI HTTP server for deploying Flask applications)
3. Libraries - Numpy, Pandas, Sci-kit Learn
4. Version Control - Git, GitHub, VSCode

## Installation
1. **Clone the repository:**
   ```bash
   git clone https://github.com/Shreyas19-ai/cricket_pred.git
2. **Create a virtual environment (optional but recommended):**
   ```bash
   python -m venv myenv  
   myenv/Scripts/activate 
3. **Install required dependencies:**
   ```bash
   pip install -r requirements.txt
4. **Run the application:**
   ```bash
   python app.py

## Contributing
Contributions are welcome!
1. Fork this repository.
2. Create a new branch: git checkout -b feature-branch-name.
3. Commit your changes: git commit -m 'Add some feature'.
4. Push to the branch: git push origin feature-branch-name.
4. Submit a pull request.
