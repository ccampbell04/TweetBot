import discord
import tweepy
import tokens

client = discord.Client()

TOKEN = tokens.discordToken

auth = tweepy.OAuthHandler(tokens.consumerKey, tokens.consumerSecret)
auth.set_access_token(tokens.accessToken, tokens.accessTokenSecret)

api = tweepy.API(auth)


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!tweet'):
        await message.channel.send("What would you like to tweet?")

        def check(msg):
            return msg.author == message.author and msg.channel == message.channel

        msg = await client.wait_for("message", check=check)

        await message.channel.send(f"Posting tweet - {msg.author} says {msg.content}".format(message.author.mention))
        api.update_status(f"{msg.author} says {msg.content}")

client.run(TOKEN)
