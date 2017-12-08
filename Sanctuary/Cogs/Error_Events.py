from discord.ext import commands
from Cogs.Utils.custom_bot import Bot


class Error_Events(object):

	def __init__(self, bot:Bot):
		self.bot = bot


	async def on_command_error(self, ctx, error):
		'''
		Runs when there is an error in the vote command
		Either there's no content, or the user doesn't have the required permissions to run it
		'''

		if isinstance(error, commands.CheckFailure):
			'''The check failed, they don't have permission'''
			await ctx.send("You don't have the required permissions to run this command.")
			return

		elif isinstance(error, commands.MissingRequiredArgument):
			'''Missing content'''
			await ctx.send('Sorry, but you aren\'t using this commmand correctly. Please refer to the help command.')
			return

		else:
			raise error
			return


def setup(bot:Bot):
	x = Error_Events(bot)
	bot.add_cog(x)
