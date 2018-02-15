# -*- coding: iso-8859-15 -*-
#from listening import startStream
from sentitest import RateSentiment
from decider import decide
from Strategeme import strategem_poster

import keyboard

import re
import tweepy
import logging
import time
import sys
import requests
import os
import json
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
from random import randint

ckey_main = ""
csecret_main = ""
akey_main = ""
asecret_main = ""

bot_name = "empty"
tweet = 0

Hashtag = "#PferdHenne"

auth = tweepy.OAuthHandler(ckey_main, csecret_main)
auth.set_access_token(akey_main, asecret_main)
api = tweepy.API(auth)


def transformer(_twt_undeb):
    for s in _twt_undeb:
        return s

#Tweet-Klasse (intern)
class Tweet:

    def __init__(self, _twt):

        self.text = _twt.text
        self.date = time.time()  # Zeitpunkt des Ladens reicht zur Analyse

        self.in_reply_to_status_id = _twt.in_reply_to_status_id

        self.username = _twt.user.screen_name  # zusätzlich User-Name
        self.userid = _twt.user.id  # twitter user id
        self.tweetId = _twt.id  # Tweet-ID

        self.sentiment_pos = 0  # Hier wird für den jeweiligen Tweet das Sentiment bewertet
        self.sentiment_neg = 0
        self.rateTweet()

    def rateTweet(self):

        rating = RateSentiment(self.text)

        # Positive Bewertung
        self.sentiment_pos = rating[0]
        self.sentiment_pos = int(self.sentiment_pos)

        # Negative Bewertung
        self.sentiment_neg = rating[1]
        self.sentiment_neg = int(self.sentiment_neg)


#Twitterstrang-Klasse (intern)
class Twitterstrang:

    def __init__(self):

        # Ein Twitterstrang besteht aus den chronologischen Tweets, den involvierten Charakteren und benutzten Strategemen

        self.hasUpdate = True
        self.tweets = []
        self.involvedCharacters = []
        self.usedStrategems = []


# LISTENING-TOOL: Listening-Tool, dass auf eine Antwort auf den Tweet wartet

class MyStreamListener(tweepy.StreamListener):
    def on_status(self, status):
        print(status.user.screen_name)
        if status.retweeted == "True":  # won't respond to reTweets, direct tweets only
            return

        elif status.user.screen_name == 'derDotzkal':
            return

        elif status.user.screen_name == 'flinkerfinker':
            return

        elif status.user.screen_name == 'AlexthemanKraft':
            return

        elif status.user.screen_name == 'lenakonfus':
            return

        elif status.user.screen_name == 'timlandich':
            return

        elif status.user.screen_name == 'nadjerado':
            return

        else:
            print("Es wurde geantwortet:", status.text)
            fetchedTweets.append(Tweet(status))

myStreamListener = MyStreamListener()
myStream = tweepy.Stream(auth = api.auth, listener=MyStreamListener())
myStream.filter(track=['derDotzkal', 'flinkerfinker', 'AlexthemanKraft', 'lenakonfus', 'timlandich', 'nadjerado'],async=True)


#------------------------------- Main Handler ---------------------------------------------------

# Persona
# 0 superior
# 1 confrontation
# 2 attack
# 3 confusing
# 4 gaining
# 5 desperate

print("Initialisiere Botnetzwerk...\n")
time.sleep(5)
print("@flinkerfinker: Bereit!")
print("@AlexthemanKraft: Bereit!")
print("@lenakonfus: Bereit!")
print("@timlandich: Bereit!")
print("@nadjerado: Bereit!")
time.sleep(2)
print("\nSHOWTIME\n")

fetchedTweets = []
twitterstraenge = []

timer = time.time()

while True:

    maxStraenge = 1
    maxLoops = 6 #max Loops, bis ein Tweet akzeptiert werden muss

    if len(twitterstraenge) < maxStraenge:
        status = tweepy.Cursor(api.search, q=Hashtag + "-filter:retweets", lang="de", result_type="recent").items(maxLoops)
        tweetSearch = []
        for s in status:
            tweetSearch.append(s)
        print(len(tweetSearch))

    while len(twitterstraenge) < maxStraenge:
        twitterstraenge.append(Twitterstrang())

        # Ersten Tweet raussuchen
        foundUnique = False

        nowLoop = 0
        print("\n###########")
        time.sleep(1)
        print("\nErstelle und verfolge neuen Twitterstrang: ID ",len(twitterstraenge)-1)
        time.sleep(1)
        print("Anzahl der Twitterstraenge ist nun: ",len(twitterstraenge))
        time.sleep(5)
        while foundUnique is False and nowLoop < maxLoops:

            __twt_transformed = Tweet((tweetSearch[nowLoop]))
            foundUnique = True

            for i, strang in enumerate(twitterstraenge):
                if i != len(twitterstraenge) - 1:
                    for t in twitterstraenge[i].tweets:
                        if t.tweetId == __twt_transformed.tweetId:
                            foundUnique = False

            nowLoop += 1


        print("\nIn Twitterstrang [",len(twitterstraenge)-1,"] wird der Recent-Tweet[",nowLoop-1,"] nun analysiert:")
        time.sleep(5)
        print(__twt_transformed.text, "\n\n")
        twitterstraenge[-1].tweets.append(__twt_transformed)

        _str = decide(twitterstraenge[-1])
        time.sleep(5)
        # Strategem-Poster
        # gibt unter info folgende Infos als Liste zurück: letzter TweetText, letzter Bot, letzte Strategem-Nummer

        _twt = strategem_poster(twitterstraenge[-1].tweets[-1].tweetId, _str, Hashtag)


        twitterstraenge[-1].tweets.append(Tweet((_twt[0])))


        bot_name = _twt[1]

        twitterstraenge[-1].usedStrategems.append(str(_str))
        twitterstraenge[-1].involvedCharacters.append(bot_name)

        print("\nTwitterstrang initialisiert, Antwort gesetzt, warte auf weitere Interaktionen von Usern an Strang[",len(twitterstraenge)-1,"]")

    #(time.time() - timer) > (1 * 60):
    if input("Bereit zum Antworten...") == "":
        timer = time.time()


        for strang in reversed(twitterstraenge):
            strang.hasUpdate = False
            for f in fetchedTweets:

                if strang.tweets[-1].tweetId == f.in_reply_to_status_id:

                    strang.tweets.append((f))
                    time.sleep(1)
                    print("\nErkannter Tweet wird analysiert...")
                    strang.hasUpdate = True
                    time.sleep(1)
                    _str = decide(strang)
                    time.sleep(5)
                    _twt = strategem_poster(strang.tweets[-1].tweetId, _str, Hashtag)
                    strang.tweets.append(Tweet(_twt[0]))

                    bot_name = _twt[1]

                    strang.usedStrategems.append(str(_str))
                    strang.involvedCharacters.append(bot_name)

            if strang.hasUpdate is False:
                twitterstraenge.remove(strang)

        fetchedTweets.clear()

        """
        _tempstrang = twitterstraenge
        twitterstraenge.clear()
        for x in _tempstrang:
            if x.hasUpdate == True:
                twitterstraenge.append(x)
                print("append!")"""
