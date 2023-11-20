import asyncio
from bot import bot

bot = bot.Bot()

async def launch():
    """Launchs the bot"""
    await bot.start()

@bot.command(name="sync")
async def sync(ctx):
    synced = await bot.tree.sync()
    print(f"Synced {len(synced)} command(s).")

asyncio.run(launch())