import asyncio
import logging
import discord
from discord.ext import commands
import os
import yaml
import dotenv
from pathlib import Path
from get_docker_secret import get_docker_secret

class Util:
    @staticmethod
    def load_yml(file: str) -> dict:
        if not os.path.basename(file).endswith((".yml", ".yaml")):
            raise ValueError(f"parameter file with value {file} is not a .yml or .yaml file")
        with open(file, 'r') as f:
            data = yaml.safe_load(f)
        return data

    @staticmethod
    def load_env(file: str):
        if not os.path.basename(file).endswith(".env"):
            raise ValueError(f"parameter file with value {file} is not a .env file")
        dotenv.load_dotenv(file)
    
    @staticmethod
    def setupLogger(name: str, level: int) -> logging.Logger:
        logger = logging.getLogger(name)
        logger.setLevel(level)
        console = logging.StreamHandler()
        console.setLevel(level=level)
        formatter =  logging.Formatter('%(asctime)s - %(name)s - %(levelname)s : %(message)s')
        console.setFormatter(formatter)
        logger.addHandler(console)
        return logger


class MyBot(commands.Bot):
    def __init__(self, config: dict) -> None:
        self.config = config

        super().__init__(self.config["prefix"], intents=discord.Intents.all())
        

        self.remove_command("help")
    
    async def load_all_cogs(self):
        await self.load_extension("cogs.ping")



async def main():
    # setup logger
    RESOURCES_FOLDER = Path("app/.resources")
    Util.setupLogger("DiscordBot", logging.INFO)
    
    # load variables
    CONFIG_YML = Util.load_yml(RESOURCES_FOLDER / "config.yml")

    # create discordBot
    bot = MyBot(CONFIG_YML)
    # load extensions
    await bot.load_all_cogs()
    # start bot
    await bot.start(get_docker_secret("discord_token", secrets_dir=os.path.join(os.path.abspath(os.sep), "run", "secrets")))


if __name__ == "__main__":
    asyncio.run(main())
    