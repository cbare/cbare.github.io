# Intro to NLP

Natural Language Processing (NLP) is a set of techniques for computing on human language.


## Tasks

- Information retrieval/search
- Classification
  - sentiment analysis
  - Topic modeling
- Named entity recognition
- Information extraction
- Summarization
- Translation
- Question answering


## Word Vectors

300 dimensions is typical, allowing for “multiple degrees of similarity”

Lots of ways for two words to be similar or different.



"The horse raced past the barn fell."

"Time flies like an arrow; fruit flies like a banana."

"One morning I shot an elephant in my pajamas. How he got into my pajamas I'll never know."

Read a book vs book a flight.


## Transfer learning

Training a model on one task, then applying the model to a different task. Learning on self-labeling tasks - predict next word, predict 



## Experience at 98point6

Text-based primary care medicine. Medical interview partially handled by chat-bot. Framed as a multiclass classification problem.

Chief complaint -> ~200 vector of scores.



(Word2Vec) Efficient Estimation of Word Representations in Vector Space. 2013
Tomas Mikolov, Kai Chen, Greg Corrado, Jeffrey Dean

GloVe: Global Vectors for Word Representation.
Jeffrey Pennington, Richard Socher, and Christopher D. Manning. 2014

