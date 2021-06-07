---
layout: post
title:  "TensorFlow in Practice"
date:   2019-11-12 22:12 -0800
categories: machine-learning deep-learning
---

Notes from the [deeplearning.ai][0] course [TensorFlow in Practice][1].

The course is organized into 4 modules:

1. Introduction to TensorFlow for AI, ML and DL
2. Convolutional Neural Networks in TensorFlow
3. Natural Language Processing in TensorFlow
4. Sequences, Time Series, and Prediction

Notebooks can be found at: [github.com/lmoroney/dlaicourse][8]

## tf.keras

Keras layers a simpler API over Tensorflow and the course makes heavy use of tf.keras. You'll have to fix a few rough spots due to the tf 1.x to tf 2.x transition.


[Loss functions][2]


## Regularization

[Dropout][5]


## Resources

* Geoffrey Hinton's [Neural Networks and Machine Learning class material][3] from csc321 (2014).
* [Rethinking the Inception Architecture for Computer Vision][4]
* Leo Dirac's [geometric-intuition][7]


[0]: https://www.deeplearning.ai/
[1]: https://www.deeplearning.ai/tensorflow-in-practice/
[2]: https://gombru.github.io/2018/05/23/cross_entropy_loss/
[3]: http://www.cs.toronto.edu/~tijmen/csc321/
[4]: https://arxiv.org/abs/1512.00567
[5]: https://www.youtube.com/watch?v=ARq74QuavAo
[6]: https://www.kaggle.com/datamunge/sign-language-mnist
[7]: https://github.com/leopd/geometric-intuition/tree/master/quantifying-uncertainty
[8]: https://github.com/lmoroney/dlaicourse

