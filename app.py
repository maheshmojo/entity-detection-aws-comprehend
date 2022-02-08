# Importing essential libraries
from flask import Flask, render_template, request
import pickle
import boto3

comprehend = boto3.client(service_name='comprehend', region_name='ap-south-1',aws_access_key_id = "AKIAZBPWXPNP3X2DRRBJ", aws_secret_access_key = "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")

# Load the Multinomial Naive Bayes model and CountVectorizer object from disk
filename = 'spam-sms-mnb-model.pkl'
classifier = pickle.load(open(filename, 'rb'))
cv = pickle.load(open('cv-transform.pkl','rb'))
app = Flask(__name__)

@app.route('/')
def home():
	return render_template('main.html')

@app.route('/predict',methods=['POST'])
def predict():
    if request.method == 'POST':
    	message = request.form[comprehend.detect_sentiment(Text=text, LanguageCode='en')]
    	data = [message]
    	vect = cv.transform(data).toarray()
    	my_prediction = classifier.predict(vect)
    return render_template('result.html', prediction=my_prediction)
   

if __name__ == '__main__':
	app.run(debug=True)