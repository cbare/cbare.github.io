---
layout: post
title:  "Security for Developers"
date:   2021-08-11 09:38 +1300
categories: ops software-engineering
---

Who got hacked this week? In the cat-and-mouse game of security, you can't avoid the impression that the attackers are way out ahead of the defenders, these days.

Developers can't really escape security, no matter how removed that is from our true specialty. Partially inspired by an episode of [Software Engineering Radio on Secure Coding][4], I'm collecting a few resources on practical application security for the busy developer.

The first place to go is [Open Web Application Security Project (OWASP)][1], where you'll find [guides][14], [videos][12], [cheat sheets][13].


## What could go wrong?

The STRIDE threat classification model gives a few answers.

| Threat                     | Desired property  |
+----------------------------+-------------------+
| **S**poofing               | Authenticity      |
| **T**ampering              | Integrity         |
| **R**epudiation            | Non-repudiability |
| **I**nformation disclosure | Confidentiality   |
| **D**enial of Service      | Availability      |
| **E**levation of Privilege | Authorization     |


## Code

How do you write code that resists hacking?

- Validate and sanitize inputs
- Keep secrets safe and rotatable


## Hygiene

- least-privilege
- 2-factor auth
- key rotation
- logging for infra changes


## Vulnerability scanning

docker scan / Snyk gives you OS level vulnerabilities. You can do little about them other than `apt upgrade` to latest patches.

Safety from PyUp scans Python dependencies. It gave msf-pipeline 0.0.7 the thumbs up.

Open source dependencies.
[SLSA - Supply-chain Levels for Software Artifacts][9]

Application security is just one of the [elements of cybersecurity][11].


## User login and authorization

## API security

## Container security

## Capture the flag

Sometimes I wish I had misspent my misspent youth breaking into websites. Then I could have a lucrative career now as a security consultant.

## Designing secure systems

Boundaries of Trust. System design and cloud configuration.


[1]: https://owasp.org/
[2]: https://jacobian.org/2021/jul/8/appsec-pagnis/
[3]: https://docs.microsoft.com/en-us/azure/architecture/serverless-quest/functions-app-security
[4]: https://www.se-radio.net/2021/08/episode-475-rey-bango-on-secure-coding-veracode/
[5]: https://sysdig.com/blog/container-security-best-practices/
[6]: https://www.whitesourcesoftware.com/resources/blog/application-security/
[7]: https://www.sans.org/top25-software-errors/
[8]: https://pythonspeed.com/articles/docker-python-security-scan/
[9]: https://slsa.dev/
[10]: https://octoverse.github.com/static/github-octoverse-2020-security-report.pdf
[11]: https://cyberthreatportal.com/elements-of-cybersecurity/
[12]: https://www.youtube.com/user/OWASPGLOBAL
[13]: https://cheatsheetseries.owasp.org/
[14]: https://owasp.org/www-pdf-archive/OWASP_Code_Review_Guide_v2.pdf
