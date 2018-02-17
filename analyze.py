import errno
import time

KEYWORD = input("Enter the search string for analysis (in double quotes): ")
num = int(input("Enter the number of records to display: "))

try:
    capture = open('./captures/' + KEYWORD + '.txt', 'r')

except (OSError, IOError) as e:
    if getattr(e, 'errno', 0) == errno.ENOENT:
        print("File path does not exist.")

records = []

for l in capture.readlines():
    tweet = l[l.find('"'):l.rfind('"')+2]
    timestamp = l[l.find('['):l.find(']')+2]
    data = l.replace(tweet, '').replace(timestamp, '').split(' ')

    records.append({
        "user": data[0],
        "timestamp": timestamp,
        "tweet": tweet,
        "retweets": int(data[1]),
        "followers": int(data[2].replace('\n', ''))
    })

capture.close()

# function to format output lines
def formatLine(index, prefix, text):
    return str(index + 1) + '. (' + str(prefix) + ') ' + text + '\n'

# file for writing output
analysis = open('./analyses/' + KEYWORD + '.txt', 'w')

# top n users who have tweeted the most for the entire timeline
analysis.write('Users with the most tweets for the entire period:\n')

user_tweet_counts_all = []

for record in records:
    user = record["user"]

    if (any(x["user"] == user for x in user_tweet_counts_all)):
        index = user_tweet_counts_all.index(
            next(obj for obj in user_tweet_counts_all if obj["user"] == user))
        user_tweet_counts_all[index]["tweets"] += 1
    else:
        user_tweet_counts_all.append({ "user": user, "tweets": 1 })

user_tweet_counts_sorted = sorted(user_tweet_counts_all, key=lambda record: record["tweets"], reverse=True)

for index, record in enumerate(user_tweet_counts_sorted):
    if index < num:
        analysis.write(formatLine(index, record["tweets"], record["user"]))

# top n users who have tweeted the most for every hour
analysis.write('\nUsers with the most tweets for every hour:\n')

for index, record in enumerate(user_tweet_counts_sorted):
    if index < num:
        analysis.write(formatLine(index, record["tweets"], record["user"]))
        
# top n users who have the maximum followers
analysis.write('\nUsers with the most followers:\n')

max_followers = sorted(records, key=lambda record: record["followers"], reverse=True)

for index, record in enumerate(max_followers):
    if index < num:
        analysis.write(formatLine(index, record["followers"], record["user"]))

# top n tweets which have the maximum retweet count
max_retweets = sorted(records, key=lambda record: record["retweets"], reverse=True)

analysis.write('\nTweets with the highest retweet count:\n')

for index, record in enumerate(max_retweets):
    if index < num:
        analysis.write(formatLine(index, record["retweets"], record["tweet"]))

# print confirmation
print('Analysis complete!')
