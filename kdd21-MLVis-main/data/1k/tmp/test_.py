import pickle
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


with open('wide-and-deep-used_variable_config_mapping_list.pkl', 'rb') as f:
    f = pickle.load(f)
# with open('wide-and-deep-dataset2config.pkl','rb') as f:
    # f = pickle.load(f)

print(type(f))
print(len(f))
print((list(f))[0])