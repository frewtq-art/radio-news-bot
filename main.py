import os
import requests
import feedparser
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

TOKEN = os.environ.get("BOT_TOKEN")

RSS_FEEDS = {
    "argentina": "https://eleconomista.com.ar/ultimas-noticias/feed/",
    "mexico": "https://www.eluniversal.com.mx/rss/portada.xml"
}

def get_news(feed_url):
    feed = feedparser.parse(feed_url)
    news_text = ""
    for entry in feed.entries[:5]:
        news_text += f"• {entry.title}\n"
    return news_text

async def news(update: Update, context: ContextTypes.DEFAULT_TYPE):
    argentina_news = get_news(RSS_FEEDS["argentina"])
    mexico_news = get_news(RSS_FEEDS["mexico"])

    message = f"🇦🇷 Новости Аргентины:\n{argentina_news}\n\n🇲🇽 Новости Мексики:\n{mexico_news}"
    await update.message.reply_text(message)

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("news", news))

app.run_polling()
