---
layout: page
title: 萍水相逢
tagline: 陈自新的博客
---

**Latest Posts**

<ul>
　　　　{% for post in site.posts %}
　　　　　　<li>{{ post.date | date_to_string }} <a href="{{ site.baseurl }}{{ post.url }}">{{ post.title }}</a></li>
　　　　{% endfor %}
</ul>

----

**Links** 

* [4what](http://4what.github.com/cn/)
* [Python](http://www.pyivy.com/)
* [JavaScript](http://www.jsoops.com/)
* [Scala](http://www.scalac.com/)

----

从小，就有许多梦想，现在，一个也不曾留下。我也没有了眼泪。黑沉沉的夜里总是开满黑沉沉的花。慢慢睡去，月光撒落，这个世界干燥冰凉。