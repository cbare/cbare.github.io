---
layout: post
title:  "Python mysterious logging library"
date:   2020-03-12 11:51 -0800
categories: python
---

Python's logging module has confused me for years. Why doesn't this work?

```
logger = logging.getLogger('foo')
logger.setLevel(logging.INFO)
logger.info('nope')
```



Let's say I'm debugging the tricky module foo.quux. So, I want to see debug level logs for that module, but only warnings or higher for the rest of the vast and chatty code base.

## TL;DR

Log messages propagate up through tree of loggers toward the root.

[Logging facility for Python][1]
[Logging HOWTO][2]
[Logging Cookbook][3]
[The logging section of The Hitchhiker’s Guide to Python][4]
[Logging in Python][5]
[Python Logging: A Stroll Through the Source Code][6]


[1]: https://docs.python.org/3/library/logging.html
[2]: https://docs.python.org/3/howto/logging.html
[3]: https://docs.python.org/3/howto/logging-cookbook.html
[4]: https://docs.python-guide.org/writing/logging/
[5]: https://realpython.com/python-logging/
[6]: https://realpython.com/python-logging-source-code/
