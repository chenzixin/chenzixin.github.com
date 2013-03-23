---
layout: post
title: "Linux .bash_profile .bashrc 什么区别"
description: "<p>以前公司的 Linux 貌似写 .bash_profile 是不管用的，所以一些 alias 和 PS1 都是写在 bashrc 里，现在自己的电脑反过来了，bashrc 不管用，要写 bash_profile。</p><p>这两个文件到底有什么区别？是不是有哪里可以配置，让用户登陆的时候去加载某个文件的？</p>"
category: program 
tags: [linux, bash]
---
{% include JB/setup %}

Jekyll 和 SAE 都有大量的命令行操作，在控制台下敲

`cd /some/other/dir/`

有些费劲，昨天找到一下方法，可能设置 `别名`。

于是我在 `~/.bashrc` 下添加了一批别名

{% highlight python%}
alias ll='ls -l'
alias la='ls -a'
alias df='df -h'
alias rm='rm -i'


alias cdwiki='cd /opt/confluence/bin/'

alias cdsae='cd ~/SAE/olservice/1/'
alias cdwp='cd ~/SAE/chenzixin/1/'

alias cdgit='cd ~/GitHub/chenzixin/'
alias cdpy='cd ~/GitHub/pyivy/'
alias cdjs='cd ~/GitHub/jsoops/'
alias cdsc='cd ~/GitHub/scalac/'
{% endhighlight %}

`source ~/.bashrc`

之后就可以直接 `cdwiki` 进入 Confluence 启动目录了，但是今天开机，发现 `cdwiki` 不好用了

>-bash: cdwiki: command not found

网上搜索，发现这个文章：

`/etc/profile` 此文件为系统的每个用户设置环境信息。

当用户第一次登录时，该文件被执行，并从 `/etc/profile.d` 目录的配置文件中搜集 shell 的设置。


`/etc/bashrc` 为每一个运行 bash shell 的用户执行此文件。当 bash shell 被打开时，该文件被读取。


`~/.bash_profile` 每个用户都可使用该文件输入专用于自己使用的 shell 信息，当用户登录时，该
文件仅仅执行一次！默认情况下，他设置一些环境变量，执行用户的`.bashrc`文件。

`~/.bashrc` 该文件包含专用于你的 bash shell 的 bash 信息，当登录时以及每次打开新的 shell 时，该该文件被读取。

`~/.bash_logout` 当每次退出系统(退出bash shell)时，执行该文件。

另外，`/etc/profile` 中设定的变量(全局)的可以作用于任何用户。

而` ~/.bashrc` 等中设定的变量(局部)只能继承 `/etc/profile` 中的变量，他们是"父子"关系。
 
`~/.bash_profile` 是交互式、login 方式进入 bash 运行的。

`~/.bashrc` 是交互式 non-login 方式进入 bash 运行的。

通常二者设置大致相同，所以通常前者会调用后者。

文章来自[ChinaUnix](http://linux.chinaunix.net/doc/system/2005-02-03/1084.shtml)，应该非常专业，但是没有解决我的疑惑。

---

同时，[SegmentFault](http://segmentfault.com/q/1010000000133177)上，也有网友问答，提问者我和的遭遇一样：

## Q：

>以前公司的 Linux 貌似写 .bash_profile 是不管用的，所以一些 alias 和 PS1 都是写在 bashrc 里，现在自己的电脑反过来了，bashrc 不管用，要写 bash_profile。

>这两个文件到底有什么区别？是不是有哪里可以配置，让用户登陆的时候去加载某个文件的？

被采纳的回答，也是引用上面的那段文字。

但二楼更精彩：

>其实这个问题的核心就是 Shell 初始化时读取配置文件的步骤，而 Shell 又可以分为两类：Login Shell 和 Non-login Shell

#### Login Shell 初始化时配置文件读取顺序的伪代码示意：

{% highlight python %}
execute /etc/profile

IF ~/.bash_profile exists THEN
    execute ~/.bash_profile
ELSE
    IF ~/.bash_login exist THEN
        execute ~/.bash_login
    ELSE
        IF ~/.profile exist THEN
            execute ~/.profile
        END IF
    END IF
END IF
{% endhighlight %}

#### Non-Login Shell 初始化时配置文件读取顺序的伪代码示意：

{% highlight python %}
execute /etc/bash.bashrc
IF ~/.bashrc exists THEN
    execute ~/.bashrc
END IF
{% endhighlight %}

最后，Mac 的终端默认开启为 Login Shell。而 Ubuntu 的 Gnome Terminal 默认开启的是 Non-Login Shell。

该回答参考了[这个文章](http://www.thegeekstuff.com/2008/10/execution-sequence-for-bash_profile-bashrc-bash_login-profile-and-bash_logout/)。

我想说：小白长得`真相大白`～

全文完。
