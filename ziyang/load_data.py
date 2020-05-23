import os,sys
sys.path.append('/home/aistudio/external-libraries')
import nibabel as nib
import numpy as np

data_path = "/home/aistudio/work/data/train_data/"
gt_path = "/home/aistudio/work/data/gt/"

def test_load():
    n = 0
    for gt_file_name in os.listdir(gt_path):
        for train_file_name in os.listdir(data_path):
            train_id_number = train_file_name.split("-")[1]
            gt_id_number = gt_file_name.split("-")[1]
            if train_id_number == gt_id_number:
                train_data = read_data(data_path+train_file_name)
                gt = read_data(gt_path+gt_file_name)
                out = np.concatenate([train_data,gt],axis=3)
                print("shape is equal: ",out.shape)
                n+=1
    print(n)

def read_data(file_name):
    data = nib.load(file_name)
    data = data.get_fdata()
    data = data - np.mean(data)
    data = data / np.std(data)
    data =  np.expand_dims(data,axis=3)
    return data

test_load()