#!/usr/bin/env bash

WEIGHT='yolov5l.pt'
CFG='configs/yolov5-Improved/yolo_convnext_l_backbone.yaml'
HYP='data/hyp.scratch.custom.yaml'
IMGSIZE=640
NAME='yolov5_convnext'
WORKERS=12
DATA='data/domain/city_foggycity_8class.yaml'
EPOCH=200
BATCH=16
set -x

python train.py\
  --weight $WEIGHT\
  --data $DATA\
  --cfg $CFG\
  --workers $WORKERS\
  --name $NAME\
  --img-size $IMGSIZE\
  --hyp $HYP\
  --epochs $EPOCH\
  --batch-size $BATCH