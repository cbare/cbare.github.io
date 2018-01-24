Python 3.6 supports optional type checking with the [typing library](https://docs.python.org/3/library/typing.html) for adding type annotations and [mypy](http://mypy-lang.org/) that does the actual type checking.

![Greatest common divisor function with type annotations]({{ "/images/gcd_with_type_annotations.png" | absolute_url }})
*from Łukasz's [slides](fb.me/gradual-typing)*

After hearing Łukasz Langa present [Gradual Typing of Production Applications](fb.me/gradual-typing), I wanted to try these new tools out.

It's easy to get started.

```
pip install mypy
```

For example, the greatest-common-divisor function takes two ints and returns an int:

``` Python
def gcd(a: int, b: int) -> int:
    while b:
        a, b = b, a % b
    return a

print('gcd(24, 42) = ', gcd(24, 42))
```

Now, if you fall asleep on your keyboard and do this...

```
wut = gcd('zzz', 42)
```

...the type checker properly complains, like so:

```
> mypy gcd.py
gcd.py:8: error: Argument 1 to "gcd" has incompatible type "str"; expected "int"
```

You can also create typed collections, such as a list of strings:

``` Python
from typing import List

def caps(strings: List[str]) -> List[str]:
    return [s.upper() for s in strings]
```

Parameterized types are done using `TypeVar`.

```
from typing import List, TypeVar

T = TypeVar('T')
def first(list: List[T]) -> T:
    return list[0] if list else None
```

The above function works and type checks, but we're lying a little bit. The function doesn't always return a value of type T. It returns None as the first element of an empty list. We can state that using `Optional` which is an experimental feature at this point:

```
from typing import List, TypeVar, Optional

T = TypeVar('T')
def first(seq: Sequence[T]) -> Optional[T]:
    return seq[0] if seq else None
```

I don't know why, but I had to use `Sequence` rather than `List`. Mypy complained about [variance](http://mypy.readthedocs.io/en/latest/common_issues.html#variance). I'm not convinced it was right, but maybe that's why it's experimental.

```
curses = ['dangit', 'shucks', 'flapdoodle']

def twice(a: Optional[str]) -> str:
    return a + ', ' + a if a else 'um, um'

double_curse = twice(first(caps(curses)))
```


