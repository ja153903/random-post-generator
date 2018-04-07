import requests
import json

subreddit = r'http://www.reddit.com/r/AMA/.json?count=1'

r = requests.get(subreddit, headers = {'User-agent': 'hacknyuf2018'})

data = r.json()

for i in range(1, 11):

    print(data['data']['children'][i]['data']['title'])


