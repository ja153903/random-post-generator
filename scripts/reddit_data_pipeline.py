import csv
import markovify
import os
import praw

class SubredditPipeline:

    def __init__(self):
        self.__reddit = praw.Reddit(
                        client_id='Fg7Mp55-RljBGw',
                        client_secret='zrtsEBfCU2kt5m-e8pRtdhaawgQ',
                        user_agent="Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36")
        self.__subreddit_closure = self.__reddit.subreddit
        self.result_string = [] # this will hold the raw string data
    
    def __iter_subreddit(self, subreddit):
        # returns an iterator
        return self.__subreddit_closure(subreddit)
    
    def __get_filepath(self, subreddit):
        return "./../data/{}.csv".format(subreddit)
    
    def __write(self, subreddit):
        # given a subreddit try to get as many lines as possible
        filepath = self.__get_filepath(subreddit)
        try:
            with open(filepath, 'a') as f:
                file = csv.writer(f, delimiter=' ')
                for post in self.__iter_subreddit(subreddit).top(time_filter='all'):
                    file.writerow(post.title.split(' '))
        except ValueError:
            print("Write failed")
    
    def __read(self, subreddit):
        filepath = self.__get_filepath(subreddit)
        try:
            if not os.path.exists(filepath):
                raise ValueError("No such path. Pipeline broken...")
            else:
                with open(filepath, 'r') as f:
                    file = csv.reader(f, delimiter=' ')
                    for row in file:
                        for word in row:
                            self.result_string.append(word)
        except ValueError:
            print("File does not exist")
    
    def _markov_model(self):
        sentence = " ".join(self.result_string)
        return markovify.Text(sentence)
    
    # Function returns a markov model where we can 
    # apply various function to generate sentences
    def apply_(self, subreddit):
        try:
            if not os.path.exists(self.__get_filepath(subreddit)):
                self.__write(subreddit)
            self.__read(subreddit)
            return self._markov_model()
        except ValueError:
            print("Pipeline Failed")