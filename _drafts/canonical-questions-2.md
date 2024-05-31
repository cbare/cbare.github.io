Education

My first year of high school and the preceeding three years of middle school were at the American School of the Hague in the Netherlands. The adventure of living overseas suited me quite well – the next two years in a buttoned-down New England suburb much less so. I was placed in accelerated math and did reasonably well on the SAT, with percentiles in the 90's in both categories. My last year was at a school in a Philadelphia suburb. Going to three different high schools is something I don't recommend. In those days, I was mostly interested in skateboarding, reading science fiction, and listening to bands that would make your lawn die. I spent a lot of time programming Apple IIs. Really, not much has changed.

University was altogether a better experience, mostly due to the freedom to choose your own path, an approach I described as the major-of-the-month club. I dug heavily into biology and economics, dabbled in math and English, and took CS courses throughout. I've continued through a Master's degree in CS from University of Washington, a pile of online courses, and wide reading, with no plans to stop learning.

The best thing I did as an undergrad was to work in a plant molecular biology lab. I painted tiny dots on cucumber seedlings, wrote data analysis scripts, and watched droplets of purified protein solution flow off the end of a liquid chromatography device. That was a time when technology was giving scientists new powers to inspect individual parts of biological machinery.


Context

I've spent a big part of my working life, so far, building software for biomedical applications in research and healthcare contexts. I've found particular satisfaction in building tools that leverage the abilities of deep experts in medicine, genomics, and statistics.

The Institute for Systems Biology and Sage Bioinformatics were both explicitly open-source environments. I built tools for integrating genomics data and for open data and open science. During my time at Sage, I was the lead developer of the Python client library for the Synapse data sharing platform. I was proud of having the highest level of outside contribution of any project at the company. Bring in code, feature requests, and sometimes critical feedback from the community was, at times, contentious, but made our offerings stronger and more respected.

In different roles, I've built APIs that provided back-end CRUD operations or access to machine-learning models, following a dev-ops model. Docker has played a big role. I've deployed to several flavors of Unix, AWS Elastic Container Service, Lambda, Azure Functions, and Aptible (managed container hosting) with varying degrees of ops support. I've also provided infrastructure support for researchers running Jupyter notebooks and R-Studio on AWS. I've not yet done more that scratch the surface of Kubernetes.

As a member of the target audience, I appreciate Canonical's work towards automating application management. Application developers should focus on software engineering and domain knowledge. Managing a compute cluster can't be their job unless it becomes much easier.

The ability of an open approach to create value has, by this point, been well demonstrated. I'm a long-time believer. For years, I've benefited from tools like Ubuntu and Apt and would love the chance to make my own contribution.


Engineering Experience

I learned a lot of software engineering in the context of Java - modularity, concurrency, algorithms, and design patterns - but in the end I felt limited by the single abstraction of, "everything is an object." As my roles began to focus on providing engineering support for machine learning teams and biomedical researchers, I adopted the native tools in those areas and moved first to R then Python, with a few interesting side-trips through Lisp-family and typed-functional languages. SQL has been a constant throughout.

These days, Python is my main language. I appreciate its pragmatic foundations and the "less is more" approach of a few flexible and composable abstractions. Also, the depth of libraries for all purposes, especially data manipulation and machine learning is hard to beat. I feel like I have a good grasp of the Python data model and can confidently write tasteful idiomatic code. But, there's always so much more to learn. Go is a great choice for modern infrastructure and a great complement to Python. I've only done the beginner tutorial, but would be eager to learn more.

I've deployed code to various flavors of Unix for most of my career. I've learned as-needed enough to provision a machine for development or to host production code. Ubuntu and Apt make this easy. For cloud deployment, I've worked with Terraform, CloudFormation, and CDK, at a productive beginner level. In a professional environment, I'd typically collaborate with dedicated ops, cloud, and security engineers.

I've tried not spent much time on the fads related to engineering process, instead slowly collecting good engineering practices that I've found to make a concrete difference. The DORA metrics align fairly well with my experience.

- Automated testing is fast, repeatable, and reliable, in contrast to manual testing which is none of those. A typical project for me will have 50-80% unit test coverage. Where code has external dependencies, I prefer integration tests to mocking, as the questionable assumptions you made when writing the code will likely also be baked into the mock. When fixing a bug, I first write the test, watch it fail, write the fix, and, with satisfaction, watch it turn green. This prevents regression and concentrates testing effort on bug-prone parts of the code.

- Automated CI/CD provides the ability to rapidly iterate on incremental changes, keeping feedback loops tight and context for any particular change limited. The ability to quickly deploy puts new features in the hands of users quicker, which means bugs get found and fixed quicker.

- Logging and monitoring provides the means to observe errors, latency, and usage patterns, which helps in prioritize work.

- Direct access to users is something I've highly valued. Sitting with medical doctors, molecular biologists, or other users and watching them work gives insights that are hard to come by any other way. There's nothing quite as motivating when you get it wrong and satisfying when you get it right as direct feedback from users.

- Code review is taking some flak these days. I agree that a LGTM in the comments of a PR is worth little, but I've gotten a lot of benefit out of code review done well, more in the form of knowledge transfer and consistency than seeing bugs. I'm not a fan of fighting style wars or pointless gatekeeping, but good code review is a worthwhile skill.

- Automated documentation tools like Javadoc or Sphinx are underrated. Good documentation explains why. Writing good docs push you to think from the perspective of the caller, which encourages APIs that minimize cognitive load.
