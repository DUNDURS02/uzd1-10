#created by Mucenieks

from textblob import TextBlob
import sys

sys.stdout.reconfigure(encoding='utf-8')

sentences = [
    "Šis produkts ir lielisks, esmu ļoti apmierināts!",
    "Esmu vīlies, produkts neatbilst aprakstam.",
    "Neitrāls produkts, nekas īpašs."
]

def analyze_sentiment(sentence):
    polarity = TextBlob(sentence).sentiment.polarity
    if polarity > 0:
        return "Pozitīvs"
    elif polarity < 0:
        return "Negatīvs"
    else:
        return "Neitrāls"

sentiments = {sentence: analyze_sentiment(sentence) for sentence in sentences}

print(sentiments)
