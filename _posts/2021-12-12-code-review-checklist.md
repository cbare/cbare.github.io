---
layout: post
title:  "Code Review Checklist"
date:   2021-12-12 19:22:00 +1200
categories: software-engineering
---

Good code review has a lot of benefits. Walking through a pull-request is a vector for knowledge transfer. It's a tool for detecting and fixing issues early and maintaining consistency across a code base. It's not easy to do well, but giving thoughtful and constructive code review is one of the most valuable skills you can develop.


## What to ask

![Frog and Toad by Arnold Lobel]({{ "/images/frog-and-toad-list.jpg" | absolute_url }})
*Frog and Toad by Arnold Lobel*
{:style="width: 400px; height: 647px; float: right;"}

First, consider the requirements. Every bit of code should be there because it gives something to a user. If the code adds a feature that someone wants, works, and has tests, the bias should be towards merging. Later PRs can always refactor and generalize, assuming continuous deployment.

Is it the right scope? Ideally, a pull-request should add a bite size piece of functionality - a single feature, a bug fix, or a refactoring, but not all three. Refactorings are cleaner if no new code is added at the same time.

You'll have a gut feel about how well new code fits into an existing code base. Does it deal in the same abstractions? Does it reimplement existing functionality? Is the new code immitating deprecated patterns? Or not following existing patterns that are good? If the PR clearly adds technical debt, make sure that's warranted. Note the decision in the PR and create a ticket to resolve the quick and dirty parts while it's fresh in mind.

Here's a checklist I put together as a reminder to myself. Maybe it will help you, too. You'll notice that several of the bullet points below contradict others. If you're spotting such trade-offs and weighing them, that's judgement.


## Checklist

- Fits requirements
- Clarity, readability, naming, comments
- Complexity, simpler is better
  - Single responsibility
  - [Code is the enemy][8]
- Duplication
  - Don't reinvent the wheel; make use of libraries and in-house components.
  - Finding overlap with existing functionality? Factor out common code.
  - Keep code DRY
- Abstraction and modularity
  - Does the code live in the right place? In the right layer?
  - Does the code introduce circular dependencies?
  - Minimize surface area and cognitive load
  - What implementation details do we want to hide?
  - What level of generality are we shooting for?
- Extensibility
  - Consider extension points for likely vectors of change
  - Also, consider that you ain't gonna need it
- Efficiency and performance
  - Choice of data structures
  - Memory and cpu usage
  - Look at inner loops, repeated work
- Testing
  - Reasonable test coverage: happy path and edge cases
  - Is code factored into small testable units?
  - Look for missing test cases
  - Test properties or invariants
- Dependencies
  - Fewer is better
  - Watch out for circular dependencies between modules
- Error handling
  - What could go wrong and what should happen?
  - Fail fast
- Clean up
  - opened resources get closed; use finally
- Logging
  - Log errors and very sparsely to INFO.
- [Security][3]
  - Sanitize inputs
  - If I was trying to steal data, how might I exploit this code?

## Style points

[Idiomatic use of a programming language][11] results in elegant and efficient solutions. Idiomatic style can be a great topic for code review, lifting intermediate skills toward expertise.

On the other hand, don't fight the style wars. We all love beautiful code. But my aesthetic isn't necessarily yours. You can convene the committee to write the style guide and zealously flame-broil your colleagues over every violation, or adopt standards like [gofmt][6] or [Black][7] and forget about it.


## What is good code?

There's a lot of advice out there about what makes for good or bad code and what it means to be well-factored, most of it well-intended, some of it occasionally useful. Popular heuristics include:

- [SOLID][12]
- YAGNI
- [Code smells][13]
- Favor composition over inheritance
- Code to an interface

![Code Complexity vs Years of Programming by @flaviocopes]({{ "/images/code-complexity-vs-years-of-programming.jpg" | absolute_url }})
*[Code Complexity vs Years of Programming][15] by @flaviocopes*

Simplicity deserves special mention. A simpler implementation will allow us to deploy working code and start getting feedback sooner. It costs less to maintain and probably has fewer bugs. Simplicity and generality often go together. We can always iterate based on feedback to fix rough spots and add features. You won't regret giving a listen to [Rich Hickey's thoughts][14] on the topic.

Programming languages provide primitives, means of combination, and means of abstraction, according to [SICP][10]. When looking at any piece of code, take note of which of the available means were chosen and why. Immutable data and pure functions are easy to reason about and should generally be our first choices. I write way fewer classes than I used to. Your mileage may vary.


## Give Props

As developers, we're proud of our work. Executives, PMs, and customers don't care about pretty code or a clever hack. So, it's nice when someone gets it. A little positive energy goes a long way. Don't forget to give your fellow code-monkey some props.


## Other code review checklists

- [mgreiler][2]
- [Codementor][4]
- [Evoke][5]


[1]: https://www.digitalocean.com/community/conceptual_articles/s-o-l-i-d-the-first-five-principles-of-object-oriented-design#interface-segregation-principle
[2]: https://www.michaelagreiler.com/code-review-checklist-2/
[3]: https://owasp.org/www-pdf-archive/OWASP_Code_Review_Guide_v2.pdf
[4]: https://www.codementor.io/blog/code-review-checklist-76q7ovkaqj
[5]: https://www.evoketechnologies.com/blog/code-review-checklist-perform-effective-code-reviews/
[6]: https://go.dev/blog/gofmt
[7]: https://black.readthedocs.io/en/stable/
[8]: http://www.skrenta.com/2007/05/code_is_our_enemy.html
[9]: https://blog.codinghorror.com/the-best-code-is-no-code-at-all/
[10]: https://mitpress.mit.edu/sites/default/files/sicp/index.html
[11]: https://cbare.github.io/2019-12-03/idiomatic-python.html
[12]: https://www.digitalocean.com/community/conceptual_articles/s-o-l-i-d-the-first-five-principles-of-object-oriented-design
[13]: https://mmantyla.github.io/BadCodeSmellsTaxonomy
[14]: https://www.youtube.com/watch?v=SxdOUGdseq4
[15]: https://twitter.com/JavierGonzalez/status/1463685147333738497
