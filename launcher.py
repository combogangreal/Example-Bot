import asyncio
import sys
from bot import bot
from api import api
from dashboard import dashboard

bot = bot.Bot()


async def main():
    """Main function, allows launching of the bot, api, or dashboard"""
    if sys.argv[1] == "bot":
        await bot.start()
    elif sys.argv[1] == "api":
        api.app.run(host="localhost", port=3000, debug=True)
    elif sys.argv[1] == "dashboard":
        dashboard.app.run(host="127.0.0.1", port=8080, debug=True)


asyncio.run(main())
