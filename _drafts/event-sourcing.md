---
layout: post
title:  "Event Sourcing and CQRS"
date:   2021-05-26 10:35:00 +1300
categories: software-engineering data-engineering
---

The code-ish podcast episode [105: Event Sourcing and CQRS][1] from December, 2020 hosted by Robert Blumen with guest Andrzej Ludwikowski kept me company on my


Event logs are the source of truth.

Command Query Responsibility Segregation (CQRS)


Greg Young



“Turning the database inside out” was a phrase coined by Martin Kleppmann. Essentially it is the idea that a database has a number of core components—a commit log, a query engine, indexes, and caching—and rather than conflating these concerns inside a single black-box technology like a database does, we can split them into separate parts using stream processing tools and these parts can exist in different places, joined together by the log. So Kafka plays the role of the commit log, a stream processor

Designing Event-Driven Systems by Ben Stopford






[Data on the Outside versus Data on the Inside][2]
Pat Helland








Double-entry book keeping.

Turning your database inside out.

Inside a relational database, writes are made first to a journal, which is its internal source of truth. Updates can be replayed to update tables in the event of failure.



[Event streaming as the source of truth][4]


[New Directions in Cloud Programming][7] by Alvin Cheung, Natacha Crooks, Joseph M. Hellerstein, and Matthew Milano at Berkeley





[1]: https://www.heroku.com/podcasts/codeish/105-event-sourcing-and-cqrs
[2]: http://cidrdb.org/cidr2005/papers/P12.pdf
[3]: https://www.thoughtworks.com/radar/techniques/event-streaming-as-the-source-of-truth
[4]: https://www.thoughtworks.com/radar/techniques/event-streaming-as-the-source-of-truth
[5]: https://martin.kleppmann.com/2015/11/05/database-inside-out-at-oredev.html
[6]: https://www.eventstore.com/blog/transcript-of-greg-youngs-talk-at-code-on-the-beach-2014-cqrs-and-event-sourcing
[7]: http://cidrdb.org/cidr2021/papers/cidr2021_paper16.pdf


