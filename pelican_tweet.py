# -*- coding: utf-8 -*-
"""
Post new articles on Twitter
"""

import string

import logging
logger = logging.getLogger(__name__)

from pelican import signals

# https://github.com/bear/python-twitter/wiki
import twitter


def read_articleslist():
   try:
      with open('posted_on_Twitter.txt', 'r') as f:
         result = list(map(str.rstrip, f))
   except IOError:
      result = []
   return result

def write_articleslist(articleslist):
   articleslist.sort()
   with open('posted_on_Twitter.txt', 'w') as f:
      for article in articleslist:
         f.write("%s\n" % article)

def shorten(message, limit, replacement = ' …'):
   if twitter.twitter_utils.calc_expected_status_length(message) <= limit:
      return message
   limit -= twitter.twitter_utils.calc_expected_status_length(replacement)
   words = message.split()
   result = words.pop(0)
   if twitter.twitter_utils.calc_expected_status_length(result) > limit:
      return result[:limit] + replacement
   while words:
      candidate = result + ' ' + words.pop(0)
      if twitter.twitter_utils.calc_expected_status_length(candidate) <= limit:
         result = candidate
      else:
         break
   result += replacement
   return result

def post_on_twitter(settings, new_posts):
   consumer_key = settings.get('TWITTER_CONSUMER_KEY', '')
   consumer_secret = settings.get('TWITTER_CONSUMER_SECRET', '')
   access_token_key = settings.get('TWITTER_ACCESS_TOKEN_KEY', '')
   access_token_secret = settings.get('TWITTER_ACCESS_TOKEN_SECRET', '')

   if consumer_key == '' or consumer_secret == '' or access_token_key == '' or access_token_secret == '':
      print('Pelican-tweet: Twitter credentials not configured...')
      return False

   api = twitter.Api(consumer_key = consumer_key,
      consumer_secret = consumer_secret,
      access_token_key = access_token_key,
      access_token_secret = access_token_secret)

   try:
      api.VerifyCredentials()
   except:
      print('Pelican-tweet: error while authenticating on Twitter...')
      return False

   limit = 275 # actually 280 but let's account for some bugs and miscalculations
   message = 'Put_here_your_message: %s\n%s\n'

   for article in new_posts:
      url = article.get_siteurl() + '/' + article.url
      free_space = limit - twitter.twitter_utils.calc_expected_status_length(message % ('', url))
      title = shorten(article.title, free_space)
      post = message % (title.replace('&nbsp;',' '), url)
      print(post.encode('utf-8'))
      api.PostUpdate(post)

   return True


def post_updates(generator, writer):
   articleslist = read_articleslist()
   new_posts = []
   for article in generator.articles:
      if article.url not in articleslist:
         new_posts.append(article)

   # we only write the newly found sites to disk if posting them worked. that way we can retry later
   if new_posts:
      if post_on_twitter(generator.settings, new_posts):
         for article in new_posts:
            articleslist.append(article.url)
         write_articleslist(articleslist)


def register():
   """Plugin registration"""
   try:
      signals.article_writer_finalized.connect(post_updates)
   except AttributeError:
      pass
