import tweepy
import csv
import json


consumer_key = 'TaGkgXomNTj3KxJY9252Tg75e'
consumer_secret ='EFEOQklTvV9S40n7Usp6DUKYIFOJPIDKvR1g1FmvyiKPwE5eYU'
access_key = '2565365424-dqkHvoCoNBNyH9g75iVuzjaGrIHINbN4lVVi02Y'
access_secret = 'MFR9ZQbtnjfysxpzLQQOe5i1N07hk8bSEBBJDwfP2maJI'

# Create the api endpoint

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
api = tweepy.API(auth)

# Mention the maximum number of tweets that you want to be extracted.

maximum_number_of_tweets_to_be_extracted = \
    int(input('Enter the number of tweets that you want to extract- '))

# Mention the hashtag that you want to look out for

hashtag = input('Enter the hashtag you want to scrape- ')

for tweet in tweepy.Cursor(api.search, q='#' + hashtag, lang='en',
                           rpp=100).items(maximum_number_of_tweets_to_be_extracted):
    
    print(str(tweet.text.encode('utf-8'))+ tweet.user.location + '\n')