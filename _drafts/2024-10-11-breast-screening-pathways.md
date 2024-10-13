---
layout: post
title:  "Breast cancer screening clinical pathways"
category: Health-tech and Biotechnology
---

> [Comparison of AI-integrated pathways with human-AI interaction in population mammographic screening for breast cancer][1]
> Helen ML Frazer et al, Nature Communications, 2024

This paper from a team of researchers in Australia, asks a smart question - how best to integrate AI readers into clinical workflows?

In retrospective simulation, the paper takes the the standard of care in Australia, which is double read with arbiration in cases of disagreement, and compares that against AI alone and several configurations of human readers:

## Screening episode flows for the current reader system and AI-integration scenarios

- Standard of care: double read with arbitration
- AI stand-alone
- AI with single human reader
- AI reader-replacement: AI and human reader with arbitration
- AI band pass: AI makes easy calls, sends harder calls to double read with arbitration
- AI triage: AI triages between single human reader and double read with arbitration

[![Screening episode flows for the current reader system and AI-integration scenarios.]({{ "/images/breast-screening-pathways.png" | absolute_url }}){:style="width: 86%; margin: 2em 2em;"}](https://www.nature.com/articles/s41467-024-51725-8/figures/1)

The study also models, albeit simply, Human-AI interactions which may be complementary or introduce detrimental bias.

The study uses an in-house computer-vision model called BRAIx AI Reader, which they describe as “an ensemble of modern deep-learning neural networks and trained on millions of screening mammograms. We studied and created an ensemble from ResNet, DenseNet, ECA-Net, EfficientNet, Inception, Xception, ConvNext and four model architectures developed specifically for our problem, including two multi-view models that use two mammographic views of the same breast concurrently, and two single-image interpretable models that provide improved prediction localisation and interpretability.”

The result is insight into how different workflows impact sensitivity, specificity, cost, and workload.

Questions:

- Would the conclusions be robust across differnt models or change according to the characteristics of different AI models?
- Can humans and AIs be trained to spot each others mistakes, effectively boosting between human and AI?
- How do these workflows lend themselves to collecting high-value training data - the cases the models get wrong and expert-consensus annotations or better yet, ground truth, for those cases?

[1]: https://www.nature.com/articles/s41467-024-51725-8
