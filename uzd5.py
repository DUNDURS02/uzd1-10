#created by Mucenieks

import re
import sys

sys.stdout.reconfigure(encoding='utf-8')


raw_text = "@John: Šis ir lielisks produkts!!! Vai ne? 👏👏👏 http://example.com"


author_match = re.search(r'@\w+', raw_text)
author = author_match.group() if author_match else ""


clean_text = re.sub(r'http\S+', '', raw_text)
clean_text = re.sub(r'[^\w\s@!?]', '', clean_text)
clean_text = re.sub(r'!+', '!', clean_text)

if author:
    clean_text = re.sub(rf'{author}:?', '', clean_text).strip()

clean_text = re.sub(r'\s+', ' ', clean_text).strip()

clean_text = f"{author}: {clean_text}"

print(clean_text)

