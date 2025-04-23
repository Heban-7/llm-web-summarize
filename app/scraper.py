import requests
from bs4 import BeautifulSoup

headers = {
 "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36"
}
       
        

def scrape_texr_from_url(url):
    """ Fetch and extraxs readable text content from a webpage.

    Args:
        url (str): http addres of the url
    """
    try:
        response= requests.get(url, headers=headers)
        response.raise_for_status()
        
    except requests.RequestException as e:
        raise Exception(f"Failed to fetch the URL: {e}")
        
    soup = BeautifulSoup(response, 'html.parser')
    title= soup.title.string if soup.title else "No Title Found"
    for tag in soup(["script", "style", "noscript", "header", "footer", "aside", "nav", "img"]):
        tag.decompose()
            
    text = soup.body.get_text(separator="\n", strip=True)
    return title, text

        
class Website:

    def __init__(self, url):
        """ Fetch and extraxs readable text content from a webpage.

        Args:
            url (str): http addres of the url
        """
        self.url = url
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.content, 'html.parser')
        self.title = soup.title.string if soup.title else "No title found"
        for irrelevant in soup.body(["script", "style", "img", "input", "noscript", "aside", "nav",]):
            irrelevant.decompose()
        self.text = soup.body.get_text(separator="\n", strip=True)
        
    def display_webpage(self):
        print(self.title)
        print("=============================")
        print(self.text)