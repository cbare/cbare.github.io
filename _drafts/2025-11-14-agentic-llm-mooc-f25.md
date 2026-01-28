---
layout: post
title:  "Agentic AI MOOC Fall 2025"
categories:
    - AI, Machine Learning, Deep Learning
    - Learning
tags: AI LLMs Classes
---

![Berkeley Campanile](../images/UC-Berkeley-campanile.png) _Image by [jngai58](https://www.flickr.com/photos/john_n_berk_pics_xyz/51096342158/)_


Notes on the [Agentic AI MOOC, Fall 2025][f25], from UC Berkeley, an online class that continues from:

- [Large Language Model Agents MOOC, Fall 2024][f24]
- [Advanced Large Language Model Agents MOOC, Spring 2025][sp25]

## Class Resources

- [LLM Agents Discord][14]

## Instructors

- [Dawn Song][3], Professor, UC Berkeley
- [Xinyun Chen][4], Research Scientist, Google DeepMind


## Lecture 1: LLM Agents Overview

Yann Dubois, OpenAI

https://www.youtube.com/watch?v=r1qZpYAmqmg

This lecture covers the stages of LLM training:

- Pretraining
- Supervised finetuning (SFT)
- Reinforcement learning (RLHF, GRPO)
- Evaluation (close ended & open ended)


![LLM training pipeline](../images/llm-agents/f2025-lecture-1-llm-training-pipeline.png)

hacks -  model finds a shortcut to optimizing reward

![LLM training - what's important?](../images/llm-agents/f2025-lecture-1-llm-training-whats-important.png)


Recommended reading:

- [Fineweb][1001]
- [Bitter lesson][1002]
- [Kimi2][1003]
- [DeepSeek R1][1004]

## Lecture 2: Evolution of system designs from an AI engineer perspective

Yangqing Jia, NVIDIA

[video](https://www.youtube.com/watch?v=xqRAS6rAouo)

Yangqing Jia created the Caffe library during his PhD with Trevor Darrell at UC Berkeley, then moved to Google Brain and later to Facebook AI, Alibaba, and his own start-up Lepton.

### Applications

- Pro-sumer is the best market for AI tools. People are willing to pay and there are fewer barriers that making a enterprise sales.
- Capabilities of the fronteir models keep over-running special-purpose wrappers.

![AI Tech Stack](../images/llm-agents/ai-tech-stack.png)

### Infrastructure for AI

![AI is different from conventional compute](../images/llm-agents/ai-vs-conventional-compute.png)

![Root cause of interruptions in Llama 3 pretraining](../images/llm-agents/root-cause-of-interruptions-llama-3.png)

### RAG

Spend a little effort over lots of data to find relevant bits. Spend more effort on data that is relevant. Carefully look at a small amount of highly relevant.

What is the boundary between common knowledge and specific knowledge?

## Lecture 3: Post-Training Verifiable Agents

Jiantao Jiao, NVIDIA

- Chat models use RLHF to yield human aligned models.

- Agentic models are aligned to environmental feedback. Interactions are designed train the model to maximize vwerifiable rewards.

- data: get good verifiable training data
- evals: verify that we have strong models
- recipe: how to feed data to model

Dilema:

- Easy training problems, models always get it right and doesn't learn anythin
- Too hard, models can't make progress, get the wrong answer and don't learn anything

Either way, you're spending resources without making progress.

## Lecture 4: Agent Evaluation & Project Overview

https://www.youtube.com/watch?v=VfOA2a0dj4w


## Lecture 5: Some Challenges and Lessons from Training Agentic Models

Weizhu Chen, Microsoft

[video](https://www.youtube.com/watch?v=xNxrBHZPDvM)

### Agentic system

- goal oriented
- tool use
- planning / reasoning
- user interaction

### Data

- Verifiable: code & math
- Non-verifiable
  - open and subjective
  - rubrics
  - data synthesis

### Curating high quality data often outperforms parameter tuning alchemy

Tips:

1. Hard problem are usually more useful for powerful models.
2. The goodness of data is also model dependent.
3. Combine the use of real data and synthetic data. Real data helps in real cases, while synthetic data can be formalized in multiple style.
4. Use powerful models as judge and to generate more data.

### Reinforcement learning with verifiable reward (RLVR)

- can be very data efficient
- lots of roll-outs can be evaluated on the same example
- one example can be enough to work out many building blocks
- a high quality example has to encourage exploration and be at the right level of difficulty. If it's too hard, you never make progress and get no signal. Too easy, no learning

paper: [Beyond Pass@1: Self-Play with Variational Problem Synthesis Sustains RLVR][1005]

### Data Synthesis

- [Kimi K2: Open Agentic Intelligence][1003] data synthesis pipeline
- frontier labs are not sharing the most exciting parts

![Kimi-K2 data synthesis pipeline](../images/llm-agents/kimi2-data-synthesis-pipeline.jpg)


## Lecture 6: Multi-Agent AI

Noam Brown

Two-player perfect-information zero-sum games are a special case - an especially easy case. Multi-player games without full information are much harder. The kind of self-play that gave Alpha-Go superhuman performance doesn't work, something that is also true of training LLMs.

How to get recursive self-improvement in non-zero sum, partial-information, multiplayer games?

Treat humans as part of the environment

1. Collect a lot of human data and train an imitation model
2. Scale inference-time compute to better model humans
3. Scale RL with these human imitation models




## Lecture 7: Predictable Noise in LLM

## Lecture 8: AI Agents to Automate Scientific Discoveries

## Lecture 9: Practical Lessons from Deploying Real-World AI Agents

## Lecture 10: Multi-Agent Systems in the Era of LLMs

## Lecture 11: Autonomous Agents: Embodiment, Interaction, and Learning

## Lecture 12: Agentic AI Safety & Security

[f25]: https://agenticai-learning.org/f25
[sp25]: https://llmagents-learning.org/sp25
[f24]: https://llmagents-learning.org/f24
[3]: https://dawnsong.io/
[4]: https://jungyhuk.github.io/
[5]: /2024-12-10/llm-agents-mooc.html
[7]: https://cbare.github.io/2025-05-31/llm-agents-mooc-spring-2025.html
[14]: https://discord.com/channels/1280234300012494859

[1001]: https://arxiv.org/abs/2406.17557
[1002]: http://www.incompleteideas.net/IncIdeas/BitterLesson.html
[1003]: https://arxiv.org/abs/2507.20534
[1004]: https://arxiv.org/abs/2501.12948
[1005]: https://arxiv.org/abs/2508.14029
