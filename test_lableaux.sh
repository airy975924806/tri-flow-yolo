#!/usr/bin/env bash

python test_lableaux.py --weights 'runs/train/muti_17_0.8comosaic_0.2scale_SoftIOU_17_LABLE_0.1count_1grl/weights/best.pt' \
        --data data/domain/city_foggycity_8class.yaml\
        --batch-size 8\
        --img-size 960  \
        --verbose \
        --name city2foggycity_960
#         --name voc2watercolor_960
