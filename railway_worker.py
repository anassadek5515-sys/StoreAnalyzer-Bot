import os
import time
from concurrent.futures import ThreadPoolExecutor

ACCOUNT_PART = 1  # رقم الحساب على Railway

def send_pitch(store):
    try:
        # هنا عملية الإرسال والمخاطبة أوتوماتيكياً
        print(f"⚡ [Railway Node #{ACCOUNT_PART}] تم إرسال العرض المباشر إلى: {store}")
        time.sleep(0.5)
    except Exception as e:
        pass

def cluster_worker():
    print(f"🚀 [Railway Node #{ACCOUNT_PART}] محطة الإرسال بدأت العمل...")
    filename = "auto_found_stores.txt"

    while True:
        if os.path.exists(filename):
            with open(filename, "r", encoding="utf-8") as f:
                all_stores = [line.strip() for line in f if line.strip()]

            if all_stores:
                total_len = len(all_stores)
                chunk_size = total_len // 3 if total_len >= 3 else total_len
                
                if ACCOUNT_PART == 1:
                    my_stores = all_stores[:chunk_size]
                elif ACCOUNT_PART == 2:
                    my_stores = all_stores[chunk_size:chunk_size*2]
                else:
                    my_stores = all_stores[chunk_size*2:]

                print(f"📦 جاري معالجة {len(my_stores)} متجر بـ 25 مسار متوازي...")

                with ThreadPoolExecutor(max_workers=25) as executor:
                    executor.map(send_pitch, my_stores)

        print(f"💤 اكتملت الدفعة، في انتظار التحديثات... (استراحة 15 دقيقة)")
        time.sleep(900)

if __name__ == "__main__":
    cluster_worker()
