from glob import glob
from CustomBot import Bot


bot = Bot(
	command_prefix='/'
)


# List all files in the Cogs directory that end in .py
extensions = ['Cogs.' + i.split('/')[-1][:-3] for i in glob("./Cogs/*.py")]


@bot.event
async def on_ready():
	print("Booted and ready for action")
	print(f" :: {bot.user}")
	print(f" :: {bot.user.id}")

	for ext in extensions:
		try:
			bot.load_extension(ext)
			print("Loaded extension", ext)
		except Exception as e:
			exc = '{}: {}'.format(type(e).__name__, e)
			print('Failed to load extension {}\n{}'.format(ext, exc))

	print("All extensions loaded")


bot.run_custom()
