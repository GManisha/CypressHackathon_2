README
-------
A simple python bot, which interfaces with Twitter to handle user tweets.

The pre-requisites are: 

1. Python 2.7 and above. 

2. Python Modules: Tweepy API, time, keys and sys. 

3. Setting up twitter application to generate the application keys (visit http://dev.twitter.com)

This program connects with Twitter and replies to the user, when the below lines are tweeted.
1.	Steps to create a memo.

2.	Steps to submit an ECN.

3.	Support team/person for an application.

4.	Provide Cypress.com forums RSS feeds.

Below is the cmd to run this program:

$python cy_bot.py argv1 argv2 argv3 argv4

Files:

Cy_bot.py is the main python file which has the logic to connect to a twitter handle, read a particular tweet, compare it with the string pattern and then post the reply.

Keys.py: To import the keys dictionary to access the twitter application.

argv1 to argv4 are text files taken though cmd line as input files, which contain the responses that will get posted on to twitter based on the tweet.

Ex: argv1: memo.txt

1.	Below are the steps to submit a Memo:

2.	Login into doc.cypress.com

3.	Enter you LDAP Credentials

4.	.......................... etc .....

Example output is uploaded to the repository.

