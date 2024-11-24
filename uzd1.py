#created by Mucenieks

from collections import Counter
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

text = "Mākoņainā dienā kaķis sēdēja uz palodzes. Kaķis domāja, kāpēc debesis ir pelēkas. Kaķis gribēja redzēt sauli, bet saule slēpās aiz mākoņiem."

words = re.findall(r'\b\w+\b', text.lower())
word_frequency = Counter(words)

print(word_frequency)
