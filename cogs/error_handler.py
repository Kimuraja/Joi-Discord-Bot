from discord.ext.commands import Cog, MissingRequiredArgument, CommandInvokeError, MemberNotFound, MissingPermissions


class CommandErrorHandler(Cog):
    def __init__(self, bot):
        self.bot = bot

    @Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error, MissingRequiredArgument):
            await ctx.reply('Please pass in all requirements :rolling_eyes:')
        elif isinstance(error, CommandInvokeError):
            if ctx.command.name in ['play']:
                await ctx.reply(f"You're not on a specific voice channel")
            else:
                await ctx.reply(f"Command Invoke Error: {error}")
        elif isinstance(error, MemberNotFound):
            await ctx.reply("Member not found")
        elif isinstance(error, MissingPermissions):
            if ctx.command.name in ['kick', 'ban', 'warn']:
                await ctx.reply("You don't have the required permissions to run this command.")


async def setup(bot):
    await bot.add_cog(CommandErrorHandler(bot))
