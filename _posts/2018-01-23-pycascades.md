---
layout: post
title:  "Type checking in Python with mypy"
date:   2018-01-24 11:39 -0800
categories: python
---

When I switched from Java to dynamic languages, I sometimes missed type checking. I flirted with rocket-science type systems, like you'll find in Scala or Haskell.

Now, Python 3.6 supports optional type checking with two new components. The [typing library](https://docs.python.org/3/library/typing.html) lets you annotate parameters and return types. [Mypy](http://mypy-lang.org/) does the actual type checking.

![Greatest common divisor function with type annotations]({{ "/images/gcd_with_type_annotations.png" | absolute_url }})
*from Łukasz's [slides](fb.me/gradual-typing)*

After hearing Łukasz Langa present [Gradual Typing of Production Applications](fb.me/gradual-typing), I got the itch to try these new tools out.

It's easy to get started. First, install mypy:

``` sh
$ pip install mypy
```

If we want to say, for example, that the greatest-common-divisor function takes two ints and returns an int, we can:

``` py
def gcd(a: int, b: int) -> int:
    while b:
        a, b = b, a % b
    return a

print('gcd(24, 42) = ', gcd(24, 42))
```

Now, if we fall asleep on our keyboard...

``` py
wut = gcd('zzz', 42)
```

...we want the type checker to give us a heads-up. We invoke mypy on the command line and get what we deserve - a nice error message:

``` sh
$ mypy type_check_me.py
type_check_me.py:8: error: Argument 1 to "gcd" has incompatible type "str"; expected "int"
```

You can also create typed collections, such as a list of strings:

``` py
from typing import List

def caps(strings: List[str]) -> List[str]:
    return [s.upper() for s in strings]
```

Parameterized types are done using `TypeVar`.

``` py
from typing import List, TypeVar

T = TypeVar('T')
def first(list: List[T]) -> T:
    return list[0] if list else None
```

The above function works and type checks, but we're lying a little bit. The function doesn't always return a value of type T. It returns `None` as the first element of an empty list. Mypy lets us get away with that by treating `None` as a special case.

We can be explicit about possible `None` values using `Optional`, an experimental feature similar to Scala's `Option` or Haskell's `Maybe`:

``` py
from typing import List, TypeVar, Sequence, Optional

T = TypeVar('T')
def first(seq: Sequence[T]) -> Optional[T]:
    return seq[0] if seq else None
```

I don't know why, but I had to use `Sequence` rather than `List`. Mypy complained about [variance](http://mypy.readthedocs.io/en/latest/common_issues.html#variance).

Our consumers of our `first` function are on notice that they need to handle `None`:

``` py
curses = ['dangit', 'shucks', 'flapdoodle']

def twice(a: Optional[str]) -> str:
    return a + ', ' + a if a else 'um, um'

double_curse = twice(first(caps(curses)))
```

There's yet another choice besides strict-optional and not strict-optional. The `first` function could throw an exception if no first element exists.

``` py
def first_or_die(seq: Sequence[T]) -> T:
    return seq[0]
```

I imagine these awkward bits will get worked out as recommended practices get established. In Haskell, the only slightly exaggerated saying is, "If it type-checks, it runs". Bringing some of that magic to Python is pretty cool.


