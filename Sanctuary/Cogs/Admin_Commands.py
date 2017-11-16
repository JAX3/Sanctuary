from random import choice
from discord.ext import commands
from Cogs.Utils.CustomBot import Bot


class Admin_Commands(object):

	def __init__(self, bot:Bot):
		self.bot = bot


	@commands.command()
	@commands.has_any_role('Caleb', 'Moderators', 'Administrators')
	async def vote(self, ctx, *, content:str):
		'''
		Adds a thumbs up/down emoji to the message you wrote.

		This is useful for making votes for given things on your guild - an impartial bot view to help
		with things for you.
		'''

		message = await ctx.send(content)
		thumbs = ['👍', '👎']  # Thumbs up, thumbs down
		for r in thumbs:
			await message.add_reaction(r)
		await ctx.message.delete()


	@vote.error 
	async def vote_error(self, ctx, error):
		'''
		Runs when there is an error in the vote command
		Either there's no content, or the user doesn't have the required permissions to run it
		'''

		if isinstance(error, commands.CheckFailure):
			'''The check failed, they don't have permission'''
			await ctx.send('You don\'t have permission to run this command.')
			return

		elif isinstance(error, commands.MissingRequiredArgument):
			'''Missing content'''
			await ctx.send('Sorry, but you aren\'t using this commmand correctly. Please refer to the help command by running `help vote`.')
			return

		else:
			raise error
			return


def setup(bot:Bot):
	x = Administration(bot)
	bot.add_cog(x)
