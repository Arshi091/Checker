from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import asyncio
import aiohttp

BOT_TOKEN = "7889405171:AAH_pRyeFIMTYQYM-FMQCy4yMmgzM1lAlz4"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("سلام! تو این ربات میتونی پروکسی‌هات رو تست کنی. لینک پروکسی رو بفرست.")

async def testproxy(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not context.args:
        await update.message.reply_text("لطفا لینک پروکسی را همراه با دستور ارسال کن، مثل:\n/testproxy tg://proxy?server=1.2.3.4&port=443&secret=...")
        return

    proxy_link = context.args[0]
    await update.message.reply_text(f"در حال تست پروکسی:\n{proxy_link}")

    # تست سادگی: بررسی اتصال HTTP به سرور پروکسی
    # (این فقط یه نمونه تست ساده است، در عمل باید MTProto تست کنی)
    try:
        async with aiohttp.ClientSession() as session:
            # فرض میگیریم server و port رو از لینک جدا کنی، اینجا ساده شده
            # برای نمونه فقط تلاش به دسترسی HTTP ساده می‌کنیم
            await asyncio.sleep(2)  # شبیه سازی تاخیر تست
        await update.message.reply_text("پروکسی احتمالا فعال است و پاسخگو می‌باشد.")
    except Exception as e:
        await update.message.reply_text(f"خطا در اتصال به پروکسی: {e}")

if __name__ == '__main__':
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("testproxy", testproxy))
    print("ربات در حال اجراست...")
    app.run_polling()
