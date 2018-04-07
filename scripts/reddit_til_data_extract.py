import praw

class SubredditBot:
    def __init__(self):
        self.__reddit = praw.Reddit(
                        client_id='Fg7Mp55-RljBGw',
                        client_secret='zrtsEBfCU2kt5m-e8pRtdhaawgQ',
                        user_agent="Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36")
        self.__subreddit_closure = self.__reddit.subreddit
        
  
    def _iter_subreddit(self, subreddit):
        # returns an iterator
        return self.__subreddit_closure(subreddit)

if __name__ == '__main__':
    subreddit = SubredditBot()
    for post in subreddit._iter_subreddit('todayilearned').hot(limit=10):
        print(post.title)
