import boto3
import json
from flask import Flask
app = Flask(__name__)

comprehend = boto3.client(service_name='comprehend', region_name='ap-south-1',aws_access_key_id = "AKIAZBPWXPNP3X2DRRBJ", aws_secret_access_key = "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")


@app.route('/')
def home():
	return render_template('main.html')

@app.route('/predict',methods=['POST'])
    text = "President Ram Nath Kovind, who is currently on Uttar Pradesh visit, will arrive in Lucknow by the presidential train on Monday (June 28, 2021) morning. The President will arrive in the state capital for a two-day visit and will return to Delhi on a plane from Lucknow airport the next day.President Kovind is scheduled to board the presidential train from Kanpur railway station at 10 am on Monday. After an estimated 90-minutes journey, President Kovind will reach Lucknow’s Charbagh railway station, the President will head straight to Raj Bhavan where he will stay overnight."

    print('Calling DetectSentiment')
    print(json.dumps(comprehend.detect_sentiment(Text=text, LanguageCode='en'), sort_keys=True, indent=4))
    print('End of DetectSentiment\n')

    print('Calling DetectEntities')
    print(json.dumps(comprehend.detect_entities(Text=text, LanguageCode='en'), sort_keys=True, indent=4))
    print('End of DetectEntities\n')