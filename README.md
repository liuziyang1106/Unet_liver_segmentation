# Unet_liver_segmentation
## 项目解耦
- get_training_set.p:将0-100的被试样本采集数据提取肝脏和肿瘤并上下扩张20个slice
- train:包含两个文件ct和seg，分别存储处理后的原图和金标准
- data_org.py用于将data10273重新组织
