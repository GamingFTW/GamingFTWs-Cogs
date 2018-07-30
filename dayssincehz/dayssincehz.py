import datetime
from datetime import date
import discord
from discord.ext import commands


class DaysSinceHz:
    """Simple display of number days since the last Hanazuki episode."""

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def dayssincehz(self):
        """Display days since the last Hanzuki Episode"""

        now = datetime.datetime.now()
        today = date(now.year, now.month, now.day)

        year = now.year
        if (now.month == 7 and now.day > 13):
            year = now.year + 1

        dayssincehz = date(2017, 7, 13)

        delta = today - dayssincehz

        await self.bot.say("```" + str(delta.days) + " days since last Hanazuki Episode!```")


def setup(bot):
    bot.add_cog(DaysSinceHz(bot))