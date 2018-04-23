
import pickle
import sys


from .vocab import Vocab

with open(sys.argv[1], 'r') as fin:
    vocab = pickle.load(fin)
    token2ids = vocab.token2id
    print(token2ids)