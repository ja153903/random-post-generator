import json
import requests 
import pandas

# /r/AskReddit 

r = requests.get(r'http://www.reddit.com/r/funny/top/.json?count=1', headers = {'User-agent': 'your bot 0.1'})

# r = requests.get(r'http://www.reddit.com/r/funny/top/.json?count=1');






data = r.json();




# data_ = data.keys()[1];
# InsideDictionary = data[data_]; 
# children = InsideDictionary.keys()[4];
# insideArr = InsideDictionary[children][20];
# title = insideArr['data']['title'];



# print(insideArr['data']['title']);


titles = []; 


for i in range(1,5):
	# print(data['data']['children'][i]['data']['title']);
	titles.append(data['data']['children'][i]['data']['title']);



print(len(titles));



# for key in r.text.items():
# 	print(key);



# for child in data['data']['children']:
# 	print(child['data']['id'], " ", child['data']['author'], child['data']['body']); 