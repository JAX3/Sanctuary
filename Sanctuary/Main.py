from glob import glob
from discord import Game
from Cogs.Utils.CustomBot import Bot


bot = Bot(
	command_prefix='/',
	pm_help=True
)


# List all files in the Cogs directory that end in .py
#extensions = [i.split('/')[-1][:-3].replace('\\', '.').replace('/', '.') for i in glob("./Cogs/*.py")]
extensions = []
for filepath in glob("./Cogs/*.py"):
	file = filepath.replace('\\', '/').split('/')[-1]
	filename = 'Cogs.' + file[:-3]
	extensions.append(filename)


@bot.event
async def on_ready():
	print("Booted and ready for action")
	print(f" :: {bot.user}")
	print(f" :: {bot.user.id}")
	print()

	for ext in extensions:
		try:
			bot.load_extension(ext)
			print(" - Loaded extension", ext)
		except Exception as e:
			exc = '{}: {}'.format(type(e).__name__, e)
			print(' - Failed to load extension {}\n       {}'.format(ext, exc))

	print("All extensions loaded")

	game = Game(name=bot.config['Game']['Name'], type=bot.config['Game']['Type'])
	await bot.change_presence(game=game)


bot.run_custom()
