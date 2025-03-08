---
layout: post
title:  "AIML 428: Text Mining and Natural Language Processing"
categories:
    - AI, Machine Learning, Deep Learning
    - Learning
tags: AI LLMs Classes NLP
---

![Victoria University of Wellington](../images/vuw-logo-green-full.svg){:style="float: right; width: 33%; margin-left: 1em; margin-top: 2em;"} 

## Class resources

- [AIML 428: Text Mining and Natural Language Processing][1]
- [ECS AIML 428 (2025) Home Page][2]
- [Nuku 25.1.AIML428: Text Mining and Natural Language Processing][3]

## Instructors

- Dr Xiaoying Gao
- Prof Ali Knott

## Lectures

24 February 2025 - 22 June 2025

| day     | time        | room                  |
|---------+-------------+-----------------------|
| Tuesday | 10:00-10:50 |          Murphy LT102 |
| Friday  | 10:00-10:50 | Alan MacDiarmid LT105 |


### Lecture 1: Introduction to language modelling

AI is in the middle of an old-fashioned scientific revolution right now.

- Copernicus, Kepler, Galileo (1542, 1609, 1630)
- Newton (1687)
- Watt’s steam engine (1769), and the industrial revolution
- Darwin (1859)
- Einstein (1905, 1915)
- Turing, von Neumann (1936, 1945): the computer revolution.
- The AI revolution:
    - Hinton, le Cun (1986, 1989, 2012): neural networks
    - Bengio, Bahdanau (2014, 2017): neural networks for language
    - ChatGPT (2022)

**What’s a language model?** It’s a scientific/technical description of a human language. The model has to do some work for us: to support various tasks, such as:

- understand language. extract meaning.
- generate language, conversation.
- represent the ‘structures’ of a language - grammar, vocabulary, idioms.
- explain how languages are learned.

**Rule-based models** dominated linguistics for years! ...starting with Noam Chomsky in the 1950s.

Problems for rule-based language models:

1. You need many rules to represent language as it’s actually used.
2. If you have many rules, your grammar overgenerates.
3. If you have many rules, your grammar gives too many possible interpretations for actual sentences.
4. Your grammar doesn’t tell you how to do anything with language.
    - E.g. have a dialogue, answer questions...
5. How do babies learn the rules of their language, just from hearing it spoken?
6. How are grammar rules represented in the brain? NN language models can address all of these problems.

### Lecture 2: Intro to probabilistic language models: n-grams

Probabilistic language models often make a Markovian assumption: that the probability of a word just depends on the most recent _n_ words.

**n-grams**: Probability of the next word conditioned on the previous _n_ words.

The conditional probability of the next word is estimated based on counts of observed word sequences in the training corpus.

$$
P(x_{t+1} \mid x_{t-n}, \dots, x_t) = \frac{P(x_{t-n}, \dots, x_t, x_{t+1})}{P(x_{t-n}, \dots, x_t)} \approx \frac{\textit{count}(x_{t-n}, \dots, x_t, x_{t+1})}{\textit{count}(x_{t-n}, \dots, x_t)}
$$

### Lecture 3: Classification, KNN, Text Features

Text classification based on classic ML algorithms, e.g. KNN and SVM, or neural models. What features inform classification tasks?

Characters, words, or tokens? All have problems. Vectors can capture meaning and semantic similarity.

#### Similarity measures

For vector representations, **cosine similarity** is often used:

$$
\cos (\theta ) = \dfrac {A \cdot B} {\left\| A\right\| _{2}\left\| B\right\| _{2}}
$$


[1]: https://www.wgtn.ac.nz/courses/aiml/428/2025/offering?crn=33070
[2]: https://ecs.wgtn.ac.nz/Courses/AIML428_2025T1/
[3]: https://nuku.wgtn.ac.nz/courses/23691
