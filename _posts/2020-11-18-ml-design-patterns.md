---
layout: post
title:  "Machine Learning Design Patterns"
date:   2020-11-19 15:47:00 +1300
categories: machine-learning
---

[![Machine Learning Design Patterns]({{ "/images/ml-design-patterns.jpg" | absolute_url }}){:style="float: right; margin: 0px 24px"}][1]

The [Seattle Google Developers Group][5] hosted a talk by the authors of [Machine Learning Design Patterns][1]. Though ML is not yet at a point where it's “just another library”, there's a body of engineering knowledge building up around ML as people get more experience using models as parts of larger software systems. This book looks to be a nice addition to that trend.

The talk highlights three pattern out of the thirty in the book.

### Imbalanced training data

Imbalanced training data is typical in anomaly detection. Here are 3 strategies:

- Downsample the majority class
- Upsample minority class (see [SMOTE][3])
- Weighted classes


###  Continuous Model Evaluation

In order to monitor models for concept/data drift, we need a way to compare model with ground truth.  But, it might be necessary to wait some time to get true labels for model predictions.


### Bridged Schema

Data gets better over time. A categorical feature might gain finer grained categories, ex. card -> credit card, debit card, gift card.

Solution:
- Data augmentation on old examples, replacing one-hot values with floats from estimated distribution

### More

- [Machine Learning Design Patterns][1] by Valliappa Lakshmanan, Sara Robinson, Michael Munn
- Github: [ml-design-patterns repo][2]
- During Q&A, Sara Robinson mentioned that she had written a blog post about the writing process: [Writing a technical book: from idea to print][4].



[1]: https://www.oreilly.com/library/view/machine-learning-design/9781098115777/
[2]: https://github.com/GoogleCloudPlatform/ml-design-patterns
[3]: https://arxiv.org/abs/1106.1813
[4]: https://sararobinson.dev/2020/11/17/writing-a-technical-book.html
[5]: https://www.meetup.com/gdg-seattle/
