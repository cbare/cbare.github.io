---
layout: post
title:  "Teaching Git"
date:   2021-03-28 11:55:00 +1300
categories: programming tools
---

Version control

## Tools for software quality

Software engineering gives us a set of tools for maintaining quality. Source code version control tracks changes to a codebase over time.

- Tests
- ***Version control  <<=====***
- CI/CD Automated continuous integration and deploy
- Code review
- Logging & Monitoring
- Standard project template
- [Infra-as-code tools, e.g. Terraform, ARM (Azure Resource Manager)][22]

Working with data and models brings a few new variables into the mix - non-deterministic behavior and testing assumptions about data. The new buzzwords are ML-ops and data-ops. You can version models and even data. More on that later.

## Starting a new project

``` sh
mkdir hackalicious-nasty
cd hackalicious-nasty
git init
touch README.md
echo '# hackalicious\n\n' >> README.md
git add README.md
git commit -m 'initial commit'
```

## Staging changes

## Branching

## Merging

Apparently, there's a [commit in the Linux Kernel with 66 parents][23].



[22]: https://docs.microsoft.com/en-us/dotnet/architecture/cloud-native/infrastructure-as-code
[23]: https://www.destroyallsoftware.com/blog/2017/the-biggest-and-weirdest-commits-in-linux-kernel-git-history

