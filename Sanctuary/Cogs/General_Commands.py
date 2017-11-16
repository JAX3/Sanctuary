from discord.ext import commands
from Cogs.Utils.CustomBot import Bot


class General_Commands(object):

	def __init__(self, bot:Bot):
		self.bot = bot


	@commands.command()
	async def ping(self, ctx):
		'''
		The most original bot command.
		'''

		await ctx.send('Pong.')


	@commands.command()
	async def discord(self, ctx):
		'''
		PMs you a guild invite link
		'''

		try:
			await ctx.author.send('You can invite your friends by using this link: ' + self.bot.config['Guild Invite'])
			await ctx.message.add_reaction('👌')
		except Exception:
			await ctx.send('I tried to send you a PM, but you have them disabled. Please send me a DM first so I can run this command properly.')


def setup(bot:Bot):
	x = General_Commands(bot)
	bot.add_cog(x)
