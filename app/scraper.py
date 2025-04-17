import requests
from bs4 import BeautifulSoup

headers = {
 "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36"
}
       
        
class ScrapeTextFromURL():
    def __init__(self, url):
        """ Fetch and extraxs readable text content from a webpage.

        Args:
            url (str): http addres of the url
        """
        self.url = url
        try:
            response= requests.get(self.url, headers=headers)
            response.raise_for_status()
            
        except requests.RequestException as e:
            raise Exception(f"Failed to fetch the URL: {e}")
        
        soup = BeautifulSoup(response, 'html.parser')
        self.title= soup.title.string if soup.title else "No Title Found"
        for tag in soup(["script", "style", "noscript", "header", "footer", "aside", "nav", "img"]):
            tag.decompose()
            
        text = soup.body.get_text(separator="\n", strip=True)
        self.text = text[:5000]
        
