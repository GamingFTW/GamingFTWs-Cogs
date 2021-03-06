import datetime
from datetime import date
import discord
from redbot.core import commands


class DaysSinceHZ(commands.Cog):
    """Simple display of the number days and seconds since the last official Hanazuki episode."""

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def dayssincehz(self, ctx):
        """Display the date and time between now and the last Hanazuki episode."""

        now = datetime.datetime.now()

        dayssincehz = datetime.datetime.fromtimestamp(1556989200)

        delta = now - dayssincehz
        hours, remainder = divmod(delta.seconds, 3600)
        minutes, seconds = divmod(remainder, 60)

        await ctx.send("It has been {} days, {} hours, {} minutes and {} seconds since last official Hanazuki Episode!".format(delta.days, hours, minutes, seconds))