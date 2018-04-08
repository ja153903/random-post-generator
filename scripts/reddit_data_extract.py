import praw
import csv
import os

class SubredditBot:
    def __init__(self):
        self.__reddit = praw.Reddit(
                        client_id='Fg7Mp55-RljBGw',
                        client_secret='zrtsEBfCU2kt5m-e8pRtdhaawgQ',
                        user_agent="Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36")
        
        self.__subreddit_closure = self.__reddit.subreddit
        
    def __iter_subreddit(self, subreddit):
        # returns an iterator
        return self.__subreddit_closure(subreddit)
    
    def to_csv(self, subreddit):
        # given a subreddit try to get as many lines as possible
        file_path = "./../data/{}.csv".format(subreddit)
        if os.path.exists(file_path):
            write_or_append = 'a'
        else:
            write_or_append = 'w'
        
        with open(file_path, write_or_append) as f:
            file = csv.writer(f, delimiter=' ')
            for post in self.__iter_subreddit(subreddit).top():
                file.writerow(post.title)
            for post in self.__iter_subreddit(subreddit).hot():
                file.writerow(post.title)
            f.close()

    


