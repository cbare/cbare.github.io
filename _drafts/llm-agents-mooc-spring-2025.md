---
layout: post
title:  "Advanced LLM Agents MOOC"
categories:
    - AI, Machine Learning, Deep Learning
    - Learning
tags: AI LLMs Classes
---

![Berkeley Campanile](../images/UC-Berkeley-campanile.png) _Image by [jngai58](https://www.flickr.com/photos/john_n_berk_pics_xyz/51096342158/)_


Notes on [Advanced Large Language Model Agents, Spring 2025][1], an online class that picks up where [Large Language Model Agents MOOC, Fall 2024][2] left off. In the Berkeley catalog, it's [CS294/194-280][12].



## Class Resources

- [LLM Agents Discord][14]

### Instructors

- [Dawn Song][3], Professor, UC Berkeley
- [Xinyun Chen][4], Research Scientist, Google DeepMind
- [Kaiyu Yang][5], Research Scientist, Meta FAIR


### Topics

- Inference-time techniques for reasoning
- Post-training methods for reasoning
- Search and planning
- Agentic workflow, tool use, and functional calling
- LLMs for code generation and verification
- LLMs for mathematics: data curation, continual pretraining, and finetuning
- LLM agents for theorem proving and autoformalization

### Reading

- OpenAI blog [Learning to reason with LLMs][13]
- [The Bitter Lesson][20] by Rich Sutton


## Lecture 1: _Inference-Time Techniques for LLM Reasoning_

[Xinyun Chen][4]
Google DeepMind

![Large language model agents](../images/llm-agents/llm-agents.jpg)

Solving real world tasks typically involves a trial-and-error process. Leveraging external tools and retrieving from external knowledge expand LLM's capabilities. Agentic workflows facilitate complex tasks.

- Task decomposition
- allocation of subtasks to specialized modules
- division of labor for collaboration


### “Let’s think step by step”

In chain-of-thought prompting, we allow the model to adapt the amount of computation to the difficulty of the problem. For complex questions, the model can use more reasoning steps. Models can be trained or instructed to use reasoning strategies like decomposition, planning, analogies, etc.

Models can automate prompt design and optimize prompts. They can generate exemplars gaining the benefits of few-shot reasoning without human effort to write examples.

- [Large Language Models Are Human-Level Prompt Engineers][16]
- [Large Language Models As Optimizers][17]
- [Large Language Models As Analogical Reasoners][18]


### Explore multiple branches

We should not limit the LLM to only one solution per problem. Exploring multiple branches allows the LLM to recover from mistakes, generate multiple candidate solutions, or multiple next steps.

#### Self-consistency

Self-consistency is a simple and general principle in which we ask the model for several responses and select the response with the most consistent final answer. Consistency is highly correlated with accuracy.

- [Self-Consistency Improves Chain of Thought Reasoning in Language Models][19]

#### Sample-and-rank

Rather than counting, we can instead select the response with the highest log probability. This performs less well than self-consistency, unless the model has been specifically fine-tuned for this purpose.

She showed a nice example of clustering LLM output in the context of code generation.

![LLM Code Generations](../images/llm-agents/llm-code-generation.jpg)


#### Tree of thought

Using the LLM to compare or rank candidate solution, or prioritize exploration of more promising partial solutions enables us to:

- increase token budget for a single solution
- increase width to explore the solution space
- increase depth to refine the final solution over many steps




## Lecture 2: _Learning to Self-Improve & Reason with LLMs_

Jason Weston, Meta & NYU

Goal: An AI that "trains" itself as much as possible

- Creates new tasks to train on (challenges itself)
- Evaluates whether it gets them right ("self-rewarding")
- Updates itself based on what it understood

![RLHF vs DPO](../images/ai/rlhf-vs-dpo.jpg)

Research question: can this help it become superhuman? Can an LLM improve itself by assigning rewards to its own outputs and optimizing?

### Self-rewarding LMs

#### Observations:

- LLMs can improve if given good judgements on response quality
- LLMs can provide good judgements

#### Train a self-rewarding language model that:

- Has instruction following capability
- Has evaluation capability, i.e., given a user instruction, one or more responses, can judge the quality of responses, aka LLM-as-judge

...then this model can go through an iterative process of data creation/curation training on new data. And, get better at both instruction following and
evaluation in each cycle.

![Self-rewarding language models](../images/ai/self-rewarding-language-models.jpg)


## Lecture 3: On Reasoning, Memory, and Planning of Language Agents

Yu Su, Ohio State University

![Language agent framework](../images/llm-agents/yu-su-language-agents-framework.jpg)


### Memory

Memory is central to human learning. We recognize patterns and associations relevant to the current context. [HippoRAG][301] uses a learned associative concept map as an index for non-parametric (in context) learning. Large embedding models perform at least as well. 

### Reasoning

Can LLMs learn compositional and comparative reasoning?

Examples:

- Barack's wife is Michelle. Michelle was born in 1964. When was Barack's wife born?
- Trump is 78. Biden is 82. Who is younger?

[Grokked transformers are implicit reasoners][302]: extended training far beyond overfitting enables reasoning without prompting or fine-tuning.

### Planning

Simplified definition: Given a goal G, decide a sequence of actions (a_0, a_1, ..., a_n) that will lead to a state that passes the goal test g(•).

General trends in planning settings for language agents

- Increasing expressiveness in goal specification, e.g., in natural language as opposed to formal language
- Substantially expanded or open-ended action space
- Increasing difficulty in automated goal test


Language Agents tutorial: https://language-agent-tutorial.github.io/


## Lecture 4: Open Training Recipes for Reasoning in Language Models

[Hanna Hajishirzi][401], University of Washington, Allen AI Institute Ai2

It's critical for research that there be open frontier models with training process that is transparent and reproducible. Ai2 has produced produced open pretrained LLMs: OLMo, OLMo2, OLMoE and an open post-training process called Tulu. HH's talk is on open recipes for training LLMs and reasoning models.

### Overview of open recipe for training LLMs and reasoning models

![Open training recipe](../images/llm-agents/tulu-post-training-recipe.png)

### Data curation

Training sets for proprietary models are kept secret, not least due to use of copyrighted material. Open models require a training set free of legal conflicts.

![Datasets graphics](../images/llm-agents/tulu-datasets-graphic.jpg)

![Datasets table](../images/llm-agents/tulu-datasets.jpg)

### Open post training recipe

Post training consists of three strategies - instruction fine-tuning, preference tuning (RLHF or RLAIF), and reinforcement learning with verifiable feedback (RLVF).

![Open post-training recipe](../images/llm-agents/tulu-post-training-process.jpg)

### Preference tuning

Preference tuning takes a base model oriented to document completion and improves its ability to follow instructions, hold a conversation, and perform reasoning tasks.

#### Proximal policy optimization

Proximal Policy Optimization (PPO; Schulman et al., 2017) first trains a reward model and then uses RL to optimize the policy to maximize those rewards.

$$
\max_{\pi_{\theta}} \mathbb{E}_{x \sim \mathcal{D}, y \sim \pi_{\theta}(y \mid x)} \left[ r_{\phi}(x, y) \right] 
- \beta \mathbb{D}_{\text{KL}} \left[ \pi_{\theta}(y \mid x) \,||\, \pi_{\text{ref}}(y \mid x) \right]
$$

#### Direct policy optimization

Direct Preference Optimization (DPO; Rafailov et al., 2024) directly optimizes the policy on the preference dataset; no explicit reward model.

$$
\mathcal{L}_{\text{DPO}}(\pi_{\theta}; \pi_{\text{ref}}) = 
- \mathbb{E}_{(x, y_w, y_l) \sim \mathcal{D}} 
\left[ \log \sigma \left( \beta \log \frac{\pi_{\theta}(y_w \mid x)}{\pi_{\text{ref}}(y_w \mid x)} 
- \beta \log \frac{\pi_{\theta}(y_l \mid x)}{\pi_{\text{ref}}(y_l \mid x)} \right) \right]
$$

#### SimPO

SimPO (Meng et al., 2024) does not use a reference model.

$$
\mathcal{L}_{\text{SimPO}}(\pi_{\theta}) = 
- \mathbb{E}_{(x, y_w, y_l) \sim \mathcal{D}} 
\left[ \log \sigma \left( \frac{\beta}{|y_w|} \log \pi_{\theta}(y_w \mid x) 
- \frac{\beta}{|y_l|} \log \pi_{\theta}(y_l \mid x) - \gamma \right) \right]
$$

#### GRPO

Group relative policy optimization (GRPO) was introduced in the DeepSeek R1 paper. For each question 𝑞, GRPO samples a group of outputs {𝑜1, 𝑜2, …, 𝑜𝐺} from the old policy $$\pi_{\theta_{\text{old}}}$$ and then optimizes the policy model $$\pi_{\theta}$$ by maximizing the following objective:

$$
\mathcal{J}_{GRPO}(\theta) = \mathbb{E} \left[ \frac{1}{G} \sum_{i=1}^{G} 
\min \left( \frac{\pi_{\theta}(o_i \mid q)}{\pi_{\theta_{\text{old}}}(o_i \mid q)} A_i, 
\text{clip} \left( \frac{\pi_{\theta}(o_i \mid q)}{\pi_{\theta_{\text{old}}}(o_i \mid q)}, 1 - \epsilon, 1 + \epsilon \right) A_i \right) 
\right] - \beta \mathbb{D}_{\text{KL}} \left( \pi_{\theta} \| \pi_{\text{ref}} \right)
$$

$$
A_i = \left( \frac{r_i - \bar{r}}{\sigma_r} \right)
$$

Or, as a loss to be more comparable to the other preference tuning losses:

$$
\mathcal{L}_{GRPO}(\theta) = - \mathbb{E} \left[ \frac{1}{G} \sum_{i=1}^{G} \hat{A_i} \right] + \beta \mathbb{D}_{\text{KL}} \left( \pi_{\theta} \| \pi_{\text{ref}} \right)
$$

...where $$\hat{A_i}$$ is the _clipped policy advantage_ of the _ith_ output in the group.

Each output is assigned a reward $$r_i$$, and the rewards are normalized by subtracting the mean and dividing by the standard deviation. This  group-based reward normalization is more efficient by eliminating the need for a separate value function, and appears effective in practice.

I'm still working on understanding GRPO, so don't take this as gospel.

### Mid-training

Given the observation that post-training yields larger improvements on more capable base models, how do we go about trying to improve reasoning capabilities of base models? A mid-training stage can be inserted at the end of pre-training that trains on next-token prediction on curated high-quality data including human curated reasoning traces, and math and coding with a verifiably correct answer.


## Lecture 5: Coding Agents and AI for Vulnerability Detection

Charles Sutton, Google DeepMind




[1]: https://llmagents-learning.org/sp25
[2]: https://llmagents-learning.org/f24
[3]: https://dawnsong.io/
[4]: https://jungyhuk.github.io/
[5]: https://yangky11.github.io/
[5]: /2024-12-10/llm-agents-mooc.html

[12]: https://rdi.berkeley.edu/adv-llm-agents/sp25
[13]: https://openai.com/index/learning-to-reason-with-llms/
[14]: https://discord.com/channels/1280234300012494859
[16]: https://arxiv.org/abs/2211.01910
[17]: https://arxiv.org/abs/2309.03409
[18]: https://arxiv.org/abs/2310.01714
[19]: https://arxiv.org/abs/2203.11171
[20]: http://incompleteideas.net/IncIdeas/BitterLesson.html

[301]: https://arxiv.org/abs/2405.14831
[302]: https://arxiv.org/abs/2405.15071

[401]: https://homes.cs.washington.edu/~hannaneh/



