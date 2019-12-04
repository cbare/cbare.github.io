---
layout: post
title:  "Idiomatic Python"
date:   2019-12-02 17:20 -0800
categories: python
---

Idiomatic use of language makes the difference between code that concisely expresses intent and code that hides its intent in an awkward misshapen structure.

Python provides a sparse and carefully-considered set of primitives that compose nicely together. Using these tools with good taste takes a little practice. Luckily, the community has produced some great resources on writing idiomatic Python code.

- Raymond Hettinger's talks:
  - [Transforming Code into Beautiful, Idiomatic Python][3] (old but good)
  - [Beyond PEP 8 -- Best practices for beautiful intelligible code][4]
  - [Preventing, Finding, and Fixing Bugs On a Time Budget][5]
  - [Python's Class Development Toolkit][7]

- [The Hitchhiker’s Guide to Python][6] aims to be a handbook of best practices.

- [Fluent Python][1] by Luciano Ramalho is a well-written intermediate-level programming book. Working your way through its chapters will take you from competence to proficiency.

- Chip Huyen's [Python-is-cool][2] covers some of Python's unique syntax.


## Python language constructs

### Modules

[Modules][901] can hold variables, functions, class definitions, or executable code that runs on import. They are the preferred tool for namespacing and generally should not be deeply nested. Cyclic dependencies between modules should be avoided.

### Built-in functions and magic methods

[Built-in Functions][902] together with [magic methods][202] provide a common interface for Python objects.

### Laziness

The transition from Python 2 to Python 3, brought with it more _lazy evaluation_. For example, [range][903], [zip][904], and [dict.items][905] all went from eager to lazy. Judicously lazy code runs faster using less memory.

### Comprehensions

[Comprehensions][907] are Python's syntactic sugar for _map_ and _filter_ operations. Comprehensions come in different flavors for different types of containers or for generators.

Comprehensions combine well with [itertools][908] and [functools][909] libraries to compose processing steps into pipelines as in [functional programming][907].


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

``` python
'ok!' if foo_processor.succeded else 'failed!'
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

[Decorators][203] are syntax for creating a wrapper around a function, method or class. Usually, you'll import and use them from libraries. Examples include:
- property
- classmethod
- lrucache


### NamedTuple

Classes are needed less than you might think. [Named tuples](https://docs.python.org/3/library/collections.html#namedtuple-factory-function-for-tuples-with-named-fields) are memory-efficient, immutable and can be defined in one line.

For a mutable alternative, consider [argparse.Namespace](https://docs.python.org/3/library/argparse.html#argparse.Namespace).


## Habits to avoid

- putting everything in a class; use modules
- singleton classes; use modules
- static methods; use functions, prefer pure functions
- class hierarchies; prefer composition over inheritence
- record / struct style classes; use namedtuple or [dataclass][204]
- getters / setters; use member variables, covert to @property when needed and not before
- defining custom exceptions; prefer [built-in exceptions][906]


## Testing

Testing tools
- [py.test](https://docs.pytest.org/en/latest/)
- [pytest-cov](https://github.com/pytest-dev/pytest-cov)
- [doctest](https://docs.python.org/3/library/doctest.html)
- [Hypothesis](https://hypothesis.readthedocs.io/en/latest/)


## Style

The Python style guide, known as [PEP-8][101], starts with the admonition, “A Foolish Consistency is the Hobgoblin of Little Minds”. But, “Beautiful is better than ugly” and “Readability counts”.

Rather than spend time developing your own style guide, consider using an autoformatter (e.g. [Black][103]). Flake8 checks your code against a [Big Ol' List of Rules][102] covering style as well as more substantial issues like unused imports.


### Naming

Conventional usage of single-letter variables:

|---------|-----------------------|
|  name   |  meaning              |
|---------|-----------------------|
|  i,j,k  |  indexes              |
|  n,m    |  counting numbers     |
|  x,y,z  |  real numbers         |
|  a,b,c  |  coefficients         |
|  e,ex   |  exceptions           |
|  f,g,h  |  functions            |
|  p      |  predicate            |
|---------|-----------------------|



[1]: http://shop.oreilly.com/product/0636920032519.do
[2]: https://github.com/chiphuyen/python-is-cool
[3]: https://www.youtube.com/watch?v=OSGv2VnC0go
[4]: https://www.youtube.com/watch?v=wf-BqAjZb8M
[5]: https://pybay.com/site_media/slides/raymond2018-keynote/index.html
[6]: https://docs.python-guide.org/
[7]: https://www.youtube.com/watch?v=HTLu2DFOdTg

[101]: https://www.python.org/dev/peps/pep-0008/
[102]: https://lintlyci.github.io/Flake8Rules/
[103]: https://github.com/psf/black

[201]: https://realpython.com/python-kwargs-and-args/
[202]: https://rszalski.github.io/magicmethods/
[203]: https://realpython.com/primer-on-python-decorators/
[204]: https://docs.python.org/3/library/dataclasses.html

[901]: https://docs.python.org/3/tutorial/modules.html
[902]: https://docs.python.org/3/library/functions.html
[903]: https://docs.python.org/3/library/functions.html#func-range
[904]: https://docs.python.org/3/library/functions.html#zip
[905]: https://docs.python.org/3/library/stdtypes.html#dict.items
[906]: https://docs.python.org/3/library/exceptions.html#exception-hierarchy
[907]: https://docs.python.org/3/howto/functional.html#generator-expressions-and-list-comprehensions
[908]: https://docs.python.org/3/library/itertools.html
[909]: https://docs.python.org/3/library/functools.html
