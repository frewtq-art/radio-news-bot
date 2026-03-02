import os 
TOKEN = os.getenv("8782328242:AAH5gW4CuLhsUdTb4Bmaq7568nTKZdcaMgw")
import requests
import feedparser
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

TOKEN = os.environ.get("8782328242:AAH5gW4CuLhsUdTb4Bmaq7568nTKZdcaMgw")

RSS_FEEDS = {
    "argentina": "https://eleconomista.com.ar/ultimas-noticias/feed/",
    "RadioFarda": "https://www.en.radiofarda.com/rssfeeds",
    "Mehr News" : "http://www.mehrnews.com/rss"
}

def get_news(feed_url):
    feed = feedparser.parse(feed_url)
    news_text = ""
    for entry in feed.entries[:5]:
        news_text += f"• {entry.title}\n"
    return news_text

async def news(update: Update, context: ContextTypes.DEFAULT_TYPE):
    argentina_news = get_news(RSS_FEEDS["argentina"])
    iran_news = get_news(RSS_FEEDS["Iran"])

    message = f"🇦🇷 Новости Аргентины:\n{argentina_news}\n\n🇲🇽 Новости ирана:\n{iran_news}"
    await update.message.reply_text(message)

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("news", news))

app.run_polling()
