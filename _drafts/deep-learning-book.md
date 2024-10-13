---
layout: post
title:  "Deep Learning Book, Mathematical Foundations"
category: AI, Machine Learning, Deep Learning
tags: deep-learning books
---

...notes on part 1 of the [Deep Learning Book][1] by Ian Goodfellow, Yoshua Bengio, and Aaron Courville.

## Introduction

The book describes **deep learning** from a couple of points of view:

Deep learning is a particular kind of machine learning representing the world as a nested hierarchy of concepts, with each concept defined and computed in terms of simpler concepts.

Another perspective on deep learning is that depth enables the computer to learn a multistep computer program. The output of each layer can be thought of as the state of the computer’s memory after executing a set of instructions in parallel.

Trends in deep learning:

- increasing data volume
- increasing model size and depth
- increasing the parts of the system that can be learned from data, for example feature extraction

ToDo: link to Sarath Chandar's lecture on the history of deep learning from RLDL 2024.


## Part I: Applied Math and Machine Learning Basics

Part 1 of the [Deep Learning Book][1] tries to give the reader enough background to understand the rest of the book. Inevitably, it won't be enough, but you have to start somewhere.

The helpful [notation][2] guide is a great reference.


### 2 Linear Algebra

Resources:

- [Essence of linear algebra][102], 3Blue1Brown
- Steve Brunton's lecture series on [Singular Value Decomposition][105]
- [Linear Algebra By Georgi E. Shilov][203] 1977


### 3 Probability and Information Theory

#### Probability

Resources:

- Probability Theory: The Logic of Science, Edwin T. Jaynes, WUSTL
- [Probability Theory Lectures][103] by Aubrey Clayton
- [Probabilistic Reasoning in Intelligent Systems: Networks of Plausible Inference][202], Judea Pearl, 1988

#### Information Theory

“**Shannon entropy** of a distribution is the expected amount of information in an event drawn from that distribution. It gives a lower bound on the number of bits needed on average to encode symbols drawn from a distribution P.”

$$H(X) = \mathbb{E}_[x~P][-\log_b P(X)] $$

For discrete random variables, we write:

$$H(X) = -\sum_{i=1}^{n} p(x_i) \log_b p(x_i)$$


**Kullback-Leibler (KL) divergence** is a measure of difference between two probability distributions.

$$D_{\text{KL}}(P \| Q) = \mathbb{E}_{[x \sim P]} \left[ \log_b \frac{P(X)}{Q(X)} \right] = \mathbb{E}_{[x \sim P]} \left[ \log_b P(X) - \log_b Q(X) \right]$$

or...

$$D_{\text{KL}}(P \| Q) = \sum_{i=1}^{n} p(x_i) \log_b \frac{p(x_i)}{q(x_i)}$$

The KL divergence is non-negative and 0 when P = Q. It is not truly a distance measure because it is not symmetric. $$ D_{\text{KL}}(P \| Q)$$ is not necessarily the same as $$D_{\text{KL}}(Q \| P)$$.


Written this way, the expression highlights that cross-entropy is the expected value of the negative log probability of 𝑄, with the expectation taken over the distribution 𝑃.

$$H(P, Q) = \mathbb{E}_{[x \sim P]} \left[-\log_b Q(x)\right]$$

Minimizing the cross-entropy with respect to Q is equivalent to minimizing the KL divergence, because Q does not participate in the omitted term.

The discrete form is:

$$H(P, Q) = -\sum_{x\in\mathcal{X}} P(x)\, \log Q(x)$$

Resources:

- [KL Divergence][101], ritvikmath
- [Information Theory, Inference, and Learning Algorithms][203], David J.C. MacKay


### 4 Numerical Computation

See the [Essence of Calculus][104] series by 3Blue1Brown for review on the Chain Rule and Taylor Series.


vector **gradient**

the gradient of f is the vector containing all the partial derivatives, denoted ∇xf(x). Element i of the gradient is the partial derivative of f with respect to xi

$$\nabla f(x) = \left[ \frac{\partial f(x)}{\partial x_1}, \frac{\partial f(x)}{\partial x_2}, \ldots, \frac{\partial f(x)}{\partial x_n} \right]$$

Jacobian

Hessian



[Neural Net Training Dynamics][401], Roger Grosse, U of Toronto



### 5 Machine Learning Basics

- train/test split
- baseline models
- model evaluation
- overfitting
- underfitting
- cross-validation
- hyperparameter tuning

Example: Linear Regression
Todo: work through derivation of update rule for linear regression in a notebook.

The error incurred by an oracle making predictions from the true distribution p(x, y) is called the **Bayes error**.



[1]: https://www.deeplearningbook.org/
[2]: https://www.deeplearningbook.org/contents/notation.html
[3]: https://www.deeplearningbook.org/contents/linear_algebra.html
[4]: https://www.deeplearningbook.org/contents/prob.html
[5]: https://www.deeplearningbook.org/contents/numerical.html

[101]: https://www.youtube.com/watch?v=q0AkK8aYbLY
[102]: https://www.youtube.com/playlist?list=PLZHQObOWTQDPD3MizzM2xVFitgF8hE_ab
[103]: https://www.youtube.com/watch?v=rfKS69cIwHc&list=PL9v9IXDsJkktefQzX39wC2YG07vw7DsQ_
[104]: https://www.youtube.com/playlist?list=PLZHQObOWTQDMsr9K-rj53DwVRMYO3t5Yr
[105]: https://www.youtube.com/playlist?list=PLMrJAkhIeNNSVjnsviglFoY2nXildDCcv

[202]: https://dl.acm.org/doi/book/10.5555/534975
[203]: https://www.inference.org.uk/mackay/itila/
[204]: https://store.doverpublications.com/products/9780486635187

[401]: https://www.cs.toronto.edu/~rgrosse/courses/csc2541_2021/
