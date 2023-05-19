from discord.ext import commands
import logging

class Message(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.logger = logging.getLogger("DiscordBot")

    @commands.Cog.listener()
    async def on_message(self, message):
        self.logger.info(f'Message from {message.author}: {message.content}')

async def setup(bot):
    await bot.add_cog(Message(bot))