---
layout: post
title:  "Data Engineering"
date:   2019-06-27 11:51 -0800
categories: data-engineering
---


A guide to building a data pool and an environment on which to do research.


- big picture goals
- how will goals evolve?
- how frequently data should be refreshed
- data sources, quality, how collected? expected invariants in data


Learn from other technology companies.

[Data Quality at Airbnb][301][MIDAS process][302]

- Accuracy: Is the data correct?
- Consistency: Is everybody looking at the same data?
- Usability: Is data easy to access?
- Timeliness: Is data refreshed on time, and on the right cadence?
- Cost Efficiency: Are we spending on data efficiently?
- Availability: Do we have all the data we need?


Components of a modern data stack
- ingest
- query
- snapshots?
- models?
- quality and metrics?


Write-audit-publish pattern.





privacy, regulation, ethical issues and anti-tech backlash


Pieces of infrastructure

Relational databases
key-value stores
object stores (S3)

Kafka
Spark
Flink
Beam


How to build and operate a data lake in cloud providers


https://www.waitingforcode.com/data-aws/doing-data-aws-overview/read

https://dataengweekly.com/index.html


[Podcast.__init__][102]
[Data Engineering podcast][103]

[Designing Data-Intensive Applications][1] Book
[A Beginner’s Guide to Data Engineering][2]


[Why your data needs a QA process][12]


## Tools

- [Apache Airflow][3]
- [Dagster][4]
- [Prefect][5]
- [fivetran][13]
- [dbt][6]
- [Great Expectations][7]
- [Dask][8]
- [Meltano][9]
- [DVC][10]
- [Pandas][11]


[1]: https://dataintensive.net/
[2]: https://medium.com/@rchang/a-beginners-guide-to-data-engineering-part-i-4227c5c457d7
[3]: https://airflow.apache.org/
[4]: https://dagster.io/
[5]: https://www.prefect.io/
[6]: https://www.getdbt.com/
[7]: https://github.com/great-expectations/great_expectations
[8]: https://dask.org/
[9]: https://meltano.com/
[10]: https://dvc.org/
[11]: https://pandas.pydata.org/
[12]: https://stackoverflow.blog/2021/09/13/why-your-data-needs-a-qa-process/
[13]: https://fivetran.com/

[101]: https://talkpython.fm/episodes/show/302/the-data-engineering-landscape-in-2021
[102]: https://www.pythonpodcast.com/
[103]: https://www.dataengineeringpodcast.com/


[201]: https://www.youtube.com/watch?v=AG56ThOMBwo

[301]: https://medium.com/airbnb-engineering/data-quality-at-airbnb-e582465f3ef7
[302]: https://medium.com/airbnb-engineering/data-quality-at-airbnb-870d03080469

https://www.getdbt.com/blog/future-of-the-modern-data-stack/
https://www.blef.fr/
https://www.dataengineeringweekly.com/
https://roundup.getdbt.com/
https://metadataweekly.substack.com/
https://datatalks.club/
https://allhandsondata.substack.com/
https://datastackshow.com/
https://www.youtube.com/airbytehq
https://www.youtube.com/c/andreaskayy
