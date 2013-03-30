---
layout: post
title: "Learn Perl in about 2 hours 30 minutes"
description: "<p class='justify'>Perl is a dynamic, dynamically-typed, high-level, scripting (interpreted) language most comparable with PHP and Python. Perl&#39;s syntax owes a lot to ancient shell scripting tools, and it is famed for its overuse of confusing symbols, the majority of which are impossible to Google for. Perl&#39;s shell scripting heritage makes it great for writing glue code: scripts which link together other scripts and programs. Perl is ideally suited for processing text data and producing more text data. Perl is widespread, popular, highly portable and well-supported. Perl was designed with the philosophy &quot;There&#39;s More Than One Way To Do It&quot; (TMTOWTDI) (contrast with Python, where &quot;there should be one - and preferably only one - obvious way to do it&quot;).</p> <p class='justify'>Perl has horrors, but it also has some great redeeming features. In this respect it is like every other programming language ever created.</p>"
category: porgram
tags: [perl]
---
{% include JB/setup %}

By [Sam Hughes](http://qntm.org/perl)

<p class='justify'>Perl is a dynamic, dynamically-typed, high-level, scripting (interpreted) language most comparable with PHP and Python. Perl's syntax owes a lot to ancient shell scripting tools, and it is famed for its overuse of confusing symbols, the majority of which are impossible to Google for. Perl's shell scripting heritage makes it great for writing glue code: scripts which link together other scripts and programs. Perl is ideally suited for processing text data and producing more text data. Perl is widespread, popular, highly portable and well-supported. Perl was designed with the philosophy "There's More Than One Way To Do It" (TMTOWTDI) (contrast with Python, where "there should be one - and preferably only one - obvious way to do it").</p>

Perl has horrors, but it also has some great redeeming features. In this respect it is like every other programming language ever created.

This document is intended to be informative, not evangelical. It is aimed at people who, like me:

* dislike the official Perl documentation at <http://perl.org/> for being intensely technical and giving far too much space to very unusual edge cases
* learn new programming languages most quickly by "axiom and example"
* wish Larry Wall would get to the point
* already know how to program in general terms
* don't care about Perl beyond what's necessary to get the job done.

This document is intended to be as short as possible, but no shorter.

## Preliminary notes

<p class='justify'>The following can be said of almost every declarative statement in this document: "that's not, strictly speaking, true; the situation is actually a lot more complicated". If you see a serious lie, point it out, but I reserve the right to preserve certain critical lies-to-children.</p>

<p class='justify'>Throughout this document I'm using example print statements to output data but not explicitly appending line breaks. This is done to prevent me from going crazy and to give greater attention to the actual string being printed in each case, which is invariably more important. In many examples, this results in alotofwordsallsmusheduptogetherononeline if the code is run in reality. Try to ignore this.</p>

## Hello world

A Perl script is a text file with the extension **.pl**.

Here's the full text of **helloworld.pl**:

```perl
use strict;
use warnings;

print "Hello world";
```

Perl scripts are interpreted by the Perl interpreter, **perl** or **perl.exe**:

```
perl helloworld.pl [arg0 [arg1 [arg2 ...]]]
```

<p class='justify'>A few immediate notes. Perl's syntax is highly permissive and it will allow you to do things which result in ambiguous-looking statements with unpredictable behaviour. There's no point in me explaining what these behaviours are, because you want to avoid them. The way to avoid them is to put <b>use strict; use warnings;</b> at the very top of every Perl script or module that you create. Statements of the form <b>use foo;</b> are pragmas. A pragma is a signal to <b>perl.exe</b>, which takes effect when initial syntactic validation is being performed, before the program starts running. These lines have no effect when the interpreter encounters them at run time.</p>

The symbol **#** begins a comment. A comment lasts until the end of the line. Perl has no block comment syntax.

未完……











