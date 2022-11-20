import binascii
from PIL import Image
import numpy as np
import scipy
import scipy.misc
import scipy.cluster
import discord
NUM_CLUSTERS = 5

def get_color(pic_path):
    im = Image.open(pic_path)
    im = im.resize((150, 150))      
    ar = np.asarray(im)
    shape = ar.shape
    ar = ar.reshape(scipy.product(shape[:2]), shape[2]).astype(float)


    codes, dist = scipy.cluster.vq.kmeans(ar, NUM_CLUSTERS)


    vecs, dist = scipy.cluster.vq.vq(ar, codes)         
    counts, bins = scipy.histogram(vecs, len(codes))    

    index_max = scipy.argmax(counts)                    
    peak = codes[index_max]
    color = binascii.hexlify(bytearray(int(c) for c in peak)).decode('ascii')
    col = discord.Color(value=int(color, 16))
    return col

# for paste
import postbin
def mainSync(): 
    url = postbin.postSync(f"FooBar Bazz 2")
    print(f"Your paste is located at {url}")

