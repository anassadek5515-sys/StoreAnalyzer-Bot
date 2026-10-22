import os
import requests
from bs4 import BeautifulSoup

SEARCH_QUERIES = [
    "online store shopify",
    "woocommerce store",
    "متجر إلكتروني تسوق"
]

def search_stores():
    print("🚀 [GitHub Scout] بدأ الكشاف السحابي بالبحث عن المتاجر...")
    discovered_stores = set()
    filename = "auto_found_stores.txt"
    
    if os.path.exists(filename):
        with open(filename, "r", encoding="utf-8") as f:
            for line in f:
                discovered_stores.add(line.strip())

    for query in SEARCH_QUERIES:
        try:
            url = f"https://html.duckduckgo.com/html/?q={query}"
            headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}
            response = requests.post(url, data={"q": query}, headers=headers, timeout=10)
            
            if response.status_code == 200:
                soup = BeautifulSoup(response.text, 'html.parser')
                links = soup.find_all('a', class_='result__url')
                for link in links:
                    href = link.get('href')
                    if href and "http" in href:
                        discovered_stores.add(href)
        except Exception as e:
            print(f"[!] خطأ في البحث: {e}")

    with open(filename, "w", encoding="utf-8") as f:
        for store in discovered_stores:
            f.write(store + "\n")

    print(f"💾 تم تحديث وحفظ المتاجر! الإجمالي الحالي في القاعدة: {len(discovered_stores)}")

if __name__ == "__main__":
    search_stores()
