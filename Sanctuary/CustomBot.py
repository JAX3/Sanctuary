from json import load
from discord.ext import commands


class Bot(commands.AutoShardedBot):

	def __init__(self, **kwargs):
		super().__init__(**kwargs)
		self.config = {}

		with open('./Config/Bot.json') as a:
			data = load(a)
		self.config = data 

	def run_custom(self):
		token = self.config["Bot Token"]
		return self.run(token)

