# tri-flow-yolo
mix-supervised object detection
This is the repo for the manuscripts "Tri-Flow-YOLO: Counter Helps to Improve Cross-Domain Object Detection"
# This is the repo for the manuscripts "Tri-Flow-YOLO: Counter Helps to Improve Cross-Domain Object Detection"

# data processing
* **Cityscape and FoggyCityscape:** Download the [Cityscape](https://www.cityscapes-dataset.com/) dataset, see dataset preparation code in [DA-Faster RCNN](https://github.com/yuhuayc/da-faster-rcnn/tree/master/prepare_data).
* **PASCAL_VOC 07+12:** Please follow the [instruction](https://github.com/rbgirshick/py-faster-rcnn#beyond-the-demo-installation-for-training-and-testing-models) to prepare VOC dataset.
* **Clipart:** Please follow the [instruction](https://github.com/naoto0804/cross-domain-detection/tree/master/datasets) to prepare Clipart dataset.

# weight processing
* ** download the [pretrained-weight](https://share.weiyun.com/cpVOF1xC) to the weight folder

# train with the tri-flow-yolo in Cityscapes2FoggyCityscape
bash train-lableaux.sh

# test in Cityscapes2FoggyCityscape
bash test-lableaux.sh


## Acknowledgement

Our code is based on the project [yoloair](https://github.com/iscyy/yoloair).
