import asyncio
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

# Your actual bot token (REGENERATE if you haven't yet)
BOT_TOKEN = "7821879456:AAHQbXRkg8JK0FmbH1cyV52BYsUx7z71aJ0"

# /start handler
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "👋 Hello! Welcome to our Investment Bot.\nType /help to see what I can do."
    )

# /help handler
async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "/start - Welcome message\n"
        "/help - List of commands\n"
        "/plans - Show available investment plans"
    )

# /plans handler
async def plans_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    plans = (
        "📈 *Our Investment Plans:*\n"
        "1. *Starter Plan* - ₦10,000 min, 30 days, 1% daily\n"
        "2. *Growth Plan* - ₦100,000 min, 60 days, 1.5% daily\n"
        "3. *Premium Plan* - ₦1,000,000 min, 90 days, 2% daily"
    )
    await update.message.reply_text(plans, parse_mode='Markdown')

# Main async setup
async def main():
    # Create application
    app = Application.builder().token(BOT_TOKEN).build()
    
    # Add command handlers
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(CommandHandler("plans", plans_command))
    
    print("✅ Bot is running...")
    
    # Start the bot
    async with app:
        await app.start()
        await app.updater.start_polling()
        await app.updater.idle()

# Entry point
if __name__ == "__main__":
    asyncio.run(main())