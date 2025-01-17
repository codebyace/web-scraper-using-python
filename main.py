import urllib.request
from urllib.parse import urljoin
from bs4 import BeautifulSoup
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)


class Scraper:
    def __init__(self, site):
        self.site = site

    def fetch_html(self):
        """Fetches the HTML content of the page."""
        try:
            req = urllib.request.Request(self.site, headers={'User-Agent': 'Mozilla/5.0'})
            with urllib.request.urlopen(req) as response:
                html = response.read()
                return html
        except urllib.error.URLError as e:
            logging.error(f"Error fetching {self.site}: {e}")
            return None

    def scrape(self):
        """Scrapes the site for links containing 'articles'."""
        html = self.fetch_html()
        if html is None:
            return

        soup = BeautifulSoup(html, "html.parser")
        for tag in soup.find_all("a", href=True):  # Filter out None href values
            url = tag.get("href")
            if "articles" in url:
                # Make sure to convert relative URLs to absolute
                full_url = urljoin(self.site, url)
                logging.info(f"Found article URL: {full_url}")


# Test
news = "https://www.bbc.com/"
scraper = Scraper(news)
scraper.scrape()

