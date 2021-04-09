# Pelican-tweet

A Pelican plugin for automatically publish new posts on Twitter

Hacked from [darktable-dtorg](https://github.com/darktable-org/dtorg).

## How it works

*Pelican-tweet* will scan your `content` directory for articles (i.e. all items except pages)

On first run it creates a file called `posted_on_Twitter.txt` in your Pelican working directory entering the URLs of all articles found. All these URLs will be posted immediatly on Twitter.

On every further run it matchs the actual articles list with the list in `posted_on_Twitter.txt` file and writes on it the new articles found (and posts new articles on Twitter).

## Twitter APIs

In order to publish on Twitter you need to enter in `pelicanconf.py` the following information:

``` python
TWITTER_CONSUMER_KEY = ''
TWITTER_CONSUMER_SECRET = ''
TWITTER_ACCESS_TOKEN_KEY = ''
TWITTER_ACCESS_TOKEN_SECRET = ''
```

You can follow [this guide](https://www.slickremix.com/docs/how-to-get-api-keys-and-tokens-for-twitter/) in order to understand the correct procedure to obtain these information from Twitter developers area.

To re-tweet anything you have simply to cancel the relevant URL from `posted_on_Twitter.txt` file and run `pelican content`.
