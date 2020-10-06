# scrapers

import praw 
import twitter
import youtube_scraper
import facebook

import os 

def scrape_reddit(TOPIC, LIMIT): 
    api = praw.Reddit(
                    client_id='cjLkZqLNMESs7A', \
                     client_secret='tOyC_e7VmVxNW5JuZ517YgvxQYY', \
                     user_agent='quora_query_bot test', \
            )
    return [submission.title for submission in api.subreddit(TOPIC).hot(limit=LIMIT)]


def scrape_twitter(TOPIC, LIMIT):
    api = twitter.Api(consumer_key='Qe793APvI0r26teLOJq4XqWYb',
                  consumer_secret='rGKxc7KhfFzB8bUdU2f7D7GHrtrXZocX7qJBFoAmopetDldBrs',
                  access_token_key='1108423746040168448-VvQ6gQr6Y96rICUFXedQGtrlaKSDqb',
                  access_token_secret='pzv4k9rKvWS8JGPjTUXtiC8cBz797eQdsIeXJxUxL9uzt',
                  tweet_mode='extended'
            )
    return [tweet['full_text'] for tweet in api.GetSearch( term=TOPIC, count=LIMIT, 
                                                            return_json=True)['statuses']]


def scrape_youtube(TOPIC, LIMIT):
    LIMIT = int(LIMIT/240) + 1 # convert number of comments to number of videos
    os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'
    service = youtube_scraper.get_authenticated_service()
    results = youtube_scraper.search_videos_by_keyword(service, LIMIT, q=TOPIC, 
                                    part='id,snippet', eventType='completed', type='video')
    return [comment[2] for comment in results]



def scrape_facebook(TOPIC, LIMIT):
    # TODO: make functional
    token = 'EAAEg1rUPEXYBAJOKSnrIlqLFhL9dCeiNikIT0e7k9ZATsXHyBMOkQCmH1FYeaP7LqDZBr1LIUOegFCJcZAmYw8Qfs4L3jOBTzpmRrGEhRMCbd2B7j58NuBIvZAZCJJOcwF9RjX2vTKxHZCPFQyzksPyhgt8LY4FI98iZAFfhSAikOC8ZAnZB87DjHoyZCIUVRnzaHXp5JBfAcPRAZDZD'
    graph = facebook.GraphAPI(token, version="3.0")
    query = "aquafresh"
    post = requests.get("https://graph.facebook.com/search?access_token=" + token +  "&q=" + query + "&type=page")
  
    pass
    




