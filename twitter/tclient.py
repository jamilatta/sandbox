import math
import codecs
import json
from requests_oauthlib import OAuth1Session

MAX_TWEETS = 100
BASE_URL = "https://api.twitter.com/1.1/search/tweets.json"


class TClient(object):
    '''
    TClient is a Twitter Client interactive with twitter RESTFull API.
    '''

    API_KEY = ""
    API_SECRET = ""
    ACCESS_TOKEN = ""
    ACCESS_TOKEN_SECRET = ""

    def __init__(self):
        self.session = OAuth1Session(self.API_KEY,
                                     self.API_SECRET,
                                     self.ACCESS_TOKEN,
                                     self.ACCESS_TOKEN_SECRET)
        self.tweets = []

    def get_tweets(self, keywords, quantity=15):
        '''
        A method to get tweets by keyword.

        @param keyword: the keyword to search for.
        @param quantity: tweets returned, default 15 tweets.

        '''

        num_requests = int(math.ceil(float(quantity)/float(100)))
        quantity = MAX_TWEETS if quantity > MAX_TWEETS else quantity

        for keyword in keywords:

            #the id of the latest tweet.
            max_id = None

            print "Get tweets from term: %s" % keyword

            for n in range(num_requests):
                url = BASE_URL + "?q=%s&count=%d" % (keyword, quantity)

                if max_id is not None:
                    url = url + "&max_id=%d" % (max_id)

                response = self.session.get(url)

                if response.status_code == 200:
                    tweets = json.loads(response.content)

                    if not len(tweets['statuses']) > 0:
                        break

                    max_id = min([tweet['id'] for tweet in tweets['statuses']])-1

                    self.tweets += tweets['statuses']

        return self.tweets

    def save(self, filename):
        '''
        Save the tweets with format:

        ```id  date  @user  text```

        '''

        fp = codecs.open(filename, 'w', 'utf-8')

        for tweet in self.tweets:

            screated = tweet['created_at'].split()
            fcreated = '%s  %s %s' % (screated[1], screated[2], screated[3][0:5])

            fp.write('%s  %s  %s    %s\n' % (tweet['id'], fcreated,
                                             '#user_' + tweet['user']['screen_name'],
                                             tweet['text'].replace('\n', ' ')))

        fp.close()
