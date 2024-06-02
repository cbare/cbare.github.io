---
layout: post
title:  "Startup Software Engineering"
date:   2020-02-09 21:01 -0800
category: Programming
tags: software-engineering
---

Notes on start-up software engineering.

_“Sixty percent of startups don’t survive the first five years,
and 75 percent of venture capital funded startups fail.”_ [[3]][3]

## Characteristics

Some characteristics of software engineering in a start-up are:

- uncertainty
- innovation
- rapid prototyping
- small teams
- informal process
- unconstrained technology choices
- no legacy systems (at first)
- accumulation of technical debt

Flexibility, more than structure, plays an important role in startup companies. Working on innovative products requires creativity. Rigorous process is not effective and is seen as an obstacle to creativity and flexibility. [[1]][1] Early startup developers often have the technical skill and domain knowledge to work with little guidance.

At some point, startups need more process shifting the balance between flexibility and repeatability. Absence of structure might hinder knowledge sharing and team coordination, especially as the team grows. [[1]][1]

This can be an awkward transition. One start-up, upon reaching a certain size, added a layer of project managers. An analysis showed the number of commits per week per developer fell by nearly half at this point and never recovered.

## Strategies

- design for flexibilty
- build general purpose components that apply to a wide range of scenarios
- prototype quickly, get feedback, iterate
- emphasize experimentation, proof-of-concepts, trial and error
- don't focus on process or scalability, until later
- recruiting like-minded team members

Having a feel for vectors of change versus invariants is important. This allows a degree of anticipation for how the software will be extended over time, what changes it will need to accomodate.

Different software components will be at different places along the axis of experimental vs well-defined with different needs for engineering rigor. Billing and auth are at one end of the spectrum. Unique and unproven domain-specific features are at the other.

## Practices

Process should be optimized for quick iteration. The obvious stuff still applies, unless it gets in the way.

- continuous integration / deployment
- code review
- testing
- automation

## The four F's

Karan Gupta offers these principles in order of priority[[5]][5]:

- Fast-ness (speed)
- Function (capabilities provided)
- Form (how it looks and feels)
- Fabrication (how it is built on the inside)

## Updates

The April 2023 article “Late Architecture with Functional Programming” discusses how functional programming enables “functionality that is independent of the macroarchitecture.”


## References

1. [Software development in startup companies: A systematic mapping study][1], Paternoster, 2013
2. [Software Development in Startup Companies:The Greenfield Startup Model][2], Giardino, 2016
3. [What Do We Know about Software Development in Startups?][3], Giardino, 2014
4. [How to build a startup engineering team][4], Stewart, 2019
5. Code-ish Podcast: [Principles of Pragmatic Engineering, with guest Karan Gupta][5]


[1]: http://dx.doi.org/10.1016/j.infsof.2014.04.014
[2]: https://ieeexplore.ieee.org/document/7360225
[3]: https://www.computer.org/csdl/magazine/so/2014/05/mso2014050028/13rRUxjyX2e
[4]: https://increment.com/teams/how-to-build-a-startup-engineering-team/
[5]: https://www.heroku.com/podcasts/codeish/principles-of-pragmatic-engineering
[6]: https://www.infoq.com/news/2023/04/late-arch-functional-programming/
