---
layout: post
title:  "Blood protein as predictive markers of future disease"
category: Health-tech and Biotechnology
tags: biology cancer
---

Information flows in the cell from DNA to RNA to protein and ultimately to phenotype. The project of modern biology is to understand each of those steps in sufficient detail to predict future outcomes and intervene in beneficial ways. Predicting, preventing, or curing disease is just one example.

In recent months, a truckload of tasty research papers has been published based on data from advanced proteomic technologies. Proteins are a critical piece of the puzzle because they are the machinery of the cell. While the genome gives information on potentialities and predispositions, what might happen, proteins are a window into what's happening right now.

## History

![Arivale]({{ "/images/Arivale_Logo-300x134.jpg" | absolute_url }})
{:style="float: right; margin: 18px 18px 18px 18px; width: 204px; height: 85px;"}

A couple of jobs and 6-ish years ago, I sat in the Dexter Horton building at a company called Arivale. The premise was to monitor human health like [aerospace engineers monitor airliner engines][7]. 

The company wasn't destined to make it off the runway, which is a sad tale for another time. But, the hope was that gathering [personal, dense, dynamic data clouds][9] from genetics, blood, saliva and microbiome at multiple time points would allow each participant to be an n-of-1 experiment in healthier living. Cynics called it an expensive way to get people to eat right and exercise and they weren't entirely wrong. But, we did assemble a very rich data set and the research team did some nice work.

The Arivale cohort contained lots of boringly healthy people. Good on 'em, but it's the sick data points that are the interesting ones. More valuable still are the rare glimpses that show the transition from healthy to sick.

Our researchers caught a few of those sneaky time points using proteomics technology from a Swedish biotech company called Olink. In 2020, after Arivale's demise, they published [Untargeted longitudinal analysis of a wellness cohort identifies markers of metastatic cancer years prior to diagnosis][2].

<figure>
    <img
      src="/images/blood-proteins/magis-ceacam-fig-1.webp"
      alt="Untargeted longitudinal analysis of a wellness cohort identifies markers of metastatic cancer years prior to diagnosis"
      >
    <figcaption style="font-size: small; font-style: italic;">“Longitudinal trajectories of selected outlier proteins across multiple cancer types in individuals. Plus (+) signs indicate the diagnosis date (if applicable) for that disease trajectory. Y-axis values are median absolute deviation (MAD). Unlabeled trajectories (grey lines) represent trajectories for all other samples in the study for that protein. (a) CEACAM5 was a persistent outlier in pre-diagnosis samples for two metastatic cancer individuals (lung and pancreatic) and exhibited rapid change to extreme outlier levels for metastatic breast cancer. One undiagnosed individual with skin lesions also exhibited elevated levels and fluctuating outlier status for CEACAM5. (b) CALCA was a persistent outlier in metastatic pancreatic cancer. (c) DLK1 was a persistent outlier in metastatic pancreatic cancer. (d) ERBB2 rapidly increased from low levels to outlier levels over a period of six months preceding the diagnosis of metastatic breast cancer.”
    </figcaption>
</figure>

While the _n_ was too small for big claims, the findings hint that you might be able to see a cancer diagnosis coming months or years in advance. Notably, the outlier proteins have very plausible links to cancer:

- [CEACAM5][8] functions in cell-cell adhesion and has known association with cancer.
- [DLK1][14] has a role as a regulator of cell growth and neuroendocrine differentiation.
- [ERBB2][15] is a synonym for HER2, a human epidermal growth factor receptor that promotes cell growth and is often overactive in breast cancer.


## Olink

![Olink]({{ "/images/blood-proteins/olink-logo.png" | absolute_url }})
{:style="float: right; margin: 18px 18px 18px 18px; width: 204px; height: 85px;"}

[Olink][16] calls it's proteomic technology [PEA for proximity extension assay][4]. (Extra points for the Gregor Mendel reference.) The company spun out of Ulf Landegren's lab at Uppsala University.

Their method works by growing up a pair of different antibodies to a particular target and binding each antibody with an DNA oligonucleotide. The two oligo's are complimentary, so if both antibodies bind, the strands anneal and you have a double-stranded DNA bar code. Amplifying and reading those bar codes results in a quantitative measure of relative abundance.

![Olink]({{ "/images/blood-proteins/pea-technology.png" | absolute_url }})
{:style="margin: 1em; width: 66%;"}



- Olink blood protein panels
- antibody linked to a short strand of DNA
    - uniquely barcodes each identified protein
    - can be read out quantitatively
- 15 panels of 96 proteins per panel
    - Cardiovascular (3)
    - Immuno-Oncology (2)
    - Neurology (2)
    - Oncology (2)
    - Inflammation (1)
    - Biological Process (5)

- Thermo Fisher acquired Olink for $3.1 billion, transaction completed in July 2024.


Affinity-based proteomics is cheap (relative to mass-spectrometry) and scalable. The catch is you have to know what you're looking for.


## UK Biobank

As Arivale demonstrated, building a big -omic data set with venture capital is hard. They probably don't have the patience to sustain the effort long enough. Verily has the benefit of Google's deep pockets.



“plasma proteomic measures can infer age, sex, BMI, blood groups, and renal and liver function with high predictive accuracy” [[Sun et al][10]]










Nautilus Biotechnology







[Cell-free DNA analysis in current cancer clinical trials: a review][903]

[UK Biobank: a globally important resource for cancer research][301]







- information flow in the cell
- Arivale history
  - Andrew Magis's paper
  - CEACAM

- Olink
  - technology
  - company

- Dense data clouds
  - All of us
  - Google/Alphabet [Verily baseline study][401]

- UK Biobank
  - part of the British National Health Service
  - cost and scale

- UK Biobank PPP
  - insight into the biology of aging and disease
  - risk prediction
  - drug targets

- research papers
  - genetics
  - disease
    - cancer
  - aging

- Beyond UKBB
  - 

## Papers


Largest dataset of thousands of proteins marks landmark step for research into human health
https://www.ukbiobank.ac.uk/learn-more-about-uk-biobank/news/dataset-of-thousands-of-proteins-marks-landmark-step-for-research-into-human-health


### Genetics

[Plasma proteomic associations with genetics and health in the UK Biobank][10], Sun & Whelan et al, Nature, October 2023. 

### Disease

[Blood protein assessment of leading incident diseases and mortality in the UK][11] Gadd et al, Nature Aging, 2024

Blood proteins predict the risk of many diseases years before onset
https://www.nature.com/articles/s41591-024-03145-w

### Cancer

[Identifying proteomic risk factors for cancer][1]
Keren Papier et al 15 May 2024

Next generation pan-cancer blood proteome profiling using proximity extension assay
https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10354027/



#### Breast Cancer

[Evaluation of circulating plasma proteins in breast cancer using Mendelian randomisation][12] Mälarstig et al, Nature Communications, 2023

#### Lung Cancer

The blood proteome of imminent lung cancer diagnosis
https://www.nature.com/articles/s41467-023-37979-8


### Aging


Proteomic aging clock predicts mortality and risk of common age-related diseases in diverse populations
Argentieri et al, Nature Medicine, 2024




Mapping biological influences on the human plasma proteome beyond the genome
Carrasco-Zanini et al, Nature Metabolism, 2024


Large-scale plasma proteomics comparisons through genetics and disease associations
https://www.nature.com/articles/s41586-023-06563-x


As a clinical test, taking a vial of blood is much less unpleasant than tissue biopsy.

Similar to cell-free nucleic acid




[1]: https://www.nature.com/articles/s41467-024-48017-6
[2]: https://www.nature.com/articles/s41598-020-73451-z
[3]: https://www.biorxiv.org/content/10.1101/2022.05.02.490328v3
[4]: https://olink.com/our-platform/our-pea-technology/
[5]: https://olink.com/technology/pea-technology-video
[6]: https://olink.com/
[7]: https://jamanetwork.com/journals/jama/article-abstract/2715165
[8]: https://www.uniprot.org/uniprotkb/P06731/entry
[9]: https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5568837/
[10]: https://www.nature.com/articles/s41586-023-06592-6
[11]: https://www.nature.com/articles/s43587-024-00655-7
[12]: https://www.nature.com/articles/s41467-023-43485-8
[13]: https://www.nature.com/articles/s42255-024-01133-5
[14]: https://www.genecards.org/cgi-bin/carddisp.pl?gene=DLK1
[15]: https://www.uniprot.org/uniprotkb/P04626/entry
[16]: https://olink.com/


[201]: https://www.khanacademy.org/science/ap-biology/gene-expression-and-regulation/translation/a/intro-to-gene-expression-central-dogma
[202]: https://www.msdmanuals.com/home/fundamentals/genetics/genes-and-chromosomes

[301]: https://www.nature.com/articles/s41416-022-02053-5

[401]: https://www.projectbaseline.com/
[402]: https://allofus.nih.gov/

[501]: https://www.ukbiobank.ac.uk/learn-more-about-uk-biobank/news/uk-biobank-launches-one-of-the-largest-scientific-studies
[502]: https://www.ukbiobank.ac.uk/learn-more-about-uk-biobank/news/dataset-of-thousands-of-proteins-marks-landmark-step-for-research-into-human-health


[901]: https://www.resolutionbio.com/
[902]: https://grail.com/
[903]: https://www.nature.com/articles/s41416-021-01696-0
