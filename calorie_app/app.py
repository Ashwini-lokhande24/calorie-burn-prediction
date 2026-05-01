from flask import Flask, render_template, request
import pickle
import numpy as np
app= Flask(__name__)
model=pickle.load(open('model.pkl','rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    gender = request.form['gender']
    age = float(request.form['age'])
    height = float(request.form['height'])
    weight = float(request.form['weight'])
    duration = float(request.form['duration'])
    heart_rate = float(request.form['heart_rate'])
    body_temp = float(request.form['body_temp'])

    gender_encoded = 1 if gender =='male' else 0
    bmi=weight/((height/100)**2)
    exercise_intensity=duration*heart_rate

    features = np.array([[gender_encoded, age, height, weight,
                          duration, heart_rate, body_temp,
                          bmi, exercise_intensity]])

    prediction=model.predict(features)[0]
    prediction=round(prediction,1)

    return render_template('index.html', prediction=prediction)

if __name__ =='__main__':
    app.run(debug=True)
