---
layout: post
title:  "LLM Agents MOOC"
categories:
    - AI, Machine Learning, Deep Learning
    - Learning
---

![Berkeley Campanile](../images/UC-Berkeley-campanile.png)

The [Large Language Model Agents MOOC, Fall 2024][2] led by [Dawn Song][3], Professor, UC Berkeley, and [Xinyun Chen][4], Research Scientist, Google DeepMind.

The class is taught seminar-style with:

- 12 lectures each with a quiz
- Written article assignment
- 3 lab assignments
- [LLM Agents Hackathon][5]

There's some similarity and crossover with the [LLM fine-tuning lectures led by Hamel Husain][1]. That series was focused on practitioners, while the Berkeley offering is more weighted towards academics and research papers.


## Lecture Highlights

Here are a few highlights from the lectures that stood out to me.

### Denny Zhou on Chain of Thought and related techniques

Denny Zhou of Google DeepMind and senior author on [Chain-of-Thought Prompting Elicits Reasoning in Large Language Models][101] spoke on chain-of-thought and related prompting techniques.

The common theme in Zhou’s lecture is that intermediate steps help whether introduced during training, fine-tuning, or in-context.

Zhou discusses problem solving strategies from George Polya's classic book [How to Solve It][102]. Decomposing and recombining are important operations. “Let's think step-by-step”, asks the model to decompose a problem into subproblems. [Compositional generalization][103] constructs novel solutions out of simpler building blocks. To elicit analogical reasoning, you ask the model to "Recall a related problem, then solve this one."

Sampling multiple reasoning paths for the same problem and choosing the most common final result is called “self-consistency”.

### LLM Agent frameworks

Different speakers introduced frameworks designed to help build systems combining LLMs, data sources, code, and human agents.

- Autogen: An Open-Source Programming Framework for Agentic AI
- LLamaIndex: Build AI Knowledge Assistants over your enterprise data
- DSPy is the open-source framework for programming—rather than prompting—language models. It allows you to iterate fast on building modular AI systems and provides algorithms for optimizing their prompts and weights, whether you're building simple classifiers, sophisticated RAG pipelines, or Agent loops.

### Graham Neubig

Graham Neubig poses this question: “What's the delta between software, machine learning, and AI Agents in terms of valuable problems to be solved?”

### Data Pyramid

Jim Fan of NVIDIA described a data pyramid in the context of robotics that I think generalizes really well to all of machine learning. At the top of the pyramid you have expensive data, "real world" data in which you're accepting some risk to acquire, or perhaps hiring experts to hand-annotate. In the next tier, you have simulation. On the bottom you have low-quality bulk data from the internet.

### Anthropic's Responsible Scaling Policy

Ben Mann of Anthropic presented _Measuring Agent capabilities and Anthropic’s RSP_. The [responsible scaling policy][104] defines a set of safeguards matched to increasing model capabilities.

## Labs

### Autogen

Students were asked to use an LLM-Agentic framework, Autogen, to summarize reviews of American restaurant chains. The basic concept of Autogen is to factor workflows into conversations between agents, which might be code, human interaction, or models. 

That seems very sound, but I found the way Autogen maps tools use onto a conversation very strange. One agent suggests the function call and the other actually makes the call and returns the results to the first. I came in with the expectation that an agent has a job, that job entails using some tools. Go do the job, use the tools needed, and come back when it's done. It took a while to wrap my brain around the separation between suggesting and executing the tool.

### Red teaming LLMs

The two labs related to attacking and defending LLMs were super-fun. To convince GPT-4o-mini to reveal a secret key, I concocted an absurd story about tech intern Bilbo Baggins and the wise and powerful wizard Gandalf who utters ancient spells encoded in base 64. Turns out, attacking is easier than defending.

## Hackathon

The [LLM Agents Hackathon][301] wraps up on December 17th, 2024 @11:59PM PST.

I wanted to do a medication chatbot — RAG on prescription drugs. The problem with that is that current language models know a lot about prescription drugs. It's hard to come up with questions that the frontier models don't consistently answer perfectly. Here are some resources:

- [Accuracy of a chatbot in answering questions that patients should ask before taking a new medication][202]
- [PharmaBulaBot: A Chatbot to Answer Drug Questions Based on Information from Pharmaceutical Package Inserts][203]
- [Medical ChatBot][204]
- [ClinCalc Top 300 Drugs of 2022][205]

Issues with this idea:

- What lift do you get from RAG?
- How to avoid helping with drug seeking?

## Additional resources

- Hamel Husain's [LLM fine-tuning][1] class
- [LLM Powered Autonomous Agents][6], by Lilian Weng from June, 2023


[1]: https://parlance-labs.com/education/
[2]: https://llmagents-learning.org/f24
[3]: https://dawnsong.io/
[4]: https://jungyhuk.github.io/
[5]: https://rdi.berkeley.edu/llm-agents-hackathon/
[6]: https://lilianweng.github.io/posts/2023-06-23-agent/

[101]: https://arxiv.org/abs/2201.11903
[102]: https://press.princeton.edu/books/paperback/9780691164076/how-to-solve-it
[103]: https://www.nature.com/articles/s41593-024-01607-5
[104]: https://www.anthropic.com/news/announcing-our-updated-responsible-scaling-policy

[202]: https://doi.org/10.1016/j.japh.2024.102110
[203]: https://dl.acm.org/doi/abs/10.1145/3592813.3592890
[204]: https://www.johnsnowlabs.com/medical-chatbot/
[205]: https://clincalc.com/DrugStats/Top300Drugs.aspx

[301]: https://rdi.berkeley.edu/llm-agents-hackathon/
