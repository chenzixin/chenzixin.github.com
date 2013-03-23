---
layout: post
title: "源代码管理十诫摘抄"
description: "<p>写每一条提交信息时，就好象等下会读到它的人是一个斧头杀人狂，而且他还知道你住在哪里。</p><p>没有哪一条是很难理解的。老实说，它们都很基础：尽快并频繁地提交，确认你提交的东西改了什么，还有东西一定要放进版本控制系统里，解释清楚你的提交信息和确保是你自己提交的，不要忘记数据库和不要忘记附属文件。</p>"
category: program
tags: [pmp]
---
{% include JB/setup %}

[图灵社区](http://www.ituring.com.cn/)翻译的[源代码管理十诫](http://www.ituring.com.cn/article/1322)，昨天晚上通读了一遍，英文原文需要翻墙才能[打开](http://www.troyhunt.com/2011/05/10-commandments-of-good-source-control.html)。

作者的观点，有些偏激，特别是花了大量的篇章斥责 VSS ，我们可以理解为：找一个靠谱儿的源码控制工具。

列下目录，时时提醒自己：

* Stop right now if you’re using VSS – just stop it!
* If it’s not in source control, it doesn’t exist
* Commit early, commit often and don’t spare the horses
* Always inspect your changes before committing
* Remember the axe-murderer when writing commit messages
* You must commit your own changes – you can’t delegate it
* Versioning your database isn’t optional
* Compilation output does not belong in source control
* Nobody else cares about your personal user settings
* Dependencies need a home too


**精彩片断：**

There’s an old adage (source unknown), along the lines of “Write every commit message like the next person who reads it is an axe-wielding maniac who knows where you live”. If I was that maniac and I’m delving through reams of your code trying to track down a bug and all I can understand from your commit message is “updated some codes”, look out, I’m coming after you!

**总结很好：**

None of these things are hard. Honestly, they’re really very basic: commit early and often, know what you’re committing and that it should actually be in VCS, explain your commits and make sure you do it yourself, don’t forget the databases and don’t forget the dependencies. 

**附上中文：**

没有哪一条是很难理解的。老实说，它们都很基础：尽快并频繁地提交，确认你提交的东西改了什么，还有东西一定要放进版本控制系统里，解释清楚你的提交信息和确保是你自己提交的，不要忘记数据库和不要忘记附属文件。

全文完。