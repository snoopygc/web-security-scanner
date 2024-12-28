import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

def crawl(url):
    visited = set()
    to_visit = [url]

    while to_visit:
        current_url = to_visit.pop()
        if current_url not in visited:
            visited.add(current_url)
            try:
                response = requests.get(current_url)
                soup = BeautifulSoup(response.text, 'html.parser')
                for link in soup.find_all('a', href=True):
                    full_url = urljoin(current_url, link['href'])
                    if full_url.startswith(url):  # Crawl within the same domain
                        to_visit.append(full_url)
            except Exception as e:
                print(f"Error crawling {current_url}: {e}")

    return visited
