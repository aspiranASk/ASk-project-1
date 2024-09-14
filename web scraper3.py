import urllib.request
from bs4 import BeautifulSoup
import ssl
import re

# Create an SSL context to handle HTTPS requests
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


# Function to add custom User-Agent header
def fetch_url(url):
    # Create a request object with a custom User-Agent header
    request = urllib.request.Request(url, headers={
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    })

    # Open the URL and read the response
    with urllib.request.urlopen(request, context=ctx) as response:
        return response.read()


# Get the URL from the user
url = input("Enter the URL: ")

try:
    # Fetch the URL content
    html = fetch_url(url)
    soup = BeautifulSoup(html, 'html.parser')

    # Find all anchor tags
    tags = soup.find_all('a', href=True)

    # Regular expression pattern to find DOI links
    doi_pattern = re.compile(r'https://doi\.org/([^"\s]+)')

    # Search for DOI links and print them
    for tag in tags:
        href = tag.get('href')
        if doi_pattern.match(href):
            print(href)

except urllib.error.HTTPError as e:
    print(f"HTTP error: {e.code}")
except urllib.error.URLError as e:
    print(f"URL error: {e.reason}")
except Exception as e:
    print(f"An error occurred: {e}")

    print(f"URL error: {e.reason}")
except Exception as e:
    print(f"An error occurred: {e}")
