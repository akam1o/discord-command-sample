from discord.ext import commands
from os import getenv
import traceback
import subprocess

bot = commands.Bot(command_prefix='/')

def res_cmd(cmd, check=False):
    return subprocess.run(
        cmd, stdout=subprocess.PIPE,
        check=check, shell=True, text=True).stdout

def _cmd(*args):
    cmd = ' '.join(args)
    return res_cmd(cmd)

@bot.event
async def on_command_error(ctx, error):
    orig_error = getattr(error, "original", error)
    error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
    await ctx.send(error_msg)

@bot.command()
async def cmd(ctx, *args):
    res = _cmd(args)
    await ctx.send(res)

token = getenv('DISCORD_BOT_TOKEN')
bot.run(token)
