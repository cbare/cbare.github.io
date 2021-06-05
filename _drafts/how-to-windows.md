---
layout: post
title:  "How to do Windows"
date:   2021-04-24 19:51 +1300
categories: programming
---

It's been a while since I packed my last Windows box with it's pair of screaming 733Gz Pentiums into a closet, never to return. The tech landscape has shifted a lot: AWS, smart phones, the evolution of JavaScript, the various permutations of data and machine-learning. Well, never say never. Here we are in 2021, the world is turned upside down, and after 15 years of Mac and Linux, I'm reluctantly back on Windows.

So, in 2021, how do you—[or can you][12]—[make Microsoft Windows tolerable][11]? Here's what I've figured out so far.

## Just say no

First, don't switch unless you have to. Expect to lose a week or two setting up, working kinks out, and getting used to a new environment. Also, expect to pay an ongoing tax on your productivity if you switch back and forth between Mac and Windows.

That said, I really only need 3 things to be productive: a text editor, a terminal, and a browser. After a few weeks, I have these more or less dialed in and it's starting to feel like a [workable development environment][13].

## Keys

While key-bindings are usually customizable, some friction around keyboard layout is unavoidable. Your choice seems to boil down to remap alt to ctrl and deal with some quirky cases or just get used to switching.

Home and end keys vs ctrl-a and ctrl-e are especially annoying. There's apparently no way to type things like em-dash and curly-quotes on a Windows laptop without a #@$%ing numeric keypad?!?

Here's more on keyboard remapping:

- [How to Remap Your Windows Cut/Copy/Paste to OS X-like Controls][3001]
- [How To Reconfigure Keyboard By Remapping Keys On Windows 10][3003]

[3001]: https://www.howtogeek.com/219156/how-to-remap-your-windows-cutcopypaste-to-os-x-like-controls-and-vice-versa/
[3003]: https://www.mobigyaan.com/how-to-reconfigure-keyboard-by-remapping-keys-on-windows-10


## Command shell and terminal

Twenty years ago, I used [Cygwin][6] to "get the Linux feeling on Windows". CygWin is still there, but these days, there's also [Windows Subsystem for Linux, aka WSL 2][2]. In true Microsoft style, you [apparently have to install WSL 1, then upgrade to WSL 2][1]. But, once you do that, you've got all the GNU-ish and Linux-y tools your grinchy little hacker heart desires. Pull your dot files off GitHub and away you go. I installed [OhMyZsh][3] and the [powerline font package][7] for an extra layer of nice.

I found [Fluent Terminal][4] first through [this post][8]. Fluent looks sharp, but I ran into issues scrolling back through long terminal sessions. Also, when pasting into IPython sessions, the indenting gets screwed up.

So far, [Windows Terminal][5] seems [more solid][10] and pasting into IPython works as expected.

### WSL2 clock skew

WSL 2 has an issue with clock skew. I kept having to reset the clock after sleeping, like so:

```sh
sudo hwclock -v -s
```

I had this version `5.4.72-microsoft-standard-WSL2`. I just upgraded to `5.10.16.3-microsoft-standard-WSL2`. True to form, the installer ".msi" file has some issue requiring  [work-around][17].

BTW, you can check the kernel version, like so:

```sh
uname -r
```

See also:

- [Setting up Windows Terminal, WSL and Oh-my-Zsh][14]
- [A Linux Dev Environment on Windows with WSL 2][15]


## Browser

Microsoft has quite a history with browsers. Internet Explorer won the browser wars and then became epically aweful. What is now called Legacy Edge was a failed rewrite.

The new Chromium-based Edge is a quite simply a decent browser. It's basically white-labeled Chrome. Perhaps an admission of defeat, but also a good call.


## Code Editors

This is a bright spot. [VS-Code][16] is excellent. JetBrains products are excellent. Both work fine on Windows.


## The rest of the ecosystem

### AzureDevOps

Works fairly well. But, why are the breadcrumbs in this order?

{{ "/images/new-repository.png" | absolute_url }}

Files and commits are *inside* a repo, so should be *below* in the implied hierarchy. What could they possibly have been thinking?

### .Net

Based on my dated view, C# seems a bit more refined in some ways than Java, but very similar in a [kingdom-of-nouns][9] kind of way. F# looks a bit like Scala. The .Net platform seems to have taken a welcome step in the right direction with it's new tag-line. "Free. Cross-platform. Open source." Good on them!

Also in the plus column, C# can be used to write desktop GUI apps and Unity has a lot of appeal.

On the other side, we all have a finite learning budget and spending that effectively is important. I generally don't want to know the Microsoft way to do things I can already do the everybody-else way. Same goes for Google or Amazon for that matter.

### Azure

There's plenty to say about Azure. Microsoft has a viable cloud platform, which in itself is something. But I'll leave that for another day.


## What the hell am I doing here?

Some Microsoft sales rep did a heck of a job here in Wellington. There seems to have been a large amount of Redmond kool-aide going around at some point. The employee handbook at one company pledges loyalty to MSFT in *the third paragraph*.

I overheard one co-worker saying that with open source software, you get what you pay for. He only trusts products where you can call tech support when they break and it's their problem to fix it. I haven't heard that voiced in ages.

As Microsoft has turned underdog, I find myself rooting for them. The company's messaging is much improved under Nadela. AWS needs a viable competitor and Google seems like it can't be bothered.


[1]: https://docs.microsoft.com/en-us/windows/wsl/install-win10
[2]: https://github.com/microsoft/wsl
[3]: https://ohmyz.sh/
[4]: https://github.com/felixse/FluentTerminal
[5]: https://github.com/microsoft/terminal
[6]: https://www.cygwin.com/
[7]: https://github.com/powerline/fonts
[8]: https://medium.com/@blurdylan/transforming-your-ugly-terminal-to-a-unicorn-b83f315a36d1
[9]: http://steve-yegge.blogspot.com/2006/03/execution-in-kingdom-of-nouns.html
[10]: https://towardsdatascience.com/new-windows-terminal-the-best-you-can-have-9945294707e7
[11]: https://news.ycombinator.com/item?id=14409441
[12]: https://blog.aaronbieber.com/2020/01/30/is-windows-tolerable-in-2020.html
[13]: https://pbpython.com/wsl-python.html
[14]: https://www.ivaylopavlov.com/setting-up-windows-terminal-wsl-and-oh-my-zsh/
[15]: https://nickjanetakis.com/blog/a-linux-dev-environment-on-windows-with-wsl-2-docker-desktop-and-more
[16]: https://code.visualstudio.com/
[17]: https://github.com/microsoft/WSL/issues/5014#issuecomment-605243281
