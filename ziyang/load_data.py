import os,sys
sys.path.append('/home/aistudio/external-libraries')
import nibabel as nib
import numpy as np
import pandas as pd

data_path = "/home/aistudio/work/data/prep_0.5/train/"
gt_path = "/home/aistudio/work/data/prep_0.5/seg/"

def read_data(file_name):
    data = nib.load(file_name)
    data = data.get_fdata()
    # data = data - np.mean(data)
    # data = data / np.std(data)
    data =  np.expand_dims(data,axis=3)
    return data

def test_load():
    n = 0
    for gt_file_name in os.listdir(gt_path):
        for train_file_name in os.listdir(data_path):
            train_id_number = "-"+train_file_name.split("-")[1]
            gt_id_number = "-"+gt_file_name.split("-")[1]

            # print(train_id_number)
            # print(gt_id_number)
            if train_id_number == gt_id_number:
                train_data = read_data(data_path+train_file_name)
                gt = read_data(gt_path+gt_file_name)
                # out = np.concatenate([train_data,gt],axis=3)
                print("ground truth shape: ",gt.shape)
                print("train data shape: ",train_data.shape)
                n+=1
    print(n)


test_load()