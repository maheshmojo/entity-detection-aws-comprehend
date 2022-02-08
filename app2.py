import boto3

comprehend = boto3.client('comprehend', region_name = 'ap-south-1', aws_access_key_id = "AKIAZBPWXPNP3X2DRRBJ", aws_secret_access_key = "uCF6D2r0ZWRgWw+JxUdPbCXZ76lynr6UYwp7+y+1")

sample_tweet = "Microsoft founder Bill Gates international foundation has helped the Chinese Communist government in various ways, according to a newly-released batch of emails from the NIAID under Dr. Fauci Judicial Watch in Fox Business. READ"

entities = comprehend.detech_entities(Text=sample_tweet, LanguageCode = "en")

for i in range(0,(len(entities['Entites']))):
        print(entities['Entities'][i][Text]+ ' : ' + entities['Entities'][i]['Type'])