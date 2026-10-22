import os
from duckduckgo_search import DDGS

# الكلمات المفتاحية المركزة للبحث السريع
SEARCH_QUERIES = [
    "متاجر إلكترونية تسوق online store",
    "متجر شوبيفاي عربي تسوق",
]

def fast_autonomous_search():
    print("🚀 بدأ البوت السريع بالبحث الفوري...")
    
    discovered_stores = set()
    filename = "auto_found_stores.txt"
    
    if os.path.exists(filename):
        with open(filename, "r", encoding="utf-8") as f:
            for line in f:
                discovered_stores.add(line.strip())

    # البحث السريع بدون فترات انتظار طويلة
    with DDGS() as ddgs:
        for query in SEARCH_QUERIES:
            print(f"🔍 جاري البحث: [{query}]")
            try:
                results = ddgs.text(query, max_results=10)
                for r in results:
                    url = r.get("href")
                    if url and url not in discovered_stores:
                        discovered_stores.add(url)
                        print(f"   [+] تم العثور على: {url}")
            except Exception as e:
                print(f"   [!] خطأ: {e}")

    # حفظ النتائج فوراً
    with open(filename, "w", encoding="utf-8") as f:
        for store in discovered_stores:
            f.write(store + "\n")

    print(f"💾 تم التحديث وحفظ المتاجر! الإجمالي الحالي: {len(discovered_stores)}")

if __name__ == "__main__":
    fast_autonomous_search()
