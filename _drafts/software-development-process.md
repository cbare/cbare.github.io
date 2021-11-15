# Software development process and practice

The following are a few recommendations to improve software development process based on prior experience in other health-related technology companies. Iterating rapidly is a key factor to innovation and our present process discourages rapid iteration. A few modest changes in process could help unlock the potential of the company's data assets and scientific talent while preserving our commitment to quality, security, and compliance.


## Caveats

My experience is limited and doesn't include building software as a medical device. It does, however, cover software that handles PHI and is subject to HIPAA developed at a hospital, two big pharmas, two research groups, and two health-related start-ups, one providing primary care medicine. Previous projects consisted of data ingest, databases, web services, and model retraining and deployment, but no "shrink-wrapped" software.


## Goals

What are the goals of software development process?

### Safety and quality

- Users experience few bugs or downtime
- Reduce risk of security incidents
- Handling PHI:
  - Ethical
  - Legally compliant
  - Build trust by being seen as good stewards of PHI
- Enable sales to and investments from organizations with certification requirements

### Innovation

- Develop new technology, scientific collaboration
- Use research and data pool to develop new features and products
- Enable "learning loop" in which a smart product extracts feedback from users that improve the product.
- Respond quickly to opportunities, react quickly to changing technology, etc.

Over all, we want to build innovative products safely and at a competitive pace. These goals are in conflict and must, to some extent, be traded off with each other and with available resources. However, modern software development practice offers tools and techniques that address quality and security concerns while enabling iterative development and short release cycles.


## Strategies

What strategies are used in modern software development to help achieve the above goals?

- Version control
- Code review
- Automated testing
- Automated deployment
- Monitoring
- Containerization
- Managed components / serverless

### CI/CD

>> “Continuous integration and Continuous development, are the premier examples of the value of automation. CI/CD puts in place guardrails that allow developers to push new code and features that then automatically deploy to production environments. Before CI/CD gained popularity merging code and deploying were a much more cumbersome process. [...] The guardrails that enable CI/CD are version control systems, automated tests, and monitoring tools.” [Atlassian - Software Development: Modern practices and where it’s headed][1]

The key difference from "waterfall" is the emphasis on minimizing the scope and cost of bugs, rather than upfront effort to eliminate bugs, which is subject to increasing cost and diminishing returns.

### Cookie-cutter patterns

Establish architectural patterns for commonly used building blocks:

- Authentication of users and software
- Configuration for Azure resources
- No need to repeatedly review the same patterns
- Review can be limited to parts that deviate from established pattern or establish new patterns

### Automation

Certifications require specific sets of controls, scans, and documentation. It's worth exploring whether parts of these requirements can be automatically generated during the build process. For example, automated vulnerability scans are becoming a standard part of CI/CD pipelines.


## Triage

How much process is the right amount?

The level of exposure and risk of a software project should dictate appropriate level of process. The heavily regulated process mandated for medical devices is slow, cumbersome, and expensive and should not serve as the model for projects outside this regime.

Projects might be triaged into three levels, roughly high, medium, and low process:

- Medical device
- Customer facing products
- Internal tools

Process should be invoked to address specific concerns in proportion to the risk. Where consequences are low, or can be deliberately managed, process can be very light.


[1]: https://www.atlassian.com/software-development
[2]: https://docs.microsoft.com/en-us/azure/architecture/example-scenario/apps/devops-dotnet-webapp
[3]: https://itrevolution.com/accelerate-book/
[4]: https://queue.acm.org/detail.cfm?id=3454124
