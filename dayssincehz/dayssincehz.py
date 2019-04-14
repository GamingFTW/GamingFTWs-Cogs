import datetime
from datetime import date
import discord
from discord.ext import commands


class DaysSinceHz:
    """Simple display of number days and seconds since the last official Hanazuki episode."""

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def dayssincehz(self):
        """Display days and seconds since the last official Hanzuki Episode"""

        now = datetime.datetime.now()

        dayssincehz = datetime.datetime.fromtimestamp(1555174800)

        delta = now - dayssincehz
        hours, remainder = divmod(delta.seconds, 3600)
        minutes, seconds = divmod(remainder, 60)

        await self.bot.say("```It has been " + str(delta.days) + " days " + str(hours) + " hours " + str(minutes) + " minutes and " + str(seconds) + " seconds since last official Hanazuki Episode!```")

def setup(bot):
    bot.add_cog(DaysSinceHz(bot))
