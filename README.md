# TweetBot
### Discord bot allowing users to remotely tweet from a discord server using a twitter dev account


--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
This bot was created as a project during my first semester of University

When setting up the bot there are a few steps that need to be completed. I will attatch a link to in depth explanations for the configuration below:

[Discord setup](https://realpython.com/how-to-make-a-discord-bot-python/#how-to-make-a-discord-bot-in-the-developer-portal)

[Twitter developer setup](https://realpython.com/twitter-bot-python-tweepy/#creating-twitter-api-authentication-credentials)

After you have completed the steps above and have your Discord and Twitter tokens, add them to the below code in the tokens.py file

```
Discord Token
discordToken = "*discordTokenGoesHere*"

Twitter Tokens
consumerKey = "*consumerKeyGoesHere*"
consumerSecret = "*consumerSecretGoesHere*"
accessToken = "*accessTokenGoesHere*"
accessTokenSecret = "*accessTokenSecretGoesHere"
```

After you complete this step the bot should be fully functional. The bot has the following features:
- Post text based tweets
  > DiscordUsername says message
- Post text including a tag
  > DiscordUsername says @username
- Post gifs
  > DiscordUsername says *insert gif here*

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Although the bot runs currently there are some future changes which could be beneficial:
- Currently if a user uploads an image to discord the account tweets the blank template of, DiscordUsername says. I am unsure if posting an image is possible and, if not, I would like to implement a change which asks the user for a valid input
- Also I am experiencing a bug where the program crashes if a tweet that has already been made is inputted 
- One final change could be adding a feature to allow the bot to read tweets into the discord from the accounts feed
