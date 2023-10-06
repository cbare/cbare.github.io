# Tech Writing

Blathering about software engineering, programming languages, machine learning, data science, bioinformatics, health-tech, and other techno-babble-icious flapdoodle.

https://cbare.github.io/


## Running locally

Made with [Jekyll](https://jekyllrb.com/docs/usage/). Commonly used commands:

```
jekyll build --drafts

jekyll serve --drafts --future
```

### Ruby set up

Installing Ruby via homebrew results in this:

> ruby is keg-only, which means it was not symlinked into /usr/local,
> because macOS already provides this software and installing another version in
> parallel can cause all kinds of trouble.

```
export PATH="/usr/local/opt/ruby/bin:$PATH"
```

To figure out which gems are installed and where do:
```
gem list
gem environment
```

And, once you have the path to the jekyll executable, add that to the path:
```
export PATH="/usr/local/lib/ruby/gems/3.1.0/gems/jekyll-4.2.0/exe:$PATH"
```
