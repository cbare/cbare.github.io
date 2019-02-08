---
layout: post
title:  "Deep Learning - Sequence Models"
date:   2019-01-27 09:50 -0800
categories: machine-learning python
---

After some delay, I'm getting around to finishing the Andrew Ng series of [deep learning classes][1]. The [Sequence Model][2] class is especially interesting due to the progress being made in [applying deep learning to NLP][3].

## What is a recurrent neural network?

In [The Unreasonable Effectiveness of Recurrent Neural Networks][6], Andrej Karpathy explains it like this:

“The core reason that recurrent nets are more exciting is that they allow us to operate over sequences of vectors: Sequences in the input, the output, or in the most general case both.”[6] A basic neural network simulates some unkown function, mapping a fixed-size vector of inputs to a fixed-size vector of outputs. “If training vanilla neural nets is optimization over functions, training recurrent nets is optimization over programs.”[6] RNNs accumulate state over an arbitrary length sequence of steps, enabling information from previous steps to inform output at the current step. A common example is subject-verb agreement in constructing grammatical sentences.

Another good resource is [Understanding LSTM Networks][5] by Chris Olah.

## Applications of RNNs

![RNN Applications]({{ "/images/rnn-applications.png" | absolute_url }})

## RNN Structure

An RNN unit uses both the current input, X<sup>&lt;t&gt;</sup> and the activations for the previous step, a<sup>&lt;t-1&gt;</sup> to produce the output y<sup>&lt;t&gt;</sup>.

![RNN Structure]({{ "/images/rnn-structure.png" | absolute_url }})

## Summary of RNN Types

![Summary of RNN types]({{ "/images/recurrent-neural-net-types.png" | absolute_url }})

## Gated recurrent unit

The gated recurrent unit is simplified relative to LSTM. It has the advantage of fewer parameters to tune, at the expense of a less expressive model. See: [Empirical Evaluation of Gated Recurrent Neural Networks on Sequence Modeling][4]

![GRU]({{ "/images/gru.png" | absolute_url }}){:style="width: 402px; height 246px; margin: 0px 18px 18px 18px;"}

## Long short-term memory

LSTM units add a bit more sophistication, taking previous activation *a<sup>&lt;t-1&gt;</sup>* and the contents of a memory cell *c<sup>&lt;t-1&gt;</sup>*, which maybe be additively updated or forgotten at each step.

![LSTM diagram]({{ "/images/LSTM.png" | absolute_url }})


## Programming exercises

The 1st week of the class has 3 programming exercises. The first is the mechanics of the RNN and LSTM cells and the corresponding backpropagation. I need to work on understanding the calculus better. In the 2nd exercise, they have you train character based language models for dinosaur names and Shakespeare sonnets.

The 3rd exercise, an LSTM Jazz generator, is near and dear to my heart as a music fanatic.

### References 

#### Text generation

- [Minimal character-level Vanilla RNN model. Written by Andrej Karpathy][8]
- [LSTM text generation example][7] by the Keras team


#### Jazz

The ideas presented in this notebook came primarily from three computational music papers cited below. The implementation here also took significant inspiration and used many components from Ji-Sung Kim's github repository.

- Ji-Sung Kim, 2016, [deepjazz](https://github.com/jisungk/deepjazz)
- Jon Gillick, Kevin Tang and Robert Keller, 2009. [Learning Jazz Grammars](http://ai.stanford.edu/~kdtang/papers/smc09-jazzgrammar.pdf)
- Robert Keller and David Morrison, 2007, [A Grammatical Approach to Automatic Improvisation](http://smc07.uoa.gr/SMC07%20Proceedings/SMC07%20Paper%2055.pdf)
- François Pachet, 1999, [Surprising Harmonies](http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.5.7473&rep=rep1&type=pdf)





[1]: https://www.coursera.org/specializations/deep-learning
[2]: https://www.coursera.org/learn/nlp-sequence-models
[3]: ../2018-09-09/nlp-generalization.html
[4]: https://arxiv.org/pdf/1412.3555.pdf
[5]: http://colah.github.io/posts/2015-08-Understanding-LSTMs/
[6]: http://karpathy.github.io/2015/05/21/rnn-effectiveness/
[7]: https://github.com/keras-team/keras/blob/master/examples/lstm_text_generation.py
[8]: https://gist.github.com/karpathy/d4dee566867f8291f086

