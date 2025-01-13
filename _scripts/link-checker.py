import os
from bs4 import BeautifulSoup
import requests
from urllib.parse import urlparse, urljoin

# Function to fetch all the URLs from an HTML file
def get_urls_from_html(file_path):
    urls = []
    with open(file_path, 'r', encoding='utf-8') as file:
        soup = BeautifulSoup(file, 'html.parser')
        for link in soup.find_all('a', href=True):
            href = link['href']
            if not href.startswith('mailto:') and not href.startswith('#') and is_absolute_url(href):
                urls.append(href)
    return urls

# Function to check if a URL is absolute
def is_absolute_url(url):
    parsed_url = urlparse(url)
    return bool(parsed_url.scheme)  # Check if there's a scheme like http or https

# Function to check if the URL is valid
def is_valid_url(url):
    try:
        response = requests.head(url, allow_redirects=True, timeout=5)
        return response.status_code < 400
    except requests.RequestException:
        return False

# Function to scan the static website and check for broken URLs
def find_broken_urls(directory):
    broken_urls = []
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith(".html"):
                file_path = os.path.join(root, file)
                urls = get_urls_from_html(file_path)
                for url in urls:
                    print("checking url: ", url)
                    if not is_valid_url(url):
                        broken_urls.append((file_path, url))
    return broken_urls

# Main script execution
if __name__ == "__main__":
    website_directory = '../_site'  # Update this with the path to your local website
    broken_urls = find_broken_urls(website_directory)

    if broken_urls:
        print("Broken URLs found:")
        for file_path, url in broken_urls:
            print(f"File: {file_path}, Broken URL: {url}")
    else:
        print("No broken URLs found.")
