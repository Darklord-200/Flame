from discord.ext import commands
import logging

class Ping(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.logger = logging.getLogger("DiscordBot")

    @commands.Cog.listener()
    async def on_ready(self):
        self.logger.info(f'discord bot is online as: {self.bot.user}')

    @commands.command("ping")
    async def ping(self, ctx):
        await ctx.send('pong')

async def setup(bot):
    await bot.add_cog(Ping(bot))