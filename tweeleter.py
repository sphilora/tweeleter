import twitter
from datetime import datetime, timedelta, timezone
import time
import settings

DATETIME_FORMAT = '%a %b %d %H:%M:%S %z %Y'  # e.g. : Tue Nov 20 17:08:43 +0000 2018

api = twitter.Api(consumer_key=settings.consumer_key,
                  consumer_secret=settings.consumer_secret,
                  access_token_key=settings.access_token_key,
                  access_token_secret=settings.access_token_secret)


# defaults to cutting off at 90 days ago
def get_cutoff(days_ago: int=90):
    return datetime.now(timezone.utc) - timedelta(days_ago)


def as_date_time(datetime_string: str):
    return datetime.strptime(datetime_string, DATETIME_FORMAT)


def status_created_before_cutoff(status):
    return as_date_time(status.created_at) < cutoffDate


def delete_statuses(statuses_to_delete):
    for status in statuses_to_delete:
        time.sleep(1)
        try:
            delete_status(status.id)
        except:
            print(f'Could not delete status with ID {status.id}')


def find_latest_tweet(timeline):
    return max(timeline, key=lambda x: x.id).id


def find_earliest_tweet(timeline):
    return min(timeline, key=lambda x: x.id).id


def delete_status(status_id):
    print(f'About to delete status with id: {status_id}')
    api.DestroyStatus(status_id)
    time.sleep(1)


def get_all_existing_statuses():
    timeline = api.GetUserTimeline(count=200)

    earliest_tweet_id = find_earliest_tweet(timeline)

    while True:
        tweets = api.GetUserTimeline(
            max_id=earliest_tweet_id, count=200
        )
        if tweets:
            new_earliest = find_earliest_tweet(tweets)

        if not tweets or new_earliest == earliest_tweet_id:
            break
        else:
            earliest_tweet_id = new_earliest
            timeline += tweets

    return timeline


#get all tweets
statuses = get_all_existing_statuses()

# get the earliest date at which tweets should be kept
cutoffDate = get_cutoff(settings.cutoff_date)

# create a collection of the tweets that are before the cutoff date
filtered_statuses = [status for status in statuses if (status_created_before_cutoff(status))]

# delete all the tweets before the cutoff date
delete_statuses(filtered_statuses)


