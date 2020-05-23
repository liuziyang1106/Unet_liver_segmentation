import os,sys
sys.path.append('/home/aistudio/external-libraries')
import nibabel as nib
import numpy as np

data_path = "/home/aistudio/work/data/test_data/"
gt_path = "/home/aistudio/work/data/gt/"
n = 0
for gt_file_name in os.listdir(gt_path):
    for train_file_name in os.listdir(data_path):
        train_id_number = train_file_name.split("-")[1]
        gt_id_number = gt_file_name.split("-")[1]
        if train_id_number == gt_id_number:
            data = nib.load(data_path+train_file_name)
            data = data.get_fdata()
            print("shape is equal: ",data.shape)
            n+=1
print(n)