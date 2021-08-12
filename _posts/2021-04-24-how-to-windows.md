---
layout: post
title:  "How to do Windows"
date:   2021-04-24 19:51 +1300
categories: programming
---

![Windows]({{ "/images/windows-logo.svg" | absolute_url }}){:style="float: right; margin: 0px 18px 18px 18px; width: 25%"}

It's been a while since I packed my last Windows box with it's pair of screaming 733 MHz Pentiums into a closet, never to return. The tech landscape has shifted a lot: AWS, smart phones, the evolution of JavaScript, the various permutations of data and machine-learning. Well, never say never. Here we are in 2021, the world is turned upside down, and after 15-plus years of Mac and Linux, I'm reluctantly back on Windows.

So, in 2021, how do you—[or can you][12]—[make Microsoft Windows tolerable][11]? Here's what I've figured out so far.

## Just say no

First, don't switch unless you have to. Expect to lose a week or two setting up, working kinks out, and getting used to a new environment. Also, expect to pay an ongoing tax on your productivity if you switch back and forth between Mac and Windows.

CTOs, VPs of technology, don't do this to your people. Allow them to choose the platform on which they are most productive. Whatever you gain from standardization will be more than offset by losses in productivity, increased vendor lock-in, and decreased hiring pool.

That said, I really only need 3 things to be productive: a text editor, a terminal, and a browser. After a few weeks, I have these more or less dialed in and it's starting to feel like a [workable development environment][13].

## Keys

Pushing things like typing down into muscle memory frees up space for higher-level thinking. Switching keyboards makes that harder.

While key-bindings are customizable, some friction around keyboard layout is unavoidable. Your choice seems to boil down to remap alt to ctrl and deal with the quirks that induces or just get used to switching and pay the tax.

It took me while to figure out that `windows-key + .` brings up a special-characters menu like `control + command + space` on MacOS. Apparently, you can't directly type things like curly-quotes without a numeric keypad.

Here's more on keyboard remapping:

- [How to Remap Your Windows Cut/Copy/Paste to OS X-like Controls][3001]
- [How To Reconfigure Keyboard By Remapping Keys On Windows 10][3003]

[3001]: https://www.howtogeek.com/219156/how-to-remap-your-windows-cutcopypaste-to-os-x-like-controls-and-vice-versa/
[3003]: https://www.mobigyaan.com/how-to-reconfigure-keyboard-by-remapping-keys-on-windows-10


## Text Editors

![Windows]({{ "/images/vs-code-logo.png" | absolute_url }}){:style="float: right; margin: 0px 18px 18px 18px; width: 8%"}

This is a bright spot. [VS-Code][16] is excellent. JetBrains products are, too. Both work fine on Windows.

## Command shell and terminal

![Windows Terminal]({{ "/images/windows-terminal.png" | absolute_url }})

In the old days, I used [Cygwin][6] to "get the Linux feeling on Windows". CygWin is still there, but these days, there's also [Windows Subsystem for Linux, aka WSL 2][2]. In true Microsoft style, you [apparently have to install WSL 1, then upgrade to WSL 2][1]. But, once you do that, you've got all the GNU-ish and Linux-y tools your grinchy little hacker heart desires. Pull your dot files off GitHub and away you go. I installed [OhMyZsh][3] and the [powerline font package][7] for an extra layer of nice.

I found [Fluent Terminal][4] first through [this post][8]. Fluent looks sharp, but I ran into issues scrolling back through long terminal sessions. Also, when pasting into IPython sessions, the indenting gets screwed up.

So far, [Windows Terminal][5] seems [more solid][10] and pasting into IPython works as expected.

See also:

- [Setting up Windows Terminal, WSL and Oh-my-Zsh][14]
- [A Linux Dev Environment on Windows with WSL 2][15]


## Browser

![Windows Edge]({{ "/images/edge-logo.jpg" | absolute_url }}){:style="float: right; margin: 0px 18px 18px 18px; width: 15%"}

Microsoft has quite a history with browsers. Internet Explorer won the browser wars and then became epically aweful. What is now called “Legacy Edge” was a failed rewrite.

The new Edge is basically white-labeled Chrome. Perhaps an admission of defeat, but it's quite simply a decent browser. Seems like a good call.


## Say something nice

The desktop switching feature works nicely. You can even label desktops. Why [Apple won't implement named desktops[19] is totally beyond me. People have been [asking for a decode][18].


## What the hell am I doing here?

Some Microsoft sales rep did a heck of a job here in Wellington. There seems to have been a large amount of Redmond kool-aide going around at some point. One employee handbook I happened to peruse pledges commitment to Microsoft in *the third paragraph*.

I overheard a co-worker saying, “you get what you pay for with open source software.” He only trusts products where you can call tech support when they break and it's their problem to fix it. There's a sentiment I hadn't heard in ages.

As Microsoft turned underdog, I've found myself rooting for them. The company's messaging is much improved under Nadela. AWS needs a viable competitor and Google seems like it can't be bothered. I'd like to see a Microsoft that produces great products that mesh nicely with the non-Windows world.


## Misadventures in Windows-land

...I'm just complaining now, preserving my travails for the record.

### WSL2 DNS issues

Apparently, WSL2 does some behind the scenes hackery to configure `/etc/resolv.conf` based on the host OS settings, which [can or maybe used to run into problems][2001]. You can fall back on [manually configuring DNS][2002].

[2001]: https://github.com/microsoft/WSL/issues/5256
[2002]: https://gist.github.com/sivinnguyen/8bc0125b274250683a97e149cf270040

### WSL2 clock skew

WSL 2 has an issue with clock skew. I kept having to reset the clock after sleeping, like so:

```sh
sudo hwclock -v -s
```

It looks like the latest update fixes the clock skew issue. I had this version `5.4.72-microsoft-standard-WSL2`. I upgraded to `5.10.16.3-microsoft-standard-WSL2`. True to form, the installer ".msi" file has some issue requiring a [workaround][17].

BTW, you can check the kernel version, like so:

```sh
uname -r
```

### Azure DevOps WTF

What could they have been thinking? Look at the order of the breadcrumbs. They put “Pull requests” *above* the name of the repository, implying that a pull request has repositories inside it. Just weird.

![Azure DevOps]({{ "/images/azure-devops-breadcrumbs.png" | absolute_url }})



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
[18]: https://apple.stackexchange.com/questions/18029/how-can-i-rename-desktops-in-mission-control
[19]: https://www.reddit.com/r/osx/comments/aqtgvi/is_it_possible_to_rename_a_desktop/
