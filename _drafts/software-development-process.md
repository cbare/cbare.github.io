---
layout: post
title:  "Modern software development process and practices"
date:   2021-01-19 15:47:00 +1300
categories: software-engineering
---

## Preamble

Should we move fast and break things? ...um, no. I have very little love for that philosophy because it fails to recognize the costs and consequences involved and, when it succeeds, it's often by offloading pain onto unfortunate others. When some over-hyped go-getter moves fast and breaks things, the execs go looking for a steady even-keeled engineer to clean up the mess. I've been that person.

It's a valid point that we may learn valuable lessons by moving fast and breaking things. But, must that come at the cost of doing some damage? Is it just a trade-off?

Let's take a brief detour into [Pareto optimality], an economist's way to reason about trade-offs. A system, resource allocation in an economy for instance, is said to be on the Pareto optimal fronteir if an increase in one objective can only be achieved at the cost of a decrease in another objective. X gets richer, but Y gets poorer. More coffee, fewer artichokes. (A fine trade, if you ask me.)

If we are not yet at the fronteir, then we can increase some objective without sacrificing any other - and we should do so. That moves us closer to the fronteir. Moving around on the fronteir is the province of value judgement. My value for coffee over artichokes might be contested by a few very foolish people. But nobody objects to more coffee with no loss of artichokes.


## Iteration

You can learn a lot by trying things. Did it work? Were users happy? Was it too slow? The more often you try things, the more you can learn, if you're paying attention.

![Frequency of deployment]({{ "/images/frequency_of_deployment_2014_2015.jpg" | absolute_url }}){:style="margin: 0px 18px 18px 18px; width: 66%"}

What happened in 2015? The frontier moved.

Cloud. Saas (2 aspects)
GitHub founded in 2008.
The kind of dev environments available only to elite organizations with teams dedicated to build tooling were now available as free-mium or pay-per-use models.


[Continuous Delivery Pipelines: How to Build Better Software Faster][5], Dave Farley's presentation at GOTO 2021.



## Goals

What are the goals of software development process?

### Quality and safety

- Users experience few bugs or downtime
- Reduce risk of security incidents
- Handling PHI:
  - Ethical
  - Legally compliant
  - Build trust by being seen as good stewards of PHI
- Enable sales to and investments from organizations with certification requirements

### Innovation

- Develop new technology, scientific collaboration
- Use research and data pool to develop new features and products
- Enable "learning loop" in which a smart product extracts feedback from users that improve the product.
- Respond quickly to opportunities, react quickly to changing technology, etc.

Over all, we want to build innovative products safely and at a competitive pace. These goals are in conflict and must, to some extent, be traded off with each other and with available resources. However, modern software development practice offers tools and techniques that address quality and security concerns while enabling iterative development and short release cycles.


## Strategies

What strategies are used in modern software development to help achieve the above goals?

- Version control
- Code review
- Automated testing
- Automated deployment
- Monitoring
- Containerization
- Managed components / serverless

### CI/CD

>> “Continuous integration and Continuous development, are the premier examples of the value of automation. CI/CD puts in place guardrails that allow developers to push new code and features that then automatically deploy to production environments. Before CI/CD gained popularity merging code and deploying were a much more cumbersome process. [...] The guardrails that enable CI/CD are version control systems, automated tests, and monitoring tools.” [Atlassian - Software Development: Modern practices and where it’s headed][1]

The key difference from "waterfall" is the emphasis on minimizing the scope and cost of bugs, rather than upfront effort to eliminate bugs, which is subject to increasing cost and diminishing returns.

### Cookie-cutter patterns

Establish architectural patterns for commonly used building blocks:

- Authentication of users and software
- Configuration for Azure resources
- No need to repeatedly review the same patterns
- Review can be limited to parts that deviate from established pattern or establish new patterns

### Automation

Certifications require specific sets of controls, scans, and documentation. It's worth exploring whether parts of these requirements can be automatically generated during the build process. For example, automated vulnerability scans are becoming a standard part of CI/CD pipelines.


## Triage

How much process is the right amount?

The level of exposure and risk of a software project should dictate appropriate level of process. The heavily regulated process mandated for medical devices is slow, cumbersome, and expensive and should not serve as the model for projects outside this regime.

Projects might be triaged into three levels, roughly high, medium, and low process:

- Medical device
- Customer facing products
- Internal tools

Process should be invoked to address specific concerns in proportion to the risk. Where consequences are low, or can be deliberately managed, process can be very light.


Capability Maturity Model

Defined and repeatable process. Use of metrics, ill-defined what exactly these are. Continuous improvement. Is having a process that is defined, repeatable, measurable and continuously improving.

## Engineering metrics

The DevOps Research and Assessment (DORA) team at Google designed a six-year program to understand what sets high-performing software engineering teams apart from low-performing software engineering teams. tThey identified four key metrics that indicate the performance of a software engineering team:

1. Deployment frequency
2. Mean change lead time
3. Mean time to restore
4. Change failure rate


## Developer experience

- self-service, don't make process the blocker.
- empowering, rather than disabling
- trust, measures exist because they demonstrably work. Otherwise, they are impediments to be worked around.






[1]: https://www.atlassian.com/software-development
[2]: https://docs.microsoft.com/en-us/azure/architecture/example-scenario/apps/devops-dotnet-webapp
[3]: https://itrevolution.com/accelerate-book/
[4]: https://queue.acm.org/detail.cfm?id=3454124
[5]: https://www.youtube.com/watch?v=MYVrLXKJp0Y
[6]: https://stackoverflow.blog/2021/11/29/the-four-engineering-metrics-that-will-streamline-your-software-delivery/
