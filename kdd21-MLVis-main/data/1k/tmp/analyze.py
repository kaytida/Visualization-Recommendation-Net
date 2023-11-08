# load wide-and-deep-used_variable_config_mapping_list.pkl

import pickle
import pandas as pd
import numpy as np
import random

# with open('wide-and-deep-used_variable_config_mapping_list.pkl', 'rb') as f:
#     a = pickle.load(f)
#     xsrc  =[]
#     ysrc = []
#     configs = []
#     x = []
#     for i in range(len(a)):
#         # make a[i][-1] into a list of tuples
#         # print(list(a[i][-1]))

#         # tracerse through the list(a[i][-1] and make list of tuples based on '(' and ')'
#         x = a[i][-1]
#         # remove '[' and ']'
#         x = x.replace('[', '')
#         x = x.split('),')
#         x = [i.replace('(','') for i in x]
#         x = [i.replace(')','') for i in x]
#         x = [i.replace(' ','') for i in x]
#         x = [i.replace("'","") for i in x]
#         x = [i.replace(']','') for i in x]
#         x = [i.split(',') for i in x]
#         x = [(i[0],i[1]) for i in x]
#         # replace '"' with ''

#         xsrc.append(x)
        

#     # make it one dimensional
#     #xsrc = [item for sublist in xsrc for item in sublist] 
#     # print(xsrc)

#     configs = []
#     for item in xsrc:
#         # empty dictionary
#         #print(item)
#         d = {}
#         for tup in item:
#             d[tup[0]] = tup[1]
#         configs.append(d)

# # print(type(configs))
# # print(len(configs))
# # print(type(configs[0]))
# # print the unique dictionaries of the list
# # configs = (set(tuple(sorted(d.items())) for d in configs))
# print(type(configs))
# print(len(configs))
# # print(type(configs[-1]))
# for i in configs:
#     print(type(i)     )
#     break

# list_unique_configs = []
# for i in configs:
#     if i not in list_unique_configs:
#         list_unique_configs.append(i)

# print(len(list_unique_configs))
# print(type(list_unique_configs))
# print(type(list_unique_configs[0]))

# # save to the pickle file
# with open('configs_space.pkl', 'wb') as f:
#     pickle.dump(list_unique_configs, f)

# # load the pickle file
# with open('configs_space.pkl', 'rb') as f:
#     configs_space = pickle.load(f)

#     print(type(configs_space))
#     print(len(configs_space))
#     print((configs_space[34]))



# # load meta_variable_mapping.pkl
# with open('meta_variable_mapping.pkl', 'rb') as f:
#     a = pickle.load(f)

#     print(type(a))
#     print(len(a))
#     # print(a[0])
#     # print(a[0][0])
#     # print(len(a[0]))
#     keys = list(a.keys())
#     values = list(a.values())
#     print(keys[random.randint(0,len(keys))] ,":" ,np.std(values[random.randint(0,len(keys))]))

# with open('wide-and-deep-dataset2config.pkl', 'rb') as f:
#     f = pickle.load(f)

#     print(type(f))
#     print(len(f))
#     print(f['bpatoutset:570.csv'])

# with open('wide-and-deep-used_variable_config_mapping_list.pkl', 'rb') as f:
#     f = pickle.load(f)

#     print(type(f[0]))
#     # print(len(f[0][3]))
#     # print(f[4533])
#     a = list(f[0])
#     print(len(a))
#     a.append("1")
#     print(len(a))
#     print(a)
    # print(list(f[0][3]))
    # x = f[0][3]
    # x = x.replace('[', '')
    # x = x.split('),')
    # x = [i.replace('(','') for i in x]
    # x = [i.replace(')','') for i in x]
    # x = [i.replace(' ','') for i in x]
    # x = [i.replace("'","") for i in x]
    # x = [i.replace(']','') for i in x]
    # x = [i.split(',') for i in x]
    # x = [(i[0],i[1]) for i in x]
# # replace '"' with ''
#     print(x)
# with open('wide-and-deep-config2id.pkl','rb') as f:
#     f = pickle.load(f)

#     print(type(f))
#     b =((list(f.keys())[9]))
#     print(f[str(b)])



    

# with open('wide-and-deep-variable2id.pkl', 'rb') as f:
#     f = pickle.load(f)

# print(type(f))
# print(len(f))
# d = random.randint(0,len(f))
# print(list(f.keys())[d])
# print(list(f.values())[d])
