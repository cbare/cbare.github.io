---
layout: post
title:  "Deep learning summer school 2019"
date:   2019-12-07 9:15:00 -0800
categories: machine-learning deep-learning
---

I've been working my way through the videos from the [2019 CIFAR DLRL Summer School Lectures](https://dlrlsummerschool.ca/) held July 24 – August 2 in Alberta, Canada. Imagine living in a world where all this material is available for free. See the [playlist](https://www.youtube.com/playlist?list=PLKlhhkvvU8-aXmPQZNYG_e-2nTd0tJE8v) on YouTube.

- [x] Deep Learning I - Hugo Larochelle
- [x] Deep Learning II - Hugo Larochelle
- [x] AI & Society Panel Discussion
- [x] CNNs - Graham Taylor
- [ ] Images - Angel Chang
- [x] RNNs - Yoshua Bengio
- [ ] Video - Greg Mori
- [ ] Optimization in DL - Jimmy Ba
- [x] Natural Language Processing - Alona Fyshe
- [x] Bayesian Deep Learning - Roger Grosse
- [/] Autoencoders/Unsupervised: Jörn-Henrik Jacobsen
- [-] GANs - Ke Li
- [-] Biological DL - Blake Richards
- [x] What’s Next - Yoshua Bengio
- [-] TD/RL Intro - Adam White
- [-] Bandits - Csaba Szepesvári
- [ ] Sample Efficient RL - Harm Van Seijen
- [ ] Off Policy - Doina Precup
- [ ] POMDPs - Pascal Poupart
- [ ] Model-Based RL - Martha White
- [ ] Optimization in RL - Dale Schuurmans
- [-] Human in the Loop - Matt Taylor
- [ ] Robust RL - Marek Petrik
- [ ] Multi-Agent Systems - James Wright
- [ ] Multi-Agent RL - Michael Bowling
- [-] Career Panel feat. Rich Sutton, Yoshua Bengio & Martha White
- [ ] Policy Search Methods for Robotics - Jan Peters
- [ ] DRL I - Matteo Hessel
- [ ] DRL II - Anna Harutyunyan
- [ ] Options (HRL) - Andre Barreto
- [ ] Doing RL on Robots - Jan Peters
- [ ] Science with Robots - A. Rupam Mahmood
- [ ] Applied RL on Robots - Patrick Pilarski
- [ ] RL Research/Frontiers - Rich Sutton


## Deep Learning I & II - Hugo Larochelle

Really nice overview with pointers to recent research. Hugo Larochelle is a good speaker and has several of talks online.

## RNNs - Yoshua Bengio


## Natural Language Processing - Alona Fyshe


## What’s Next - Yoshua Bengio



## Bayesian Deep Learning - Roger Grosse

Calibration - do the scores output by a model reflect the actual probability distribution?

Bayesians treat model parameters as random variables rather than point estimates.

n-armed bandit problem: you have _n_ slot machines in front of you each of which pays out $1 with some probability. Need to trade off exploration vs. exploitation.

Possible strategies:
 - Greedy strategy: keep picking the arm that paid out most frequently so far.
 - Pick arm we're most uncertain about.
 - Epsilon-greedy: do greedy with probability 1-epsilon, otherwise pick randomly.

Thompson sampling: Sample parameters for each bandit from current posterior distributions. Choose the optimal action as if those samples were the true parameters. See Russo (2017), “A Tutorial on Thompson Sampling”.

Bayesian Neural Nets training by HMC (hamiltonian monte carlo) is computationally expensive. Quick and dirty approximations include:
 - ensembles of networks with each member trained on a random subset or bootstrap sample of the training data.
 - Monte Carlo dropout which uses the variance of predictions sampled with different dropout masks, see Gal et al “Dropout as Bayesian approximation”. Viewing dropout as an implicit ensemble is cool.

A couple things I didn't understand:
 - linkage between Bayes nets and network compression
 - obtaining bounds on generalization error

