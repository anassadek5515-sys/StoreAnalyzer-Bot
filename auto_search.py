import os
import requests

# الكلمات المفتاحية للبحث
SEARCH_QUERIES = [
    "online store",
    "ecommerce shop",
    "متجر إلكتروني تسوق"
]

def search_via_api():
    print("🚀 بدأ البوت بالبحث عبر محرك الويب المباشر...")
    discovered_stores = set()
    filename = "auto_found_stores.txt"
    
    # قراءة المواقع القديمة
    if os.path.exists(filename):
        with open(filename, "r", encoding="utf-8") as f:
            for line in f:
                discovered_stores.add(line.strip())

    for query in SEARCH_QUERIES:
        print(f"🔍 جاري البحث عن: [{query}]")
        try:
            # استخدام API بحث عام ومجاني وسريع
            url = f"https://html.duckduckgo.com/html/?q={query}"
            headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}
            response = requests.post(url, data={"q": query}, headers=headers, timeout=10)
            
            if response.status_code == 200:
                from bs4 import BeautifulSoup
                soup = BeautifulSoup(response.text, 'html.parser')
                links = soup.find_all('a', class_='result__url')
                
                count = 0
                for link in links:
                    href = link.get('href')
                    if href and "http" in href:
                        discovered_stores.add(href)
                        count += 1
                        if count >= 10:  # جلب أول 10 روابط لكل كلمة
                            break
                print(f"   [+] تم العثور على نتائج لهذه الكلمة.")
            else:
                print(f"   [-] فشل الاتصال بمحرك البحث.")
        except Exception as e:
            print(f"   [!] حدث خطأ: {e}")

    # حفظ النتائج
    with open(filename, "w", encoding="utf-8") as f:
        for store in discovered_stores:
            f.write(store + "\n")

    print(f"💾 تم تحديث وحفظ المتاجر! الإجمالي الحالي: {len(discovered_stores)}")

if __name__ == "__main__":
    search_via_api()
