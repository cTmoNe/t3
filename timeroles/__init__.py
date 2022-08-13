from .timerole import TimeRole, log

async def setup(bot):
    bot.add_cog(TimeRole(bot))
    log.debug("Timerole loaded.")