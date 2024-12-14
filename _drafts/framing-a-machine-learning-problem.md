---
layout: post
title:  "Framing a machine learning problem"
date:   2018-04-28 13:05 -0800
categories: machine-learning python
---

I think you need to describe your problem more precisely to get any serious advice:
 - What does your existing data look like.  What is the target of prediction (if any), what other measurements do you have available for predictors.
 - Are there any other supplementary data sources available?
 - What patterns do you already suspect lie in the data?  What is the state of your domain knowledge on the problem?
 - What is currently known about the solution to your problem?  Is this a totally new thing, or is there an existing solution you are looking to improve?
 - What is the goal.  To automate decisions?  To automate some decisions and flag others for review?  To infer something about the genes themselves?


Is there a simple rule or heuristic that solves the problem reasonably well?


Build your first system quickly, then iterate

1. Set up train, dev, and test sets
2. Define metric
3. Build quick and dirty baseline model
4. Bias / Variance analysis
5. Error analysis



What metric will we used to assess the performance of any model?
What data will be required?
Will data annotation be required?
What will be the input to the model?
What is the desired specific output?
Does a human currently perform this task? What is human-level performance?
What is the minimum acceptable model performance to make the model useful?

If successful, is there a plan to productionize the model into a product?
Are there specific bias’s we should measure and report on as part of developing this model? What is the potential for the model to cause harm?
