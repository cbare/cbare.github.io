---
layout: post
title:  "Notes on Monads"
date:   2020-10-24 09:15:00 +1300
categories: haskell functional-programming
---


Purity

Baggage

Pipe

Typeclass

Monad laws



Pure functions are:

- stateless
- deterministic (return identical values for identical arguments)
- no side-effects

They are more like mathematical functions and less like procedures or methods on an object.

Higher order functions take functions as arguments, for example, _apply_ and _compose_. Map takes a collection and a function, applies the function to each member of the collection and yields a new collection.


[The Y Combinator (Slight Return)][3], Mike Vanier


[1]: https://hackage.haskell.org/package/base-4.14.0.0/docs/Control-Monad.html
[2]: https://hackage.haskell.org/package/base-4.14.0.0/docs/src/GHC.Base.html#Monad
[3]: https://mvanier.livejournal.com/2897.html
