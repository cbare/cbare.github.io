---
layout: post
title:  "C#"
category: Programming
tags: programming c-sharp dotnet
---

_A stubborn person's guide to coding in C#._

Having reached a point of disillusionment with Java, I do C# only reluctantly. Part of the design philosophy of the dotnet ecosystem is a heavy reliance on the IDE. If you're not very stubborn, you'll probably want to give in and install Visual Studio. However, I can be quite subborn.

I've been modestly successful in doing C# using VS-Code and the [dotnet cli][4]. Sometimes, things only work in powershell, but mostly will also work in WSL.

## Dotnet projects

Microsoft distinguished engineer [David Fowler][3] has good info on:

- [.NET project structure][1]
- [DotNetCodingPatterns][2]

## Commands

```sh
dotnet build
```


## Logging

I just want logs to go to the console, which should happen by default. You have to work for it a little bit, I suppose because the language is built for the IDE.

https://github.com/cbare/Etudes/blob/master/csharp/JustLogSomething/README.md



[1]: https://gist.github.com/davidfowl/ed7564297c61fe9ab814
[2]: https://github.com/davidfowl/DotNetCodingPatterns
[3]: https://github.com/davidfowl
[4]: https://learn.microsoft.com/en-us/dotnet/core/tools/dotnet


-l, --logger <LOGGER>  The logger to use for test results.
    Examples:
    Log in trx format using a--logger trx
    Log in trx format using name: --logger "trx;LogFileName=<TestResults.trx>"

    See https://aka.ms/vstest-report for more information on logger arguments.

Argument "verbosity" define the verbosity level of console logger. Allowed values for verbosity are "quiet", "minimal", "normal" and "detailed".

dotnet test -l "console;verbosity=detailed" | Set-Content -Path log.txt

