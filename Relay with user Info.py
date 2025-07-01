async def whoami(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    await update.message.reply_text(f'Your name: {user.full_name}\nYour ID: {user.id}')

app.add_handler(CommandHandler("whoami", whoami))