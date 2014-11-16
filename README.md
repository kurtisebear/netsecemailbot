Gets hot posts from /r/netsec and emails the links and titles to a specified email address

Uses a csv to keep track of what links have been sent before to avoid duplicates,so you need a file called list.csv

requires praw reddit libary installed

    sudo pip install praw

update settings.py with your gmail details and the email address where you want to receive updates. You can also change the subreddit here.

add cron job to run every few hours or when ever you want it to check.



