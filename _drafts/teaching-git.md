---
layout: post
title:  "Learning Git"
date:   2021-03-28 11:55:00 +1300
categories: programming tools
---

This is a set of notes for a presentation I gave to a group of data oriented folks and a refresher on version control for data people.

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

Let's start a new project.

``` sh
mkdir hackalicious
cd hackalicious
```

Make a README file.

``` sh
touch README.md
echo '# hackalicious\n\n' >> README.md
```

Initialize a local repo and make our first commit.

``` sh
git init
git add README.md
git commit -m 'initial commit'
```

## Staging changes

1. make changes to working copy.
2. stage changes
3. commit

```
(wc) ---> (index) ---> (HEAD)
      ^            ^
   git add       git commit


(wc) <---------------- (HEAD)
             ^
         git checkout
```


``` sh
git add [-u] [--all] [<pathspec>…​]
```

``` sh
git commit [-m] [--amend]
```

``` sh
git reset [--soft] [--hard] [commit]
reset [commit] <paths>
```

## Branching

Git was designed to make branching easy.

``` sh
git branch [--list] [-d] [-D] 
```

## Merging

Normal commits have 1 parent. Merge commits have 2. Or more. Apparently, there's a [commit in the Linux Kernel with 66 parents][23].

### Dealing with conflicts

## Rebasing

You could merge, then deal with conflicts. But, why not deal with conflicts, then merge?

## Squashing

## Flow



## monorepos vs polyrepos

If you have to make coordinated changes across several repos, you might have too many repos.

If you have code of different maturity, different release cycles, different teams, different tooling, these might be better off in different repos.



[22]: https://docs.microsoft.com/en-us/dotnet/architecture/cloud-native/infrastructure-as-code
[23]: https://www.destroyallsoftware.com/blog/2017/the-biggest-and-weirdest-commits-in-linux-kernel-git-history

