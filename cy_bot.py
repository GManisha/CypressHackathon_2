#!/usr/bin/env python
import tweepy
#from our keys module (keys.py), import the keys dictionary
from keys import keys
import time 
import sys
 
CONSUMER_KEY = keys['consumer_key']
CONSUMER_SECRET = keys['consumer_secret']
ACCESS_TOKEN = keys['access_token']
ACCESS_TOKEN_SECRET = keys['access_token_secret']
 
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)
 
# input files

argfile1 = str(sys.argv[1])
argfile2 = str(sys.argv[2])
argfile3 = str(sys.argv[3])
argfile4 = str(sys.argv[4])

twt1 = api.search(q="Steps to create a memo.")     
twt2 = api.search(q="Steps to submit an ECN.")
twt3 = api.search(q="Support team/person for an application.")
twt4 = api.search(q="Provide Cypress website forums RSS feeds.")

#list of specific strings we want to check for in Tweets for memo creation 
t1 = ['Steps to create a memo.',
    'Steps to create a memo!',
    'CY memo Creation!!!']

#list of specific strings we want to check for in Tweets for ECN submission 
t2 = ['Steps to submit an ECN.',
    'Steps to submit an ECN!',
    'CY ECN Submission!!']

#list of specific strings we want to check for in Tweets to get support person for application 
t3 = ['Support team/person for an application.',
    'Support team/person for an application!',
    'Support Person for CY Apps!!!']

#list of specific strings we want to check for in Tweets for posting RSS feeds
t4 = ['Provide Cypress website forums RSS feeds.',
    'Provide Cypress website forums RSS feeds!',
    'RSS feed generation!!!']

#reading the files
filename1=open(argfile1,'r')
f1=filename1.readlines()
filename1.close()

filename2=open(argfile2,'r')
f2=filename2.readlines()
filename2.close()

filename3=open(argfile3,'r')
f3=filename3.readlines()
filename3.close()

filename4=open(argfile4,'r')
f4=filename4.readlines()
filename4.close()



m1 = " "
for s in twt1:
    for i in t1:
        if i == s.text:
            sn = s.user.screen_name
            for line in f1:
                m1 += line
            my = "@%s" % (sn)
            m1 = str(my) + m1
            s = api.update_status(m1, s.id)
            print ("Tweeted",s.id)
            time.sleep(10)

m2 = " "
for q in twt2:
    for j in t2:
        if j == q.text:
            sn = q.user.screen_name
            for line in f2:
                m2 +=line
            my = "@%s" % (sn)
            m2 = str(my) + m2
            q = api.update_status(m2, q.id)
            print ("Tweeted",s.id)
            time.sleep(10)

m3 = " "
for r in twt3:
    for k in t3:
        if k == r.text:
            sn = r.user.screen_name
            for line in f3:
                m3 += line
            my = "@%s" % (sn)
            m3 = str(my) + m3
            s = api.update_status(m3, r.id)
            print ("Tweeted",s.id)
            time.sleep(10)

m4 = " "
for u in twt4:
    for l in t4:
        if l == u.text:
            sn = u.user.screen_name
            for line in f4:
                m4 += line 
            my = "@%s" % (sn)
            m4 = str(my) + m4
            s = api.update_status(m4, u.id)
            print ("Tweeted",s.id)
            time.sleep(10)



