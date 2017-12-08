from discord.ext import commands
from discord.ext.commands import Context
from Cogs.Utils.custom_bot import Bot
from Cogs.Utils.file_handling import read_file


class Role_Management(object):

	def __init__(self, bot:Bot):
		self.bot = bot


	@commands.command()
	@commands.has_any_role('Caleb', 'Administrators')
	async def addrole(self, ctx:Context, *, role_name:str):
		'''
		Adds an available role to the list of self-assignable roles
		'''

		# Grab the role they want to add
		role_to_use = []
		for i in ctx.guild.roles:
			if role_name.casefold() in i.name.casefold() or role_name == str(i.id):
				role_to_use.append(i)

		# Make sure it exists
		if not role_to_use:
			await ctx.send('No role by the name `{}` could be found.'.format(role_name))
			return
		if len(role_to_use) > 1:
			await ctx.send('There were multiple roles that matched that name. Try using its role ID instead.')
			return

		# Write the role to database
		role = role_to_use[0]
		async with self.bot.database() as db:
			x = await db('SELECT id FROM available_roles WHERE id=$1', role.id)
			if x:
				await ctx.send('That role is already self-assignable.')
				return
			await db('INSERT INTO available_roles VALUES ($1)', role.id)
		await ctx.send('The role `{.name}` is now self self-assignable.'.format(role))


	@commands.command()
	async def role(self, ctx:Context, *, role_name:str):
		# Grab the role they want to add
		role_to_use = []
		for i in ctx.guild.roles:
			if role_name.casefold() in i.name.casefold() or role_name == str(i.id):
				role_to_use.append(i)

		# Make sure it exists
		if not role_to_use:
			await ctx.send('No role by the name `{}` could be found.'.format(role_name))
			return
		if len(role_to_use) > 1:
			await ctx.send('There were multiple roles that matched that name. Try using its role ID instead.')
			return
		role = role_to_use[0]

		# Check that the role they want is in the table
		async with self.bot.database() as db:
			x = await db('SELECT id FROM available_roles WHERE id=$1', role.id)

		# Get whether or not they can modify that
		if not len(x):
			await ctx.send('That role is not self-assignable.')
			return

		# Check whether they have the role already
		if len([i for i in ctx.author.roles if i == role]):
			await ctx.send('You already have that role.')
			return
		else:
			await ctx.author.add_roles(role, reason='Use of the `role` command.')
			await ctx.send('Done.')
			return


	@commands.command()
	async def roleremove(self, ctx:Context, *, role_name:str):
		# Grab the role they want to add
		role_to_use = []
		for i in ctx.guild.roles:
			if role_name.casefold() in i.name.casefold() or role_name == str(i.id):
				role_to_use.append(i)

		# Make sure it exists
		if not role_to_use:
			await ctx.send('No role by the name `{}` could be found.'.format(role_name))
			return
		if len(role_to_use) > 1:
			await ctx.send('There were multiple roles that matched that name. Try using its role ID instead.')
			return
		role = role_to_use[0]

		# Check that the role they want is in the table
		async with self.bot.database() as db:
			x = await db('SELECT id FROM available_roles WHERE id=$1', role.id)

		# Get whether or not they can modify that
		if not len(x):
			await ctx.send('That role is not self-assignable.')
			return

		# Check whether they have the role already
		if len([i for i in ctx.author.roles if i == role]):
			await ctx.author.remove_roles(role, reason='Use of the `roleremove` command.')
			await ctx.send('Done.')
			return
		else:
			await ctx.send('You don\'t have that role for me to remove.')
			return


def setup(bot:Bot):
	x = Role_Management(bot)
	bot.add_cog(x)
