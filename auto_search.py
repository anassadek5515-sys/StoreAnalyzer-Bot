import os
from duckduckgo_search import DDGS

# الكلمات المفتاحية العالمية والعربية للبحث السريع
SEARCH_QUERIES = [
    "online store",
    "ecommerce shop",
    "متجر إلكتروني تسوق",
]

def fast_autonomous_search():
    print("🚀 بدأ البوت السريع بالبحث الفوري...")
    
    discovered_stores = set()
    filename = "auto_found_stores.txt"
    
    # قراءة المواقع القديمة لو موجودة
    if os.path.exists(filename):
        with open(filename, "r", encoding="utf-8") as f:
            for line in f:
                discovered_stores.add(line.strip())

    # البحث باستخدام المكتبة
    try:
        with DDGS() as ddgs:
            for query in SEARCH_QUERIES:
                print(f"🔍 جاري البحث عن: [{query}]")
                results = ddgs.text(query, max_results=10)
                if results:
                    for r in results:
                        url = r.get("href")
                        if url and url not in discovered_stores:
                            discovered_stores.add(url)
                            print(f"   [+] تم العثور على: {url}")
                else:
                    print(f"   [-] لم تُرجع نتائج لهذه الكلمة.")
    except Exception as e:
        print(f"   [!] حدث خطأ عام أثناء البحث: {e}")

    # حفظ النتائج في الملف
    with open(filename, "w", encoding="utf-8") as f:
        for store in discovered_stores:
            f.write(store + "\n")

    print(f"💾 تم التحديث وحفظ المتاجر! الإجمالي الحالي: {len(discovered_stores)}")

if __name__ == "__main__":
    fast_autonomous_search()
