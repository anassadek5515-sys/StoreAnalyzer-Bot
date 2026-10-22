import os
import time
from duckduckgo_search import DDGS

# الكلمات المفتاحية اللي البوت هيدور بيها لوحده في الإنترنت عن المتاجر والشركات
SEARCH_QUERIES = [
    "متاجر إلكترونية تسوق online store",
    "متجر شوبيفاي عربي تسوق",
    "ecommerce stores online shopping arabic",
]

def autonomous_store_search():
    print("🚀 بدأ البوت الآلي بالسحاب بالبحث التلقائي عن المتاجر...")
    
    # تحميل المتاجر القديمة لو موجودة عشان ميكررهاش
    discovered_stores = set()
    filename = "auto_found_stores.txt"
    
    if os.path.exists(filename):
        with open(filename, "r", encoding="utf-8") as f:
            for line in f:
                discovered_stores.add(line.strip())

    initial_count = len(discovered_stores)

    # البحث التلقائي لكل كلمة مفتاحية
    with DDGS() as ddgs:
        for query in SEARCH_QUERIES:
            print(f"\n🔍 جاري البحث أوتوماتيكياً عن: [{query}]")
            try:
                results = ddgs.text(query, max_results=15)
                for r in results:
                    url = r.get("href")
                    title = r.get("title")
                    if url and url not in discovered_stores:
                        discovered_stores.add(url)
                        print(f"   [+] تم العثور على متجر جديد: {title} --> {url}")
                time.sleep(3)
            except Exception as e:
                print(f"   [!] حدث خطأ أثناء البحث عن '{query}': {e}")

    print(f"\n--- 📊 ملخص البحث السحابي ---")
    print(f"إجمالي المتاجر المخزنة حالياً: {len(discovered_stores)}")

    # حفظ القائمة المحدثة بالكامل في الملف
    with open(filename, "w", encoding="utf-8") as f:
        for store in discovered_stores:
            f.write(store + "\n")

    print(f"💾 تم تحديث وحفظ الملف '{filename}' بنجاح في المستودع السحابي.")

if __name__ == "__main__":
    autonomous_store_search()
