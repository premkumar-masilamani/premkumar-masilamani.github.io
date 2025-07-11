import os
import time
import urllib.parse
from urllib.request import Request, urlopen
from urllib.error import URLError, HTTPError
from bs4 import BeautifulSoup

# Constants
USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
TIMEOUT = 10  # seconds
SPECIAL_DOMAINS = [
    "medium.com",
    "linkedin.com",
    "www.linkedin.com",
    "facebook.com",
    "twitter.com",
    "x.com",
]


def extract_urls_from_html(file_path):
    """Extract all URLs from an HTML file."""
    urls = set()
    base_url = f"file://{os.path.dirname(os.path.abspath(file_path))}/"

    try:
        with open(file_path, "r", encoding="utf-8") as file:
            soup = BeautifulSoup(file, "html.parser")

            # Process <a href="..."> links
            for link in soup.find_all("a", href=True):
                url = link.get("href")
                if url and not url.startswith(("#", "mailto:", "tel:")):
                    # Make relative URLs absolute
                    if not url.startswith(("http://", "https://")):
                        url = urllib.parse.urljoin(base_url, url)
                    urls.add(url)

            # Process <img src="..."> and other elements with src attribute
            for tag in soup.find_all(["img", "script"], src=True):
                url = tag.get("src")
                if url and not url.startswith(("#", "data:")):
                    if not url.startswith(("http://", "https://")):
                        url = urllib.parse.urljoin(base_url, url)
                    urls.add(url)

    except Exception as e:
        print(f"Error parsing {file_path}: {e}")

    return urls


def is_external_url(url):
    """Check if a URL points to an external domain."""
    parsed = urllib.parse.urlparse(url)
    return (
        parsed.scheme in ("http", "https")
        and parsed.netloc
        and not parsed.netloc.startswith(("localhost", "127.", "0.0.0.0"))
    )


def is_special_domain(url):
    """Check if URL belongs to a domain that typically blocks bots."""
    parsed = urllib.parse.urlparse(url)
    return any(domain in parsed.netloc for domain in SPECIAL_DOMAINS)


def check_url(url):
    """Check if a URL is valid and accessible."""
    if is_special_domain(url):
        print(f"Checking: {url} → Status: SPECIAL (assumed valid)")
        return True

    try:
        req = Request(url, headers={"User-Agent": USER_AGENT})
        response = urlopen(req, timeout=TIMEOUT)
        status_code = response.getcode()
        print(f"Checking: {url} → Status: {status_code}")
        return True
    except HTTPError as e:
        print(f"Checking: {url} → Status: {e.code}")
        return False
    except URLError as e:
        print(f"Checking: {url} → Error: {e.reason}")
        return False
    except Exception as e:
        print(f"Checking: {url} → Error: {str(e)}")
        return False


def find_broken_links(directory):
    """Scan HTML files and check external links."""
    start_time = time.time()
    broken_links = []
    all_urls = {}  # file_path -> set of urls
    checked_urls = {}  # url -> is_valid

    # Step 1: Collect all URLs from HTML files
    print(f"Scanning files in {directory}...")
    html_files = []
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith((".html", ".htm")):
                html_files.append(os.path.join(root, file))

    print(f"Found {len(html_files)} HTML files")

    # Step 2: Extract URLs from HTML files
    for file_path in html_files:
        urls = extract_urls_from_html(file_path)
        all_urls[file_path] = urls

    # Count external URLs
    external_urls = set()
    for urls in all_urls.values():
        for url in urls:
            if is_external_url(url):
                external_urls.add(url)

    print(f"Found {len(external_urls)} unique external URLs to check")

    # Step 3: Check each external URL
    print("\nChecking external URLs...")
    for url in external_urls:
        # Skip if already checked
        if url in checked_urls:
            continue

        # Check URL and store result
        is_valid = check_url(url)
        checked_urls[url] = is_valid

        # Add to broken links if invalid
        if not is_valid:
            for file_path, urls in all_urls.items():
                if url in urls:
                    broken_links.append((file_path, url))

    # Step 4: Report results
    print("\nLink Checker Summary:")
    print(f"Total files scanned: {len(html_files)}")
    print(f"Total unique URLs checked: {len(checked_urls)}")
    print(f"Total broken links found: {len(broken_links)}")
    print(f"Time taken: {time.time() - start_time:.2f} seconds")

    # Report broken links
    if broken_links:
        print("\nBroken URLs found:")

        # Group by file
        broken_by_file = {}
        for file_path, url in broken_links:
            if file_path not in broken_by_file:
                broken_by_file[file_path] = []
            broken_by_file[file_path].append(url)

        for file_path, urls in broken_by_file.items():
            rel_path = os.path.relpath(file_path, directory)
            print(f"File: {rel_path}")
            for url in urls:
                print(f"  - {url}")
    else:
        print("\nNo broken URLs found!")

    return broken_links


if __name__ == "__main__":
    try:
        # Default to _site directory or allow command line argument
        import sys

        website_directory = os.path.abspath(
            os.path.join(os.path.dirname(__file__), "..", "_site")
        )

        if len(sys.argv) > 1:
            website_directory = sys.argv[1]

        if not os.path.exists(website_directory):
            print(f"Error: Directory {website_directory} does not exist!")
            sys.exit(1)

        # Run the link checker
        broken_links = find_broken_links(website_directory)

    except KeyboardInterrupt:
        print("\nLink checking interrupted by user.")
        sys.exit(130)
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)
