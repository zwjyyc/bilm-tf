
import pickle
import sys

from vocab import Vocab

with open(sys.argv[1], 'r') as fin:
    vocab = pickle.load(fin)
    token2ids = vocab.token2id

    for token, id in token2ids.items():
        out_str = '{}\t{}'.format(token, id)
        print(out_str.encode('utf-8'))