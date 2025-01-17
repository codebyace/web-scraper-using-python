import urllib.request
from urllib.parse import urljoin
from bs4 import BeautifulSoup
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)


class Scraper:
    def __init__(self, site, site_name):
        self.site = site
        self.site_name = site_name

    def fetch_html(self):
        """Fetches the HTML content of the page."""
        try:
            req = urllib.request.Request(self.site, headers={'User-Agent': 'Mozilla/5.0'})
            with urllib.request.urlopen(req) as response:
                html = response.read()
                return html
        except URLError as e:  # Use the explicitly imported URLError
            logging.error(f"Error fetching {self.site}: {e}")
            return None

    def scrape(self):
        """Scrapes the site for links containing 'articles' or 'news'."""
        html = self.fetch_html()
        if html is None:
            return

        soup = BeautifulSoup(html, "html.parser")
        for tag in soup.find_all("a", href=True):  # Filter out None href values
            url = tag.get("href")
            if "articles" in url or "news" in url:  # Match for both sites
                full_url = urljoin(self.site, url)
                logging.info(f"Found article URL: {full_url}")


# Websites to scrape
bbc_news = "https://www.bbc.com/"
india_times_news = "https://timesofindia.indiatimes.com/"

# Scrape BBC News
print("Fetching BBC News:")
scraper_bbc = Scraper(bbc_news, "BBC News")
scraper_bbc.scrape()

# Scrape Time of India News
print("\nFetching Time of India News:")
scraper_india = Scraper(india_times_news, "Time of India News")
scraper_india.scrape()
