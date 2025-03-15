import os
import asyncio
import httpx
from bs4 import BeautifulSoup
from urllib.parse import urlparse, urljoin

# Function to fetch all URLs from an HTML file
def get_urls_from_html(file_path):
    urls = set()  # Use a set to store unique URLs
    with open(file_path, 'r', encoding='utf-8') as file:
        soup = BeautifulSoup(file, 'html.parser')
        for link in soup.find_all('a', href=True):
            href = link['href']
            if not href.startswith('mailto:') and not href.startswith('#'):
                urls.add(href)  # Add to set to avoid duplicates
    return urls

# Function to check if a URL is external
def is_external_url(url):
    parsed_url = urlparse(url)
    return parsed_url.netloc and not parsed_url.netloc.startswith("localhost") and not parsed_url.netloc.startswith("127.")

# Asynchronous function to check if a URL is valid
async def is_valid_url(url, client, checked_urls):
    if url in checked_urls:  # Skip duplicate checks
        return True

    headers = {"User-Agent": "Mozilla/5.0"}
    try:
        response = await client.head(url, follow_redirects=True, timeout=5, headers=headers)
        if response.status_code >= 400:
            response = await client.get(url, follow_redirects=True, timeout=5, headers=headers)
        status_code = response.status_code
        is_valid = response.status_code < 400
    except (httpx.RequestError, httpx.TimeoutException):
        is_valid = False
        status_code = "ERROR"

    # Print only once per unique URL
    print(f"Checking: {url} → Status: {status_code}")

    checked_urls.add(url)  # Mark URL as checked
    return is_valid

# Function to scan HTML files and check external links
async def find_broken_urls(directory):
    broken_urls = []
    checked_urls = set()  # Ensure it's a set

    async with httpx.AsyncClient() as client:
        for root, _, files in os.walk(directory):
            for file in files:
                if file.endswith(".html"):
                    file_path = os.path.join(root, file)
                    urls = get_urls_from_html(file_path)
                    for url in urls:
                        if is_external_url(url):  # Ignore localhost
                            if not await is_valid_url(url, client, checked_urls):
                                broken_urls.append((file_path, url))

    return broken_urls

# Main script execution
if __name__ == "__main__":
    website_directory = "../_site"  # Update this to your Jekyll output directory
    broken_urls = asyncio.run(find_broken_urls(website_directory))

    if broken_urls:
        print("\nBroken URLs found:")
        for file_path, url in broken_urls:
            print(f"File: {file_path}, Broken URL: {url}")
    else:
        print("\nNo broken URLs found.")
