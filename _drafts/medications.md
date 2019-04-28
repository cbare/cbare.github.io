---
layout: post
title: "Computing on medications and supplements"
date: 2018-07-09 11:55 -0700
categories: data-science
---



This article on [Making Sense of Drug Classification](https://www.verywellhealth.com/drug-classes-1123991) is a great place to start.

There are at least four different ways of classifying medications:

* *indication or therapeutic use*, meaning the types of condition they are used to treat
* *mechanism of action*, meaning the specific biochemical reaction that occurs when you take a drug
* *mode of action*, meaning the specific way in which the body responds to a drug
* *chemical structure*

The [ATC classification system](https://www.whocc.no/atc/structure_and_principles/) from the World Health Organization (WHO) classifies substances into a hierarchy with five levels.


Download costs €200.

[RxNorm](https://www.nlm.nih.gov/research/umls/rxnorm/) provides normalized names for clinical drugs and links its names to many of the drug vocabularies commonly used in pharmacy management and drug interaction software, including those of First Databank, Micromedex, Gold Standard Drug Database, and Multum. The web interface for RxNorm is [RxNav](https://mor.nlm.nih.gov/RxNav/search?searchBy=String&searchTerm=metoprolol).

[RxClass](https://mor.nlm.nih.gov/RxClass/) is a classification maintained by the US NLM.


[USP Drug Classification](http://www.usp.org/health-quality-safety/usp-drug-classification-system)


Project: track usage of medications and supplements

FDA National Drug Code (NDC).
Supplements are not regulated by the FDA. 

[Dietary Supplement Label Database (DSLD)](https://dsld.nlm.nih.gov/dsld/).

Data quality.
 people don't know what they're taking
 communicating is hard
   - nomenclature
     - generic vs proprietary
     - chemical naming
   - drug classification


http://clincalc.com/DrugStats/

https://www.drugbank.ca/


Bar codes
 FDA regulated meds have NDC bar codes
 supplements bar coded with UPC code


Drug-drug interactions
Drug-supplement interactions




Medication Adherence: WHO Cares?
Marie T. Brown, MD and Jennifer K. Bussell, MD
https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3068890/


ADHERENCE TO LONG-TERM THERAPIES
Evidence for action
WHO 2003
https://apps.who.int/iris/bitstream/handle/10665/42682/9241545992.pdf


Adherence to Medication
Lars Osterberg, M.D., and Terrence Blaschke, M.D.
https://www.nejm.org/doi/full/10.1056/NEJMra050100


The Language of Medication-Taking
John F. Steiner, MD, MPH; Mark A. Earnest, MD
https://annals.org/aim/article-abstract/713531/language-medication-taking



