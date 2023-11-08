import pickle
import random
import numpy as np
import pandas as pd

with open('wide-and-deep-dataset2config.pkl', 'rb') as f:
    dataset2config = pickle.load(f)

with open('wide-and-deep-used_variable_config_mapping_list.pkl', 'rb') as f:
    used_variable_config_mapping_list = pickle.load(f)

with open('wide-and-deep-dataset2config.pkl','rb') as f:
    dataset2id = pickle.load(f)

with open('wide-and-deep-config2id.pkl','rb') as f:
    config2id = pickle.load(f)

datasets = list(dataset2id.keys())
configs = list(config2id.keys())
all_data = []
# print(len(configs[0]))
# print(configs[0])
# print(len(datasets))
# print(len(configs))
# x = configs[0]

def get_config(x):
    x = x.replace('[', '')
    x = x.split('),')
    x = [i.replace('(','') for i in x]
    x = [i.replace(')','') for i in x]
    x = [i.replace(' ','') for i in x]
    x = [i.replace("'","") for i in x]
    x = [i.replace(']','') for i in x]
    x = [i.split(',') for i in x]
    x = [(i[0],i[1]) for i in x]

    return x

for vis in range(len(used_variable_config_mapping_list)):
    vis_temp = list(used_variable_config_mapping_list[vis])
    vis_temp.append("1")
    all_data.append(vis_temp)

# in datasets, replace Masakazu with 'Masakazu_Nakamura:1.csv'

for i in range(len(datasets)):
    if datasets[i] == 'Masakazu':
        datasets[i] = 'Masakazu_Nakamura:1.csv'
    if datasets[i] == 'spartan':
        datasets[i] = 'spartan_hpc:61.csv'
    

# print(type(all_data[0][-1]))
first = len(all_data)
for dataset in datasets:
    
    # if dataset is one of Masakazu, SangYoung, f20, kang then skip
    if dataset in ['Masakazu', 'SangYoung', 'f20', 'kang']:
        continue

    data_path = "../dataset/" + str(dataset)
    # try:
    data = pd.read_csv(data_path,low_memory=False)
    # except:
    #     continue

    for i in range(4):
        config = random.choice(configs)
        attributes_count = 0
        config = get_config(config)

        for tup in config:
            if tup[0] == 'xsrc' or tup[0] == 'ysrc':
                attributes_count += 1
        
        # randomly choose attributes_count number of attributes from data with are unique, using random.choose
        
        # attributes = [random.choice(data.columns)]
        # for i in range(attributes_count-1):
        #     t = random.choice(data.columns)
        #     # while t in attributes:
        #     #     t = random.choice(data.columns)
        #     attributes.append(t)    

        try:
            attributes = random.sample(list(data.columns), attributes_count)
        except:
            continue

        # attributes = [random.choice(data.columns) for i in range(attributes_count)]
        # print(attributes)

        # get the values in first row of the attributes
        values = [data[attributes[i]][0] for i in range(attributes_count)]
        # print(values)
        
        temp_data = []
        temp_data.append(str(dataset))
        
        # name the attriutes as dataset_value correspondingly
        for i in range(len(attributes)):
            temp_data.append(str(dataset) + "_" + str(values[i]))
        
        temp_data.append(str(config))
        temp_data.append("0")
        all_data.append(temp_data)
    


second = len(all_data)
print(first)
print(second)
print((all_data[-7]))
# j = 0
# # check if datasets contain Masakazu
# for i in range(len(datasets)):
#     if ".csv" not in datasets[i]:
#         print(datasets[i-1],datasets[i],datasets[i+1])
#     if "spartan" in datasets[i]:
#         j += 1
#         print(datasets[i])

# print(j)


# save the list all_data as a pickle file
with open('../../../../all_data.pkl', 'wb') as f:
    pickle.dump(all_data, f)


