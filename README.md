# Telegram Bot

Simple telegram bot that could answer traceroute request on provided IP address or domain name.

__Requirements__:
* Deploy on a [Heroku](https://dashboard.heroku.com/apps/telegram-trace)
* Hosting on a [Bitbucket](https://bitbucket.org/maximka07/telegram-trace/src/main/)
* Use Telegram API: I chose a [Python framework](https://github.com/python-telegram-bot/python-telegram-bot)

## Installation

```
# optional virtual env
virtualenv local_env 
source local_env/bin/activate

pip install -r requirements.txt
```

## Heroku
heroku-community/apt and heroku/python buildpacks are needed.

```
heroku config:set T_TOKEN=YOUR_OWN_API_KEY
heroku buildpacks:add --index 1 heroku-community/apt
heroku ps:scale worker=1
```

Some useful commands for debugging your cloud:
```
heroku run bash
heroku logs --tail

# git push -f heroku main
```

## Usage

You will require unique API key that Telegram generates for each bot - ask [BotFather](https://t.me/botfather) for this.
Run each time you want to start a bot-server.
```
export T_TOKEN=YOUR_OWN_API_KEY
python3 __main__.py
```
Run the bot until you press Ctrl-C or the process receives SIGINT, SIGTERM or SIGABRT.

**NOTE**: May be required root rights for the traceroute command -- use __sudo -E__ while starting server 


Here are some examples of conversation:

![alt-Image](example.png "Here you can see example of the traceroute output")
![alt-Image](example1.png "Here you can see example of the tracepath output")

## Author

**Maksym Halchenko** - [maxs-im](https://github.com/maxs-im)

[Github Repository](https://github.com/maxs-im/telegram-trace)

## __Troubleshooting__

Unfortunately, we cannot use traceroute without [root privileges](https://github.com/ValentinBELYN/icmplib/issues/6#issuecomment-780099407), so I implemented a second tracing method via tracepath via the command line (I could not find a similar Python framework).

Also, there is a problem that the bot is not asynchronous, so it serves each user in the order of the queue :woozy_face:
