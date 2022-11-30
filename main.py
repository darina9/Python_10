from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from bot_commands import*





app = ApplicationBuilder().token("5818907334:AAHcDHiEBCVVXzT4xkCQFC1_QCcxX8WDsc0").build()

app.add_handler(CommandHandler("hi", hi_command))
app.add_handler(CommandHandler("date", date_command))
app.add_handler(CommandHandler("time", time_command))
app.add_handler(CommandHandler("help", help_command))
app.add_handler(CommandHandler("sum", sum_command))
app.add_handler(CommandHandler("sub", sub_command))
app.add_handler(CommandHandler("mult", mult_command))
app.add_handler(CommandHandler("div", div_command))

print('Старт работы')
app.run_polling()
