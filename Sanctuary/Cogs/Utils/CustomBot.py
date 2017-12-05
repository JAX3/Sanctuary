from html import unescape
from asyncio import sleep
from json import load
from aiohttp import ClientSession
from discord import Embed
from discord.ext import commands


class Bot(commands.AutoShardedBot):

	def __init__(self, **kwargs):
		super().__init__(**kwargs)
		self.config = {}
		self.last_message = None

		with open('./Config/Bot.json') as a:
			data = load(a)
		self.config = data 
		self.session = ClientSession(loop=self.loop)
		self.tweet_task = self.loop.create_task(self.get_latest_tweet())

	def __unload(self):
		self.session.close()

	def run_custom(self):
		token = self.config["Bot Token"]
		return self.run(token)

	async def get_latest_tweet(self):
		'''
		Gets the latest Tweet, pushes it to the announcements channel
		'''

		URL = 'https://api.twitter.com/1.1/statuses/user_timeline.json'
		TOKEN = self.config['Twitter Bearer Token']
		params = {'screen_name': 'LeoHartUK', 'count': 1, 'tweet_mode': 'extended'}
		headers = {'Authorization': TOKEN, 'User-Agent': 'Sacntuary Discord bot'}
		last_said_id = None
		await self.wait_until_ready()

		while not self.is_closed():
			channel = self.get_channel(self.config['Tweet Announcement Channel'])
			async with self.session.get(URL, params=params, headers=headers) as r:
				data = await r.json()

			tweet = data[0]
			if last_said_id == None:
				last_said_id = tweet['id']
			elif last_said_id == tweet['id']:
				pass
			else:
				last_said_id = tweet['id']
				e = Embed(
					colour=0x0084b4
				)
				e.set_author(
					name='NEW TWEET', 
					url='https://twitter.com/{0}/statuses/{1}'.format(tweet['user']['screen_name'], tweet['id']),
					icon_url='https://cdn1.iconfinder.com/data/icons/logotypes/32/circle-twitter-512.png%22%7D'
				)
				e.set_thumbnail(url=tweet['user']['profile_image_url'].replace('_normal', ''))
				e.add_field(name=b'\xe2\x94\x80'.decode()*10, value=unescape(tweet['full_text']), inline=False)
				e.add_field(name=b'\xe2\x94\x80'.decode()*10, value='Follow [@\u200B{0}](https://twitter.com/{0}) on Twitter to stay updated!'.format(tweet['user']['screen_name']), inline=False)
				await channel.send(embed=e)
			await sleep(120)

