
import sys, os
import re
sys.path.append('/home/aistudio/external-libraries')

import shutil
from shutil import copyfile

import time
 
time_start=time.time()


data_dir = os.getcwd() + '/data'
train_ct_dir = data_dir + '/train'+'/ct/'
train_seg_dir  = data_dir + '/train'+'/seg/'
test_ct_dir = data_dir + '/test'+'/ct/'
test_seg_dir = data_dir + '/test'+'/seg/'

# 创建文件夹
if not os.path.exists(data_dir):
    os.makedirs(train_ct_dir)
    os.makedirs(train_seg_dir)
    os.makedirs(test_ct_dir)
    os.makedirs(test_seg_dir)

old_path = r'/home/aistudio/data/data10273/'
all_list = os.listdir(old_path)
seg_list = ['1.0.zip']
train_list = ['2.0.zip','3.0.zip','4.0.zip']
test_list = ['5.0.zip','6.0.zip']


for k in all_list:
    if k in seg_list:
        print('正在拷贝金标准：', str(k))
        copyfile(old_path+k, train_seg_dir+k)
    elif k in train_list:
        print("正在拷贝训练集的原始图像：", str(k))
        copyfile(old_path+k, train_ct_dir+k)
    elif k in test_list:
        print("正在拷贝测试集的原始图像：", str(k))
        copyfile(old_path+k, test_ct_dir+k)
    else:
        print('这个数据集用不到')
    
copyfile(old_path+'1.0.zip', train_seg_dir+'1.0.zip')

# 解压缩操作
print("解压缩开始...")
os.system("find ./data/train/ct -name *.zip | xargs -n1 unzip -d ./data/train/ct")
os.system("find ./data/train/ct -name *.nii.zip | xargs -n1 unzip -d ./data/train/ct")
os.system("rm ./data/train/ct/*.zip")

os.system("find ./data/test/ct -name *.zip | xargs -n1 unzip -d ./data/test/ct")
os.system("find ./data/test/ct -name *.nii.zip | xargs -n1 unzip -d ./data/test/ct")
os.system("rm ./data/test/ct/*.zip")

os.system("find ./data/train/seg -name *.zip | xargs -n1 unzip -d ./data/train/seg")
os.system("find ./data/train/seg -name *.nii.zip | xargs -n1 unzip -d ./data/train/seg")
os.system("rm ./data/train/seg/*.zip")

# 处理训练集的金标准
for root, dirs,files in os.walk(train_seg_dir):
    for name in files:
        pathname = os.path.splitext(os.path.join(root,name))
        name_slice = re.split("[-.]",name)

        if int(name_slice[1]) > 100:
            shutil.move(os.path.join(root,name),os.path.join(test_seg_dir,name)) # 移动到test的金标准文件夹

time_end=time.time()
time_elapsed = time_end-time_start
print('time cost {:.0f}m {:.0f}s'.format(time_elapsed // 60, time_elapsed % 60)) # 打印出来时间








