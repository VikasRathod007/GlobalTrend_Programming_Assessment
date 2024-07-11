import requests
from time import sleep


def download_urls(urls, max_retries=3, delay=2):
    results = []

    for url in urls:
        attempts = 0
        success = False
        while attempts < max_retries and not success:
            try:
                response = requests.get(url)
                response.raise_for_status()
                results.append((url, response.content))
                success = True
            except requests.exceptions.RequestException as e:
                print(f"Error downloading {url}: {e}")
                attempts += 1
                if attempts < max_retries:
                    print(f"Retrying in {delay} seconds...")
                    sleep(delay)
                else:
                    print(f"Failed to download {url} after {max_retries} attempts")
                    results.append((url, None))

    return results


urls = [
    "https://www.example.com",
    "https://www.nonexistenturl.xyz",
    "https://www.python.org",
]

downloaded_contents = download_urls(urls)
for url, content in downloaded_contents:
    if content:
        print(f"Successfully downloaded content from {url}")
    else:
        print(f"Failed to download content from {url}")
