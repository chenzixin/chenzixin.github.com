---
layout: post
title: "使用 Markdown 改进你的工作"
description: "<p>其实很多年以前，从国外的网站下载软件，我就留意过，根目录下常有 README.md 这样的文件，可用记事本打开，一般是软件说明和安装指南等，但是从未深入的研究过 md 的含义。</p><p>直到 January 11, 2013，天才黑客 Aaron Swartz 自杀，我才知道，原来世界上有这么优秀的文档工具。</p>"
category: program
tags: [markdown, md]
---
{% include JB/setup %}


## 源起

其实很多年以前，从国外的网站下载软件，我就留意过，根目录下常有 README.md 这样的文件，可用记事本打开，一般是软件说明和安装指南等，但是从未深入的研究过 md 的含义。

直到 January 11, 2013，天才黑客 Aaron Swartz 自杀，我才知道，原来世界上有这么优秀的文档工具。

## 身世

### Markdown

<http://www.aaronsw.com/weblog/001189>

<p class='justify'>For months I’ve been working with John Gruber on a new project. The idea was to make writing simple web pages, and especially weblog entries, as easy as writing an email, by allowing you to use much the same syntax and converting it automatically into HTML.</p>

<p class='justify'>Together we pored over the syntax details from top to bottom, trying to develop the perfect format, and I think we’ve got something pretty darn great. We’ve tested it extensively: on our blogs, in my comments form, in our emails. It’s all worked amazingly well.</p>

<p class='justify'>The format, and John Gruber’s perl implementation of it, is called Markdown. I highly recommend it. It plugs right into Movable Type and makes writing entries so much easier and fun.</p>

- [Official Website](http://daringfireball.net/projects/markdown/)
- [Gruber Manifesto](http://daringfireball.net/2004/03/dive_into_markdown)

<p class='justify'>As John was getting ready to release, I did another <a href="http://www.aaronsw.com/weblog/000918">couple-hour project</a> and wrote the software to go in reverse: to take HTML and turn it back into Markdown. It’s just a first alpha draft, but it seems to handle everything I’ve thrown at it. (If you run into problems, please let me know.)</p>

- [html2text](http://www.aaronsw.com/2002/html2text/)

Both projects are free software, available under the GNU GPL. Share and enjoy!

posted March 19, 2004 05:36 PM

### Wikipedia

#### Aaron Swartz

<http://en.wikipedia.org/wiki/Aaron_Swartz#Markdown>

<p class='justify'>Swartz was co-creator, with John Gruber, of Markdown, a simplified markup standard derived from HTML, and author of its html2text translator. Markdown remains in widespread use.</p>

#### Markdown

<http://en.wikipedia.org/wiki/Markdown>

<p class='justify'>Markdown is a lightweight markup language, originally created by John Gruber with substantial contributions from <b>Aaron Swartz</b>, allowing people “to write using an easy-to-read, easy-to-write plain text format, then convert it to structurally valid XHTML (or HTML)”. The language takes many cues from existing conventions for marking up plain text in email. In other words, Markdown is a text-to-HTML conversion tool for web writers.</p>

## 语法

关于 Markdown 的生世就摘抄到这里，Markdown 的语法，官方网站有，如果英文吃力，可以看这里：

<http://wowubuntu.com/markdown/>

## 应用

这小半年以来，我的工作深度依赖 Markdown：

- Jekyll：静态博客工具，你现在看到的这个文章，就是基于 Jekyll，使用 Markdown 书写

- Mou：Mac 下的 Markdown 编辑器，支持导出为 html & pdf

- mdpress：将 Markdown 文件发布 PPT 的工具，使用 Impress.js 作为效果库

- Google html5slides：另一款 PPT 工具，支持 Markdown，样式更加大方

- Markdoc：简单的 Wiki 引擎，将 Markdown 文件发布为 html，内置 Server

如果你也是一名程序员，强烈推荐你学习使用 Markdown，书写干净的文档。



