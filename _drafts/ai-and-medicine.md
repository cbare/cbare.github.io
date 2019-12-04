---
layout: post
title:  "AI and medicine"
date:   2019-06-10 9:15:00 -0800
categories: machine-learning deep-learning health-tech
---

The practice of medicine entails quickly making high-stakes decisions based on incomplete and uncertain information. Somewhat belatedly, medicine is getting to the point where there's enough machine-readable data to start applying algorithms that learn from data. At the same time, the algorithms are racing ahead.

For medicine, at least the parts visible to public, the human-in-the-loop approach is going to be a lot more palatable for some time to come. Machines may outperform humans at tasks like staging cancer from lung x-rays. Humans remain better at the metacognition tasks, like "hey, this is an image of the wrong patient's lung" or "hey, this is an image of the exam room floor."

Some technologies displace older technologies, others interoperate with the existing system. In general, the later approach is more likely to succeed, and I think this will prove especially true in health-care. But, no technology will succeed by adding one more thing onto the backs of [already overburdened docs][10].


## AI in Medicine


Eric Topol writes on [the convergence of human and artificial intelligence][2] (paraphrased due to compulsive copy editing on my part):

> Medicine is at the crossroads of two major trends. The first is a failed business model, with increasing expenditures and deteriorating outcomes. The second is the massive quantities of data from sources such as high-resolution medical imaging, biosensors with continuous output of physiologic metrics, genome sequencing, and electronic medical records.

> The limits on analysis of such data by humans alone have clearly been exceeded, necessitating an increased reliance on machines. Accordingly, at the same time that there is more dependence than ever on humans to provide healthcare, algorithms are desperately needed to help. Yet the integration of human and artificial intelligence for medicine has barely begun.

Jeff Dean and co-authors from Stanford and Google offer [A guide to deep learning in healthcare][1], a nice overview of areas where deep learning is being applied - computer vision, NLP on medical records, and sequence analysis.


## Drug development

While the above work focuses on clinical practice, another layer of healthcare facing diminishing returns is drug development with costs spiraling and high-profile drug trails ending in failure.

The founding idea of Sage Bionetworks (my former gig) was a run at this problem using the toolkit of open-data / open-science.

Recently announced partnerships between pharma and health-tech focus on different steps on the path from the lab and the pharmacy. [Glaxo's $300 million investment in 23andMe][6] given the pharma giant access to 5 million genotypes from which to mine “genetically validated targets” and develop drugs. [Novartis, Otsuka, Pfizer and Sanofi have formed a strategic alliance to run clinical trials with Verily][5].

Daphne Koller's new venture, [insitro][3], is constructing a highly automated [bio-data-factory][4] with the aim of building a data pool that will enable machine-learning to support decisions early in the drug development pipeline. They won't be the only only ones trying to [bring AI to pharma and drug development][9].



“Care traffic control”: A patient-relationship platform that sits atop otherwise disconnected systems (EHR, wearables, etc.) providing a coordinated view across the healthcare ecosystem delivering a more coordinated, tailored patient experience at a lower total cost of care.

https://hbr.org/2019/10/how-new-health-care-platforms-will-improve-patient-care



[1]: https://www.nature.com/articles/s41591-018-0316-z
[2]: https://www.nature.com/articles/s41591-018-0300-7
[3]: http://www.insitro.com/
[4]: https://www.youtube.com/watch?v=uyLT7EfWmsg
[5]: https://www.biospace.com/article/releases/verily-forms-strategic-alliances-with-novartis-otsuka-pfizer-and-sanofi-to-transform-clinical-research/
[6]: https://www.nbcnews.com/health/health-news/drug-giant-glaxo-teams-dna-testing-company-23andme-n894531
[7]: /2019-05-31/multi-omic-studies.html
[8]: /2018-08-24/data-health-tech-companies.html
[9]: https://www.ft.com/content/e450a688-ddfb-11e8-b173-ebef6ab1374a
[10]: https://www.nytimes.com/2019/06/08/opinion/sunday/hospitals-doctors-nurses-burnout.html




https://www.nytimes.com/2019/11/14/technology/apple-harvard-health-studies.html


Google's 'Project Nightingale'
https://www.wsj.com/articles/google-s-secret-project-nightingale-gathers-personal-health-data-on-millions-of-americans-11573496790

Google, new owner of Fitbit, has made a deal with Ascension, the second-largest health system in the U.S. giving it access to health records of millions of Americans. This adds to another deal with Mayo Clinic.


WSJ Your Health Data Isn’t as Safe as You Think

