from .dayssincehz import DaysSinceHZ

def setup(bot):
    bot.add_cog(DaysSinceHZ(bot))