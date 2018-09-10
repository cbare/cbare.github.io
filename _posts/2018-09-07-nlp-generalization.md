---
layout: post
title:  "Generalization in NLP"
date:   2018-09-09 21:15 -0800
categories: machine-learning deep-learning
---

Natural language processing is still at a point closer to Eliza than HAL.

[The Shallowness of Google Translate][5] points out a number of cases where the algorithms fall short of human-level nuance.

[The Gradient][7] has some interesting reading on the brittleness of NLP models and how that's being addressed. The article [NLP’s generalization problem, and how researchers are tackling it][1] names three strategies:

1. using more [inductive bias][6].
2. working towards imbuing NLP models with common sense,
3. working with unseen distributions and unseen tasks.

How to evaluate generalization isn't entirely clear. One proposal is: "Every paper, together with evaluation on held-out test sets, should evaluate on a novel distribution or on a novel task"

Transfer learning, applying pretrainined networks to new tasks, has been very successful in computer vision. A pair of articles describes work to bring transfer learning to NLP based on language modeling, predicting the next word in a sequence.

* [NLP's ImageNet moment has arrived][2]
* [Introducing state of the art text classification with universal language models][3]

Also featuring pretrained language models: [Efficient Contextualized Representation][4]


[1]: https://thegradient.pub/frontiers-of-generalization-in-natural-language-processing/
[2]: https://thegradient.pub/nlp-imagenet/
[3]: http://nlp.fast.ai/classification/2018/05/15/introducting-ulmfit.html
[4]: https://arxiv.org/abs/1804.07827
[5]: https://www.theatlantic.com/technology/archive/2018/01/the-shallowness-of-google-translate/551570/
[6]: http://www.lauradhamilton.com/inductive-biases-various-machine-learning-algorithms
[7]: https://thegradient.pub/


