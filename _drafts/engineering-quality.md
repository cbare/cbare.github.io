## Software-engineering
- Testing
- Logging
- Monitoring
- Code review
- Automated continuous deploy
- Standard project template
- Standards for ops, e.g. terraform, CDK
- [Docs](https://www.sohamkamani.com/blog/how-to-write-good-documentation/)
  
## Design
- [functional core, imperative shell](https://gist.github.com/kbilsted/abdc017858cad68c3e7926b03646554e)

## Continuous improvement
- retrospectives on errors / downtime
  - fill gaps in test coverage
  - error handling / retry / recovery

## Machine-learning
- critical analysis of training data
- establish baseline model
- reproducible model training
- reproducible hyperparameter tuning
- model / data provenance
- model assessment
  - post-training
  - in-production
  - held-out test set
  - acquire or label new test sets
  - compare against baseline model
  - real world measures
  - test for unintentional bias
- periodic retraining / online learning

## Data pipelines
- assertions: sanity checks built into processing code
- check pre- and post-conditions


## APIs
- [REST API Guidelines from Microsoft][5]
- example's of excellent API docs:
  - [Stripe's API docs][6]
  - [Github][7]



## Ensuring code quality

- ask: "How to ensure code quality?"
- CI/CD, build and deploy process
  - ask: "How do we reduce the likelihood of bugs into production?"
  - feature flags
- logging, error analysis
  - ask: "If you get bug reports, how do you dig in?"
- monitoring & analytics
  - ask: "How do we better understand user behavior, role out new features?"
    - dashboards?
    - paging?
    - A/B tests?
- users, auth, accounts
  - ask: "How do we track users?"
- infra management
  - terraform / cloudformation / CDK
  - staging / prod






[5]: https://github.com/Microsoft/api-guidelines/blob/master/Guidelines.md
[6]: https://stripe.com/docs/api
[7]: https://developer.github.com/v3/





