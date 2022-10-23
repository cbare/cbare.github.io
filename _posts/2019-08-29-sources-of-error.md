---
layout: post
title:  "Sources of Error in Software Development"
date:   2019-08-29 15:47:00 +0200
categories: software-engineering programming
---

_“[Writing code isn't the problem; Understanding the problem is the problem.][11]”_

In a statically typed programming language, a type-checker runs at compile time catching mistakes that would otherwise lead to runtime errors or crashes. This means that a certain class of error will be discovered earlier and earlier is better. Languages like Haskell and Scala pioneered advanced and expressive type systems, which then inspired TypeScript and [static type checking in Python][10].

But what kinds of bugs do type checkers catch? And what bugs are invisible at the level of static typing? What are the sources of error in software development?

[![Sources of software errors]({{ "/images/sources-of-error-in-software-development.png" | absolute_url }}){:style="width: 94%; margin: 0px 24px"}](/images/sources-of-error-in-software-development.png)

I wouldn't conclude from this that static typing is useless. But, it's just a tool. In skilled hands, types are a tool for understanding a problem domain, making concepts explicit and checking for internal consistency. Even so, there are certainly sources of error well outside the scope of types.

## More thinking about errors

For more thinking on errors, check out this talk by Marian Petre at Strange Loop 2022: [Expert Software Developers' Approach to Error][12].


[10]: https://realpython.com/python-type-checking/
[11]: https://dl.acm.org/doi/10.1145/50087.50089
[12]: https://www.youtube.com/watch?v=UNMF5AS4SLg
