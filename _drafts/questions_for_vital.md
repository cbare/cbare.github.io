1. Please describe a product or system you have worked on, where you encountered an interesting software development problem. What did you find interesting? How did you and your team solve it?

One of the coolest projects I've worked on was called QuestionBot. It's purpose was to ask the first few questions of a patient interview in a text-based primary care visit. The responses would then be displayed and summarized to the provider who would then join the visit via text or video.

The framing of the problem was especially smart. Given a patient's chief complaint in natural language as input, the model did multi-label classification where the labels corresponded to a bank of questions written by MDs.

Casting the problem as classification meant that a relatively small model with modest requirements in data and training time yielded good performance. Saving a couple of minutes of a primary care visit is an achievable goal with significant value. In healthcare especially, the approach of making small improvements within the existing system is much more welcome than disruptive change with unproven technology.

When I joined, the group had already established good ML practices, using baseline models, version control in git/git-lfs, and a feedback loop to bring production data back for weekly retraining. But there was a gap between the data scientists who viewed their role as stopping at model building and the engineering team who felt (quite reasonably), "If it's not production quality, it doesn't go into production."

Bridging that gap involved cleaning up “research code” and laying in some engineering practices. By removing dead or repeated code, I was able to shrink the code base by about 1/3 (SLOC) while increasing test coverage to ~90%. Between myself and another engineer, we added monitoring, alerting, feature flags, and improved CI/CD. We also managed container deployment and coordinated on-call incidents with the production engineering group.

After a period of building trust between teams, the team was able to iterate quickly, adding new features with the goal of saving time in the clinical workflow, lowering cost, and ultimately increasing access to care.


2. In your ideal working situation, how do you ensure a high standard of quality? Consider both code and product perspectives. What roles are involved, and in what way?

In all creative endeavors, the product is the result of the process. Rapid iteration, incremental change, and automation are key elements of successful software engineering, the goal being to progress in small steps and gather feedback while minimizing risk. Specific practices I've found valuable are: automatied testing, version control, code review, logging and monitoring, and continuous deployment. Tools like managed components and infrastructure-as-code expand the scope what's possible for a small team.

Technology evolves quickly which means there's always more to learn. Knowledge transfer among teammates helps everyone grow together. Many of my favorite experiences as an engineer come from interacting with domain experts - molecular biologists, statisticians, and medical doctors. Getting to know a bit of their vocabulary is lots of fun. And, direct access to users provides insight you can't get any other way and helps target engineering effort where it's most useful.

The working environment can make or break your day-to-day experience. A supportive environment helps everyone do their best work. I appreciate and try to practice a collaborative, low-ego, blame-free approach. Building new things may have it's ups and downs, but should be fun and rewarding for all concerned. The most satisfying projects combine a high level of practice, the right amount of autonomy and challenge, and a worthwhile mission.
