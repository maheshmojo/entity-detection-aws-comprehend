import boto3
import json

comprehend = boto3.client(service_name='comprehend', region_name='ap-south-1',aws_access_key_id = "AKIAZBPWXPNP3X2DRRBJ", aws_secret_access_key = "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")
                
text = "It is raining today in Seattle"

print('Calling DetectSentiment')
print(json.dumps(comprehend.detect_sentiment(Text=text, LanguageCode='en'), sort_keys=True, indent=4))
print('End of DetectSentiment\n')