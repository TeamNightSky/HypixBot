from hypixelio.ext.asyncio import AsyncClient
from discord.ext.commands import Bot


dtoken, htoken = open("tokens.txt", 'r').read().split("\n")
client = AsyncClient(api_key=htoken)
cogs = open("cogs.txt", 'r').read().split("\n")


class HypixBot(Bot):
    def __init__(self):
        super().__init__("?")
        self.client = client

        for cog in cogs:
            self.load_extension(f"cogs.{cog}")

    async def on_ready(self):
        print(f"RUNNING : USERNAME {self.user.display_name} : ID {self.user.id}")


bot = HypixBot()

bot.run(dtoken)
