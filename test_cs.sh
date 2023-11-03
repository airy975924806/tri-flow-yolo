#!/usr/bin/env bash

python test_cs.py --weights 'runs/train/muti_17_0.8comosaic_sqrtro/weights/best.pt' \
        --data data/domain/city_foggycity_8class.yaml --batch-size 8\
        --img-size 640  --verbose --name muti_17_0.8comosaic_sqrtro
