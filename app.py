# Importing essential libraries
from email import message
from flask import Flask, render_template, request
import pickle
import boto3

comprehend = boto3.client(service_name='comprehend', region_name='ap-south-1',aws_access_key_id = "AKIAZBPWXPNP3X2DRRBJ", aws_secret_access_key = "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")

app = Flask(__name__)

@app.route('/')
def home():
	return render_template('main.html')

@app.route('/predict',methods=['POST'])
def predict():
    if request.method == 'POST':
    	message = request.form['message']
		data = [message] 
		data = obj.get()['Body'].read().decode("utf-8")
    	text_redact = comprehend.detect_sentiment	(Text=data , LanguageCode='en')
		my_prediction = json.dumps(text_redact)
    return render_template('result.html', prediction=my_prediction)
   

if __name__ == '__main__':
	app.run(debug=True)