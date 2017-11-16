from discord import TextChannel
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

		This is useful for making votes for given things on your guild - an impartial bot view to help with things for you.
		'''

		message = await ctx.send(content)
		thumbs = ['👍', '👎']  # Thumbs up, thumbs down
		for r in thumbs:
			await message.add_reaction(r)
		await ctx.message.delete()


	@commands.command(aliases=['delete', 'purge', 'destroy', 'murder'])
	@commands.has_any_role('Caleb', 'Moderators', 'Administrators')
	async def clear(self, ctx, amount:int):
		'''
		Removes a given number of messages from the current channel.
		'''

		if amount < 1:
			await ctx.send(".-.")
			return 

		if amount > 501:
			await ctx.send("I'm sure you have no ill intent, but I don't feel comfortable deleting more than 500 messages at once. Sorry.")
			return

		await ctx.channel.purge(limit=amount+1)


	@commands.command()
	@commands.has_any_role('Caleb', 'Administrators')
	async def echo(self, ctx, *, content:str):
		'''
		Echos a string back to you.
		
		This takes a line of text that you've given the bot, and spits it right back out to you in the same channel that you called it from.
		'''

		await ctx.send(content)
		await ctx.message.delete()

	@commands.command()
	@commands.has_any_role('Caleb', 'Administrators')
	async def echointo(self, ctx, channel:TextChannel, *, content:str):
		'''
		Echos a string to a specified channel.
		
		This takes a line of text that you've given the bot, and spits it right back out to you in the same  channelthat you specified.
		'''

		try:
			await channel.send(content)
			await ctx.message.add_reaction('👌')
		except Exception:
			await ctx.send("I don't have permission to talk in that channel ;-;")


	@commands.command()
	@commands.has_any_role('Caleb', 'Moderators', 'Administrators')
	async def voteinto(self, ctx, channel:TextChannel, *, content:str):
		'''
		Sends a message to a channel, then adds the thumbs up/down emojis to it.

		This is useful for making votes for given things on your guild - an impartial bot view to help with things for you.
		'''

		try:
			message = await channel.send(content)
			thumbs = ['👍', '👎']  # Thumbs up, thumbs down
			for r in thumbs:
				await message.add_reaction(r)
			await ctx.message.add_reaction('👌')
		except Exception:
			await ctx.send("I don't have permission to talk in that channel ;-;")


def setup(bot:Bot):
	x = Admin_Commands(bot)
	bot.add_cog(x)
