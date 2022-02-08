from flask import Flask,render_template,url_for,request
import boto3

@app.route('/')
def home():
	return render_template('home.html')

@app.route('/predict',methods=['POST'])
def predict():
	if request.method == 'POST':
		message = request.form['message']
		data = [message] 
		data = obj.get()['Body'].read().decode("utf-8")
    	text_redact = comprehend.detect_sentiment(Text=data , LanguageCode='en')
		my_prediction = json.dumps(text_redact)
	return render_template('result.html',prediction = my_prediction)

if __name__ == '__main__':
	app.run(debug=True)