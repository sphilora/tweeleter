# tweeleter
A script to delete tweets before a given date


## Getting started
1. You'll need [https://github.com/bear/python-twitter] to interface with the twitter API. Install using PIP or however you like
2. You'll need to get a twitter developer account
3. rename the settings.py file to twitter_keys.py
4. In your twitter developer account, create an app, and grab the API key, API secret key,Access token, Access token secret values from the app details (you might need to generate them first)
5. Paste these values into the settings.py file
6. Ensure that the cutoff_date value represents the number of days in the past before which you want to delete all tweets. By default you'll keep anything posted in the past 365 days, and nuke anything from before
7. Run tweeleter.py to nuke your old tweets

