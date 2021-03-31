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

## Setting up 2 unique users

As the instructor, you'll want to demonstrate fun things like merge conflicts and maybe even rewriting history. You'll need an alter-ego. Mine is named [NastyHacks][21]. A little hack to your ssh config let's you identify yourself to GitHub using a different SSH key, so that you can pretend to be two different GitHub users from the same machine.

``` sh
git config "user.name" "Nasty Hacks"
git config "user.email" "nasty.hacks@foo.com"
sed -i 's/github.com/github.com-nastyhacks/g' .git/config
```

``` sh
cat ~/.ssh/config
Host github.com
        HostName github.com
        User git
        IdentityFile ~/.ssh/id_rsa

Host github.com-nastyhacks
        HostName github.com
        User git
        IdentityFile ~/.ssh/nastyhacks
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

## Upstream

If you're working by yourself, you can get by with a local repository. If you want to share and collaborate you'll need an upstream repo that you and others can access. GitHub, GitLab, BitBucket, AWS CodeCommit, and Azure DevOps provide upstream repos.

GitHub got started in 2008. My first commit is from 2010. Without the benefit of hindsight, it's not at all obvious that source control plus social would be equal to 7.5 billion. But, in retrospect, giving software developers a little help in terms of a ready-made structured social interaction is really smart.

### Remotes

Add a remote:

``` sh
git remote add origin git@github.com:cbare/hackalicious.git
```

See your repo's remotes:

``` sh
git remote -v
```

## Branching

Git was designed to make branching easy.

``` sh
git branch [--list] [-d] [-D] 
```

## Merging

Normal commits have 1 parent. Merge commits have 2. Or more. Apparently, there's a [commit in the Linux Kernel with 66 parents][23].

### Dealing with conflicts

## Logs

``` sh
git log [--compact-summary] [--name-only]
```

``` sh
git gr
```

## Rebasing

You could merge, then deal with conflicts. But, why not deal with conflicts, then merge? That's what rebasing is.

### Squashing

If you rebase, you'll probably also want to Squash and Merge (in GitHub) and `git merge --squash feature-branch` in command line Git.

## Workflow

Git is a distributed version control system. You can push from one repo to another any way you want. That could lead to a confusing situation. It's up to us as Git users to figure out a sensible pattern.

### Git-flow

The git-flow model was proposed in 2010 in [A successful Git branching model][25] by Vincent Driessen. A complex structure for cases where you need to support several versions at the same time. 

### Github-flow

[GitHub-flow][24] is simpler. There's only one rule: anything in the main branch is always deployable.

## Monorepos vs polyrepos

If you have to make coordinated changes across several repos, you might have too many repos.

If you have code of different maturity, different release cycles, different teams, different tooling, these might be better off in different repos.


[21]: https://github.com/nastyhacks
[22]: https://docs.microsoft.com/en-us/dotnet/architecture/cloud-native/infrastructure-as-code
[23]: https://www.destroyallsoftware.com/blog/2017/the-biggest-and-weirdest-commits-in-linux-kernel-git-history
[24]: https://guides.github.com/introduction/flow/
[25]: https://nvie.com/posts/a-successful-git-branching-model/
