---
layout: post
title:  "Machine learning engineering"
date:   2019-10-20 12:15:00 -0800
categories: machine-learning deep-learning software-engineering data-engineering
---


![Programming vs machine learning]({{ "/images/programming_vs_machine_learning.png" | absolute_url }})





A Few Useful Things to Know about Machine Learning. Pedro Domingos



If you engineer your product to scale right from the start, you'll probably never get to the point where it matters.



The discipline of software engineering is young compared to, say, building bridges. But the software engineering is relatively mature compared to engineering learning systems.

The toolbox of software engineering tools - modularity, testing, code review, etc. - was developed for systems that transform inputs to outputs through algorithms hand coded by humans. That toolbox still applies when the algorithm is learned from data, but some different concerns come into play.

Verifying properties of the training data.
Testing in the presence of non-determinism.
Assessing performance at training time.
Monitoring performance in production.


[Machine Learning: The High Interest Credit Card of Technical Debt][1]
[What’s your ML Test Score? A rubric for ML production systems][2]
[Software Engineering for Machine Learning: A Case Study][4]
[Safe and Reliable Machine Learning][3]
[Trials and Tribulations of Developers of Intelligent Systems][5]


[The morning paper][103] covered papers on machine-learning engineering from [Airbnb][102] and [Booking.com][104]
[Applying Deep Learning To Airbnb Search][101]

You need to be this tall:
Note that the Airbnb team already had experience with machine learning, data pipelines in place, and an online controlled experiment platform available. From this foundation, they took their first steps towards neural networks.

Google's [Rules of ML][105]


[Top 10 data engineering mistakes][201], [slides][202] by
Lars Albertsson based on experience in data-lakes scenarios using Spark, Luigi, and AirFlow with the goal of enabling new work patterns for innovative uses of data

| mistake                             | remedy                                                                 |
+-------------------------------------+------------------------------------------------------------------------+
| Weak workflow orchestration         | use Luigi or AirFlow                                                   |
| New Technology / old patterns       | work patterns >> technology                                            |
| Deviate from functional principles  | Immutability, idempotency, reproducibility                             |
| Weak online / offline separation    | careful handover                                                       |
| Premature scaling                   | go to distributed only when cost is justified                          |
| Reading all the data                | incremental                                                            |
| Premature streaming                 | go to streaming only when cost is justified                            |
| Crunching in the dark               | instrument pipelines, measure unexpected values, consistency           |
| Weak agility                        | end-to-end testing, reduce needless heterogeneity in tools and formats |
| Late governance                     | consider security, compliance, testing, schema evolution               |



[Functional Data Engineering - A Set of Best Practices][301] (2018) talk by [Maxime Beauchemin][302] creator of [Airflow][303].

[Rob Story][402] on [Data Engineering Architecture][401] with Redshift.


Data quality dimensions
 - timeliness
 - correctness
 - completeness
 - consistency



Ask HN: What is your ML stack like?
https://news.ycombinator.com/item?id=21516311



Steps
 - What is the goal or question?
 - Is data available and of sufficient quality to answer the question?
 - Alternatives?
 - Is model performance, precision / recall sufficient?
 - Operational concerns
 - Action or intervention
 - Evaluation in production, real outcomes
 - Risks
 - Ethics / privacy / unintended consequences




[1]: https://ai.google/research/pubs/pub43146
[2]: https://ai.google/research/pubs/pub45742
[3]: https://arxiv.org/abs/1904.07204
[4]: https://www.microsoft.com/en-us/research/publication/software-engineering-for-machine-learning-a-case-study/

[5]: http://web.engr.oregonstate.edu/~burnett/reprints.html


[101]: https://arxiv.org/abs/1810.09591
[102]: https://blog.acolyer.org/2019/10/09/applying-deep-learning-to-airbnb-search/
[103]: https://blog.acolyer.org
[104]: https://blog.acolyer.org/2019/10/07/150-successful-machine-learning-models/
[105]: https://developers.google.com/machine-learning/guides/rules-of-ml
[201]: https://berlinbuzzwords.de/18/session/top-10-data-engineering-mistakes
[202]: https://www.slideshare.net/lallea/top-10-data-engineering-mistakes


[301]: https://www.youtube.com/watch?v=4Spo2QRTz1k
[302]: https://medium.com/@maximebeauchemin
[303]: https://airflow.apache.org/

[401]: https://www.youtube.com/watch?v=9nX35zrN20E
[402]: https://twitter.com/oceankidbilly


[501]: https://www.thoughtworks.com/insights/blog/coding-habits-data-scientists
[502]: https://www.microsoft.com/en-us/research/project/guidelines-for-human-ai-interaction/
