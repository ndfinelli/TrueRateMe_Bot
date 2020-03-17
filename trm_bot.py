#TrueRateMeBot

import praw
 

reddit = praw.Reddit(client_id='1RgyVYuf1MTWoA',
                     client_secret='l7aBbAsBVxzhV4P_uB7e4L16tlE',
                     username='TrueRateMe_Bot',
                     password='TRMBot6969',
                     user_agent='ratingbot by /u/TrueRateMe_Bot')

subreddit = reddit.subreddit('truerateme')

keyphrase = '!TrueRateMe_Bot'

for comment in subreddit.stream.comments():
    if keyphrase in comment.body:
        try:
            comment.reply('Thanks for calling TrueRateMe_Bot')
            print('Posted')
        except:
            print('Too soon')
                     
