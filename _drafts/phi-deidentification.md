---
layout: post
title:  "De-identifying PHI"
date:   2024-05-20 12:55:00 +1300
categories: technology healthcare medicine
---

Potential benefits of applying technology to healthcare are huge but privacy is a big concern.

To make it safer to work with protected health information, HIPAA defines acceptable standards of [de-identification][7]. The HIPAA Safe Harbor rule defines [18 identifying data fields][15] that must be removed. Techniques for de-identifying while preserving desirable properties include:

- hashing
- bucketing or binning
- shifting dates
- scrubbing of extreme or rare values
- aggregates


## Review papers

- [Natural Language Processing for Enterprise-scale De-identification of Protected Health Information in Clinical Notes][1]
- [A Comparative Study of De-identification Tools to Apply to Free-Text Clinical Notes][3]


## Free text de-identification

### Philter

Philter is a project out of [UCSF's Bakar Computational Health Sciences Institute][11] led by Atul Butte. It's mostly a pile of regular expressions but also uses [NLTK][12] for part-of-speech tagging. There's experimental code that does named-entity resolution (NER), but that appears unused.

#### Papers

- [A certified de-identification system for all clinical text documents for information extraction at scale][4] - Lakshmi Radhakrishnan, Gundolf Schenk, Kathleen Muenzen, Boris Oskotsky, Habibeh Ashouri Choshali, Thomas Plunkett, Sharat Israni, Atul J Butte, Oct 2023
- [Protected Health Information filter (Philter): accurately and securely de-identifying free-text clinical notes][5]

#### Philter-lite

The UCSF version of Philter looks unmaintained. Some good folks have created a fork called [Philter-lite][10] that cleans up the code and fixes a bunch of issues. That version worked well for me.

### Other options

I was hoping to find a solution based on [spaCy][13] but didn't find something really comparable to Philter. There's a thing called [medspaCy][14] that does NER on medical text, but not de-identification.

- [scrubadub_spacy][2] - PII, not PHI
- [OpenDeID Deidentification Algorithm][6] BERT model plus rules.
- [DeID-GPT: Zero-shot Medical Text De-Identification by GPT-4][8]
- Microsoft's [Azure Health Data de-identification service][9]



[1]: https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9285160/
[2]: https://spacy.io/universe/project/scrubadub_spacy
[3]: https://dl.acm.org/doi/abs/10.5555/3566055.3566077
[4]: https://academic.oup.com/jamiaopen/article/6/3/ooad045/7219298
[5]: https://www.nature.com/articles/s41746-020-0258-y
[6]: https://www.jmir.org/2023/1/e48145/PDF
[7]: https://www.hhs.gov/hipaa/for-professionals/privacy/special-topics/de-identification/index.html
[8]: https://arxiv.org/pdf/2303.11032
[9]: https://techcommunity.microsoft.com/t5/healthcare-and-life-sciences/announcing-a-de-identification-service-for-health-and-life/ba-p/3949712
[10]: https://github.com/SironaMedical/philter-lite
[11]: https://bakarinstitute.ucsf.edu/
[12]: https://www.nltk.org/index.html
[13]: https://github.com/medspacy/medspacy
[14]: https://spacy.io/
[15]: https://www.johndcook.com/blog/hipaa-identifiers-explained/
