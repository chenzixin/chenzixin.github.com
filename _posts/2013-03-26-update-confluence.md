---
layout: post
title: "升级 Confluence 至 3.5.17"
description: "<p>自从 2009 年我找到 Confluence 之后，对其它的 Wiki 引擎，就再也没有发掘的兴趣了，很专一。</p><p>你会问，为什么写 BBS6 文档，又搞一套 DokuWiki？主要还是看重它的轻，不依赖数据库，只要有 PHP 环境就可以跑起来（其实 Confluence 也是支持嵌入式数据库的，只是 Java 的主机，远没有 PHP 普及）。</p><p>但文档还没有开始写，DokuWiki 的各种局限性开始暴露，虽然尝试用 MarkDown 插件、侧边栏插件、文字颜色插件、改名插件 等程序来增强，但最终在发现 Confluence 支持将整个空间导出为 HTML 之后，立刻决定放弃 DokuWiki，虽然它的默认主题很好看，虽然它支持分段编辑。</p>"
category: program
tags: [wiki, pmp]
---
{% include JB/setup %}

## Wiki

我记得年后没多久，我用 DokuWiki 搭建了一个写文档的平台，并初步拟好了 BBS6 DOC 的目录，但之后的一个月，项目基本搁置，主要是手上有更重要的事情要做，现在旧事重提。

关于文档，关于 Wiki 引擎，我自己可谓阅历甚广，几乎所有的主流引擎，我都尝试过，这里有一份不完全清单：


<table class="table table-bordered table-hover table-striped">
<tr>
<td>MediaWiki</td> <td><a href="http://zh.wikipedia.org/">维基百科</a>引擎</td> <td><a href="http://www.mediawiki.org/wiki/MediaWiki">官网</a></td></tr>
<tr><td>HDwiki</td><td><a href="http://www.baike.com/">互动百科</a>引擎</td><td> <a href="http://kaiyuan.hudong.com/">官网</a></td></tr>
<tr><td>trac</td><td>曾用来管理亲子项目的开发 集成 Wiki</td><td><a href="http://trac.edgewall.org/">官网</a></td></tr>
<tr><td>redmine</td><td>Ruby 开发的全功能项目管理工具 集成 Wiki</td><td><a href="http://www.redmine.org/">官网</a></td></tr>
<tr><td>Twiki</td><td>Perl 开发的 Wiki 引擎 印象中曾得到 Yahoo 的大力支持 企业 Wiki 的首选</td><td><a href="http://twiki.org/">官网</a></td></tr>
<tr><td>Pwyky</td><td>Python 开发的 30KB 单文件 Wiki 引擎</td><td><a href="http://infomesh.net/pwyky/">官网</a></td></tr>
<tr><td>MoinMoin</td><td>Python 开发的优秀的开源 Wiki 引擎</td><td><a href="http://moinmo.in/">官网</a></td></tr>
<tr><td>JspWiki</td><td>因为是 Java 开发的 当年毛翔曾极力推荐 但界面很魔兽</td><td><a href="http://www.jspwiki.org/">官网</a></td></tr>
<tr><td>DokuWiki</td><td>开源 Wiki 引擎程序 运行于 PHP 环境下 小企业知识管理首选</td><td><a href="https://www.dokuwiki.org/dokuwiki">官网</a></td></tr>
<tr><td>Xwiki</td><td>Java 编写的基于 LGPL 协议发布的开源 Wiki 和应用平台 很像 Confluence</td><td><a href="http://www.xwiki.org/xwiki/bin/view/Main/WebHome">官网</a></td></tr>
<tr><td>Confluence</td><td>这个是重点 无法超越 我喜欢的 Spring JetBrains 都用它 <a href="https://confluence.atlassian.com/display/ALLDOC/Confluence+Documentation+Directory">文档</a>很好</td><td><a href="http://www.atlassian.com/software/confluence/">官网</a></td></tr>
</table>

唉，寻找，安装，配置这些程序，浪费的，都是我的生命啊！折腾有风险，入行需谨慎。

如果你时间够多，还可以继续：

* [Comparison of wiki software](http://en.wikipedia.org/wiki/Comparison_of_wiki_software)

* [Which Open Source Wiki Works For You](http://onlamp.com/pub/a/onlamp/2004/11/04/which_wiki.html)

我个人推荐，DokuWiki 和 Confluence 不错，个人知识管理推荐前者，团队协作推荐后者，只是 Confluence 是企业软件，收费的，而且价格很高，不过，这是在中国，你懂的。

----

## 纠结

自从 2009 年我找到 Confluence 之后，对其它的 Wiki 引擎，就再也没有发掘的兴趣了，很专一。

你会问，为什么写 BBS6 文档，又搞一套 DokuWiki？主要还是看重它的轻，不依赖数据库，只要有 PHP 环境就可以跑起来（其实 Confluence 也是支持嵌入式数据库的，只是 Java 的主机，远没有 PHP 普及）。

但文档还没有开始写，DokuWiki 的各种局限性开始暴露，虽然尝试用 MarkDown 插件、侧边栏插件、文字颜色插件、改名插件 等程序来增强，但最终在发现 Confluence 支持将整个空间导出为 HTML 之后，立刻决定放弃 DokuWiki，虽然它的默认主题很好看，虽然它支持分段编辑。

----

## Confluence

别折腾了，就 Confluence 吧！

年龄大了之后，我就不再纠结软件的版本了，只要有一个可用的，一般我不会频繁的升级，一是顾虑到最新版可能有各种 Bug，二是很多时候，最新版也没有完美破解。

关于 Confluence，去年年底重建的时候，我尝试过 4.3，惊叹于它的界面，和强大的富文本编辑器，但是，它完全移除了 Wiki Markup，这一点我是不能接受的，于是继续安心使用 3.2。

昨天，4what 发现 [Confluence 3.5.17](https://confluence.atlassian.com/display/CONF35/Confluence+Documentation+Home)，说实话，当时他放着文档不写，疯了一样尝试各个版本，我心里很烦，但是最终我们发现了 Confluence 3.5.17 的很多好：

**Highlights of this Release:**

* Easy, Powerful Connections to Active Directory, LDAP and Crowd
* Improved JIRA Integration
* Drag-and-Drop for HTML5 Browsers
* Autowatch and Improved Notification Settings
* Sharing Pages and Blog Posts
* Enhanced Code Macro
* More Administrative Improvements
* "What's New" Feature Tour
* Categories, a New Way of Organising Spaces
* Embedding Audio and Video with the Multimedia Macro
* Other Improvements
* Infrastructure Changes

特别是 **Enhanced Code Macro**，期待很久了：

* More language and environment support for syntax highlighting.
* Expandable code blocks.
* Wrap long lines of code into a new line.
* Sequential line numbering.
* Themed colour schemes.

也因为这次升级，我仔细看了 youtube 上 [Atlassian Confluence 官方视频](http://www.youtube.com/user/GoAtlassian)：

**2.x**

[What's New in Confluence 2.10](http://youtu.be/3CD1Ox3FOvw)

**3.x**

* [What's New in Confluence 3.0](http://youtu.be/j5F2jLVPl0Q)
* [What's New in Confluence 3.1](http://youtu.be/BzlwZfhM7RQ)
* [What's New in Confluence 3.2](http://youtu.be/D4yoH5UhRI8)
* [What's New in Confluence 3.3](http://youtu.be/amH1b3kf_m8)
* [What's New in Confluence 3.4](http://youtu.be/cJcxm-ynto4)
* [What's New in Confluence 3.5](http://youtu.be/XnivP8FAwiY)

**5.x**

[What's New in Confluence 5](http://www.youtube.com/watch?v=KIe4NRrrYmA)

发现很多我之前不了解的功能：

* 拖拽上传附件
* 快捷键操作 按`?` 可显示全部快捷键
* 可嵌入 PPT 
* 富文本编辑器其实很强大

有耐心的还可以看年这两个视频：

Webinar: Atlassian Confluence Wiki as a Platform for Technical Documentation

<http://youtu.be/4Gmdkl4pxzQ>

Atlassian Confluence Product Demonstration Video 4.0

<http://youtu.be/KOuk3vwrao4>

What is a Wiki and 10 Reasons to Use One - Atlassian Confluence

<http://youtu.be/xu6p6bPjokc>

----

## 升级

发现 3 系列的最后一个版本如此强大，我都觉得如果不能从 3.2 平滑升级，我重新录一次数据，都在所不惜。

记住：

>关于软件选择，通常情况下，上一个主版本的最后一次更新，都是最好的。

4what 的经验之谈。为什么这听起来这么不通顺？不是我说的，只是理解了精神，未听清楚原话怎么表达的。

用英文说可能更利索一些：

> Last update of previous version.

但是很遗憾，升级非常顺利，在 3.2 的后台，运行 Backup Confluence Data，会得到一个压缩包，包含附件和 XML 化的数据。安装 3.5.17 到最后一步，选择从从其它 Wiki 恢复数据即可。软件版本升级，一般数据结构都会有变动，有的甚至更换了存储引擎（3.2 MyISAM，3.5.17 InnoDB)，把数据导出为 XML，实在是精明之选！

----

## 插件

默认安装的 Confluence，其实已经很强大了，简单的配置一下，使用就很方便。

但是，它还是有很大的插件市场：

<https://marketplace.atlassian.com/>

Atlassian 对强大的追求，是无止境的。

这里列一下我的主要配置心得：

1、PDF Export Language Support 里上传一个你喜欢的中文字体，比如 微软雅黑，这样导出的 PDF 就支持中文了。

2、3.5.17 的皮肤，似乎不太好看，我推荐 [Intranet Theme](https://studio.plugins.atlassian.com/wiki/display/CINT/Confluence+Intranet+Theme)

下载：[这里](https://marketplace.atlassian.com/plugins/com.atlassian.confluence.plugins.intranettheme)

3、如果英文不太好，可以安装中文语言包

下载：[这里](https://translations.atlassian.com/dashboard/download?lang=zh_CN)，不过我安装之后，未生效，[官方](https://confluence.atlassian.com/display/DOC/Recognised+System+Properties)说：This will only affect users if their browser does not send a language to Confluence, or if language detection is turned off by setting the confluence.browser.language.enabled property to false. 还没有研究清楚。

4、 感觉默认的外链图标太丑，但还没以更换成功，搁置。

----

## Wiki Markup

关于4系列为什么移除 [Wiki 标记](https://confluence.atlassian.com/display/DOC/Confluence+Wiki+Markup)，官方有说法，这里全文引用，打开[官方的博客](http://blogs.atlassian.com/2011/11/why-we-removed-wiki-markup-editor-in-confluence-4/)太慢了。

>Note: You cannot edit content in wiki markup. Confluence does not store page content in wiki markup. Although you can enter wiki markup into the editor, Confluence will convert it to the rich text editor format immediately. You will not be able to edit the wiki markup after initial entry.


**Why We Removed the Wiki Markup Editor in Confluence 4.0**

>This is because Wiki Markup is a very limited subset of XHTML and because any new editor feature had to be built twice…once in the RTE and once in the Wiki Markup Editor. We also had a lot of bugs when toggling between the two edit modes. 


###Collaboration Should Include Everyone


<p style='text-align:justify; text-justify:inter-ideograph'>Our perspective is that product development, and collaboration specifically, needs to include EVERYONE in the organization. Technical teams don’t live in silos – they frequently work with other cross-functional teams, like sales and marketing. Ever since we first released Confluence, way back in 2004, many of you gave us great feedback on the shortcomings of the now legacy Rich Text and Wiki Markup Editors. You told us the Rich Text Editor (RTE) was too basic, slow and unreliable, and that the Wiki Markup Editor had too high a learning curve for most users. Ultimately, we learned that the dual editing experience was the number one hindrance to adoption. Naturally, we challenged ourselves to solve this problem.</p>

###Getting New Features in Your Hands, Faster

<p style='text-align:justify; text-justify:inter-ideograph'>The dual Rich Text and Wiki Markup editing modes also presented a number of technical limitations that slowed our ability to deliver new features. Wiki markup as a storage format hindered our ability to add new features, like merge table cells, that customers had been demanding. This is because Wiki Markup is a very limited subset of XHTML and because any new editor feature had to be built twice…once in the RTE and once in the Wiki Markup Editor. We also had a lot of bugs when toggling between the two edit modes. We knew for some time that we’d need to unify the dual-RTE and Wiki Markup Editors into one simple-yet-capable editing experience and store Confluence content in a more extensible storage format – i.e. XHTML. After much debate, countless customer interviews, and many months of RD it was clear that moving away from Wiki Markup was the best way to improve the experience of editing content in Confluence. Needless to say this was a massive project in development at Atlassian over a period of years.</p>

###But Why Now?

<p style='text-align:justify; text-justify:inter-ideograph'>The idea of moving away from Wiki Markup was first seriously raised in 2006, after the release of Confluence 2.0 with the first version of our Rich Text Editor. The reason we waited five years to implement it was because the last thing we want to do is stick people with a broken editor. Before Confluence 4.0, users could always switch from the Rich Text Editor to the Wiki Markup Editor if you found it not doing quite what you expected it to. Before we could we remove that fallback, we wanted to make sure we weren’t painting users into a corner.</p>

<p style='text-align:justify; text-justify:inter-ideograph'>We set ourselves the challenge that we wouldn’t make the move unless we could come up with a solution that the hard-core Wiki Markup users in our own company – myself included – were happy with. Confluence 4.0 shipped with a completely made-over Rich Text Editor that built on all the features we’d added in the past few years – like Autocomplete, Drag-and-Drop, and the Macro Browser – and added a whole bunch of short-cuts and new features – including Autoformatting and Copy and Paste Images. It’s faster, more reliable, and more fully-featured than before, and we think it meets that original challenge and then goes further.</p>

<p style='text-align:justify; text-justify:inter-ideograph'>In December 2010, the entire Confluence Development Team moved over to using Confluence 4.0 milestones as their day-to-day collaboration space. A couple of weeks after, our Technical Writing Team moved over as well, before shifting the entire company – 400 users of all skill levels – a few months later. After 6 months of the entire company using the new editor and more than a dozen milestones, each adding improvements and tweaks based on over 1,200 pieces of user feedback – from both Atlassian’s and customers – we felt Confluence 4.0 was ready for release.
</p>

###We Know it’s Not Perfect, Yet

<p style='text-align:justify; text-justify:inter-ideograph'>Despite all the extensive dogfooding and 3-month customer beta program, we knew there would be bugs and we greatly appreciate the early adopters that have taken the time to file/vote/comment on those specific issues. This helps us IMMENSELY in being able to prioritize and respond to problems. In fact we are already addressing a number of the issues that have been raised. For example, we know that Find and Replace is an issue for our customers and we will be shipping a solution in our next major release, Confluence 4.1. This is just one example of many issues we have either already addressed or will address in a future release.</p>

<p style='text-align:justify; text-justify:inter-ideograph'>We’ll be the first to tell you that the new editor is not 100% perfect and still has bugs that need to be fixed, but we think it’s light years ahead of the previous editing experience in terms of intuitiveness, efficiency, and reliability. To the extent you and your users encounter editor bugs and issues, please keep reporting them. We’re 110% committed to making the new editor work and appreciate all your support in helping us make it the best editing experience possible for all users.</p>

###Why Don’t We Allow Users to Edit the Source of a Page?

<p style='text-align:justify; text-justify:inter-ideograph'>A lot of you have asked us this and the the main reason we don’t to allow end-user editing of the raw markup is that the editor markup is not really XHTML. It is an XML dialect that looks like XHTML so that it can be edited in a browser, but that embeds a lot of important semantic information so we can turn it back into the storage format when you hit save.</p>

###We’re Still Listening

<p style='text-align:justify; text-justify:inter-ideograph'>We know the new editor is not without bugs. If you do encounter a bug or find that there are things you can’t do in the new editor, we’d love to hear about it.</p>





