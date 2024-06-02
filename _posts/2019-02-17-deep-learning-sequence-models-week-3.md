---
layout: post
title:  "Deep Learning - Sequence Models - Week 3"
date:   2019-02-17 12:36 -0800
category: AI, Machine Learning, Deep Learning
tags: machine-learning python
---

Notes on week 3 of the [Sequence Models][3] class, part of Andrew Ng's [deep learning series][1] on [Coursera][2].

A **language model** computes a probability distribution over sequences of words in a language. It assigns a probability of a given word following a sequence of words.

## Encoder-decoder

A basic machine translation system can be designed in two stages - an encoder and a decoder.

![RNN Encoder-decoder]({{ "/images/rnn-encoder-decoder.png" | absolute_url }})

An encoder-decoder design can also be used for image captioning. In the diagram below, AlexNet is modified by chopping off the final softmax classifier, leaving a 4096-element vector that represents an encoding of the image. That encoding can then be fed to a decoder that models the probability of a phrase conditioned on the encoded image yielding the caption.

![RNN Image captioning]({{ "/images/rnn-image-captioning.png" | absolute_url }})

## Attention

The encoder-decoder design has trouble with longer sentences. A highly successful alternative is the attention model.

![RNN Attention]({{ "/images/rnn_attn_model.png" | absolute_url }})

A small NN is trained to produce an attention vector, _alpha_. At each step _t_ in the output, alpha &lt;_t_, _t‘_&gt; gives a weight for each activation _a_&lt;_t‘_&gt; in the input specifying the degree of attention on the input words while producing that output word.

![RNN Attention Mechanism]({{ "/images/rnn_attn_mechanism.png" | absolute_url }})


## Date formatting

People format dates in a ridiculous variety of ways. The first exercise is to build a translation-with-attention model to reformat dates to the standard way, like so.

| human readable      | standardized
|:-------------------:|-------------:
|          3 May 1979 | 1979-05-03
|          5 April 09 | 2009-05-05
| 21th of August 2016 | 2016-08-21
|     Tue 10 Jul 2007 | 2007-07-10
| Saturday May 9 2018 | 2018-05-09
|        March 3 2001 | 2001-03-03
|      March 3rd 2001 | 2001-03-03
|        1 March 2001 | 2001-03-01


## Speech recognition

Humans, at least those with healthy young ears, can hear frequencies between 20 and 20,000 hertz. Interpretting those frequencies into words in the presence of background noise is one of those mysterious perceptual tasks that human brains and NN's seem to do well.

![RNN Spectrogram]({{ "/images/rnn-spectrogram.png" | absolute_url }})

The spectrogram shows three spoken words, “phone”, “activate” in a male voice, “activate” in a female voice. Our goal is to detect the word “activate” as if we wanted to wake-up a device similar to an Alexa. There's a cool background-noise artifact with three clear harmonics that descend in pitch right before the first word and repeating after the last. It sounds like bird chirp.

![RNN Trigger word network]({{ "/images/rnn-trigger-word-model.png" | absolute_url }})

It would be interesting to know more about the role of the 1D convolutional layer compared to attention.


## Done!

And, just like that... we're done! Thanks, Andrew Ng.



[1]: https://www.deeplearning.ai/deep-learning-specialization/
[2]: https://www.coursera.org/specializations/deep-learning
[3]: https://www.coursera.org/learn/nlp-sequence-models


