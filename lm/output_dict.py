
import pickle
import sys
import os

reload(sys)
sys.setdefaultencoding('utf8')
from vocab import Vocab

with open(sys.argv[1], 'r') as fin:
    vocab = pickle.load(fin)
    token2ids = vocab.token2id

    print(token2ids.get('<blank>'))
    print(token2ids.get('<unk>'))