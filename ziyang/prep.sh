#! /bin/bash

training_set_path=../data/prep/
train_ct_path=../data/ct/
train_seg_path=../data/seg/

python get_training_set.py  training_set_path    \
--train_ct_path     ${train_ct_path}        \
--train_seg_path    ${train_seg_path}       \
--upper             255                     \
--lower             0                       \
--slice_thickness   1                       \
--down_scale        1                       \
--expand_slice      20                      \
--size              20                      \
