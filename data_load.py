import pickle
import random
# import test_train_split
from sklearn.model_selection import train_test_split

with open('all_data.pkl', 'rb') as f:
    all_data = pickle.load(f)



# shuffle the data
random.shuffle(all_data)
# split the data into train and test
train_data, test_data = train_test_split(all_data, test_size=0.2)

