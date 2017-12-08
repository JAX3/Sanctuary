from discord.ext import commands
from Cogs.Utils.custom_bot import Bot
from Cogs.Utils.file_handling import read_file


class General_Commands(object):

	def __init__(self, bot:Bot):
		self.bot = bot


	async def on_message(self, message):
		'''
		No shouting at the bot
		'''

		if not message.content.startswith('/'):
			return 

		if True not in [message.content.lower()[1:].startswith(i) for i in [o.name for o in self.bot.commands]]:
			return

		if message.content.isupper():
			await message.channel.send("There's no need to shout .-.")


	async def on_command(self, ctx):
		'''
		Provides a reaction for the default help command.
		'''

		if ctx.command.name == 'help':
			await ctx.message.add_reaction('\N{OK HAND SIGN}')


	@commands.command()
	async def ping(self, ctx):
		'''
		The most original bot command.
		'''

		# await ctx.send('Pong.')
		await ctx.send('My latency is `{:.2f}ms`.'.format(self.bot.latency * 100))


	@commands.command()
	async def discord(self, ctx):
		'''
		PMs you a guild invite link.
		'''

		try:
			await ctx.author.send('You can invite your friends by using this link: ' + self.bot.config['Guild Invite'])
			await ctx.message.add_reaction('\N{OK HAND SIGN}')
		except Exception:
			await ctx.send('I tried to send you a PM, but you have them disabled. Please send me a DM first so I can run this command properly.')


	@commands.command()
	async def schedule(self, ctx):
		'''
		Gives you the schedule of LeoHartUK's Twitch account.
		'''

		content = read_file('./Config/Schedule_Command.txt')
		try:
			await ctx.author.send(content)
			await ctx.message.add_reaction('\N{OK HAND SIGN}')
		except Exception:
			await ctx.send('I tried to send you a PM, but you have them disabled. Please send me a DM first so I can run this command properly.')


def setup(bot:Bot):
	x = General_Commands(bot)
	bot.add_cog(x)
