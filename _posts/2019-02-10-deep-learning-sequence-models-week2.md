---
layout: post
title:  "Deep Learning - Sequence Models - Week 2"
date:   2019-02-10 11:57 -0800
categories: machine-learning python
---

...continuing to work my way through Andrew Ng's [deep learning classes][1] on [Coursera][2]. Week 2 of the [Sequence Models][3] class focuses on word embeddings.

## Word embeddings

A word embedding is a projection of natural language words into a high dimensional space. Words are represented by vectors of sizes ranging from 50 to 300 or more. In some mysterious way, that vector space encodes relationships between words based on their co-occurence in a large corpus - relationships like countries and their capitals, verbs and their tenses, words and their comparitive and superlative forms (big, bigger, biggest), or gender-specificity of words like brother and sister.

[Word2Vec][5] is one algorithm for learning word embeddings. Another is [GloVe][4] (Global Vectors for Word Representation) with pretrained embeddings available for download from the Stanford NLP group.


## Sentiment analysis

Word embeddings can help with tasks like sentiment analysis, particularly in cases where you can extend the reach of a small training set by leveraging embeddings from a large corpus. RNNs help characterize phrases like "Not feeling happy" or "Completely lacking in good atmosphere and good taste" where memory is needed to pick up the negation of positive words.

## Debiasing

Interestingly, word embeddings make visible some of the unwanted cultural baggage we're all carrying around with us. See the paper [Man is to Computer Programmer as Woman is to Homemaker? Debiasing Word Embeddings][6].

[Textio][7] is a Seattle company that's made a product out of helping people see the structure, desired or undesirable, underneath the language used in job descriptions and elsewhere. *Hey rockstar ninja code-warriors, ready to work hard and play hard?* 🙄


[1]: https://www.deeplearning.ai/deep-learning-specialization/
[2]: https://www.coursera.org/specializations/deep-learning
[3]: https://www.coursera.org/learn/nlp-sequence-models
[4]: https://nlp.stanford.edu/projects/glove/
[5]: https://papers.nips.cc/paper/5021-distributed-representations-of-words-and-phrases-and-their-compositionality.pdf
[6]: https://www.semanticscholar.org/paper/Man-is-to-Computer-Programmer-as-Woman-is-to-Word-Bolukbasi-Chang/274459c52103f9b7880d0697aa28755ac3366987
[7]: https://textio.com/
[8]: https://medium.com/explore-artificial-intelligence/word2vec-a-baby-step-in-deep-learning-but-a-giant-leap-towards-natural-language-processing-40fe4e8602ba
