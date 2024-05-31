# How to fail at machine learning

So, you've got some data. Prototype models are looking promising. You might be on your way to AI unicorn billions. What could go wrong? Well, a few things.

## Overreach

Self-driving cars, replacing radiologists with AI... They haven't happened in the time-frames imagined a few years ago. They may well happen at some point, but not this year or next. The point is that it's quite hard to judge in advance the tractability of a problem. The next increment in performance might be exponentially harder than the previous one.

Framing a problem into a tractable form is an underrated part of machine learning.

## Data quality

The main ingredient of ML is data. But, that data comes from somewhere. The business process or research protocol that led to that dataset probably deviates an ideal randomized trial either a little bit or a lot. More than likely, your model is a new use-case for existing data and may expose quirks, bugs, or even show-stopping limitations. Forgetting to factor in time and resources for data cleaning can easily lead to missed deadlines.

Worse yet, major quality issues may yield misleading models. Is your data viable or a mess? This needs to be validated early, before lots of work goes into a lost cause.

AI can't create something from nothing. Garbage in, garbage out.

## Throwing models over a wall

Some AI practitioners view themselves as above petty product and engineering concerns. They see their job as building models. Anything beyond that is someone else's problem.

This leads to research prototypes that fail to transition to production. On-call devs get burned once or twice and then start to push back. “If it's not production quality, it doesn't go into production,” as one colleague put it. Research code may be good enough to publish a paper, but it's probably not going to cut it in front of paying customers. Throwing buggy half-baked code over the wall with the expectation that another team will make it production-ready is a recipe for friction.

Instead, the same team should be responsible for bringing a feature from conception to production and also for ongoing iterating and extending.

## Risk aversion

Handling sensitive data is scary. A leak of personal information is embarrassing at best and a legal liability at worst. So, let's STRIDE-model all the things, erect trust boundaries, credential only a chosen few, and lock things down.

OK, security is important. But now you want to build a model. Getting access to the data requires running a gauntlet of technically challenging security protocols and beaurocratic organizational barriers. Your overpaid ML experts are sitting around waiting for some committee to approve access.

How do you get the benefits of open and democratized data without hopeless insecurity? How do you reduce risk without creating a tarpit? One key strategy is deidentification and anonymization. Replacing names and identifiers with opaque tokens or hashed values goes a long way and can be readily automated. Dates are especially tricky, because they can reidentify individuals and are considered PHI under HIPAA, but are needed for reporting weekly or monthly aggregates and looking at trends over time.

Modern data environments provide different views tailored to specific roles. They can solve date issues by allowing aggregates only above some threshold of members or displaying a low-precision views of individual records. It's useful to think in terms of zones where higher levels of risk correspond to greater limitations on access. Sensitive data belongs in a restricted zone. Anonymized and aggregated data can live in an open zone.

Synthetic data is a great strategy in cases where it can be generated algorithmically or through crowd-sourcing. It can be made available without worries, even in public Kaggle-style challenges, and often comes with known ground truth.

Trustworthy ethical handling of data is important. Getting anything done entails risk. 
  - benefit rather than exploit data donors
- synthetic data
- privacy vault

## Immature development process

Machine learning has been called the high-interest credit card of technical debt. Pairing ML with a weak engineering process is asking for trouble. Continuous delivery is

## Failure to establish feedback

How do you know if a model is working?


https://github.com/dair-ai/MLOPs-Primer
https://www.oreilly.com/library/view/machine-learning-design/9781098115777/
https://www.xyonix.com/blog/10-reasons-why-ai-innovation-fails-according-to-an-ai-consultant
