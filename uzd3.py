#created by Mucenieks

import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

text1 = "Rudens lapas ir dzeltenas un oranžas. Lapas klāj zemi un padara to krāsainu."
text2 = "Krāsainas rudens lapas krīt zemē. Lapas ir oranžas un dzeltenas."

words1 = set(re.findall(r'\b\w+\b', text1.lower()))
words2 = set(re.findall(r'\b\w+\b', text2.lower()))

common_words = words1 & words2
similarity = len(common_words) / len(words1 | words2) * 100

print(f"Sakritība: {common_words}")
print(f"Sakritības līmenis: {similarity:.2f}%")
