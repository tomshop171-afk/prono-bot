from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

TOKEN = "8661186235:AAFfod0HskiYZFrX4yZF34EgTBSBnC7NH_o"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("⚽ Bienvenue sur mon bot de pronostics !")

async def prono(update: Update, context: ContextTypes.DEFAULT_TYPE):
    texte = " ".join(context.args)

    if not texte:
        await update.message.reply_text("Utilisation : /prono Votre pronostic")
        return

    await update.message.reply_text(f"📢 Pronostic :\n\n{texte}")

app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("prono", prono))

app.run_polling()