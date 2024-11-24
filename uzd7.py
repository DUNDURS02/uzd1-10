#created by Mucenieks

from gensim.models import KeyedVectors
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
import sys

sys.stdout.reconfigure(encoding='utf-8')

fasttext_model_path = "cc.lv.300.vec"
model = KeyedVectors.load_word2vec_format(fasttext_model_path)

words = ["māja", "dzīvoklis", "jūra"]

vectors = {}
for word in words:
    if word in model:
        vectors[word] = model[word]
    else:
        print(f"Vārds '{word}' nav atrodams modelī.")

for i, word1 in enumerate(words):
    for j, word2 in enumerate(words):
        if i < j and word1 in vectors and word2 in vectors:
            vec1 = vectors[word1].reshape(1, -1)
            vec2 = vectors[word2].reshape(1, -1)
            similarity = cosine_similarity(vec1, vec2)[0][0]
            print(f"Līdzība starp '{word1}' un '{word2}': {similarity:.4f}")
