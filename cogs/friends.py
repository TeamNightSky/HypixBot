from discord.ext.commands import Cog, command
from discord import Embed, Color
from hypixelio.ext.asyncio.converters import AsyncConverters


def setup(bot):
    bot.add_cog(Friends(bot))


class Friends(Cog):
    def __init__(self, bot):
        self.bot = bot

    @command("friends")
    async def friends(self, ctx, username: str):
        """Show friends of Hypixel user"""
        loading = await ctx.send("https://tenor.com/view/searching-gif-4679838")

        uuid = await AsyncConverters.username_to_uuid(username)
        friends = await self.bot.client.get_friends(uuid=uuid)

        for i, friend in enumerate(friends):
            if friend.SENDER_ID == uuid:
                friends[i] = friend.RECEIVER_ID
            else:
                friends[i] = friend.SENDER_ID

        embed = Embed(
            title=f"Friends of **{username}**",
            color=Color.green()
        )
        embed.add_field(
            name="Friends",
            value='\n'.join([
                f"- `{await AsyncConverters.uuid_to_username(user)}`" for user in friends.FRIENDS
            ])[:1000]
        )

        await loading.delete()
        await ctx.send(embed=embed)

