import urllib.request
from bs4 import BeautifulSoup
from datetime import datetime
import re


class Scraper:
    def __init__(self, site):
        self.site = site

    def scrape(self):
        # Get today's date in 'YYYY-MM-DD' format
        today_date = datetime.today().strftime('%Y-%m-%d')
        print(f"Fetching news for {today_date}")

        # Open the website and read HTML
        r = urllib.request.urlopen(self.site)
        html = r.read()
        parser = "html.parser"
        sp = BeautifulSoup(html, parser)

        # Initialize an empty list to store the news items
        news_items = []

        # Loop through all anchor tags to find news links
        for tag in sp.find_all("a"):
            url = tag.get("href")
            if url is None:
                continue

            # Check if the link contains 'articles' (assuming the news URL contains this word)
            if "articles" in url:
                # You can modify this regex or logic to match the date format
                date_match = re.search(r"\d{4}-\d{2}-\d{2}", url)
                if date_match:
                    news_date = date_match.group(0)
                    # Only store links that match today's date
                    if news_date == today_date:
                        news_items.append((url, news_date))

        # Sort the news items by date (in reverse order for most recent first)
        news_items.sort(key=lambda x: x[1], reverse=True)

        # Display the links to the user
        if not news_items:
            print("No news found for today.")
        else:
            for idx, (url, date) in enumerate(news_items, 1):
                print(f"{idx}. {url} (Date: {date})")



# Example: Modify the URL based on your news source
news_url = "https://timesofindia.indiatimes.com/"
Scraper(news_url).scrape()
