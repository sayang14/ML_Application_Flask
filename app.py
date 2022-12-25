from flask import Flask, render_template,request
from flask_s3 import FlaskS3
from keras.models import load_model, save_model
import numpy as np
import boto3
from flask import url_for as flask_url_for
from flask import current_app

app = Flask(__name__)

model = load_model('model.h5')

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/predict',methods =[ 'POST' ])
def predict():
    initial_features = [float(x) for x in request.form.values()]
    final_features = [initial_features]
    prediction = model.predict(final_features)

    output = np.round(prediction[0], 2)

    return render_template('index.html', prediction_text='The predicted age is :{}'.format(output))



if __name__ == "__main__":
    app.run(debug=True)