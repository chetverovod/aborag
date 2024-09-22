#from utilities import getconfig
import torch
from navec import Navec
from slovnet.model.emb import NavecEmbedding
import string

navec = Navec.load("emb_models/navec_hudlit_v1_12B_500K_300d_100q.tar")

def navec_embeddings(text):

    data = text 
    translator = str.maketrans(string.punctuation, ' ' * len(string.punctuation))
    data = data.translate(translator)
    translator = str.maketrans(string.whitespace, ' ' * len(string.whitespace))
    data = data.translate(translator)
    translator = str.maketrans(string.digits, ' ' * len(string.digits))
    data = data.translate(translator)

    data = data.lower()
    data = data.replace("   ", " ")
    data = data.replace("  ", " ")
    data = data.split(" ")
    data = list(filter(None, data))
    #print(f'data = {data}')
    emb = NavecEmbedding(navec)
    ids = []
    for word in data:
        if word in navec:
            ids.append(navec.vocab[word])
    in_data = torch.tensor(ids.copy())
    e = emb(in_data)
    #print(e.shape[0])
    norm = torch.sum(e, dim=0)/e.shape[0]
    res = norm.tolist()
    return {"embedding": res}