import os,sys
sys.path.append('/home/aistudio/external-libraries')
import nibabel as nib
import numpy as np

data_path = "/home/aistudio/work/data/train_data_raw/"
n = 0
for file_name in os.listdir(data_path):
    data = nib.load(data_path+file_name)
    data = data.get_fdata()
    print(data.shape)
    n+=1
print(n)