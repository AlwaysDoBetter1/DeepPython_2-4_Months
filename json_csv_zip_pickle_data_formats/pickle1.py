'''
Implement a filter_dump() function that takes three arguments in the following order:

filename — name of the pickle file, for example, data.pkl
objects — list of arbitrary objects
typename — data type
The function should create a pickle file called filename, which contains a serialized list of only
those objects in the objects list whose type is typename.
'''

import pickle

def filter_dump(filename, objects, typename):
     with open(filename, "wb") as f:
         pickle.dump([el for el in objects if isinstance(el, typename)], f)


