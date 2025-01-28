---
layout: post
title:  "Advance LLM Agents MOOC"
category: AI, Machine Learning, Deep Learning
tags: AI LLMs Classes
---

[Advanced Large Language Model Agents MOOC, Spring 2025][1]


[CS294/194-280][2]


[Learning to reason with LLMs][3]


[LLM Agents Discord][4]
[LLM Agents MOOC, Fall 2024][5]

## Lecture 1: _Inference-Time Techniques for LLM Reasoning_, Xinyun Chen

![Large language model agents](llm-agents-1.jpg)

Solving real world tasks typically involves a trial-and-error process.

Leveraging external tools and retrieving from external knowledge expand LLM's capabilities.

Agent workflow facilitated complex tasks

- Task decomposition
- allocation of subtasks to specialized modules
- division of labor for collaboration


### “Let’s think step by step”

In chain-of-thought prompting, we allow the model to adapt the amount of computation to the difficulty of the problem. For complex questions, the model can use more reasoning steps. Models can be trained or instructed to use reasoning strategies like decomposition, planning, analogies, etc.

Models can automate prompt design and optimize prompts. They can generate exemplars gaining the benefits of few-shot reasoning without human effort to write examples.

- [Large Language Models Are Human-Level Prompt Engineers][6]
- [Large Language Models As Optimizers][7]
- [Large Language Models As Analogical Reasoners][8]


### Explore multiple branches

We should not limit the LLM to only one solution per problem. Exploring multiple branches allows the LLM to recover from mistakes, generate multiple candidate solutions, or multiple next steps.

#### Self-consistency

Self-consistency is a simple and general principle in which we ask the model for several responses and select the response with the most consistent final answer. Consistency is highly correlated with accuracy.

- [Self-Consistency Improves Chain of Thought Reasoning in Language Models][9]

#### Sample-and-rank

Rather than counting, we can instead select the response with the highest log probability. This performs less well than self-consistency, unless the model has been specifically fine-tuned for this purpose.

She showed a nice example of clustering generations in the context of code generation.

![LLM Code Generations](llm-code-generation.jpg)


#### Tree of thought

Using the LLM to compare or rank candidate solution, or prioritize exploration of more promising partial solutions.

increase token budget for a single solution
increase width to explore the solution space
increase depth to refine the final solution over many steps

[The Bitter Lesson][10] by Rich Sutton



[1]: https://llmagents-learning.org/sp25
[2]: https://rdi.berkeley.edu/adv-llm-agents/sp25
[3]: https://openai.com/index/learning-to-reason-with-llms/
[4]: https://discord.com/channels/1280234300012494859
[5]: https://cbare.github.io/2024-12-10/llm-agents-mooc.html
[6]: https://arxiv.org/abs/2211.01910
[7]: https://arxiv.org/abs/2309.03409
[8]: https://arxiv.org/abs/2310.01714
[9]: https://arxiv.org/abs/2203.11171
[10]: http://incompleteideas.net/IncIdeas/BitterLesson.html
