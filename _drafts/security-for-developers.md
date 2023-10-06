---
layout: post
title:  "Security for Developers"
date:   2021-08-11 09:38 +1300
categories: ops software-engineering
---

Who got hacked this week? In the game of info-sec, you can't avoid the impression that the attackers are way out ahead of the defenders, these days.

Developers can't escape security, no matter how far removed from their core specialty. [Security needs to shift left into the software development lifecycle][17]. But, how to think about [Secure Coding][4]? I'm collecting a few resources on practical application security for the busy developer.



The first place to go is [Open Web Application Security Project (OWASP)][1], where you'll find [guides][14], [videos][12], [cheat sheets][13].


Authentication - who are you?
Authorization - what permissions do you have?

Groups
Roles
Permissions


[Why Authorization is hard][201] Sam Scott, cofounder and CTO of [Oso][202]

def authorize(u: User, a: Action, r: Resource) -> bool

Authorization Academy
Concepts. Architecture. Best Practices.
A series of technical guides for building application authorization.


organizations, sharing, ownership, project roles, folders, org charts, impersonation, caretakers, family members, groups, nested groups, custom roles, default roles, permission toggles, public resources, user status, banned users, attribute matching, demographics, usage quotas, subscription based, custom policies

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


Zero Trust, assume breach
Logging and monitoring
Use secret store
Scan dependencies for known vulnerabilies
Run code as service accounts with own privilege, don't run as root
Set cloud resource quotas
Authentication (determine identity), authorization (what priviliges)

## Types of Attacks
Server-side request forgery (also known as SSRF)
XML external entity injection (also known as XXE)
Remote code execution (RCE)
SQL injection SQLi



Talk from PyCon 2022
Securing Code with the Python Type System
Graham Bleaney, Pradeep Kumar Srinivasan



[protecting your APIs with OAuth2][15]
[Best practices for REST API security][16]

[The Nuts and Bolts of OAuth 2.0][103]

[Implementing software security in open source][18] How to automate security and build confidence in your code. By Lisa Tagliaferri, PhD

[Why JWTs Suck as Session Tokens][19]

[Container Security Site][20]



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

[15]: https://stackoverflow.blog/2022/04/11/the-complete-guide-to-protecting-your-apis-with-oauth2/
[16]: https://stackoverflow.blog/2021/10/06/best-practices-for-authentication-and-authorization-for-rest-apis/

[17]: https://stackoverflow.blog/2022/05/05/security-needs-to-shift-left-into-the-software-development-lifecycle/

[18]: https://github.com/readme/guides/sigstore-software-security

[19]: https://developer.okta.com/blog/2017/08/17/why-jwts-suck-as-session-tokens

[20]: https://www.container-security.site/


[101]: https://oauth.net/specs/
[102]: https://oauth.net/videos/
[103]: https://www.udemy.com/course/oauth-2-simplified/

[201]: https://www.osohq.com/post/why-authorization-is-hard
[202]: https://osohq.com
[203]: https://osohq.com/academy
