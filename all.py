
#pickle
 import pickle
    inputFile = open("save1.pkl", 'rb')
    dict2 = pickle.load(inputFile)
    list2 = pickle.load(inputFile)
    inputFile.close()
    print(dict2)
    print(list2)

#tensorflow
import tensorflow as tf
sess=tf.Session() 
export_path =  './savedmodel'
meta_graph_def = tf.saved_model.loader.load(
           sess,
          [tf.saved_model.tag_constants.SERVING],
          export_path)

import torch
#saving tensor in pytorch
a = torch.randn(10)
torch.save('a.t7', a)
# loding the model
from torch.utils.serialization import load_lua
a = load_lua('a.t7')

#torch loading the model
obj = torch.load('test.dat')
print(obj)