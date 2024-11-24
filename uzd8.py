#created by Mucenieks

import stanza
from googletrans import Translator
import sys

sys.stdout.reconfigure(encoding='utf-8')

stanza.download('en')
nlp = stanza.Pipeline('en')

textlv = "Valsts prezidents Egils Levits piedalījās pasākumā, ko organizēja Latvijas Universitāte."

translator = Translator()
texteng = translator.translate(textlv, src='lv', dest='en').text

doc = nlp(texteng)

for entity in doc.entities:
    word = entity.text
    label = entity.type
    if label == "PERSON":
        label = "Persona"
    elif label == "ORG":
        label = "Organizācija"
    print(f"{word}: {label}")