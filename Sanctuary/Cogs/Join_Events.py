from discord.ext import commands
from Cogs.Utils.CustomBot import Bot
from Cogs.Utils.FileHandling import read_file


class Join_Events(object):

	def __init__(self, bot:Bot):
		self.bot = bot


	async def on_member_join(self, member):
		'''
		Run when a member joins the Discord guild
		'''

		text = read_file('./Config/Member_Join.txt')
		try:
			await member.send(text)
		except Exception:
			pass


def setup(bot:Bot):
	x = Join_Events(bot)
	bot.add_cog(x)
