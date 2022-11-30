from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import datetime
from spy import*
from emoji import emojize

async def hi_command(update, context) :
    log(update,context)
    await update.message.reply_text(f'Hi {update.effective_user.first_name} 🤩 ')

async def help_command(update, context) :
    log(update,context)
    await update.message.reply_text(f'📣\n/hi\n/date\n/time\n/help')    

async def date_command(update, context) :
    log(update,context)
    await update.message.reply_text(f'📅{datetime.datetime.now().date()} ')

async def time_command(update, context) :
    log(update,context)
    await update.message.reply_text(f'🕰️{datetime.datetime.now().time()} ')

async def sum_command(update, context) :
    log(update,context)
    msg=update.message.text
    print(msg)
    items=msg.split()
    x=int(items[1])
    y=int(items[2])

    await update.message.reply_text(f'{x}+{y}={x+y}')    

async def div_command(update, context):
    log(update, context)
    msg = update.message.text
    print(msg)
    items = msg.split()
    x = int(items[1])
    y = int(items[2])
    z = x / y
    await update.message.reply_text(f'{x} / {y} = {z}')

async def sub_command(update, context):
    log(update, context)
    msg = update.message.text
    print(msg)
    items = msg.split()
    x = int(items[1])
    y = int(items[2])
    z = x - y
    await update.message.reply_text(f'{x} - {y} = {z}')

async def mult_command(update, context):
    log(update, context)
    msg = update.message.text
    print(msg)
    items = msg.split()
    x = int(items[1])
    y = int(items[2])
    z = x * y
    await update.message.reply_text(f'{x} * {y} = {z}')    

