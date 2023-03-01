# Pelican-tweet

:warning: owing to the new policies followed by Twitter this plugin could work no more. Anyway the support to this plugin has been discontinued.

A Pelican plugin for automatically publish new posts on Twitter

Hacked from [darktable-dtorg](https://github.com/darktable-org/dtorg).

Needs Python > 3.0

## How it works

*Pelican-tweet* will search your contents for articles (actually ALL contents except pages) that are not in a `draft` status.

On its first run it creates a file called `posted_on_Twitter.txt` in your Pelican root directory.

Then it tries to post all eligible articles to Twitter and - if post routine returns no errors - writes article URL in `posted_on_Twitter.txt`.

On every further run it matches the actual articles list with the list in `posted_on_Twitter.txt` file and posts only new articles (and writes them in `posted_on_Twitter.txt`).

## Twitter APIs

In order to publish on Twitter you need to enter in `publishconf.py` the following information:

``` python
TWITTER_CONSUMER_KEY = ''
TWITTER_CONSUMER_SECRET = ''
TWITTER_ACCESS_TOKEN_KEY = ''
TWITTER_ACCESS_TOKEN_SECRET = ''
```

You can follow [this guide](https://www.slickremix.com/docs/how-to-get-api-keys-and-tokens-for-twitter/) in order to understand the correct procedure to obtain these information from Twitter developers area.

This plugin depends on [python-twitter](https://code.google.com/archive/p/python-twitter/).
