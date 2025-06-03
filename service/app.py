import numpy as np
from flask import Flask, request, render_template
import pickle
import os

app = Flask(__name__)

# Загрузка модели
model = pickle.load(open('service/pipeline.pkl', 'rb'))

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    try:
        float_features = [float(x) for x in request.form.values()]
        features = [np.array(float_features)]
        prediction = model.predict(features)
        return render_template("index.html", 
                            prediction_text=f"Предсказанная стоимость: {float(prediction[0]):.2f}")
    except Exception as e:
        return render_template("index.html", 
                            prediction_text=f"Ошибка: {str(e)}")

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)