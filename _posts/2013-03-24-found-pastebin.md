---
layout: post
title: "发现在线分享文本的应用 Peastebin"
description: "<p>因为 PyCon 2013 的 Adria Richards 事件，发现了一个很有意思的应用 Pastebin。</p><p>一开始我也怀疑，在云笔记流行的今天，这类应用，还有市场吗？不过，仔细思考，它和云笔记是不冲突的，侧重于文本的分享，而笔记更多是个人记录。而且 pastebin 经过这么多年的发展，用户体验不错，细节的设计贴心，特别是针对程序员的语法高亮，个人很喜欢。</p><p>Pastebin.com 还有开放的 API 使用，也是大家风范。</p><p>Pastebin 对未注册用户也开放使用，是否有限制还不太清楚，不过既然喜欢，我也注册了自己的账号，记下注册信息和邮件提醒，也是学英文的机会。</p>"
category: program
tags: [cloud, note, pastebin, wiki]
---
{% include JB/setup %}

因为 PyCon 2013 的 Adria Richards 事件，发现了一个很有意思的应用 Pastebin。

先看下来自 [WikiPedia](http://en.wikipedia.org/wiki/Pastebin) 的释义：

<blockquote>
<p style="text-align:justify; text-justify:inter-ideograph">A pastebin is a type of web application where anyone can store text for a certain period of time. This type of website is mainly used by programmers to store pieces of source code or configuration information, but anyone can basically share any type of text. The idea behind pastebins is to make it more convenient for people to share large amounts of text online. A vast number of pastebin related websites exist on the Internet, suiting a number of different needs and providing features tailored towards the crowd they focus on most.</p>
</blockquote>

<blockquote>
<p style="text-align:justify; text-justify:inter-ideograph">Pastebin-related websites have been around since at least 2002.<a href='http://pastebin.com/' target='_blank'>Pastebin.com</a> is the most popular one and also one of the earliest. Over time, many of the public pastebins have become specialized and targeted at a single group of users. In many cases, pastes made to pastebins are kept only for a certain period of time. Some, however, allow for varying lengths of time anywhere from one minute to an infinite amount of time.</p>
</blockquote>

<blockquote>
<p style="text-align:justify; text-justify:inter-ideograph">Although there are literally hundreds of pastebins available, most have a common set of features. They may appear different or target a different user base, but at the core, they take an upload or text paste and provide a sharable HTTP URL that contains the body of text. A pastebin often has the capability to apply formatting and syntax highlighting to the text for easier viewing. Throughout the years, the number of languages and formatting styles has grown quickly as the Pastebin user base has grown and their needs have fanned out. A well-known highlighting software package called GeSHi supports the most common pastebins. Some of the newer pastebins provide features for comparing two or more pastes, synchronous notifications through IRC or XMPP, paste histories, encryption, password protection, and virtual subdomains. Nowadays, created pastebins allows pasted codes to be executed at server side.</p>
</blockquote>

一开始我也怀疑，在云笔记流行的今天，这类应用，还有市场吗？不过，仔细思考，它和云笔记是不冲突的，侧重于文本的分享，而笔记更多是个人记录。而且 pastebin 经过这么多年的发展，用户体验不错，细节的设计贴心，特别是针对程序员的语法高亮，个人很喜欢。

Pastebin.com 还有开放的 API 使用，也是大家风范。

Pastebin 对未注册用户也开放使用，是否有限制还不太清楚，不过既然喜欢，我也注册了自己的账号，记下注册信息和邮件提醒，也是学英文的机会：

**Sign Up Page**

Hi user, welcome to Pastebin!

We have sent you an email to xxx@xxx.com with an activation link in it. Please click on the activation link to activate your account.

If you cannot find this email, please check your spam/junk inbox, sometimes the registration emails end up there. If you still cannot find the link, please contact us from the email address you used in the signup form, and tell us your username. We can then activate your account manually.

**Mail Box** 

Hi user,

You are now a member of Pastebin.com

To activate your account, please click the following link: http://pastebin.com/activate_account.php?k=xxx

Below you can find your login data:

Username: user

Password: **hidden for security reasons**

You can follow Pastebin at Twitter and Facebook.

Kind regards,

The Pastebin Team 

注意，Pastebin 在邮件中隐藏了密码，我又想起了 Simpleframework 在邮件中使用明文密码的事件。当然，大公司一般都不会犯这种错误。

