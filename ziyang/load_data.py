import os,sys
sys.path.append('/home/aistudio/external-libraries')
import nibabel as nib
import numpy as np
import pandas as pd

data_path = "/home/aistudio/work/code/Unet_liver_segmentation/data/prep/ct/"
gt_path = "/home/aistudio/work/code/Unet_liver_segmentation/data/prep/seg/"
excel_path = "/home/aistudio/work/data/train.csv"

def read_data(file_name):
    data = nib.load(file_name)
    data = data.get_fdata()
    # data = data - np.mean(data)
    # data = data / np.std(data)
    data =  np.expand_dims(data,axis=3)
    return data

def load_data(excel_path):
    train_number = pd.read_csv(excel_path,header=0)
    train_id = train_number['id']
    ref_id = sorted(os.listdir(data_path))
    for i in range(len(train_id)):
        for gt_file_name in os.listdir(gt_path):
            if train_id[i] not in gt_file_name:
                continue
            gt_data = read_data(gt_path+gt_file_name)
            train_data = read_data(data_path+ref_id[i])

            out = np.concatenate([train_data,gt_data],axis=3)
            print(out.shape)
            # print(gt_file_name)


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


# load_data(excel_path)
test_load()