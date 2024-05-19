---
layout: post
title:  "De-identifying PHI"
date:   2024-05-20 12:55:00 +1300
categories: technology healtcare medicine
---

Potential benefits applying technology to healthcare are large, as is the risk. For that reason, Healthcare lags in it's adoption of technology and the state of data is healthcare is messy.

To make it safer to work with protected health information, HIPAA defines acceptable levels of [de-identification][7].

- hashing
- bucketing or binning, for example ages to decade or dates to week or month.
- scrubbing of extreme or rare values
- aggregates

[Natural Language Processing for Enterprise-scale De-identification of Protected Health Information in Clinical Notes][1]

[A Comparative Study of De-identification Tools to Apply to Free-Text Clinical Notes][3]

[scrubadub_spacy][2]

[A certified de-identification system for all clinical text documents for information extraction at scale][4]
Lakshmi Radhakrishnan, Gundolf Schenk, Kathleen Muenzen, Boris Oskotsky, Habibeh Ashouri Choshali, Thomas Plunkett, Sharat Israni, Atul J Butte
Oct 2023

[Protected Health Information filter (Philter): accurately and securely de-identifying free-text clinical notes][5]

[OpenDeID Deidentification Algorithm][6]

[DeID-GPT: Zero-shot Medical Text De-Identification by GPT-4][8]


[1]: https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9285160/
[2]: https://spacy.io/universe/project/scrubadub_spacy
[3]: https://dl.acm.org/doi/abs/10.5555/3566055.3566077
[4]: https://academic.oup.com/jamiaopen/article/6/3/ooad045/7219298
[5]: https://www.nature.com/articles/s41746-020-0258-y
[6]: https://www.jmir.org/2023/1/e48145/PDF
[7]: https://www.hhs.gov/hipaa/for-professionals/privacy/special-topics/de-identification/index.html
[8]: https://arxiv.org/pdf/2303.11032
