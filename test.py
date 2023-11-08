import numpy as np
import pickle
import random
import torch
from sklearn.model_selection import train_test_split

with open('all_data.pkl', 'rb') as f:
    all_data = pickle.load(f)



# shuffle the data
random.shuffle(all_data)
# split the data into train and test
train_data, test_data = train_test_split(all_data, test_size=0.2)


# # feature extraction
# def get_sparse_features(feature,n):
#     # normalize the feature to [0,1], by substracting mean and dividing by std
#     feature = np.array(feature)
    
#     # subtract minimum and divide by range
#     feature = (feature - np.min(feature)) / (np.max(feature) - np.min(feature))

#     # divide the range[0,1] into n bins
#     bins = np.linspace(0,1,n+1)
#     print(bins)

#     # # get the index of the bin that each feature belongs to
#     feature = np.digitize(feature,bins)
#     print(feature)
#     # # convert the index to a sparse feature
#     feature = np.eye(n+2)[feature]
#     return feature
    

# a = [1,2,3,4,5,6]
# print((a - np.mean(a))/np.std(a))
# f = get_sparse_features(a,3)
# print((f)) 
# training the model
# some encodings

with open('./kdd21-MLVis-main/data/1k/tmp/meta_variable_mapping.pkl', 'rb') as f:
    meta_variable_mapping = pickle.load(f)

with open('./kdd21-MLVis-main/data/1k/tmp/wide-and-deep-config2id.pkl','rb') as f:
    config2id = pickle.load(f)

# one_hot_encoding of 60 numerical features
one_hot_c = np.eye(60)
# print(config2id.values())

def get_dense_x(data):

    if(len(data) == 5):
        var1 = data[1]
        var2 = data[2]
    if(len(data) == 4):
        var1 = data[1]
    
    d1 = meta_variable_mapping[var1]
    if(len(data) == 5):
        d2 = meta_variable_mapping[var2]
        dx = np.concatenate((d1,d2))
    else:
        dx = d1
    
    # concatenate d1 and d2 to get dx
    # dx = torch.cat((d1,d2),1)

    return dx

def get_sparse_c(data):
    config_id = config2id[data[-2]]
    # get the one hot encoding of the config id
    sc = one_hot_c[config_id]

    return sc


data = ['knutfh:202.csv', 'knutfh:202.csv_2c8849', 'knutfh:202.csv_4984f7', "[('color', 'default'), ('size', 'default'), ('type', 'bar'), ('xsrc', 'quantitative'), ('ysrc', 'quantitative')]", '0']
data = train_data[0]
print(len(data))
dx = get_dense_x(data)
sc = get_sparse_c(data)

print(dx.shape)
print(sc.shape)