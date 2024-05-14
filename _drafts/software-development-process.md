---
layout: post
title:  "Modern software development process and practices"
date:   2021-01-19 15:47:00 +1300
categories: software-engineering
---

Assembling a productive software development team is not easy. Nor is converging on a set of practices that generate working code that does something useful. You have to do that in a competitive environment with limited resources. No wonder failure is common.

Like most engineers, I've fumbled by trial and error through a thicket of advice on process ranging from the merely useless to the actively harmful, occasionally, finding the rare pearl of true wisdom.

Here's an attempt to extract what matters - at least in my limited experience. Possibly, the best that can be acheived is whatever works reasonably well for now. Every situation is different and constantly changing. So, with expectations suitably lowered...

## Strategies

The goals of any technology organization generally focus on building innovative products efficiently, competitively, and safely. Here's what I've seen work:

- Version control
- Code review
- Automated testing
- Continuous deployment
- Feature flags
- Logging and monitoring
- Managed components/infra and containerization
- Cookie-cutter patterns
- Direct interaction with users

Underlying these strategies are two principles that work together - automation and feedback. To be useful, feeback must come quickly. And automation enables the "quickly". This approach in incremental, iterative, and experimental. Contact with the real world gives the best feedback.

## Continuous deployment

Modern software development teams deploy software to production frequently. Short cycles with smaller steps entail lower risk and enable quicker feedback improving quality and responsiveness to users.

[New Relic's developer survey][9] in 2015 captured the moment when continuous deployment became a mainstream engineering practice.

![Frequency of deployment]({{ "/images/frequency_of_deployment_2014_2015.jpg" | absolute_url }}){:style="margin: 0px 18px 18px 18px; width: 92%"}

In 2014, only 28% managed to deploy weekly or more often. In the following year, 57% of teams deployed at least weekly, 30% multiple times per week.

Did half the industry suddenly decide that moving fast and breaking things was the way to go? Mostly not. The real reason has to do with the cloud and SAAS. The kinds of automation and tooling that previously existed only within elite big-tech orgs became available to everyone.

## The DORA metrics

The DevOps Research and Assessment (DORA) team at Google set out to understand practices that characterize high-performing software engineering teams. They identified [four key metrics that indicate the performance of a software engineering team][14]:

1. Deployment frequency
2. Lead time for changes
3. Time to restore
4. Change failure rate

![DORA metrics]({{ "/images/dora-metrics.jpg" | absolute_url }}){:style="margin: 0px 18px 18px 18px; width: 92%"}

These metrics probably correlate with actual outcomes better than lines of code, but it's important to remember metrics are a means, not an end. “When a measure becomes a target, it ceases to be a good measure.”

indicators of capability

## Velocity and Iteration

The key difference between modern practices and older "waterfall" methodology is an emphasis on iteration and feedback rather than upfront effort. The result is that features get to users quickly, while the scope and cost of bugs are minimized. Top-heavy processes that attempt to produce complete, bug-free software before release are slow, expensive, and unresponsive to change. Gates on approval introduce delay and what little feedback they give comes too late in the process to be of benefit.

With tests and visibility in place, moving fast is not more risky but less so. You move fast without breaking things (much) and, when breakage happens, you fix it quickly.

>> “Continuous integration and Continuous development, are the premier examples of the value of automation. CI/CD puts in place guardrails that allow developers to push new code and features that then automatically deploy to production environments. Before CI/CD gained popularity merging code and deploying were a much more cumbersome process. [...] The guardrails that enable CI/CD are version control systems, automated tests, and monitoring tools.” [Atlassian - Software Development: Modern practices and where it’s headed][1]

In [Continuous Delivery Pipelines: How to Build Better Software Faster][5] (2021) [Dave Farley][16] makes the case for rapid iteration. Again, the conclusion is that with good practices in place, faster iteration leads to better software. When it comes to rolling out new features, finding and fixing bugs, and patching vulnerabilities, sooner is better.

## Risk mitigation

What could go wrong? That's a good question to ask. Risks include bugs and security incidents. Handling PII and PHI entails legal and ethical considerations. Trust is hard to build and easy to lose.

### Certification

Certifications like ISO-27001, SOC2, and MDSAP are a source of trust, if somewhat orthogonal to real security and reliability. Certifications are non-negotiable for selling to many large orgs, but they are painful and encourage antiquated and bloated process. The trick is passing the audit without sabotaging your engineering capability.

It's worth exploring how much compliance can be automated. For example, automated vulnerability scans are becoming a standard part of CI/CD pipelines.

Repeatable cookie-cutter patterns reduce compliance burden. A pattern can undergo review once for security and compliance. Reviewing new services can focus on parts that deviate from established pattern or establish new patterns.

The extra processed imposed by these certs are expensive and should be invoked only when it's worth the cost.

## Developer experience

We shouldn't discount the [impact of developer experience on productivity][4]. A tech org should be empowering, rather than disabling. Make everything self-service. Don't make process the blocker. Otherwise, it's just an impediment to be worked around.

Historically, software development has defied attempts at managerial control. [Creative people are driven by autonomy, mastery, and purpose][19]. Software is not like manufacturing a physical product. Code nearly infinitely malliable. Software development is about managing complexity.

The path through a challenge is like stepping stones across a creek. If the stones are too far apart, you fall in; too close together and it's boring. It's too easy. Teachers, mentors, and bosses all exist to help you find steps at the right distance to be interesting without too much risk. Finding these right-sized paths for yourself is a super-power. The reward for working at the right level of challenge is growth. And it's a lot of fun.

[The SPACE of Developer Productivity][2]


## Resources

- [‘Engineering' for Software - How to Amplify Creativity][19] by Dave Farley


Security
observability
reliability
testability
scale / perf
user impact


[How To Not Die By A Thousand Cuts. Or, How To Think About Software Quality.][21] by Aditya Athalye


## Habits and Practices

Adapted from a post by Abi Noda quoting Laura Tacho

- continuous delivery and continuous improvement
- clear goals and priorities each planning cycle
- X% slack time in each planning cycle
- Reduce useless meetings
- Engineering involved in planning process
- unified roadmap with engineering-led and business-led projects
- all features have testing, analytics, docs, and monitoring/alerting
- less than X% of work needs to be redone
- spend less than X% of time waiting for decisions from stakeholders
- accurately estimate timelines
- find and communicate delays early
- pragmatism over dogmatism


[LinkedIn Developer Productivity and Happiness Framework][22]



[1]: https://www.atlassian.com/software-development
[2]: https://docs.microsoft.com/en-us/azure/architecture/example-scenario/apps/devops-dotnet-webapp
[3]: https://itrevolution.com/accelerate-book/
[4]: https://queue.acm.org/detail.cfm?id=3454124
[5]: https://www.youtube.com/watch?v=MYVrLXKJp0Y
[6]: https://stackoverflow.blog/2021/11/29/the-four-engineering-metrics-that-will-streamline-your-software-delivery/
[7]: https://microsoft.github.io/code-with-engineering-playbook/
[8]: https://alexewerlof.medium.com/the-ownership-trio-482a4e5f666d
[9]: https://newrelic.com/blog/best-practices/data-culture-survey-results-faster-deployment
[10]: https://en.wikipedia.org/wiki/Capability_Maturity_Model_Integration
[11]: https://leaddev.com/reporting-metrics/flawed-five-engineering-productivity-metrics
[12]: https://www.thoughtworks.com/insights/blog/experience-design/approaches-for-a-better-developer-experience
[13]: https://www.youtube.com/watch?v=LdOe18KhtT4
[14]: https://cloud.google.com/blog/products/devops-sre/using-the-four-keys-to-measure-your-devops-performance
[15]: https://sre.google/sre-book/table-of-contents/
[16]: https://www.davefarley.net/
[17]: https://fly.io/blog/soc2-the-screenshots-will-continue-until-security-improves/
[18]: https://sourceless.org/posts/the-continuous-delivery-test.html
[19]: https://www.youtube.com/watch?v=1Yqw9swkO5c
[20]: https://queue.acm.org/detail.cfm?id=3454124
[21]: https://www.evalapply.org/posts/how-to-not-die-by-a-thousand-cuts/index.html
[22]: https://linkedin.github.io/dph-framework/
