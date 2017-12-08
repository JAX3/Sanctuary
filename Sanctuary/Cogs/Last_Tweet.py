from html import unescape
from aiohttp import ClientSession
from discord import Embed
from discord.ext import commands
from Cogs.Utils.custom_bot import Bot


class Last_Tweet(object):

	def __init__(self, bot:Bot):
		self.bot = bot
		self.session = ClientSession(loop=bot.loop)


	def __unload(self):
		self.session.close()


	@commands.command()
	async def lasttweet(self, ctx):
		'''
		Creates an embed from raw JSON data
		'''

		URL = 'https://api.twitter.com/1.1/statuses/user_timeline.json'
		TOKEN = self.bot.config['Twitter Bearer Token']
		params = {'screen_name': 'LeoHartUK', 'count': 1, 'tweet_mode': 'extended'}
		headers = {'Authorization': TOKEN, 'User-Agent': 'Sacntuary Discord bot'}

		async with self.session.get(URL, params=params, headers=headers) as r:
			data = await r.json()

		tweet = data[0]

		e = Embed(
			colour=0x0084b4
		)
		e.set_author(
			name='NEW TWEET', 
			url='https://twitter.com/{0}/statuses/{1}'.format(tweet['user']['screen_name'], tweet['id']),
			icon_url='https://cdn1.iconfinder.com/data/icons/logotypes/32/circle-twitter-512.png%22%7D'
		)
		e.set_thumbnail(url=tweet['user']['profile_image_url'].replace('_normal', ''))
		e.add_field(name='──────────', value=unescape(tweet['full_text']), inline=False)
		e.add_field(name='──────────', value='Follow [@\u200B{0}](https://twitter.com/{0}) on Twitter to stay updated!'.format(tweet['user']['screen_name']), inline=False)
		await ctx.message.delete()
		await ctx.author.send(embed=e)


def setup(bot:Bot):
	x = Last_Tweet(bot)
	bot.add_cog(x)
