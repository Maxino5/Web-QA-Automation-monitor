import requests
from bs4 import BeautifulSoup

def check_website(url):
    print(f"--- Checking: {url} ---")
    
    try:
        # 1. Check if the main site is up
        response = requests.get(url, timeout=10)
        if response.status_code == 200:
            print(f"✅ Main Site Status: Online (200)")
        else:
            print(f"❌ Main Site Status: Error ({response.status_code})")
            return

        # 2. Find all links on the page
        soup = BeautifulSoup(response.text, 'html.parser')
        links = soup.find_all('a')
        print(f"🔎 Found {len(links)} links. Checking for broken ones...")

        for link in links:
            href = link.get('href')
            # Only check full web links (starting with http)
            if href and href.startswith('http'):
                try:
                    link_check = requests.head(href, timeout=5)
                    if link_check.status_code == 404:
                        print(f"🚨 BROKEN LINK FOUND: {href}")
                except:
                    pass # Skip links that timeout or error out

        print("--- Check Complete ---")

    except Exception as e:
        print(f"⚠️ Error connecting to site: {e}")

# Test it on a site (You can change this URL)
check_website("https://www.google.com")