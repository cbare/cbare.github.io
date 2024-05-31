---
layout: post
title:  "Designing a modern data platform"
date:   2023-10-08 13:40:00 +1300
categories: software-engineering data
---

Designing a modern data platform is a tricky propostion. Consider the number of moving parts in this diagram stolen from here: [What is the modern data stack?][8]

![Modern Data Stack]({{ "/images/datrick-modern-data-stack-m6LoVLnrE5UPOKQa.avif" | absolute_url }})






cloud DBs - Snowflake, Redshift, Big Query


[The Modern Data Stack: Past, Present, and Future][9]
Tristan Handy  December 1, 2020

dbt 

[Best practice guides][5], [How we structure our dbt projects][4]


[Designing Data-Intensive Applications by Martin Kleppman][7]


## Is Kimball-style data modeling still relevant?

[Is Kimball dimensional modeling still relevant in a modern data warehouse?][6] My inclination is towards not, though I'm not super confident in that conclusion.

[To quote Kimball, "Dimensional modeling begins by dividing the world into measurements and context."][1] My understanding is that labeling tables as fact or dimension is based on the idea that we're going to compute aggregates on the facts and the dimensions will appear in 'where' and 'group by' clauses. 

A typical example is that you're a retailer and you want to slice and dice sales along dimensions like time, geography, product line, and organizational hierarchy. You want to figure out what bonus a regional sales director gets for last quarter. Which product lines sell well in the Northwest? We're in a fairly well defined problem space where the queries you're going to ask mostly have a similar shape.

### Performance

My guess is that part of the original motivation behind facts and dimensions is to get decent performance for these types of queries on row-oriented relational databases. Fact tables consist mostly of numeric data and foreign keys into the dimensions, which could be indexed. These days, we have column-oriented distributed databases like Snowflake, Redshift, and Big Query. Where row-oriented DBs needed some help, columnar DBs eat big aggregation queries for breakfast. So, my guess is the performance argument has faded away.

### Changing requirements

It's my experience that data science, research, and machine learning use-cases lead to open-ended questions that are harder to predict in advance. If we give up the assumption that we know what the questions are, can we so easily decide what is a fact and what is a dimension? Or is one query's fact another query's dim? Modeling the domain - it's entities and the relations among them - should provide more generalizable utility rather than optimizing up-front for what we've assumed are the right questions.


## Layers of refinement

The idea of having levels of increasing refinement seems popular. The "raw" level is "as-is" warts and all with little or no cleaning. Additional layers are constructed by transforms that perform cleaning, validation, and reconciling different data sources.

I like [Randy's "chaos modeling special blueprint"][2], in his words, lightly edited by me:

1. Raw - Ingest as raw with Fivetran / Stitch / Matillion / Custom Stages, making sure to have an ingestion time and pulling out expected predicate columns if they’re packed in a variant. Strongly prefer append-only ingestion when possible.
2. Stage - The most basic cleaning - timestamp conversion, upper/lowercasing of strings, null fills, maybe some basic mapping (like mapping AWS Account Id values to human-readable names using a case statement). These are often views.
3. Analytics - Working from the end of the pipeline, identify use case / pain points and determine the data required for this. Anything a BI tool will hit should be materialized as a table and should have human-readable names. Schemas and databases at this level should also be human-readable with schemas split by business function or access level.
4. Curated - Iteratively apply DRY concepts to pull useful models out of individual end-table computations and into a curated layer.

"Prefer to focus efforts on understanding users and delivering value early and intentionally leveraging technical debt. If we feel the pain of the technical debt, it’ll be due to [usage] so we can address modeling needs after we’ve delivered value. If we don’t feel the pain, then we avoided a costly modeling engagement and can spend all our cycles iterating on use cases to find ways to deliver real value."

## Growing a data platform

One issue the big diagram above leaves as an exercise for the reader is how to get from zero, or more realistically a shambles of fragile legacy hacks, to a nice clean modern system with a dozen thoughtfully selected components?



I like the demand driven, as-needed approach where you put effort into real use-cases and avoid modeling for the sake of modeling.




[1]: https://www.kimballgroup.com/2003/01/fact-tables-and-dimension-tables/
[2]: https://discourse.getdbt.com/t/is-kimball-dimensional-modeling-still-relevant-in-a-modern-data-warehouse/225/7
[3]: https://discourse.getdbt.com/t/is-kimball-dimensional-modeling-still-relevant-in-a-modern-data-warehouse/225
[4]: https://docs.getdbt.com/guides/best-practices/how-we-structure/1-guide-overview
[5]: https://docs.getdbt.com/guides/best-practices
[7]: https://dataintensive.net/
[8]: https://hevodata.com/learn/what-is-the-modern-data-stack/
[9]: https://www.getdbt.com/blog/future-of-the-modern-data-stack
