import tweepy
import time

ACCESS_TOKEN = '2749948033-4TJ4aloMiRex2HnCf14FexdZxbRUu2BS9cDJpZ6'
ACCESS_SECRET = 'fk4Uxwd3LQRktrLEmYaPMsVJS6rpZBJRPH7taffRXCYC9'
CONSUMER_KEY = 'Vs8tY1cxCc5ZLcSZ8pie1LV9Q'
CONSUMER_SECRET = 'Z6iFi9xu71cV1uNkuNhtVzgk0VSyd2CevajwKk0lPOqmeWmc2d'

SEARCH = 'Election' # SEARCH = input("Enter the search string (in double quotes): ")
# FROM = input("Enter the from date (YYYY-MM-DD format): ")
# TO = input("Enter the to date (YYYY-MM-DD format): ")
INPUT_FILE_PATH = './captures/' + SEARCH + '.txt'

num = 100 # num = int(input("Enter the number of tweets you want to retrieve: "))
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
api = tweepy.API(auth)
i = 0;

f = open(INPUT_FILE_PATH, 'w')

for res in tweepy.Cursor(api.search, q=SEARCH, rpp=100, since='2018-02-16', until='2018-02-17', 
                            include_entities=True, lang="en").items(num):
	i+=1
	f.write(res.user.screen_name)
	f.write(' ')
	f.write('[')
	f.write(res.created_at.strftime("%d/%b/%Y:%H:%M:%S %Z"))
	f.write(']')	
	f.write(" ")
	f.write('"')
	f.write(res.text.replace('\n', '').encode("UTF-8"))
	f.write('"')
	f.write(" ")
	f.write(str(res.user.followers_count))
	f.write(" ")
	f.write(str(res.retweet_count))
	f.write('\n')
f.close
print("Tweets retrieved ", i)
