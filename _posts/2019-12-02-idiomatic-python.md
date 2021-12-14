---
layout: post
title:  "Idiomatic Python"
date:   2019-12-02 17:20 -0800
categories: python
---

![Python logo]({{ "/images/Python-logo-notext.svg" | absolute_url }}){:style="float: right; margin: 0px 18px 18px 18px;"}

Idiomatic use of language enables clear concise expression of intent.

Python provides a sparse and carefully-considered set of primitives that compose nicely. Coding with good taste takes practice in any language. Luckily, the Python community has produced some great resources on writing idiomatic Python code.

- Python core developer Raymond Hettinger's talks:
  - [Transforming Code into Beautiful, Idiomatic Python][3] (old but good)
  - [Beyond PEP 8 -- Best practices for beautiful intelligible code][4]
  - [Preventing, Finding, and Fixing Bugs On a Time Budget][8]
  - [Python's Class Development Toolkit][7]
- [The Hitchhiker’s Guide to Python][6] is a handbook of Python best practice.
- [Fluent Python][1] by Luciano Ramalho is a well-written intermediate-level programming book. Working your way through its chapters will take you from competence to proficiency.
- Chip Huyen's [Python-is-cool][2] is a quick primer on some of Python's unique syntax.


## Python language constructs

### Modules

[Modules][901] can hold variables, functions, class definitions, or executable code. They are the preferred tool for namespacing. Avoid deeply nested modules and cyclic dependencies between modules.

### Built-in functions and magic methods

[Built-in Functions][902] together with [magic methods][202] provide a common interface for Python objects. This reduces annoying inconsistencies like: `array.length`, `string.length()` and `list.size()`. In Python, it's: `len(a)`, `len(s)` and `len(l)`.

### Laziness

Python 3 makes frequent use of _lazy evaluation_, for example, [range][903], [zip][904], and [dict.items][905]. Syntactic support for laziness comes in the form of the [generator][913], which can help your programs run faster in less memory.

For [example][914]:

``` python
def unique(iterable, key=lambda x: x):
    seen = set()
    for elem, ekey in ((e, key(e)) for e in iterable):
        if ekey not in seen:
            yield elem
            seen.add(ekey)
```

### Comprehensions

![Python logo]({{ "/images/turnip-twaddler.png" | absolute_url }}){:style="float: right; margin: 0px 18px 18px 18px; width: 12em; height: 16em; position: relative; top: -3em;"}

[Comprehensions][907] are Python's syntactic sugar for _map_ and _filter_ operations. Comprehensions come in different flavors which evaluate to different types, either containers like lists or sets or generators.

Comprehensions combine well with [itertools][908] and [functools][909] from the standard library to compose pipelines in the style of [functional programming][907].


#### List comprehensions

``` python
unmoldy_twaddled_turnips = [twaddle(turnip)
    for turnip in turnips if not is_moldy(turnip)]
```

#### Generator expressions

The lazy version of a list comprehension is a generator expression.

``` python
generator = (twaddle(turnip)
    for turnip in turnips if not is_moldy(turnip))
```

#### Set and dict comprehensions

``` python
letters = {x for x in 'abracadabra' if x not in 'abc'}
squares = {x: x**2 for x in range(10)}
```


### Conditional expressions

Expressions can be evaluated—turned into a value—in contrast to statements which are executed and don't return a value. Comprehensions enable iteration in the form of expressions. Conditional expressions do the same for branching.

``` python
'ok!' if quux.succeeded else 'failed!'
```


### Unpacking, args, and kwargs

Python supports destructuring in function arguments and assignments.

``` python
def foo(*args, **kwargs):
    """
    Accept positional and keyword arguments and print them.
    """
    print('positional args = {}'.format(', '.join(str(arg) for arg in args)))
    print(', '.join(f'{key}={value}' for key, value in kwargs.items()))
```

#### Destructuring assignment

``` python
a, b, c, d = (1, 2, 3, 4)
head, *tail = (1, 2, 3, 4)
```

#### Swap

``` python
a, b = b, a
```

### Decorators

[Decorators][203] are syntax for creating wrappers around functions, methods or classes. Usually, you'll import and use them from libraries. Examples from the standard library include:
- [property][910]
- [classmethod][911]
- [lru_cache][912]

Decorators help separate concerns. For example, the purpose of a function is completely orthogonal to caching its result. The [lru_cache][912] decorator separates the concept and implementation strategy of caching from whatever function you're applying it to.


### NamedTuple

[Named tuples](https://docs.python.org/3/library/collections.html#namedtuple-factory-function-for-tuples-with-named-fields) are memory-efficient, immutable records. For a mutable alternative, consider [argparse.Namespace](https://docs.python.org/3/library/argparse.html#argparse.Namespace) which is especially useful for configuration.


## Habits to avoid

- putting everything in a class; use modules
- singleton classes; use modules
- static methods; use functions, prefer pure functions
- class hierarchies; prefer composition over inheritence
- record / struct style classes; use namedtuple or [dataclass][204]
- getters / setters; use member variables, covert to @property when needed and not before
- methods that don't use _self_: use a function
- defining custom exceptions; prefer [built-in exceptions][906]

To a first approximation, [stop writing classes][205], as detailed in a talk by python core developer Jack Diederich. Where modules and pure functions serve, they are a better choice.

## Simple is better

Simplicity takes work. The judgement to know whether a little extra effort will pay off or become a maintenance headache comes only with experience—specifically the experience of doing it wrong.

In general, don't develop against imagined future requirements. The YAGNI principle says “you ain't gonna need it”. If it turns out that we _do_ need it, we can add it later.

Python has some features that help you avoid unnecessary work. _Properties_ mean that getters and setters can be added transparently to the client and therefore never have to be created “just in case we need them later”. In the same way, functions can become callable objects with no impact on client code.

It's important to realize that everything has a cost. Each line of code, each layer of indirection has a cost. Tricky code using exotic language features has a higher cost. That cost accrues not just when writing a piece of code, but also falls on every reader, caller and maintainer. Minimizing surface area and cognitive load is typically a great investment.


``` python
a = 1
```

...is better than...

``` python
vars = {'a': 1}
```

...which is still better than...

``` python
class VariableTwaddler:
    """Twaddles the variable"""
    def __init__(self, a):
        self.a = a
variableTwaddlerA = VariableTwaddler(1)
```


## Testing

Testing tools
- [py.test](https://docs.pytest.org/en/latest/)
- [pytest-cov](https://github.com/pytest-dev/pytest-cov)
- [doctest](https://docs.python.org/3/library/doctest.html)
- [Hypothesis](https://hypothesis.readthedocs.io/en/latest/)


## Style

The Python style guide, known as [PEP-8][101], starts with the admonition, “A Foolish Consistency is the Hobgoblin of Little Minds”. At the same time, “Beautiful is better than ugly” and “Readability counts”.

Rather than burn time developing your own style guide, consider using an autoformatter (e.g. [Black][103]). Flake8 checks your code against a [Big Ol' List of Rules][102] covering style as well as more substantial issues like unused imports.


### Naming

Naming is hard, but there are a few helpful guidelines.

Use plurals for containers:

``` python
for thing in things:
    process(thing)
```

Single-letter variables are useful in the context of abstract values, for example many Python [math functions][915] take `x` as an input.

|-----------|-----------------------|
|  Name     |  Meaning              |
|-----------|-----------------------|
|  i, j, k  |  indexes              |
|  n, m     |  counting numbers     |
|  x, y, z  |  real numbers         |
|  a, b, c  |  integers             |
|  e, ex    |  exceptions           |
|  f, g, h  |  functions            |
|  p        |  predicate            |
|  _        |  unused variable      |
|-----------|-----------------------|



[1]: http://shop.oreilly.com/product/0636920032519.do
[2]: https://github.com/chiphuyen/python-is-cool
[3]: https://www.youtube.com/watch?v=OSGv2VnC0go
[4]: https://www.youtube.com/watch?v=wf-BqAjZb8M
[6]: https://docs.python-guide.org/
[7]: https://www.youtube.com/watch?v=HTLu2DFOdTg
[8]: https://www.youtube.com/watch?v=ARKbfWk4Xyw
[9]: https://pybay.com/site_media/slides/raymond2018-keynote/index.html

[101]: https://www.python.org/dev/peps/pep-0008/
[102]: https://lintlyci.github.io/Flake8Rules/
[103]: https://github.com/psf/black

[201]: https://realpython.com/python-kwargs-and-args/
[202]: https://rszalski.github.io/magicmethods/
[203]: https://realpython.com/primer-on-python-decorators/
[204]: https://docs.python.org/3/library/dataclasses.html
[205]: https://www.youtube.com/watch?v=o9pEzgHorH0

[901]: https://docs.python.org/3/tutorial/modules.html
[902]: https://docs.python.org/3/library/functions.html
[903]: https://docs.python.org/3/library/functions.html#func-range
[904]: https://docs.python.org/3/library/functions.html#zip
[905]: https://docs.python.org/3/library/stdtypes.html#dict.items
[906]: https://docs.python.org/3/library/exceptions.html#exception-hierarchy
[907]: https://docs.python.org/3/howto/functional.html
[908]: https://docs.python.org/3/library/itertools.html
[909]: https://docs.python.org/3/library/functools.html
[910]: https://docs.python.org/3/howto/descriptor.html#properties
[911]: https://docs.python.org/3/library/functions.html#classmethod
[912]: https://docs.python.org/3/library/functools.html#functools.lru_cache
[913]: https://docs.python.org/3/tutorial/classes.html#generators
[914]: https://wiki.python.org/moin/Generators
[915]: https://docs.python.org/3/library/math.html
