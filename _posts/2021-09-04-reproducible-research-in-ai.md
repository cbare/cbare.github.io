---
layout: post
title:  "Reproducible Research in AI"
date:   2021-09-04 14:30:00 +1300
categories: machine-learning mlops gurus
---

[Joelle Pineau][1], of [Facebook AI Research][2] and McGill University, is an AI researcher studying planning and learning algorithms applied to robotics, health care, games, and conversation. She put together this awesome, if exacting, [reproducibility checklist][4] and ran a [reproducibility challenge at NeurIPS 2019][5]. Read the Nature interview here: [This AI researcher is trying to ward off a reproducibility crisis][3].

![Reproducibility Checklist]({{ "/images/reproducibility_checklist.png" | absolute_url }}){:style="margin: 0px 18px 18px 18px; width: 90%"}

The [mission to encourage reproducibility][7] gets at the question of how to do peer review in the age of arxiv. One frustrated researcher started [papers without code][8] as the naming-and-shaming mirror image of [paperswithcode][9].

Laying bricks onto the temple of science assumes the ability to build on the work of others. Once we've mastered the art of fully specifying computational methods, including source code and dependencies, data availability, and [data quality][10], then the frontier shifts to disentangling questions of [same data, different conclusions][6].

Having worked toward [reproducible research in life-science][11] in a past life, it's great to see this kind of effort in the AI community.


[1]: https://www.cs.mcgill.ca/~jpineau/
[2]: https://ai.facebook.com/people/joelle-pineau/
[3]: https://www.nature.com/articles/d41586-019-03895-5
[4]: https://www.cs.mcgill.ca/~jpineau/ReproducibilityChecklist.pdf
[5]: https://arxiv.org/abs/2003.12206
[6]: https://www.sciencedirect.com/science/article/pii/S0749597821000200
[7]: https://bdtechtalks.com/2021/03/01/papers-without-code-machine-learning-reproducibility/
[8]: https://www.paperswithoutcode.com/
[9]: https://paperswithcode.com/
[10]: https://stackoverflow.blog/2021/09/13/why-your-data-needs-a-qa-process/
[11]: https://sagebionetworks.org/
