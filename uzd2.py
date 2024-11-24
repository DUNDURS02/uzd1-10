#created by Mucenieks

import langid
import sys

sys.stdout.reconfigure(encoding='utf-8')

texts = [
    "Šodien ir saulaina diena.",
    "Today is a sunny day."
]

languages = {text: langid.classify(text)[0] for text in texts}
print(languages)