# Pelican-tweet

A Pelican plugin for automatically publish new posts on Twitter

Hacked from [darktable-dtorg](https://github.com/darktable-org/dtorg).

## How it works

*Pelican-tweet* will read your `sitemap.xml` file for articles (i.e. all items except pages)

On its first run it creates a file called `posted_on_Twitter.txt` in your Pelican working directory.

Then it tries to post all found articles to Twitter and - if post routine returns no errors, writes article URL in `posted_on_Twitter.txt`.

On every further run it matchs the actual articles list with the list in `posted_on_Twitter.txt` file and posts new articles on Twitter (and writes them in `posted_on_Twitter.txt`).

## Twitter APIs

In order to publish on Twitter you need to enter in `pelicanconf.py` the following information:

``` python
TWITTER_CONSUMER_KEY = ''
TWITTER_CONSUMER_SECRET = ''
TWITTER_ACCESS_TOKEN_KEY = ''
TWITTER_ACCESS_TOKEN_SECRET = ''
```

You can follow [this guide](https://www.slickremix.com/docs/how-to-get-api-keys-and-tokens-for-twitter/) in order to understand the correct procedure to obtain these information from Twitter developers area.
