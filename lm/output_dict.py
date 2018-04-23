
import sys
import pickle

with open(sys.argv[1], 'r') as fin:
    vocab = pickle.load(fin)
    token2ids = vocab.token2id
    print(token2ids)