---
layout: post
title: "Object detection and localization"
date: 2018-06-16 20:50 -0700
categories: machine-learning python
---

[Andrew Ng](https://twitter.com/AndrewYNg)'s class on [deep learning with convolutional neural nets](https://www.coursera.org/learn/convolutional-neural-networks) covers object detection and localization with the YOLO algorithm, non-max suppression and anchor boxes.

![YOLO]({{ "/images/yolo.png" | absolute_url }})


Using the pretrained network from the YOLOv2 model, I picked a random street scene image and it did this:

![Object detection and localization]({{ "/images/object_detection_and_localization.png" | absolute_url }})


### References:

* [You Only Look Once: Unified, Real-Time Object Detection](https://arxiv.org/abs/1506.02640) (2015)

* [YOLO9000: Better, Faster, Stronger](https://arxiv.org/abs/1612.08242) (2016)

* [YAD2K: Yet Another Darknet 2 Keras](https://github.com/allanzelener/YAD2K)

* The official [YOLO website](https://pjreddie.com/darknet/yolo/)
