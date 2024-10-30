---
layout: post
title:  "C#"
date:   2022-01-11 11:47:00 +1300
categories: programming c-sharp dotnet
---


## Sources of good information

- https://gist.github.com/davidfowl/ed7564297c61fe9ab814
- https://github.com/davidfowl


-l, --logger <LOGGER>  The logger to use for test results.
    Examples:
    Log in trx format using a--logger trx
    Log in trx format using name: --logger "trx;LogFileName=<TestResults.trx>"

    See https://aka.ms/vstest-report for more information on logger arguments.

Argument "verbosity" define the verbosity level of console logger. Allowed values for verbosity are "quiet", "minimal", "normal" and "detailed".

dotnet test -l "console;verbosity=detailed" | Set-Content -Path log.txt

