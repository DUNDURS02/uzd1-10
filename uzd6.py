#created by K.Mucenieks DT4-1

from nltk.tokenize import sent_tokenize
import nltk
import sys


sys.stdout.reconfigure(encoding='utf-8')

nltk.download('punkt')

text = """
Latvija ir valsts Baltijas reģionā. Tās galvaspilsēta ir Rīga, kas ir slavena ar savu vēsturisko centru un skaistajām ēkām. Latvija robežojas ar Lietuvu, Igauniju un Krieviju, kā arī tai ir piekļuve Baltijas jūrai. Tā ir viena no Eiropas Savienības dalībvalstīm.
"""

sentences = sent_tokenize(text)

summary = []
for sentence in sentences:
    if "galvaspilsēta" in sentence or "robežojas" in sentence or "Eiropas Savienības" in sentence:
        summary.append(sentence.split(",")[0] + ".")

final_summary = " ".join(summary)

print("Kopsavilkums:")
print(final_summary)