Projects consisting of software and machine learning components often suffer from difficulties collaborating across disciplines. Abstraction and a divide and conquer strategy are essential. Dividing software into components (modules, functions, subsystems) and hiding internals behind interfaces is a key principle of modular software development that allows teams to divide work. The component interface plays a key role. It is where teams negotiate and renegotiate how to divide work and assign responsibilities.

Training and retraining
monitoring data and models


Model requirements
- accuracy
- training time
- inference time
- fairness
- explainability


How much tolerence/budget do we have for research, with uncertain timelines and results?

ownership and control of access to data
data quality
how much data cleaning is needed?
understanding context of a dataset: how data was collected, biases and flaws
assessing consistency in annotation
understanding the need for retraining with up-to-date training data
training data sources can change format, semantics, or distribution
Security and privacy concerns can also limit access to data

To build an ML-enabled system both ML components and traditional non-ML components need to be integrated and deployed, requiring data scientists and software engineers to work together, typically across multiple teams. We found many conflicts at this collaboration point, stemming from unclear processes and responsibilities, as well as differing practices and expectations.

Culture Clashes between data science and software engineering, made worse by unclear responsibilities and boundaries.

siloing data scientists is widely recognized as problematic
Siloing data scientists fosters integration problems 
some orgs, particularly big tech, expect engineering skills from all data science hires

Code quality, documentation, and versioning expectations
differ widely and cause conflicts

software engineers
expressed frustration in interviews that data scientists do not follow
the same development practices or have the same quality standards
when it comes to writing code.

extending version control to data and models desired but “elusive”

Testing systems that include ML models is tricky.

Monitoring in production is important, but often skipped.
Model teams benefit from receiving feedback
on their model from production systems

Data scientists and software engineers are certainly not the first
to realize that interdisciplinary collaborations are challenging and fraught with communication and cultural problems

Many organizations seem to underestimate the engineering effort required to turn a model into a product to be operated and
maintained reliably. Arguably adopting machine learning increases
software complexity and makes engineering practices
such as data quality checks, deployment automation, and testing in
production even more important.
